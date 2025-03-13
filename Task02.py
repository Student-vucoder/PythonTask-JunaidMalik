#part 1
books = {}
# Adding books
books["969-416-123-4"] = ("Peer-e-Kamil", "Umera Ahmed", 950, {"fiction", "spiritual"})
books["978-1-4028-9462-6"] = ("Python Programming", "Jane Smith", 800, {"education", "technology"})
books["969-416-222-1"] = ("Haalim", "Nimra Ahmed", 1050, {"mystery", "thriller"})

# Printing the dictionary
print(books)

#Part 2
def search_by_author(author):
    result = []
    for isbn, book_info in books.items():  
        if book_info[1] == author:
            result.append((isbn, book_info[0]))  # (ISBN, Title)
    return result
print(search_by_author("Nimra Ahmed"))

#Part 3

def update_price(isbn, new_price):
    if isbn in books:  
        title, author, _, genres = books[isbn] 
        books[isbn] = (title, author, new_price, genres)  
print("Before update:", books["969-416-222-1"])  
update_price("969-416-222-1", 999)  
print("After update:", books["969-416-222-1"])  

#Part 4
def standardize_genres():
    for isbn, book_info in books.items(): 
        title, author, price, genres = book_info  
        cleaned_genres = {genre.strip().lower() for genre in genres}
        books[isbn] = (title, author, price, cleaned_genres)
standardize_genres()
print(books)

#Part 5
def display_inventory():
    print("\n{:<20} | {:<25} | {:<20} | {:<8} | {:<30}".format(
        "ISBN", "Title", "Author", "Price", "Genres"))
    print("-" * 110)  # Print a separator line

    for isbn, book_info in books.items(): 
        title, author, price, genres = book_info  
        genre_list = ", ".join(genres)  
        print("{:<20} | {:<25} | {:<20} | {:<8} | {:<30}".format(
            isbn, title, author, price, genre_list))
# Run the function
display_inventory()

#Part 6
def list_all_books():
    book_titles = [book_info[0] for book_info in books.values()]  
    book_titles.sort()  
    return book_titles  
# Run the function and print the result
sorted_books = list_all_books()
print(sorted_books)


