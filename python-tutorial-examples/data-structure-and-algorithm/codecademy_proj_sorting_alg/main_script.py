import utils_opening_csv as utils
from sorting_algorithms import bubble_sort, quicksort

bookshelf = utils.load_books('books_small.csv')
bookshelf_large = utils.load_books('books_large.csv')

# for book in bookshelf:
#     print(book['title'])

# print(ord('a'))
# print(ord('b'))
# print(ord('a') < ord('b'))


def by_title_ascending(book_a, book_b):
    return book_a['title_lower'] > book_b['title_lower']


def by_author_ascending(book_a, book_b):
    return book_a['author_lower'] > book_b['author_lower']


bookshelf_v1 = bookshelf
bookshelf_v2 = bookshelf

sort_1 = bubble_sort(bookshelf, by_title_ascending)

print('------\nbubble sorted by title ascending:\n-----')
for idx, book in enumerate(sort_1):
    print(book['title'])
    if idx == len(sort_1)-1:
        print('----')


sort_2 = bubble_sort(bookshelf_v1, by_author_ascending)

print('------\nbubble sorted by author ascending:\n-----')
for idx, book in enumerate(sort_1):
    print(book['title'] + ': ' + book['author'])
    if idx == len(sort_1)-1:
        print('----')

quicksort(bookshelf_v2, 0, len(bookshelf_v2)-1, by_author_ascending)

print('------\nquick sorted by author ascending:\n-----')
for idx, book in enumerate(bookshelf_v2):
    print(book['title'] + ': ' + book['author'])
    if idx == len(sort_1)-1:
        print('----')
