from todo import Todo
from todo_item import TodoItem


def main():
    todo = Todo()
    while True:
        print("How can I help you?\n")
        print("1.Add task\n"
              "2.List tasks\n"
              "3.Toggle done\n"
              "4.Remove task\n"
              "0.Exit\n")
        number = input("\nPlease select number: ")
        if number == "1":
            item = TodoItem(input("\nPlease add a task: "))
            todo.add_item(item)
            print("\nTask added.")
        elif number == "2":
            print("\nItems list: ")
            todo.list_items()
        elif number == "3":
            todo.list_items()
            done = input("\nChoose a number for task which is done?: ")
            todo.items[int(done) - 1].toggle_done()
            todo.list_items()
        elif number == "4":
            todo.list_items()
            remove = input("\nChoose a number for task to remove: ")
            removed = int(remove) - 1
            todo.remove_item(removed)
            todo.list_items()
        elif number == "0":
            print("\nGoodbye!")
        else:
            print("Please choose a valid option.")


if __name__ == "__main__":
    main()
