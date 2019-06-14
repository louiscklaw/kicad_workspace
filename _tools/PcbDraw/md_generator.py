#!/usr/bin/env python3

import mistune
import lib.mdrenderer
import re
import codecs
import pybars
import yaml
import argparse
import sys
import os
import subprocess
import re

from copy import deepcopy
from pprint import pprint

CWD = os.path.dirname(os.path.abspath(__file__))

PCB_TEMP_DIR = '/tmp'

PCBDRAW_BIN = os.getenv('PCBDRAW_BIN','./pcbdraw.py')
PCB_PATTERN = '.*\[\[(.+)\|?(.*)?\]\](.*)'

CWD_PATH = os.getenv('PWD',os.path.dirname(os.path.abspath(__file__)))

def flatten(l):
    return [item for sublist in l for item in sublist]


def svg_to_png(infile, outfile, dpi=300):
    import cairo
    import gi
    gi.require_version('Rsvg', '2.0')
    from gi.repository import Rsvg

    handle = Rsvg.Handle()
    svg = handle.new_from_file(infile)
    svg.set_dpi(dpi)
    dim = svg.get_dimensions()
    w, h = dim.width, dim.height
    img =  cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h)
    ctx = cairo.Context(img)
    svg.render_cairo(ctx)
    img.write_to_png(outfile)


def generate_image(boardfilename, libs, side, components, active, parameters, outputfile):
    svgfilename = os.path.splitext(outputfile)
    svgfilename, ext = svgfilename[0] + ".svg", svgfilename[1]

    # TODO: fallback, origional
    # command = [PCBDRAW_BIN, "-f", ",".join(components), "-a", ",".join(active)]

    # command = [PCBDRAW_BIN, ",".join(active)]

    # if side.startswith("back"):
    #     command.append("-b")
    # command += flatten(map(lambda x: x.split(" ", 1), parameters))
    # command.append(libs)
    # command.append(boardfilename)
    # command.append(svgfilename)

    command = [PCBDRAW_BIN]
    if side.startswith("back"):
        command.append("-b")
    command.append(libs)
    command.append(boardfilename)
    command.append(svgfilename)
    print(' '.join(command))

    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        print("PcbDraw failed with code {} and output: ".format(e.returncode))
        print(e.output)
        sys.exit(1)
    if ext != ".svg":
        if ext == ".png":
            svg_to_png(svgfilename, outputfile)
            os.remove(svgfilename)
        else:
            print("Unsupported image type: {}".format(ext))
            sys.exit(1)

# def generate_images(content, boardfilename, libs, parameters, name, outdir):
#     dir = os.path.dirname(os.path.join(outdir, name))
#     if not os.path.exists(dir):
#         os.makedirs(dir)
#     counter = 0
#     for item in content:
#         if item["type"] == "comment":
#             continue
#         for x in item["steps"]:
#             if x["comment"].find('[x]') >= 0 or x["comment"].find('[ ]') >= 0:
#                 pass
#             else:
#                 # pprint(x['side'])
#                 counter += 1
#                 filename = name.format(counter)
#                 generate_image(boardfilename, libs, x["side"], x["components"], x["active_components"], parameters, os.path.join(outdir, filename))
#                 x["img"] = filename
#     return content

def merge_args(args, header):
    for key in filter(lambda x: not x.startswith("_"), dir(args)):
        val = getattr(args, key)
        if val is not None:
            header[key] = val
    if "params" not in header:
        header["params"] = []
    return header

def find_command(list, command):
    for x in list:
        if x.startswith(command):
            return x
    return None

def relativize_header_paths(header, to):
    for key in ["template", "board", "libs"]:
        if key not in header:
            continue
        if os.path.isabs(header[key]):
            continue
        x = os.path.join(to, header[key])
        header[key] = os.path.normpath(x)
    if "params" in header:
        x = header["params"]
        newlist = []
        for key in ["--style", "--remap"]:
            c = find_command(x, key)
            if c is None:
                continue
            y = c.split(" ")
            command, arg = y[0], y[1]
            if os.path.isabs(arg):
                continue
            c = command + " " + os.path.normpath(os.path.join(to, arg))
            newlist.append(c)
        header["params"] = newlist
    return header

def load_content(filename):
    header = None
    with codecs.open(filename, encoding="utf-8") as f:
        content = f.read()
        if content.startswith("---"):
            end = content.find("...")
            if end != -1:
                header = yaml.load(content[3:end])
                content = content[end+3:]
    return header, content

def check_pcb_drawing_mark(md_text):
    # if re.search('.*\[\[.*\]\].*',md_text):
    m = re.match(PCB_PATTERN,md_text)
    return m

def get_pcb_drawing_md_text(pcb_drawing_path, alt_text):
    return """![{}]({} "{}")""".format(alt_text,
        pcb_drawing_path, alt_text
    )

def inject_pcb_drawing_placeholder(alt_text, pcb_drawing_path):
    pcb_placeholder_string = get_pcb_drawing_md_text(pcb_drawing_path, alt_text)
    return pcb_placeholder_string

def get_pcb_drawing_link():
    pass

def scan_content_for_pcb_drawing_mark(md_content):
    kicad_pcb_path = os.path.join(CWD_PATH, args["board"])
    lib_path = args["libs"]
    pcbdraw_params = args["params"]
    img_name_path_template = args["img_name"]
    md_outoput_path = args["output"]

    pcb_draw_number = 0
    for i in range(0,len(md_content)):
        md_line = md_content[i]
        m = check_pcb_drawing_mark(md_line)
        if m is not None:
            side = m.group(1)
            highlight_component = m.group(2)
            alt_text = m.group(3)
            pcb_draw_number+=1

            # TODO: refactor me
            img_name_path = os.path.join(md_outoput_path,img_name_path_template.format(pcb_draw_number))

            generate_image(kicad_pcb_path, lib_path, side, highlight_component, highlight_component, pcbdraw_params, img_name_path)

            print(img_name_path)

            md_content[i] = inject_pcb_drawing_placeholder(alt_text, img_name_path_template.format(pcb_draw_number))

    return md_content

def replace_pcb_drawing_placeholder_by_drawing():
    pass

def main():
    print('helloworld')


if __name__ =="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="source file")
    parser.add_argument("output", help="output directory")

    args = parser.parse_args()

    try:
        header, content = load_content(args.input)
    except IOError:
        print("Cannot open source file " + args.input)
        sys.exit(1)
    header = relativize_header_paths(header, os.path.dirname(args.input))
    args = merge_args(args, header)
    content = content.split('\n')

    # inject pcb_drawing_mark for md_content
    md_temp = scan_content_for_pcb_drawing_mark(content)

    INPUT_MD_PATH = os.path.join(args['input'])
    OUTPUT_MD_PATH = os.path.join(args['output'], 'index.md')

    print('input markdown: %s' % INPUT_MD_PATH)
    print('output markdown: %s' % OUTPUT_MD_PATH)

    with open(OUTPUT_MD_PATH,'w+') as f:
        f.write('\n'.join(md_temp))


    # main()
