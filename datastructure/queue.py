class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def print_queue(self):
        print(self.items)


if __name__ == "__main__":
    q = Queue()
    q.enqueue("a")
    q.enqueue("b")
    q.enqueue("42")
    q.print_queue()

    q.dequeue()
    q.print_queue()
