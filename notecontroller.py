class NoteController:
    def __init__(self, view, service):
        self.view = view
        self.service = service

    def start(self):
        while True:
            choice = self.view.show_menu()
            if choice == "1":
                self.add_note()
            elif choice == "2":
                self.view_note()
            elif choice == "3":
                self.edit_notes()
            elif choice == "4":
                self.delete_note()
            elif choice == "5":
                self.search_note()
            elif choice == "6":
                self.pin_note()
            elif choice == "7":
                print("Thank You for using NoteApp")
                break

    def add_note(self):
        title, content = self.view.get_note_input()
        note = self.service.create_note(title, content)
        self.view.show_note_create(note)

    def view_note(self):
        notes = self.service.all_notes()
        self.view.show_all_notes(notes)

    def edit_notes(self):
        noteId = self.view.get_note_id()
        title, content = self.view.get_note_input()
        updated = self.service.update_note(noteId, title, content)
        self.view.show_note_updated(updated)

    def delete_note(self):
        noteId = self.view.get_note_id()
        deleted = self.service.delete_note(noteId)
        self.view.show_note_deleted(deleted)

    def search_note(self):
        noteId = self.view.get_note_id()
        note = self.service.search_note(noteId)
        self.view.show_searched_note(note)

    def pin_note(self):
        noteId = self.view.get_note_id()
        pinned, note = self.service.pin_note(noteId)
        self.view.pin_note(pinned, note)


