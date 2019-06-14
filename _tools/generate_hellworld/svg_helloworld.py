import os,sys
import pcbnew
import shutil

# http://scottbezek.blogspot.com/2016/04/scripting-kicad-pcbnew-exports.html

# Load board and initialize plot controller
board_file = '/home/logic/_workspace/3D-printer-board/hardware/printer-board/printer-board.kicad_pcb'

board_dir = os.path.dirname(board_file)
output_dir  = os.path.join(board_dir,'_output')
taobao_dir = os.path.join(output_dir,'_to_taobao')
taobao_drill_dir = os.path.join(taobao_dir,'_drill')

board = pcbnew.LoadBoard(board_file)
pc = pcbnew.PLOT_CONTROLLER(board)
po = pc.GetPlotOptions()
po.SetPlotFrameRef(False)


# https://github.com/KiCad/kicad-source-mirror/blob/829fa97f3c8dcbcc934abbc1c206dafa3ceceeec/include/layers_id_colors_and_visibility.h#L52
plot_configs=[
    # (pcbnew.In1_Cu, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "In1_Cu", '_output'),
    # (pcbnew.In2_Cu, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "In2_Cu", '_output'),
    # (pcbnew.In3_Cu, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "In3_Cu", '_output'),
    # (pcbnew.In4_Cu, [pcbnew.Phttps://www.google.com/search?q=pcb+%E5%B1%A4%E6%A7%8B%E6%88%90&client=ubuntu&hs=3ua&channel=fs&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiZpezFrYbiAhUBc3AKHcoABfQQ_AUIDigB&biw=1920&bih=879LOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "In4_Cu", '_output'),
    # (pcbnew.In5_Cu, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "In5_Cu", '_output'),
    # (pcbnew.In6_Cu, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "In6_Cu", '_output'),
    # (pcbnew.In7_Cu, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "In7_Cu", '_output'),
    # (pcbnew.In8_Cu, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "In8_Cu", '_output'),
    # (pcbnew.In9_Cu, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "In9_Cu", '_output'),
    # (pcbnew.In10_Cu, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "In10_Cu", '_output'),
    # (pcbnew.In11_Cu, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "In11_Cu", '_output'),
    # (pcbnew.In12_Cu, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "In12_Cu", '_output'),
    # (pcbnew.In13_Cu, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "In13_Cu", '_output'),
    # (pcbnew.In14_Cu, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "In14_Cu", '_output'),
    # (pcbnew.In15_Cu, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "In15_Cu", '_output'),
    # (pcbnew.In16_Cu, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "In16_Cu", '_output'),
    # (pcbnew.In17_Cu, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "In17_Cu", '_output'),
    # (pcbnew.In18_Cu, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "In18_Cu", '_output'),
    # (pcbnew.In19_Cu, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "In19_Cu", '_output'),
    # (pcbnew.In20_Cu, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "In20_Cu", '_output'),
    # (pcbnew.In21_Cu, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "In21_Cu", '_output'),
    # (pcbnew.In22_Cu, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "In22_Cu", '_output'),
    # (pcbnew.In23_Cu, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "In23_Cu", '_output'),
    # (pcbnew.In24_Cu, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "In24_Cu", '_output'),
    # (pcbnew.In25_Cu, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "In25_Cu", '_output'),
    # (pcbnew.In26_Cu, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "In26_Cu", '_output'),
    # (pcbnew.In27_Cu, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "In27_Cu", '_output'),
    # (pcbnew.In28_Cu, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "In28_Cu", '_output'),
    # (pcbnew.In29_Cu, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "In29_Cu", '_output'),
    # (pcbnew.In30_Cu, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "In30_Cu", '_output'),
    (pcbnew.F_Cu, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "F_Cu", output_dir),
    (pcbnew.B_Cu, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "B_Cu", output_dir),
    (pcbnew.B_Adhes, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "B_Adhes", output_dir),
    (pcbnew.F_Adhes, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "F_Adhes", output_dir),
    (pcbnew.B_Paste, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "B_Paste", output_dir),
    (pcbnew.F_Paste, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "F_Paste", output_dir),
    (pcbnew.B_SilkS, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "B_SilkS", output_dir),
    (pcbnew.F_SilkS, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "F_SilkS", output_dir),
    (pcbnew.B_Mask, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "B_Mask", output_dir),
    (pcbnew.F_Mask, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "F_Mask", output_dir),
    (pcbnew.Dwgs_User, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "Dwgs_User", output_dir),
    (pcbnew.Cmts_User, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "Cmts_User", output_dir),
    (pcbnew.Eco1_User, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "Eco1_User", output_dir),
    (pcbnew.Eco2_User, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "Eco2_User", output_dir),
    (pcbnew.Edge_Cuts, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "Edge_Cuts", output_dir),
    (pcbnew.Margin, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "Margin", output_dir),
    (pcbnew.B_CrtYd, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "B_CrtYd", output_dir),
    (pcbnew.F_CrtYd, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "F_CrtYd", output_dir),
    (pcbnew.B_Fab, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "B_Fab", output_dir),
    (pcbnew.F_Fab, [pcbnew.PLOT_FORMAT_SVG, pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "F_Fab", output_dir),

    (pcbnew.F_Cu, [ pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "F_Cu", taobao_dir),
    (pcbnew.B_Cu, [ pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "B_Cu", taobao_dir),
#     (pcbnew.B_Adhes, [ pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "B_Adhes", taobao_dir),
#     (pcbnew.F_Adhes, [ pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "F_Adhes", taobao_dir),
#     (pcbnew.B_Paste, [ pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "B_Paste", taobao_dir),
#     (pcbnew.F_Paste, [ pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "F_Paste", taobao_dir),
    (pcbnew.B_SilkS, [ pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "B_SilkS", taobao_dir),
    (pcbnew.F_SilkS, [ pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "F_SilkS", taobao_dir),
    (pcbnew.B_Mask, [ pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "B_Mask", taobao_dir),
    (pcbnew.F_Mask, [ pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "F_Mask", taobao_dir),
#     (pcbnew.Dwgs_User, [ pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "Dwgs_User", taobao_dir),
#     (pcbnew.Cmts_User, [ pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "Cmts_User", taobao_dir),
#     (pcbnew.Eco1_User, [ pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "Eco1_User", taobao_dir),
#     (pcbnew.Eco2_User, [ pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "Eco2_User", taobao_dir),
    (pcbnew.Edge_Cuts, [ pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "Edge_Cuts", taobao_dir),
#     (pcbnew.Margin, [ pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "Margin", taobao_dir),
#     (pcbnew.B_CrtYd, [ pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "B_CrtYd", taobao_dir),
#     (pcbnew.F_CrtYd, [ pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "F_CrtYd", taobao_dir),
#     (pcbnew.B_Fab, [ pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "B_Fab", taobao_dir),
#     (pcbnew.F_Fab, [ pcbnew.PLOT_FORMAT_GERBER, pcbnew.PLOT_FORMAT_PDF], "F_Fab", taobao_dir),
]


def clear_directory(dir_to_clear):
    if os.path.isdir(dir_to_clear):
        print('rmdir %s' % dir_to_clear)
        shutil.rmtree(dir_to_clear)

def get_all_output_directory(plot_configs):
    output={}
    for plot_config in plot_configs:
        _,_,_,output_dir = plot_config
        output[output_dir]=''

    return output.keys()

def clear_output_directory(plot_configs):
    for dir_need_clear in get_all_output_directory(plot_configs):
        dir_need_clear = os.path.join(os.path.dirname(board_file),dir_need_clear)
        clear_directory(dir_need_clear)
        print(dir_need_clear)

def get_drill_output_dir(board_kicad_file_path):
    return os.path.join(os.path.dirname(board_kicad_file_path), '_output','drill')

def create_dir_if_not_exist(dir_to_create):
    if os.path.isdir(dir_to_create):
        pass
    else:
        os.mkdir(dir_to_create)

def get_drill_file(drill_output_dir):

    create_dir_if_not_exist(drill_output_dir)

    drlwriter = pcbnew.EXCELLON_WRITER( board )
    drlwriter.SetMapFileFormat( pcbnew.PLOT_FORMAT_PDF )

    mirror = False
    minimalHeader = False
    offset = pcbnew.wxPoint(0,0)
    # False to generate 2 separate drill files (one for plated holes, one for non plated holes)
    # True to generate only one drill file
    mergeNPTH = False
    drlwriter.SetOptions( mirror, minimalHeader, offset, mergeNPTH )

    metricFmt = True
    drlwriter.SetFormat( metricFmt )

    genDrl = True
    genMap = True
    print('create drill and map files in %s' % drill_output_dir)
    drlwriter.CreateDrillandMapFilesSet( drill_output_dir, genDrl, genMap );

    # One can create a text file to report drill statistics
    rptfn = os.path.join(drill_output_dir, 'drill_report.rpt')
    print('report: %s' % rptfn)
    drlwriter.GenDrillReportFile( rptfn );


def gen_taobao_files():
    drill_output_dir = get_drill_output_dir(board_file)
    create_dir_if_not_exist(drill_output_dir)


def plot_board(plot_configs):
    for plot_config in plot_configs:
        layer, files_format, file_suffix, plotDir = plot_config

        print(layer)
        print(file_suffix)
        # Set current layer
        pc.SetLayer(layer)

        for file_format in files_format:
            po.SetOutputDirectory(plotDir)

            # Plot single layer to file
            pc.OpenPlotfile(file_suffix, file_format, file_suffix)
            print("Plotting to " + pc.GetPlotFileName())
            pc.PlotLayer()
            pc.ClosePlot()

clear_output_directory(plot_configs)
plot_board(plot_configs)
get_drill_file(taobao_drill_dir)
