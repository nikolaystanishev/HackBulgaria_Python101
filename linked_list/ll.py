class Node:
    def __init__(self, value):
        self.value = value
        self.next_adress = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size_of_el = 0

    def add_element(self, data):
        if not self.head:
            self.head = data
            self.tail = data
        else:
            self.tail.next_adress = data
            self.tail = data
        self.size_of_el += 1

    def index(self, index):
        cur_el = self.head
        for cur_ind in range(index):
            cur_el = cur_el.next_adress
        return cur_el

    def size(self):
        return self.size_of_el

    def remove(self, index):
        if index < 0 or index >= self.size_of_el:
            raise Exception("Out of range!")
        rm_el = self.index(index)
        if rm_el == self.head:
            self.head = self.head.next_adress
        elif rm_el == self.tail:
            self.index(index - 1).next_adress = None
            self.tail = self.index(index - 1)
        else:
            self.index(index - 1).next_adress = self.index(index + 1)
        self.size_of_el -= 1

    def pprint(self):
        result = ''
        for i in range(self.size_of_el - 1):
            result += str(self.index(i).value) + '->'
        result += str(self.index(self.size_of_el - 1).value)
        return result

    def to_list(self):
        result = []
        for i in range(self.size_of_el):
            result.append(self.index(i).value)
        return result

    def add_at_index(self, index, data):
        data.next_adress = self.index(index)
        self.index(index - 1).next_adress = data
        self.size_of_el += 1

    def add_first(self, data):
        data.next_adress = self.index(0)
        self.head = data
        self.size_of_el += 1

    def add_list(self, ll: list):
        for el in ll:
            self.add_element(Node(el))

    def add_linked_list(self, ll):
        self.add_element(ll.head)
        self.tail == ll.tail
        self.size_of_el += ll.size() - 1

    def ll_from_to(self, start_index, end_index):
        ll = LinkedList()
        for i in range(start_index, end_index + 1):
            ll.add_element(self.index(i))
        return ll

    def pop(self):
        self.remove(self.size_of_el - 1)

    def reduce_to_unique(self):
        result = []
        for i in range(self.size_of_el):
            for j in range(i + 1, self.size_of_el):
                if self.index(i).value == self.index(j).value:
                    result.append(j)
        for i in sorted(list(set(result)), reverse=True):
            self.remove(i)
