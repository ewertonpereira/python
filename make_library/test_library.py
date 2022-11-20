# from unittest import mock, TestCase
# from tools import get_author_book


# class TestBookCase(TestCase):
    
#     # @mock.patch('tools.get_author_book', return_value='ewerton')
#     # def test_get_author_book(self, author):
#     #     self.assertEqual(get_author_book(), 'ewerton')
        
#     @mock.patch('tools.get_author_book', side_effect=[
#         'ewerton',
#         'eduardo',
#         'kerlen'
#      ])
#     def test_get_author_book(self, author):
#         self.assertEqual(get_author_book(), 'ewerton')
#         self.assertEqual(get_author_book(), 'eduardo')
#         self.assertEqual(get_author_book(), 'kerlen')
        
        
# if __name__ == '__main__':
#     unittest.main()
