import os,sys
from pcbnew import *
import shutil

board_file = '/home/logic/_workspace/3D-printer-board/hardware/printer-board/printer-board.kicad_pcb'

board_file_new = '/home/logic/_workspace/3D-printer-board/hardware/printer-board/printer-board_new.kicad_pcb'

board = GetBoard()

startx = 100
starty = 100

j=1

forward = 1

# loop for number of integer
for i in range(0,3+1):


    # loop for number of led in col
    for l in range(0,7+1):
        ymils = starty + (500*l)
        xmils = startx + (500 * 8 * i)

        # loop for number of led in a row

        component_start = 1+(8*l) + (64*i)
        component_end = component_start+8

        active_parts = ['D%s' % j for j in range(component_start,component_end)]
        if forward==0:
            active_parts = ['D%s' % j for j in range(component_end-1,component_start-1,-1)]
            forward=1
        else:
            forward=0

        print(component_start, component_end)

        for active_part in active_parts:
            xmils = xmils + 500

            print('placing %s ' % active_part)
            print('x:%s, y:%s' %(xmils, ymils))
            # # import sys
            # # sys.exit()
            for idx, rd in enumerate([active_part]):
                part = board.FindModuleByReference(rd)
                part.SetPosition(wxPoint(FromMils(xmils), FromMils(ymils)))

Refresh()
print('done')
