from Model.note import Note

class NoteService:
    def __init__(self):
        self.notes = []
        self.nope_id = 0

    def create_note(self, title, content):
        self.nope_id += 1
        note = Note(self.nope_id, title, content)
        self.notes.append(note)        
        return note
        
    def update_note(self, note_id, title=None, content=None):
        for note in self.notes:
            if note_id == note.noteID:
                if title:
                    note.title = title
                if content:
                    note.content = content
                return True
        return False
        
    def delete_note(self, note_id):
        for note in self.notes:
            if note_id == note.noteID:
                self.notes.remove(note)
                return True
        return False
    
    def all_notes(self):
        return self.notes
    
    def search_note(self, note_id):
        for note in self.notes:
            if note_id == note.noteID:
                return note
        return None
        
    def pin_note(self, note_id):
        for note in self.notes:
            if note_id == note.noteID:
                note.pin = True
                return True, note
        return False, None