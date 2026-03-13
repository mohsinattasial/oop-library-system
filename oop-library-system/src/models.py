from dataclasses import dataclass, field
from typing import Set, Optional
from abc import ABC, abstractmethod
from datetime import date

# ---------- Fine Policy ----------

class FinePolicy(ABC):

    @abstractmethod
    def calculate(self, days_late: int) -> float:
        pass


class SimpleFinePolicy(FinePolicy):

    def __init__(self, per_day: float = 5.0):
        self.per_day = per_day

    def calculate(self, days_late: int) -> float:
        if days_late <= 0:
            return 0.0
        return days_late * self.per_day


# ---------- Book ----------

@dataclass
class Book:
    book_id: str
    title: str
    author: str
    __available: bool = field(default=True, repr=False)

    def borrow(self) -> None:
        if not self.__available:
            raise ValueError("Book is not available")
        self.__available = False

    def return_book(self) -> None:
        self.__available = True

    def is_available(self) -> bool:
        return self.__available


# ---------- Member ----------

@dataclass
class Member:
    member_id: str
    name: str
    __borrowed_books: Set[str] = field(default_factory=set, repr=False)

    def borrow_book(self, book_id: str, limit: int = 3) -> None:

        if len(self.__borrowed_books) >= limit:
            raise ValueError("Borrow limit reached")

        self.__borrowed_books.add(book_id)

    def return_book(self, book_id: str) -> None:

        if book_id not in self.__borrowed_books:
            raise ValueError("Book not borrowed by this member")

        self.__borrowed_books.remove(book_id)

    @property
    def borrowed_books(self) -> Set[str]:
        return set(self.__borrowed_books)


# ---------- Borrow Record ----------

@dataclass
class BorrowRecord:
    member_id: str
    book_id: str
    borrow_date: date
    return_date: Optional[date] = None