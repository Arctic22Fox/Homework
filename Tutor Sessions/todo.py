class todo:
    def __init__(self):
        self.todos = []
        self.completed = []

    def add_todo(self, todo):
        self.todos.append(todo)

    def completed_task(self, todo):
        self.completed.append(todo)
        self.todos.remove(todo)

    def list_todos(self):
        return self.todos

    def list_completed(self):
        return self.completed