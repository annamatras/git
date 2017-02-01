class TodoItem:
    def __init__(self, name):
        self.name = name
        self.state = False

    def toggle_done(self):
        self.state = True


class Todo:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.pop(item)

    def list_items(self):
        if len(self.items) > 0:
            n = 1
            while n <= len(self.items):
                print(str(n) + '.', self.items[n-1].name, self.items[n-1].state)
                n += 1
        else:
            print("\nYou are soo free !!! No tasks to do here ;)")
