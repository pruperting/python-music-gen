import sys
sys.path.append("../")

from midiutil.TrackGen import LoopingArray
from midiutil.MidiGenerator import MidiGenerator

midiGenerator = MidiGenerator(tempo=120)

scale = reduce(lambda x,y:x+y,[[y+(12*x) for y in [0,3,5,7,8,10]] for x in range (10)])

base = 20

tracks = {
          'Bass track': {
                         'notearrays': [
                                        {
                                         'beat': LoopingArray([(8,8)]),
                                         'notearray': LoopingArray([[scale[base+x]] for x in [0,1,3,2]]),
                                         'velocities': LoopingArray([100])
                                        }
                                        ],
                         },
          'Chords 1': {
                       'notearrays': [
                                      {
                                       'beat': LoopingArray([(8,8),(16,16)]),
                                       'notearray': LoopingArray([[scale[base+x]] for x in [10,12,14,16]]),
                                       'velocities': LoopingArray([100])
                                      },
                                      {
                                       'beat': LoopingArray([(8,8),(16,16)]),
                                       'notearray': LoopingArray([[scale[base+x]] for x in [20,22,21]]),
                                       'velocities': LoopingArray([100])
                                      },
                                      {
                                       'beat': LoopingArray([(8,8),(16,16)]),
                                       'notearray': LoopingArray([[scale[base+x]] for x in [25,24,23,22,24]]),
                                       'velocities': LoopingArray([100])
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

        midiGenerator.add_track(i,0,beat=beat,notes=notearray,velocities=velocities,length=128)

midiGenerator.write()