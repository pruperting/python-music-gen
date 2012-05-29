import sys
sys.path.append("../")

from midiutil.MidiGenerator import MidiGenerator
from midiutil.Scales import MINOR, buildScale
from midiutil.TrackGen import LoopingIncrementalIndexedArray, LoopingArray

midiGenerator = MidiGenerator(tempo=105)

sc = MINOR

mscale = buildScale(sc, 48, 80)
notes = LoopingArray([
                      [mscale[x] for x in [0, 2, 4, 6]], # chord 1
                      [mscale[x] for x in [3, 5, 7, 9]], # chord 2 
                      [mscale[x] for x in [5, 7, 11]] # chord 3
                      ], functioniterator=[('add', LoopingArray([1, 1, 2]))])
chord_beats = LoopingArray([(4, 4), (2, 2)])
notes_beats = LoopingArray([(0.25, 0.25)])
velocities = LoopingArray([120, 120])
note_skip = LoopingArray([0, 1, 2, 3, 1], functioniterator=[('add', LoopingArray([1, 2]))])

midiGenerator.add_arpeggio(0, 0, chords_beat=chord_beats, notes_beat=notes_beats, chords=notes, velocities=velocities, note_skip=note_skip, length=32)

notes = LoopingIncrementalIndexedArray([[x] for x in buildScale(sc, 36, 48)], [1, 1, 2, -1, 2])
beats = LoopingArray([(4, 4)])
velocities = LoopingArray([110, 110])
midiGenerator.add_track (1, 0, beat=beats, notes=notes, velocities=velocities, length=32)

midiGenerator.write()