import sys
sys.path.append("../")

from midiutil.TrackGen import LoopingArray
from midiutil.MidiGenerator import MidiGenerator

midiGenerator = MidiGenerator(tempo=120)

scale = reduce(lambda x,y:x+y,[[y+(12*x) for y in [0,2,3,5,7,8,10]] for x in range (10)])

base = 20

tracks = {
          'Bass track': {
                         'notearrays': [
                                        {
                                         'beat': LoopingArray([(16,16)]),
                                         'notearray': LoopingArray([[scale[base+x]] for x in [0,1,2,3,4,5,6]], 
											functioniterator=[
												('add',LoopingArray([4]))
											]),
                                         'velocities': LoopingArray([100])
                                        }
                                        ],
                         },
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