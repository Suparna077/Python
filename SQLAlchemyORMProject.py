from sqlalchemy.orm import Session,Relationship,registry
from sqlalchemy import create_engine, select
from sqlalchemy import Column,Integer,String,DATETIME,Float,ForeignKey,Boolean,Text,ScalarResult
from urllib.parse import quote

engine = create_engine('postgresql+psycopg2://postgres:%s@localhost/red30' %quote('Rodopsin@7'))
Mapper_Registry = registry()
Base = Mapper_Registry.generate_base()


class Author(Base):
    __tablename__ = 'authors'
    author_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    def __repr__(self):
        return "<Author(author_id = '{0}' , first_name = '{1}' , last_name = '{2}' )>" \
            .format(self.author_id, self.first_name, self.last_name)


class Books(Base):
    __tablename__ = 'books'
    author_id = Column(Integer, primary_key=True)
    book_id = Column(Integer, primary_key=True)
    title = Column(String)
    number_of_pages = Column(String)

    def __repr__(self):
        return "<Books(author_id = '{0}' , book_id = '{1}' , title = '{2}' , number_of_pages = '{3}' )>" \
            .format(self.author_id, self.book_id, self.title, self.number_of_pages)

Base.metadata.create_all(engine)

def importtotable(Author_firstname , Author_lastname , Book_title , NumbOfPages):

    with Session(engine) as session :

        Booksearch = session.execute(select(Books).filter(Books.title == Book_title , Books.number_of_pages == NumbOfPages )).scalar()
        if Booksearch is not None :
            print("Book Already Exsists : ")
        else:
            print("Book Does not exsists adding new book : ")
            Authorsearch = session.execute(select(Author).filter(Author.first_name == Author_firstname , Author.last_name == Author_lastname)).scalar()
            if Authorsearch is not None :
                Bookidsearch = session.execute(select(Books).filter(Books.author_id == Authorsearch.author_id).order_by(Books.author_id.desc())).scalar()
                if Bookidsearch is not None:
                    Bookid = Bookidsearch.book_id + 1
                else:
                    Bookid = 1
                Bookinstance = Books(author_id = Authorsearch.author_id , book_id = Bookid , title = Book_title , number_of_pages = NumbOfPages)
                session.add(Bookinstance)
            else:
                Newauthorid = session.execute(select(Author).order_by(Author.author_id.desc())).scalar()
                if Newauthorid is not None:
                    Authorid = Newauthorid.author_id + 1
                else:
                    Authorid = 1
                Authorinstance = Author(author_id = Authorid, first_name = Author_firstname , last_name = Author_lastname)
                Bookinstance = Books(author_id=Authorid, book_id= 1, title=Book_title,number_of_pages=NumbOfPages)
                session.add(Authorinstance)
                session.add(Bookinstance)
        session.commit()




def main():

    Author_FirstName = input("Enter The First Name Of The Author: ")
    Author_LastName = input("Enter The Last Name Of The Author: ")
    Book_title = input("Enter The Book Title : ")
    NumberOfPages = input("Enter the number of pages of the book : ")
    importtotable(Author_FirstName,Author_LastName,Book_title,NumberOfPages)
    PrintdataLoadedauthor = Session(engine).execute(select("*").select_from(Author)).fetchall()
    PrintdataLoadedbook = Session(engine).execute(select("*").select_from(Books)).fetchall()
    print("--------------------------Author----------------------------\n")
    print(PrintdataLoadedauthor)
    print("--------------------------Books----------------------------\n")
    print(PrintdataLoadedbook)


if __name__ == "__main__":
    main()