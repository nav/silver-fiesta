import random
import pytest
from django.db.models.functions import TruncDate
from books.models import Book, Author


@pytest.mark.django_db
class TestBooks:
    @pytest.fixture
    def author(self):
        name=f"Author {random.randint(1000,9999)}"
        return Author.objects.create(
            name=name,
            email=f"{name.lower().replace(' ', '_')}@example.com"
        )

    @pytest.fixture
    def book(self, author):
        title = f"Book {random.randint(1000, 9999)}"
        book = Book.objects.create(title=title)
        book.authors.add(author)
        return book


    def test_can_fetch_book(self, book):
        book = Book.objects.first()
        assert book


    def test_can_truncdate(self, book):
        book = Book.objects.annotate(x_created_date=TruncDate('created_date')).first()
        assert book.x_created_date == book.created_date

