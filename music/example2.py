import sys
sys.path.append("../")

from midiutil.TrackGen import LoopingArray
from midiutil.MidiGenerator import MidiGenerator

midiGenerator = MidiGenerator(tempo=128)

scale = reduce(lambda x,y:x+y,[[y+(12*x)+36 for y in [0,2,3,5,7,8,10]] for x in range (5)])

base = 0
pos = 0
tracks = {
          'running notes': {
                       'notearrays': [
                                      {
                                       'beat': LoopingArray([(1.5,1.5),(1.5,1.5),(1.5,1.5),(1.5,1.5),(1,1),(1,1)]),
                                       'notearray': LoopingArray([[scale[(base+(x*2)) % len(scale)]] for x in [0,5,2,6,4,8]]),
                                       'velocities': LoopingArray([100,90,110,70,80])
                                      },
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