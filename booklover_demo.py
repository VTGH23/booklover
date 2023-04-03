import booklover_dir
from booklover_dir import booklover

test_1_object = booklover.BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
test_1_object.add_book("Test book", 6)
print(test_1_object.num_books_read())