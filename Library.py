from collections import Counter

"""
Class Library has Add book, display book options
All the methods inside the Library class   have private variables, which only a Library class can access

"""

class Library:
    def __init__(self,bookList):
        self.__bookList=bookList
        self.addToOriginalBookList(self.__bookList)


    def getBookNametoAdd(self):
        __bookName = input("Enter a book name to add:")
        self.addBook(__bookName)
    def getBookNametoRemove(self):
        __bookName = input("Enter a book name to Remove:")
        self.dismissBook(__bookName)

    # def checkAvailability(self,__bookName):
    #     if __bookName in self.__bookList:
    #         return "Available"
    #     elif __bookName not in self.__bookList:
    #         return "Not available"

    def addBook(self,__bookName):
        if self.__bookList.append(__bookName)==None:
            print("'{}' added successfully! ".format(__bookName))
            self.addToOriginalBookList(self.__bookList)

    def printBookList(self):
        __bookCount=Counter(self.__bookList)
        __bookStatus=__bookCount.most_common()
        print("Book Name".ljust(40),"-","Available".rjust(10))
        print("*"*50)
        for bookName,count in __bookStatus:
            print("{0:40s} - {1:3d}".format(bookName,count))

    def dismissBook(self,__bookName):
        try:
            if self.__bookList.remove(__bookName)==None:
                print("'{}' removed successfully! ".format(__bookName))
        except ValueError:
            print("'{}' does not exit/all copies are removed, please enter the exist book name [see below for reference] ".format(__bookName))
            self.printBookList()
            self.getBookNametoRemove()


    def borrowBook(self,__bookName):
        if self.__bookList.remove(__bookName)==None:
            print("'{}' borrowed successfully! ".format(__bookName))

    def addBorrowedBook(self, __bookName):
        if self.__bookList.append(__bookName) == None:
            print("'{}' returned successfully! ".format(__bookName))

    def addToOriginalBookList(self,__bookList):
        self.originalBookList=set(__bookList)

    def checkInOriginalBookList(self,__bookName):
        if __bookName in self.originalBookList:
            return "Original"
        else:
            return "Duplicate"








