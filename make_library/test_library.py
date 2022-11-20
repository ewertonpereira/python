import unittest
from Tools import get_author_book


class TestBookCase(unittest.TestCase):
    
    def setUp(self) -> None:
        self.get_author_book = get_author_book()


    def test_get_author_book(self):
        result = self.get_author_book
        #print(result)
        self.assertEqual(result, 'EWERTON')
        
        
if __name__ == '__main__':
    unittest.main()
