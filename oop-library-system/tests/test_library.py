import unittest
from datetime import date
from src.library import Library
from src.models import SimpleFinePolicy


class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library(SimpleFinePolicy())
        self.library.add_book("1", "Python", "Guido")
        self.library.add_member("M1", "Ali")

    def test_add_book(self):
        self.library.add_book("2", "Java", "James")
        self.assertEqual(len(self.library.books), 2)

    def test_add_member(self):
        self.library.add_member("M2", "Ahmed")
        self.assertEqual(len(self.library.members), 2)

    def test_borrow_book(self):
        self.library.borrow_book("M1", "1", date.today())
        self.assertFalse(self.library.books["1"].is_available())

    def test_return_book(self):
        self.library.borrow_book("M1", "1", date.today())
        fine = self.library.return_book("M1", "1", date.today())
        self.assertEqual(fine, 0)

    def test_borrow_limit(self):

        self.library.add_book("2","A","A")
        self.library.add_book("3","B","B")
        self.library.add_book("4","C","C")

        self.library.borrow_book("M1","1",date.today())
        self.library.borrow_book("M1","2",date.today())
        self.library.borrow_book("M1","3",date.today())

        with self.assertRaises(ValueError):
            self.library.borrow_book("M1","4",date.today())


    def test_borrow_limit_does_not_mark_extra_book_as_borrowed(self):
        for book_id in ("2", "3", "4"):
            self.library.add_book(book_id, book_id, "Test Author")
        for book_id in ("1", "2", "3"):
            self.library.borrow_book("M1", book_id, date.today())
        with self.assertRaises(ValueError):
            self.library.borrow_book("M1", "4", date.today())
        self.assertTrue(self.library.books["4"].is_available())
        self.assertNotIn("4", self.library.members["M1"].borrowed_books)

    def test_invalid_member(self):

        with self.assertRaises(KeyError):
            self.library.borrow_book("X","1",date.today())

    def test_invalid_book(self):

        with self.assertRaises(KeyError):
            self.library.borrow_book("M1","X",date.today())

    def test_return_not_borrowed(self):

        with self.assertRaises(ValueError):
            self.library.return_book("M1","1",date.today())


if __name__ == "__main__":
    unittest.main()