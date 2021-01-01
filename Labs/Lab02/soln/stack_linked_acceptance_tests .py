import unittest
#from stack_array import Stack
from stack_linked import Stack
from timeout_decorator import timeout

''' Add later if timing tests can be done and spec is clarified:
        Check that ALL methods are O(1)
    Add later if spec is clarified:
        None can be pushed/popped from stack'''
__unittest = True
        
        
class TestLab2(unittest.TestCase):
    @timeout(0.5)
    def test_init(self):
        stack = Stack(5)
        self.assertTrue(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(),0)

    @timeout(0.5)
    def test_is_empty(self):
        stack = Stack(5)
        self.assertTrue(stack.is_empty())
        stack.push(11)
        self.assertFalse(stack.is_empty())
        stack.pop()
        self.assertTrue(stack.is_empty())

    @timeout(0.5)
    def test_is_full(self):
        stack = Stack(5)
        self.assertFalse(stack.is_full())
        stack.push(11)
        stack.push(12)
        stack.push(13)
        stack.push(14)
        stack.push(15)
        self.assertTrue(stack.is_full())
        stack.pop()
        self.assertFalse(stack.is_full())

    @timeout(0.5)
    def test_push(self):
        stack = Stack(5)
        stack.push(11)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(), 1)
        self.assertEqual(stack.peek(), 11)
        stack.push(12)
        self.assertEqual(stack.size(), 2)
        stack.push(13)
        self.assertEqual(stack.size(), 3)
        stack.push(14)
        self.assertEqual(stack.size(), 4)
        stack.push(15)
        self.assertEqual(stack.size(), 5)
        self.assertTrue(stack.is_full())
        self.assertEqual(stack.peek(),15)
        self.assertRaises(IndexError, stack.push, 16)
        self.assertEqual(stack.size(), 5) # Make sure trying to push on full stack didn't have an effect
        self.assertTrue(stack.is_full())
        self.assertEqual(stack.peek(), 15)

    @timeout(0.5)
    def test_pop(self):
        stack = Stack(5)
        self.assertRaises(IndexError, stack.pop)
        self.assertEqual(stack.size(), 0) # Make sure trying to pop on empty stack didn't have an effect
        self.assertTrue(stack.is_empty())
        self.assertFalse(stack.is_full())
        stack.push(11)
        stack.push(12)
        stack.push(13)
        stack.push(14)
        stack.push(15)
        self.assertEqual(stack.pop(), 15)
        self.assertEqual(stack.size(), 4)
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.pop(), 14)
        self.assertEqual(stack.size(), 3)
        self.assertEqual(stack.pop(), 13)
        self.assertEqual(stack.size(), 2)
        self.assertEqual(stack.pop(), 12)
        self.assertEqual(stack.size(), 1)
        self.assertEqual(stack.pop(), 11)
        self.assertEqual(stack.size(), 0)
        self.assertTrue(stack.is_empty())

    @timeout(0.5)
    def test_peek(self):
        stack = Stack(5)
        self.assertRaises(IndexError, stack.peek)
        self.assertEqual(stack.size(), 0) # Make sure trying to peek on empty stack didn't have an effect
        self.assertTrue(stack.is_empty())
        self.assertFalse(stack.is_full())
        stack.push(11)
        self.assertEqual(stack.peek(), 11)
        self.assertEqual(stack.size(), 1)
        stack.push(12)
        self.assertEqual(stack.peek(), 12)
        self.assertEqual(stack.size(), 2)
        stack.push(13)
        self.assertEqual(stack.peek(), 13)
        self.assertEqual(stack.size(), 3)
        stack.push(14)
        self.assertEqual(stack.peek(), 14)
        self.assertEqual(stack.size(), 4)
        stack.push(15)
        self.assertEqual(stack.peek(), 15)
        self.assertEqual(stack.size(), 5)

    @timeout(0.5)
    def test_size(self):
        stack = Stack(5)
        self.assertEqual(stack.size(), 0)
        stack.push(11)
        self.assertEqual(stack.size(), 1)
        stack.push(12)
        self.assertEqual(stack.size(), 2)
        stack.push(13)
        self.assertEqual(stack.size(), 3)
        stack.push(14)
        self.assertEqual(stack.size(), 4)
        stack.push(15)
        self.assertEqual(stack.size(), 5)

    @timeout(0.5)
    def test_stack_one(self): # boundary case
        stack = Stack(1)
        self.assertRaises(IndexError, stack.pop)
        self.assertRaises(IndexError, stack.peek)
        self.assertTrue(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(),0)
        stack.push(11)
        self.assertFalse(stack.is_empty())
        self.assertTrue(stack.is_full())
        self.assertEqual(stack.size(),1)
        self.assertRaises(IndexError, stack.push, 12)
        self.assertEqual(stack.pop(),11)
        self.assertTrue(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(),0)

    @timeout(0.5)
    def test_stack_pushPopCombo_with_strings_and_floats_and_Nones(self):
        s = Stack(11)
        s.push('stuff')
        self.assertEqual(1, s.size())
        self.assertEqual('stuff', s.peek())
        self.assertFalse(s.is_empty())

        s.push(None)
        self.assertEqual(2, s.size())
        self.assertEqual(None, s.peek())

        s.pop()
        self.assertEqual(1, s.size())
        self.assertEqual('stuff', s.peek())

        s.pop()
        self.assertEqual(0, s.size())
        self.assertTrue(s.is_empty())

        s.push('stuff')
        s.push('thing')
        self.assertEqual(2, s.size())
        self.assertEqual('thing', s.peek())

        s.push(33.456)
        self.assertEqual(3, s.size())
        self.assertEqual(33.456, s.peek())

        s.push(11.123)
        self.assertEqual(4, s.size())
        self.assertAlmostEqual(11.123, s.peek())

        s.pop()
        self.assertEqual(3, s.size())
        self.assertEqual(33.456, s.peek())

        s.push(-4)
        self.assertEqual(4, s.size())
        self.assertEqual((-4), s.peek())

        s.push(89)
        self.assertEqual(5, s.size())
        self.assertEqual(89, s.peek())

        s.push(-521)
        self.assertEqual(6, s.size())
        self.assertEqual((-521), s.peek())

        s.push('blah');
        self.assertEqual(7, s.size())
        self.assertEqual('blah', s.peek())

        s.push(-9);
        self.assertEqual(8, s.size())
        self.assertEqual(-9, s.peek())

        s.push(45);
        self.assertEqual(9, s.size())
        self.assertEqual(45, s.peek())

        s.push(61);
        self.assertEqual(10, s.size())
        self.assertEqual(61, s.peek())

        s.push(None)
        self.assertEqual(11, s.size())
        self.assertTrue(s.is_full())
        self.assertEqual(None, s.peek())


        self.assertEqual(None, s.pop())
        self.assertEqual(10, s.size())
        self.assertEqual(61, s.pop())
        self.assertEqual(9, s.size())
        self.assertEqual(45, s.pop())
        self.assertEqual(8, s.size())
        self.assertEqual((-9), s.pop())
        self.assertEqual(7, s.size())
        self.assertEqual('blah', s.pop())
        self.assertEqual(6, s.size())
        self.assertEqual((-521), s.pop())
        self.assertEqual(5, s.size())
        self.assertEqual(89, s.pop())
        self.assertEqual(4, s.size())
        self.assertEqual((-4), s.pop())
        self.assertEqual(3, s.size())
        self.assertEqual(33.456, s.pop())
        self.assertEqual(2, s.size())
        self.assertEqual('thing', s.pop())
        self.assertEqual(1, s.size())
        self.assertEqual('stuff', s.pop())
        self.assertEqual(0, s.size())

    @timeout(0.5)
    def test_everything(self):
        s = Stack(100)
        for i in range(100):
            s.push(None)
            self.assertEqual(None, s.peek())
        for i in range(100):
            self.assertEqual(None, s.peek())
            self.assertEqual(None, s.pop())
            
            
        for i in range(1, 100):
            s = Stack(i)
            self.assertEqual(s.size(), 0)
            self.assertTrue(s.is_empty())
            self.assertFalse(s.is_full())
            self.assertRaises(IndexError, s.pop)
            self.assertRaises(IndexError, s.peek)
            for item in range(i):
                s.push(item)
                self.assertEqual(s.size(), item + 1)
                self.assertEqual(s.peek(), item)
                self.assertFalse(s.is_empty())
            self.assertTrue(s.is_full())
            self.assertRaises(IndexError, s.push, 100)
            for item in range(i-1, -1, -1):
                self.assertEqual(s.peek(), item)
                self.assertEqual(s.pop(), item)
                self.assertFalse(s.is_full())
                self.assertEqual(s.size(), item)
            self.assertTrue(s.is_empty)
            self.assertRaises(IndexError, s.pop)
            self.assertRaises(IndexError, s.peek)
            
    @timeout(2)
    def test_peek_size_BigO(self):
        size = 100000
        s = Stack(size)
        for i in range(size):
            self.assertEqual(i, s.size())
            s.push(i)
            self.assertEqual(i, s.peek())

    @timeout(2)
    def test_is_empty_is_full_BigO(self):
        size = 100000
        s = Stack(size)
        for i in range(size):
            self.assertFalse(s.is_full())
            s.push(i)
            self.assertFalse(s.is_empty())

    @timeout(2)
    def test_is_empty_is_full_BigO(self):
        size = 100000
        s = Stack(size)
        for i in range(size):
            s.push(i)

        for i in range(size-1, -1, -1):
            self.assertEqual(i, s.pop())

            
                        
if __name__ == '__main__': 
    unittest.main()
