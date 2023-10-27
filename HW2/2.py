# linked List implementation

class Linkedlistnode:
    def __init__(self, val, next):
        self.value = val
        self.next = next


class Linked_list:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        self.head = Linkedlistnode(data, self.head)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Linkedlistnode(data, None)
            return
        itr = self.head
        while itr:
            itr = itr.next
        itr.next = Linkedlistnode(data, None)


    def insert_at_index(self, data, index):
        if index == 0:
            self.insert_at_beginning(data)
            return
        count = -1
        itr = self.head
        while itr:
            count += 1
            if count == index-1:
                itr.next = Linkedlistnode(data, itr.next)
                break
            itr = itr.next

    def print(self):
        if self.head is None:
            print("Linked List is empty!")
        else:
            itr = self.head
            llstr = ""
            while itr:
                llstr += str(itr.value) + "-->"
                itr = itr.next
            print(llstr)


s = Linked_list()

s.insert_at_beginning(100)
s.print()
s.insert_at_beginning(101)
s.print()
s.insert_at_beginning(102)
s.print()
s.insert_at_beginning(103)
s.print()
s.insert_at_end(104)
s.print()
s.insert_at_index(105,0)
s.print()
s.insert_at_index(106,2)
s.print()
