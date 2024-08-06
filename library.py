class Library:
    def __init__(self,library_books_list):
        self.book_list=library_books_list
        self.available_book_list=library_books_list[:]
        self.book_lend={}
    def available_books(self):
        for i in self.available_book_list:
            print(i)
    def display_all_books(self):
        for i in self.book_list:
            print(i)
    def lend_books(self,name,book):
        if book not in self.book_list:
            print("_____________________________________________________________________________________________")
            print("|                                                                                           |")
            print("|!!!!!!!!!!!!!!!!!!!You interest book not availabe in our Library!!!!!!!!!!!!!!!!!!!!!!!!!!!|")
            print("|                                                                                           |")
            print("_____________________________________________________________________________________________")
            return
        if book in self.available_book_list:
            self.book_lend.update({book:name})
            self.available_book_list.remove(book)
            print("************You can take that book that is avialable in our library*********************************")
        else:
            print("Sorry already another take thatbook"+self.book_lend[book])
    def return_book(self,book):
        del self.book_lend[book]
        self.available_book_list.append(book)
        print("Thankyou for return book on correct time")
if __name__=="__main__":
    lib=Library(["thirugural","purananuru","silapathikaram","seevasinthaman"])
    print(" ---------------------------------------------------------------------------------- ")
    print("|                                                                                  |")
    print("|                                                                                  |")
    print("|                          Welcome to my Library                                   |")
    print("|                                                                                  |")
    print("|__________________________________________________________________________________|")
    while True:
        print("1.Display available books")
        print("2.Display all books")
        print("3.Borrow a book")
        print("4.Return a book")
        print("5.Quit")
        user_choice=int(input("Enter your choice:"))
        if user_choice==1:
            lib.available_books()
        elif user_choice==2:
            lib.display_all_books()
        elif user_choice==3:
            user_name=input("Enter your Name:")
            book_name=input("Enter which book you want:")
            lib.lend_books(user_name,book_name)
        elif user_choice==4:
            book=input("Enter book:")
            lib.return_book(book)
        elif user_choice==5:
            print("*******************************************************************")
            print("*                                                                 *")
            print("*                                                                 *")
            print("*         Thank you for visiting my Library                       *")
            print("*                                                                 *")
            print("*                                                                 *")
            print("*******************************************************************")
            break
        else:
            print("###################################################################")
            print("#                                                                 #")
            print("#       Your choice is invalid selcet correct option              #")
            print("#                                                                 #")
            print("###################################################################")