from data import data_list
from book import Book


def run_analysis(book_list):
    books = create_book_list(book_list)
    # print('')
    # print("*******************************************************************")
    # print('')
    # example_analysis(books)
    # print('')
    # print("*******************************************************************")
    # print('')
    # analysis_one(books)
    # print('')
    # print("*******************************************************************")
    # print('')
    # analysis_two(books)
    # print('')
    # print("*******************************************************************")
    # print('')
    # analysis_three(books)
    # print('')
    # print("*******************************************************************")
    # print('')
    # bonus_analysis_one(books)
    # print('')
    # print("*******************************************************************")
    # print('')
    bonus_analysis_two(books)
    # print('')
    # print("*******************************************************************")
    # print('')
    # bonus_analysis_three(books)


def create_book_list(data_list):
    book_list = []
    
    for book in data_list:
        new_book = Book (book)
        book_list.append (new_book)
    

    return book_list


# def example_analysis(book_list):
    print("Analysis of which book had the highest price in 2016")
    # Find all books from 2016
    # Use a Lambda filter function to find books who have a year of 2016
    # Converting to a list, and saving as variable books_2016
    books_2016 = list(filter(lambda book: book.year == 2016, book_list))
    # Calculating the maximum price, and saving that book as highest_cost_books
    # Using max(), with Lambda function
    highest_cost_book = max(books_2016, key=lambda book: book.price)
    # Print that book's name & price to terminal
    print(f"The most expensive book in 2016 was {highest_cost_book.name} with a price of {highest_cost_book.price}")

# def analysis_one(book_list):
    print("Analysis of which book had the lowest number of reviews in 2018")
    books_2018 = list (filter(lambda book: book.year == 2018, book_list))
    lowest_number_of_reviews = min(books_2018, key=lambda book: book.number_of_reviews)
    print (f"The book with the lowest number in reviews in 2018 is: {lowest_number_of_reviews.name} with {lowest_number_of_reviews.number_of_reviews} reviews!")

# def analysis_two(book_list):
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
    
    print (f"Top Genre: {most_genre_appearances ['genre']}.  Frequency: {most_genre_appearances ['count']}") 
    
# def analysis_three(book_list):
    print("Analysis of which book has appeared the most in the top 50's list, and how many times it has appeared")
    book_name_list = [book.name for book in book_list]
    distinct_book_names = set (book_name_list)
    most_book_appearances = {"name": "",
                            "count" : 0}
    for book_name in distinct_book_names:
        matching_books = list (filter(lambda book: book.name == book_name, book_list ))
        book_frequency = len(matching_books) 
        if book_frequency > most_book_appearances ["count"]:
            most_book_appearances ["name"] = book_name 
            most_book_appearances ["count"] = book_frequency                       
    
    print (f"Book Title: {most_book_appearances ['name']}.  Frequency: {most_book_appearances ['count']}")

# # BONUS USER STORIES:


# def bonus_analysis_one(book_list):
    print("Analysis of which author has shown up on the top 50's list the most (Distinct books only!)")
    author_name_list = [book.author for book in book_list]
    distinct_author = set (author_name_list)
    most_author_appearances = {"author" : "",
                               "count": 0}
    for author in distinct_author:
        matching_author = list (filter(lambda book: book.author == author, book_list))
        book_name_list = [book.name for book in matching_author]
        distinct_book = set (book_name_list)
        author_frequency = len(distinct_book)
        if author_frequency > most_author_appearances ["count"]:
            most_author_appearances ["author"] = author
            most_author_appearances ["count"] = author_frequency

#     print(f"The author who has appeared the most for distinct books is {most_author_appearances ['author']} with {most_author_appearances ['count']} different books!")

# def bonus_analysis_two (book_list):
#     print("Analysis of the top book for each year, based on the book's user ratings and number of reviews")

#     user_rating_list = list(filter(lambda book: book.user_rating, book_list))
#     sorted_user_rating = sorted(user_rating_list, key = lambda book: book.user_rating)
    
#     review_list = list(filter(lambda book: book.number_of_reviews, sorted_user_rating))
#     sorted_review_list = (sorted(review_list, key = lambda book: book.number_of_reviews))
    
#     year_list = list(filter(lambda book: book.year, sorted_review_list))
#     sorted_year_list = list(sorted(year_list, key = lambda book: book.year))
#     for year in sorted_year_list:
#         print(f"{year.year} {year.name}")
    

# def bonus_analysis_three(book_list):
#     print("Analysis of which book has appeared the most consecutively on top 50's list")
        


run_analysis(data_list)