class Task:

    def __init__(self, id=None, title="", status="Pending"):

        self.id = id
        self.title = title
        self.status = status

    def to_dict(self):

        return {
            "id": self.id,
            "title": self.title,
            "status": self.status
        }
        
        
