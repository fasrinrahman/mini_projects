class Task:

    def __init__(
        self,
        id=None,
        title="",
        description="",
        status="Todo",
        priority="Medium",
        category="General",
        due_date=None,
        created_at=None,
        updated_at=None
    ):

        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.category = category
        self.due_date = due_date
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):

        return {

            "id": self.id,

            "title": self.title,

            "description": self.description,

            "status": self.status,

            "priority": self.priority,

            "category": self.category,

            "due_date": self.due_date,

            "created_at": self.created_at,

            "updated_at": self.updated_at

        }