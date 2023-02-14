
from asyncio import exceptions
import time

class BalanceExceptionError(Exception):
    pass

class AttempExceptonError(Exception):
    pass
attempts=1
def withdraw():
    global attempts
    save_pin=123
    balance=10000 # hard -code
    pin=int(input("Enter the pin "))
    if pin==save_pin:
        try:
            amt=float(input("Enter amount to withdraw:"))
            tempery_blance=balance-amt
            if tempery_blance<1000:
                raise BalanceExceptionError("Insuficient blance")
            balance=balance-amt
            print("Remained balance is",balance)
        except Exception as var:
            print(var)
    else:
            asn=input(" worng Pin ,do you want to continue again (y/n): ")
            if  asn.lower()=='y':
                attempts+=1
                try:
                    if attempts==4:
                        raise AttempExceptonError("too many attempts, your account  is blocked for an hour")
                except Exception  as var:
                    print(var)
                    time.sleep(100)
                else:
                    withdraw()
            else:
                    print("thank you !")
                    return
withdraw() 
