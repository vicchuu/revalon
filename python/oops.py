


class Books:
    def __init__(self):
        self.book = None
        self.author = None
        self.id = None

    def add_book(self,b_name,a_name,id):
        self.book  = b_name
        self.author = a_name
        self.id = id

    def __str__(self):
        return f"book :{self.book} written by {self.author} with id:{self.id}"


class Members:
    def __init__(self):
        self.m_name = None
        self.book_list = []
        self.stu_id = None

    def  add_member(self,name,id):
        self.m_name = name
        self.stu_id = id

    def purchase_book(self,book_name):
        if book_name not in self.book_list:
            self.book_list.append(book_name)

    def returned_book(self,book_name):
        if book_name in self.book_list:
            self.book_list.remove(book_name)

    def __str__(self):
        return f" Member name :{self.m_name} and book list:{self.book_list}"



class Library:
    def __init__(self):
        self.lib_books =[]
        self.members_list = []

    def create_member(self,member_name,m_id):
        memb = Members()
        memb.add_member(member_name,m_id)
        self.members_list.append(memb)

    def add_books(self,b_name , author ,isbn):
        bk = Books()
        bk.add_book(b_name,author,isbn)
        self.lib_books.append(bk)

    def remove_book(self,isbn):
        for bk in self.lib_books:
            if bk.id ==isbn:
                self.lib_books.remove(bk)
                print(f"Book removed from library with id {isbn}")
                return
        print(f"this id {isbn} book not available")

    def __str__(self):
        return f"Library has {len(self.lib_books)} books and {len(self.members_list)} members."

l = Library()
l.create_member(member_name="Vishnu",m_id=2305)
l.add_books(b_name="The Great Gatsby", author="F. Scott Fitzgerald", isbn=1)
l.add_books(b_name="To Kill a Mockingbird", author="Harper Lee", isbn=2)
print(l)

