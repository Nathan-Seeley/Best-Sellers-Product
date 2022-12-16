from data import data_list
from book import Book

def run_analysis(book_list):
    books = create_book_list(book_list)
    analysis_two(books)   

def create_book_list(data_list):
    book_list = []
    
    for book in data_list:
        new_book = Book (book)
        book_list.append (new_book)
    

    return book_list

def analysis_two(book_list):
    print("Analysis of which genre (fiction or non-fiction) has appeared the most in the top 50's list")
    book_genre_list =[book.genre for book in book_list]
    most_genre_appearances = {"genre": "",
                              "count": 0}
    for genre in book_genre_list:
        matching_genre = list (filter(lambda book: book.genre == genre, book_list))
        matching_frequency = len(matching_genre)
        if matching_frequency > most_genre_appearances ["count"]:
            most_genre_appearances ["genre"] = genre
            most_genre_appearances ["count"] = matching_frequency