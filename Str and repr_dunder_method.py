class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

   
    def __str__(self):
        return f"Book: {self.title} by {self.author} - ₹{self.price}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.price})"



book1 = Book("Python Basics", "Hampana", 499)
book2 = Book("OOP Concepts", "John", 599)


print(book1)
print(book2)

book_list = [book1, book2]
print(book_list)