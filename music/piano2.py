import sys
sys.path.append("../")

from midiutil.TrackGen import LoopingArray, StaticIterator
from midiutil.MidiGenerator import MidiGenerator
from midiutil.Scales import *

midiGenerator = MidiGenerator()

sc = HARMONIC_MINOR_SCALE
scale = [[x] for x in buildScale(sc, 48, 80)]

l = 3
pos = 0
for k in range(2):
	for i in range(16):
		midiGenerator.add_track (0, pos, 
				beat = LoopingArray([(0.5,1.0), (0.5,1.0), (1.0,2.0), (0.5,0.5)]),
				notes = LoopingArray(scale, functioniterator = [
																	('add', StaticIterator(value=1)),
																	('mult', LoopingArray([5+(i),3+(i*2),2+(i*3)]))
																	],
								id='notes'),
				velocities = LoopingArray([100,90,110,70,80]),
				length = l)
		pos+=l
	
	for j in range(8):
		for i in range(1):
			midiGenerator.add_track (0, pos, 
					beat = LoopingArray([(0.5,1.0), (0.5,1.0), (1.0,2.0), (0.5,0.5)]),
					notes = LoopingArray(scale[5-j:], functioniterator = [
																		('add', StaticIterator(value=2)),
																		('mult', LoopingArray([5+(i),3+(i*2),2+(i*3)]))
																		],
									id='notes'),
					velocities = LoopingArray([100,90,110,70,80]),
					length = l)
			pos+=l
	
		
midiGenerator.write()