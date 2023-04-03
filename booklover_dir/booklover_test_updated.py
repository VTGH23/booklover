from booklover import BookLover
import pandas as pd
import unittest

class BookLoverTestSuite(unittest.TestCase):
    def test_1_add_book(self): 
        #add a book and test if it's in book list
        test_1_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_1_object.add_book("War of the Worlds", 4)
        
        self.assertTrue("War of the Worlds" in test_1_object.book_list['book_name'].unique())

    def test_2_add_book(self):
        #add the same book twice. test if it's in book list once
        test_2_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_2_object.add_book("War of the Worlds", 4)
        test_2_object.add_book("War of the Worlds", 4)

        expected = 1
        self.assertEqual(len(test_2_object.book_list['book_name']), expected)
    
    def test_3_has_read(self):
        #pass a book in the list and test the answer is True
        test_3_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_3_object.add_book("War of the Worlds", 4)
        self.assertTrue(test_3_object.has_read("War of the Worlds"))

    def test_4_has_read(self):
        #pass a book NOT in the list and use assert False to test if the answer is True
        test_4_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_4_object.add_book("War of the Worlds", 4)
        self.assertFalse(test_4_object.has_read("Some Other Book"))

    def test_5_num_books_read(self):
        #add some books to the list, and test num_books matches expected
        test_5_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_5_object.add_book("The Eye of the World", 7)
        test_5_object.add_book("The Great Hunt", 8)
        test_5_object.add_book("The Dragon Reborn", 6)

        expected = 3
        self.assertEqual(test_5_object.num_books_read(), expected)

    def test_6_fav_books(self): 
        #add some books with ratings to the list, making sure some of them have rating > 3. Check that the returned books have rating > 3
        test_6_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_6_object.add_book("The Eye of the World", 7)
        test_6_object.add_book("The Great Hunt", 1)
        test_6_object.add_book("The Dragon Reborn", 2)
        test_6_object.add_book("The Shadow Rising", 5)
        test_6_object_fav_books = test_6_object.fav_books()
        mask = test_6_object_fav_books['book_rating'] > 3
        mask_all = mask.all()
        self.assertTrue(mask.all())


if __name__ == '__main__':
    
    unittest.main(verbosity=3)
