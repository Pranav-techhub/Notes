from datetime import datetime
class Note:
    def __init__(self, noteID, title, content):
        self.noteID = noteID
        self.title = title
        self.content = content
        self.pin = False
        self.created_at = datetime.now()

    def __str__(self):
        return f"[{self.noteID}] -- {self.title} -- {self.content} -- {self.pin} -- {self.created_at}"