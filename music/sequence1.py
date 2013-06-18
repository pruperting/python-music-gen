import sys
sys.path.append("../")

from midiutil.MidiGenerator import MidiGenerator
from midiutil.Scales import *
from midiutil.TrackGen import *

midiGenerator = MidiGenerator(tempo=105)

sc = HARMONIC_MINOR_SCALE

playable_mscale = [[x] for x in buildScale(sc, 48, 80)]

pos = 0
for y in range(128):
    beat = LoopingArray([(0.25,0.25)])
    notes = LoopingIndexedArray(playable_mscale,[[z+(y**z)] for z in range(8)])
    velocities = LoopingArray([127])
    length = 4
    
    midiGenerator.add_track(0, pos, beat=beat, notes=notes, velocities=velocities, length=length)

    notes = LoopingIndexedArray([[x] for x in buildScale(sc, 48-12, 80-12)],[1+(y**1)])
    midiGenerator.add_track(1, pos, beat=LoopingArray([(4,4)]), notes=notes, velocities=velocities, length=length)

    pos += length

midiGenerator.write()