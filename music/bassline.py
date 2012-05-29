import sys
sys.path.append("../")

from midiutil.TrackGen import LoopingArray
from midiutil.MidiGenerator import MidiGenerator

midiGenerator = MidiGenerator(tempo=90)

scale = reduce(lambda x,y:x+y,[[y+(12*x)+36 for y in [0,7,14,8,10,7,8]] for x in range (2)])

pos = 0
for base in [10,9,8,7,6,5,4,3,2,1]:
#base = 10
    
    tracks = {
              'running notes': {
                           'notearrays': [
                                          {
                                           'beat': LoopingArray([(1,1),(0.5,0.5),(0.25,0.25),(1.5,1.5)]),
                                           'notearray': LoopingArray([[scale[(base+(x*2)) % len(scale)]] for x in range(5)]),
                                           'velocities': LoopingArray([100,90,110,70,80])
                                          },
                                          {
                                           'beat': LoopingArray([(0.5,0.5),(0.25,0.25),(2.0,2.0)]),
                                           'notearray': LoopingArray([[scale[(base+(x*3)) % len(scale)]] for x in range(9)]),
                                           'velocities': LoopingArray([90,91,49,110,93,49,69])
                                          },
                                          {
                                           'beat': LoopingArray([(2,2),(1,1)]),
                                           'notearray': LoopingArray([[scale[(base+(x*2)) % len(scale)]] for x in range(13)]),
                                           'velocities': LoopingArray([85,91,102,99,87,11,76,44,59])
                                          }
                                          ],
                           }
             }
    
    i = 0
    for track in tracks:
        print 'processing %s' % track
        
        notearrays = tracks[track]['notearrays']
        for n in notearrays:
            beat = n['beat']
            notearray = n['notearray']
            velocities = n['velocities']
            midiGenerator.add_track(i,pos,beat=beat,notes=notearray,velocities=velocities,length=128)

    pos+=8

midiGenerator.write()