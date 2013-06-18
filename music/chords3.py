import sys
sys.path.append("../")

from midiutil.TrackGen import LoopingArray
from midiutil.MidiGenerator import MidiGenerator

midiGenerator = MidiGenerator(tempo=145)

scale = reduce(lambda x, y:x + y, [[36 + y + (12 * (x)) for y in [0, 2, 3, 5, 7, 8, 11]] for x in range (5)])

base = 16

def PatternGenerator(seed, n, reduce_function, max):
	pattern = seed
	for _ in range(n):
		pattern.append(reduce(reduce_function, pattern) % max)
	return pattern[1:]

def GetLoopingArray(base, arr):
	print arr
	return LoopingArray([[scale[(base + x) % len(scale)]] for x in arr])
	

tracks = {
          'Notes 1': {
                         'notearrays': [
                                        {
                                         'beat': LoopingArray([(2,2)]),
                                         'notearray': GetLoopingArray(base, PatternGenerator([1], 10, lambda x, y: x+y, 11)),
                                         'velocities': LoopingArray([100,90,95,70])
                                        }
                                        ],
                         },
          'Notes 2': {
                       'notearrays': [
                                      {
                                       'beat': LoopingArray([(4, 4),(4, 4),(4, 4),(4, 4),(4, 4),(4, 4),(1, 1),(1, 1),(0.5, 0.5),(0.5, 0.5)]),
                                       'notearray': GetLoopingArray(base+20, PatternGenerator([1], 20, lambda x, y: x+(y+2), 13)),
                                       'velocities': LoopingArray([70,100,90,95])
                                      },
                                        ],
                         },
          'Notes 3': {
                       'notearrays': [
                                      {
                                       'beat': LoopingArray([(6, 6),(1,1)]),
                                       'notearray': GetLoopingArray(base+25, PatternGenerator([1], 6, lambda x, y: x+y, 5)),
                                       'velocities': LoopingArray([90,80,90,75,70])
                                      },
                                        ],
                         },
          'Notes 4': {
                       'notearrays': [
                                      {
                                       'beat': LoopingArray([(1,1),(2, 2),(0.5,0.5),(0.5,0.5),(0.5,0.5)]),
                                       'notearray': GetLoopingArray(base+30, PatternGenerator([1], 24, lambda x, y: x+y, 23)),
                                       'velocities': LoopingArray([80,90,70,80,100,90])
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

        midiGenerator.add_track(i, 0, beat=beat, notes=notearray, velocities=velocities, length=128)

midiGenerator.write()
