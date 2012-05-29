import sys
sys.path.append("../")

from midiutil.TrackGen import LoopingArray, StaticIterator
from midiutil.MidiGenerator import MidiGenerator

midiGenerator = MidiGenerator()

l = 3
pos = 0
for mod in range(4):
    for notepattern in [[0,2,7,8],[2,5,7,10],[0,3,7,8],[3,5,7,8,10],]:
        scale = reduce(lambda x,y:x+y,[[y+(12*x)+48 for y in notepattern] for x in range (3)])
        midiGenerator.add_track (0, pos, 
                   beat = LoopingArray([(0.5,1.0)]),
                   notes = LoopingArray([[x] for x in scale], functioniterator = [
                                                                           ('add', StaticIterator(value=1)),
                                                                           ('mult', LoopingArray([1,2,1+mod]))
                                                                           ],
                                id='notes'),
                   velocities = LoopingArray([100,90,110,70,80]),
                   length = l)
        pos+=l
    
    for notepattern in [[5,2,7,8],[7,5,7,10],[8,3,7,8],[11,5,7,3],]:
        scale = reduce(lambda x,y:x+y,[[y+(12*x)+48 for y in notepattern] for x in range (3)])
        midiGenerator.add_track (0, pos,
                   beat = LoopingArray([(0.5,1.0)]),
                   notes = LoopingArray([[x] for x in scale], functioniterator = [
                                                                           ('add', StaticIterator(value=1)),
                                                                           ('mult', LoopingArray([1,2,1+mod]))
                                                                           ],
                                id='notes'),
                   velocities = LoopingArray([100,90,110,70,80]),
                   length = l)
        pos+=l

midiGenerator.write()