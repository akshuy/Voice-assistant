# create a libariry
# display book
# lend book
# add book
# return book

# akshar=libarary(list of books ,libarary name)




from unicodedata import name


class Libariry:
    def __init__(self,list,name):
        self.bookslist=list
        self.name=name
        self.lendict={}


    def displaybook(self) :
        print(f"we have following books in libarary : {self.name}")
        for book in self.bookslist:
            print(book)

    def lendbook(self,user,book):
        if book not in self.lendict.keys():
            self.lendict.update({book:user})
            print("lendar book database has been updated . you can take the book now ")
        else:
            print(f"book is alredy used by {self.lendict[book]}")    



    def addbook(self,book):
        self.bookslist.append(book)
        print("book has been add to the book list  ")

    def returnbook(self,book):
        self.lendict.pop(book)

if __name__=="__main__":
    akshay= Libariry(["python","rich daddy poor daddy","harry poter","c++","algo with clrs"],"akshay sharma")       
    while(True):
        print(f"welcome to the {akshay.name} libarary . Enter your choice to continue  " )
        print("\t\t1. displaybook")
        print("\t\t2. leand a book")
        print("\t\t3. add a book")
        print("\t\t4.return a book")
        user_choice= int(input())

        if user_choice==1:
            akshay.displaybook()

        elif user_choice==2:
            book= input("Enter the name of the book you want to lend : ")
            user=input("Enter your name ")
            akshay.lendbook(user,book)

        elif user_choice==3:
            book=input("enter then name of book you want to add ")
            akshay.addbook(book)  


        elif user_choice==4:
            book=input("enter then name of book you want to return ")
            
            akshay.returnbook(book)    

        elif user_choice!=["1","2","3","4"]:
            print("plese choose valid option ")          

        else:
            print("not a valid option ")

        print("press Q to quite and C to continue ")
        user_choice2= ""
        while(user_choice2!="c"and user_choice2!="q"):
            user_choice2= input()
            if user_choice2=="q":
                exit()   

            elif user_choice2=="c":
                continue
