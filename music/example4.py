import sys
sys.path.append("../")

from midiutil.TrackGen import LoopingArray
from midiutil.MidiGenerator import MidiGenerator

midiGenerator = MidiGenerator(tempo=120)

x = LoopingArray([5,1,6])
note = 0
scale = []
for _ in range(10):
    scale += [36+note]
    note += x.next()

tracks = {
          'Bass track': {
                         'notearrays': [
                                        {
                                         'beat': LoopingArray([(0.25,1.0)]),
                                         'notearray': LoopingArray([[x] for x in scale],
                                                                   functioniterator=[
                                                                                     ('add',LoopingArray([1,2,3,4,5])),
                                                                                     ('dec',LoopingArray([0,0,1,2])),
                                                                                     ]),
                                         'velocities': LoopingArray([x for x in range(100,110)],
                                                                    functioniterator=[
                                                                                      ('add',LoopingArray([1,2,4,1,3])),
                                                                                     ('dec',LoopingArray([0,7,3,2])),
                                                                                      ])
                                        }
                                        ],
                         },
          }
    
for track in tracks:
    print 'processing %s' % track
    
    notearrays = tracks[track]['notearrays']
    for n in notearrays:
        beat = n['beat']
        notearray = n['notearray']
        velocities = n['velocities']

        midiGenerator.add_track(0,0,beat=beat,notes=notearray,velocities=velocities,length=256)

midiGenerator.write()