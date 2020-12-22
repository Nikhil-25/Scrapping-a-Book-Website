import requests
from pages.all_books_page import AllBookPages

page_content = requests.get('http://books.toscrape.com').content
page = AllBookPages(page_content)

books = page.books

#for book in books:
#print(book)
