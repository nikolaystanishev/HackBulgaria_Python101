import unittest
from ll import *


class LinkedListTest(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedList()
        self.node1 = Node(2)
        self.node2 = Node(5)
        self.node3 = Node(7)
        self.ll.add_element(self.node1)
        self.ll.add_element(self.node2)

    def test_adding_element(self):
        self.assertEqual(self.ll.size(), 2)
        self.assertEqual(self.ll.head, self.node1)
        self.assertEqual(self.ll.tail, self.node2)

    def test_index(self):
        self.assertEqual(self.ll.index(0), self.node1)

    def test_remove_element(self):
        size = self.ll.size()
        self.ll.remove(0)
        size2 = self.ll.size()
        self.assertFalse(size == size2)
        self.assertEqual(self.ll.head, self.node2)
        with self.assertRaises(Exception):
            self.ll.remove(-1)
        with self.assertRaises(Exception):
            self.ll.remove(1)
        self.ll.add_element(self.node2)

    def test_pprint(self):
        self.assertEqual(self.ll.pprint(), '2->5')
        self.ll.remove(1)
        self.assertEqual(self.ll.pprint(), '2')
        self.ll.add_element(self.node2)

    def test_to_list(self):
        self.assertEqual(self.ll.to_list(), [2, 5])
        self.ll.remove(1)
        self.assertEqual(self.ll.to_list(), [2])
        self.ll.add_element(self.node2)

    def test_add_at_index(self):
        self.ll.add_at_index(1, self.node3)
        self.assertEqual(self.ll.size(), 3)
        self.assertEqual(self.ll.index(1).value, self.node3.value)

    def test_add_first(self):
        self.ll.add_first(self.node3)
        self.assertEqual(self.ll.size(), 3)
        self.assertEqual(self.ll.index(0).value, self.node3.value)

    def test_add_list(self):
        self.ll.add_list([2, 3])
        self.assertEqual(self.ll.size(), 4)
        self.assertEqual(self.ll.index(2).value, 2)
        self.assertEqual(self.ll.index(3).value, 3)

    def test_add_linked_list(self):
        ll1 = LinkedList()
        ll1.add_element(self.node1)
        ll1.add_element(self.node2)
        self.ll.add_linked_list(ll1)
        self.assertEqual(self.ll.size(), 4)
        self.assertEqual(self.ll.index(2).value, 2)
        self.assertEqual(self.ll.index(3).value, 5)

    def test_add_linked_list(self):
        ll1 = LinkedList()
        ll1.add_element(self.node1)
        ll1.add_element(self.node2)
        self.ll.add_linked_list(ll1)
        self.ll.ll_from_to(1, 2)
        self.assertEqual(self.ll.size(), 4)
        self.assertEqual((self.ll.ll_from_to(1, 2)).head, self.ll.index(1))
        self.assertEqual((self.ll.ll_from_to(1, 2)).tail, self.ll.index(2))

    def test_pop(self):
        self.ll.pop()
        self.assertEqual(self.ll.size(), 1)
        self.assertEqual(self.ll.tail.value, 2)

    def test_reduce_to_unique(self):
        node4 = Node(2)
        self.ll.add_element(node4)
        self.ll.reduce_to_unique()
        self.assertEqual(self.ll.size(), 2)
        self.assertEqual(self.ll.head.value, 2)
        self.assertEqual(self.ll.tail.value, 5)


if __name__ == '__main__':
    unittest.main()
