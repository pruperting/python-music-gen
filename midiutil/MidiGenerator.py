#-----------------------------------------------------------------------------
# Name:        MidiGenerator.py
# Purpose:     MIDI file generation
#-----------------------------------------------------------------------------

import os
from os import path
import sys
from midiutil.MidiFile import MIDIFile
from midiutil.TrackGen import LoopingArray

class MidiGenerator:
    def __init__(self, filename='', tempo=120):
        """
        If filename is empty, set the midi file to the __main__file_name.mid
        """
        if filename == '':
            self.filename = os.path.basename(path.abspath(sys.modules['__main__'].__file__)).split('.')[0] + '.mid'
        else:
            self.filename = filename
            
        self.midi = MIDIFile(16)
        self.tempo = tempo
        
    def add_track(self, track, time, trackname='', beat=[], notes=[], velocities=[], length=0):
        self.midi.addTrackName(track, time, ('Track %s' % track if trackname == '' else trackname))
        self.midi.addTempo(track, time, self.tempo)
    
        beat_index = time
        while beat_index - time < length:
            beat_value, duration_value = beat.next()
            for note in notes.next():
                self.midi.addNote(track, track, note, beat_index, duration_value, velocities.next())
            beat_index += beat_value
    
    
    def add_arpeggio(self, track, time, chords_beat=[], notes_beat=[], chords=[], velocities=[], note_skip=LoopingArray([1,2,3]), length=0):
        self.midi.addTrackName(track, time, "Track %s" % track)
        self.midi.addTempo(track, time, self.tempo)
    
        beat_index = time
        bi = beat_index
        while beat_index - time < length:
            chordindex = 0
            beat_value, _ = chords_beat.next()
            chord = chords.next()
            while bi < beat_index + beat_value:
                chordindex=note_skip.next()
                note = chord[chordindex % len(chord)]
                notes_beat_value, notes_duration_value = notes_beat.next()
                self.midi.addNote(track, track, note, bi, notes_duration_value, velocities.next())
                bi += notes_beat_value
            beat_index += beat_value
        
        
    def write(self):
        binfile = open(self.filename, 'wb')
        self.midi.writeFile(binfile)
        binfile.close()

