from View.noteview import NoteView
from Service.noteservice import NoteService
from Controller.notecontroller import NoteController

if __name__ == "__main__":
    view = NoteView()
    service = NoteService()
    controller = NoteController(view, service)
    controller.start()