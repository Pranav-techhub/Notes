class NoteView:
    def __init__(self):
        print("---------------- Welcome to NoteApp ----------------")
    
    def show_menu(self):
        print("******** Note App Menu ********")
        print("1. Add Note")
        print("2. View Note")
        print("3. Edit Note")
        print("4. Delete Note")
        print("5. Search Note")
        print("6. Pin Note")
        print("7. Exit")
        return input("Please provide any option from above menu : ")
    
    def get_note_input(self):
        title = input("Enter title of your note:")
        content = input("Enter content to your note:")
        return title, content
    
    def get_note_id(self):
        note_id = int(input("Please enter the NoteID:"))
        return note_id
    
    def display_notes(self, notes):
        if notes:
            print(notes)
        else:
            print("Note does not exists")
        
    def show_note_create(self, note):
        print(f"Note Create: {note}")

    def show_note_updated(self, updated=False):
        if updated:
            print("Note Updated Successfully")
        else:
            print('Note not found')
    
    def show_note_deleted(self, deleted=False):
        if deleted:
            print("Note deleted Successfully")
        else:
            print('Note not found')

    def show_all_notes(self, notes=[]):
        for note in notes:
            print(note)
    
    def show_searched_note(self, note=None):
        if note:
            print(f"Searched Result: {note}")
        else:
            print('Note not found')

    def pin_note(self, pin=False, note=None):
        if pin:
            print(f"Note pinned Successfully : {note}")
        else:
            print('Note not found')

    





    

