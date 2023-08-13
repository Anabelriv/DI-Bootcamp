# response = requests.get("https://www.googleapis.com/books/v1/volumes?q=python")
# data = response.json()

# for item in data["items"]:
#     book_data = item["volumeInfo"]
#     Book.objects.create(
#         title=book_data["title"],
#         author=", ".join(book_data["authors"]),
#         published_date=book_data.get("publishedDate", None),
#         description=book_data.get("description", ""),
#         page_count=book_data.get("pageCount", 0),
#         categories=", ".join(book_data.get("categories", [])),
#         thumbnail_url=book_data["imageLinks"]["thumbnail"]
#         if "imageLinks" in book_data
#         else "",
#     )

import os
import requests

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "books_project.settings")
import django

django.setup()
from books.models import Book
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime


def populate_books_from_google_books(search_terms):
    url = f"https://www.googleapis.com/books/v1/volumes?q={search_terms}"

    try:
        response = requests.get(url)
        data = response.json()

        for item in data.get("items", []):
            volume_info = item.get("volumeInfo", {})
            title = volume_info.get("title", "")
            authors = volume_info.get("authors", [])
            published_date = volume_info.get("publishedDate", "")
            description = volume_info.get("description", "")
            page_count = volume_info.get("pageCount", 0)
            categories = volume_info.get("categories", [])
            thumbnail_url = volume_info.get("imageLinks", {}).get("thumbnail", "")

            # Convert published_date to the correct format if it's not already
            try:
                parsed_date = datetime.strptime(published_date, "%Y-%m-%d").date()
            except ValueError:
                # Handle invalid date format here (if needed)
                continue

            try:
                book = Book.objects.get(title=title, published_date=parsed_date)
            except ObjectDoesNotExist:
                book = Book(
                    title=title,
                    author=", ".join(authors),
                    published_date=published_date,
                    description=description,
                    page_count=page_count,
                    categories=", ".join(categories),
                    thumbnail_url=thumbnail_url,
                )
                book.save()
                print(f"Added new book: {book.title}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


# Call the function with search terms of your choice
search_terms = "python"  # Replace with your desired search terms
populate_books_from_google_books(search_terms)
