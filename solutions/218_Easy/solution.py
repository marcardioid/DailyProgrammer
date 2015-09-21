class ToDoList(object):
    def __init__(self):
        self.data = []

    def addItem(self, item):
        if item not in self.data:
            self.data.append(item)
            print("Item added.")
        else :
            print("Item already exists.")

    def deleteItem(self, item):
        try:
            self.data.remove(item)
            print("Item deleted.")
        except ValueError:
            print("Item was not found.")

    def view(self):
        print("--------------TO-DO LIST--------------")
        for i, item in enumerate(self.data, 1):
            print(str(i) + '\t' + item)

if __name__ == "__main__":
    verbose = False
    todolist = ToDoList()
    todolist.addItem("Make a better to-do list.")
    todolist.addItem("Seriously.")
    todolist.deleteItem("Make a better to-do list.")
    todolist.deleteItem("Seriously.")
    todolist.addItem("This is the best to-do list ever!!")
    todolist.view()