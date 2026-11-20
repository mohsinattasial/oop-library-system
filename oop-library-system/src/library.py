from typing import Dict, List
from datetime import date
from .models import Book, Member, BorrowRecord, FinePolicy


class Library:

    def __init__(self, fine_policy: FinePolicy):
        self.fine_policy = fine_policy
        self.books: Dict[str, Book] = {}
        self.members: Dict[str, Member] = {}
        self.records: List[BorrowRecord] = []

    def add_book(self, book_id: str, title: str, author: str) -> None:

        if book_id in self.books:
            raise ValueError("Book ID already exists")

        self.books[book_id] = Book(book_id, title, author)

    def add_member(self, member_id: str, name: str) -> None:

        if member_id in self.members:
            raise ValueError("Member ID already exists")

        self.members[member_id] = Member(member_id, name)

    def borrow_book(self, member_id: str, book_id: str, borrow_date: date) -> None:

        if member_id not in self.members:
            raise KeyError("Invalid member ID")

        if book_id not in self.books:
            raise KeyError("Invalid book ID")

        book = self.books[book_id]
        member = self.members[member_id]

        # Validate both constraints before updating either object.
        if not book.is_available():
            raise ValueError("Book is not available")
        if len(member.borrowed_books) >= 3:
            raise ValueError("Borrow limit reached")
        book.borrow()
        member.borrow_book(book_id)

        record = BorrowRecord(member_id, book_id, borrow_date)
        self.records.append(record)

    def return_book(self, member_id: str, book_id: str, return_date: date) -> float:

        if member_id not in self.members:
            raise KeyError("Invalid member ID")

        if book_id not in self.books:
            raise KeyError("Invalid book ID")

        book = self.books[book_id]
        member = self.members[member_id]

        # Find an active record before changing any domain object.
        record = next(
            (
                item for item in reversed(self.records)
                if item.member_id == member_id
                and item.book_id == book_id
                and item.return_date is None
            ),
            None,
        )
        if record is None or book_id not in member.borrowed_books or book.is_available():
            raise ValueError("No active borrow record found for this member and book")
        if return_date < record.borrow_date:
            raise ValueError("Return date cannot be earlier than borrow date")

        days = (return_date - record.borrow_date).days
        fine = self.fine_policy.calculate(max(0, days - 7))

        member.return_book(book_id)
        book.return_book()
        record.return_date = return_date
        return fine
