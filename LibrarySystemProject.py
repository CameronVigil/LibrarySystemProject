#Cameron Vigil
#Library System

import pymysql
import sqlalchemy
from sqlalchemy import Column, Integer, Unicode, UnicodeText, String, Sequence
from random import choice
import string
from library import book
from customers import customer
from transactions import transaction
import base
from base import Session, Base, engine


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    session = Session()

    #main menu system
    choice = -1
    while choice != 4:
        print("Main Menu\n")
        print("[1] Library")
        print("[2] Customers")
        print("[3] Transactions")
        print("[4] Exit")
        choice = int(input())
        if choice == 1:
            book.menu()
        elif choice == 2:
            customer.menu()
            pass
        elif choice == 3:
            transaction.menu()
            pass
        elif choice == 4:
            print("Program exited.\n")
        else:
            print("Error, please try again.\n")

    for i in book.Books:
        session.add(i)
    
    session.commit()
    session.close()