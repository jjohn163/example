import unittest
#from queue_linked import Queue
from queue_array import Queue

class TestLab1(unittest.TestCase):

    def test_queue_simple(self):
        q = Queue(5)
        q.enqueue(1)
        self.assertEqual(q.size(), 1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(5)
        self.assertEqual(q.size(), 5)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)
        self.assertEqual(q.dequeue(), 4)
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.dequeue(), 5)
        
    def test_queue_fill_to_capacity_and_dequeue_all(self):
        q = Queue(5)
        q.enqueue(1)
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.size(), 0)
        self.assertRaises(IndexError, q.dequeue)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(5)
        self.assertRaises(IndexError,q.enqueue,6)
        self.assertEqual(q.size(), 5)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)
        self.assertEqual(q.dequeue(), 4)
        self.assertEqual(q.dequeue(), 5)
        self.assertEqual(q.size(), 0)
        

    def test_queue_fill_to_capacity(self):
        q = Queue(5)
        q.enqueue(None)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(None)
        self.assertTrue(q.is_full())
        self.assertEqual(q.size(), 5)
        self.assertEqual(q.dequeue(), None)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)
        self.assertEqual(q.dequeue(), 4)
        self.assertEqual(q.dequeue(), None)
        
    def test_empty_queue(self):
        q = Queue(5)
        self.assertEqual(q.size(), 0)
        self.assertTrue(q.is_empty())
        self.assertFalse(q.is_full())
        self.assertRaises(IndexError, q.dequeue)
        

    def test_everything_and_big_O(self):
        size = 50000
        q = Queue(size)
        for i in range(size):
            q.enqueue(i)
        for i in range(size):
            self.assertEqual(q.dequeue(), i)
            q.enqueue(i)
            self.assertEqual(q.size(), size)
            self.assertFalse(q.is_empty())
            self.assertTrue(q.is_full())
        for i in range(size):
            self.assertEqual(q.dequeue(), i)
        self.assertTrue(q.is_empty())
        

if __name__ == '__main__': 
    unittest.main()
