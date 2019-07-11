#Modules Used
import pickle
import os

#Class
class account(object):
    def __init__(s):   #s instead of self
        s.acno=0
        s.name=""
        s.deposit=0
        s.type=""

    def create_account(s):  #function to get data from user
        check=True
        while check:
            s.name=raw_input("Enter The Name of The Account Holder: ")
            l=s.name.split(' ')
            n=''.join(l)
            if n.isalpha():
                check=False
            else:
                print "Name Must Contain Only Alphabets"
                print               

                
        check=True
        while check:
            print "Enter 'C' To Create A Current Account"
            print "Enter 'S' To Create A Savings Account"
            type=raw_input("Enter Account Type (C/S): ")
            s.type=type.upper()

            if s.type=='S' or s.type=='C':
                check=False
            else:
                print "Invalid Account Type"
                print

        if s.type=='S':
            print
            print 'Base Amount: 500'
        else:
            print
            print 'Base Amount: 1000'
        check=True
        while check:
            s.deposit=raw_input("Enter Amount: ")
            if s.deposit.isdigit():
                s.deposit=int(s.deposit)
                if (s.type=='S' and s.deposit>=500) or (s.type=='C' and s.deposit>=1000):
                    check=False
                else:
                    print "Invalid Amount"
                    print
            else:
                print "Invalid Input"
                print
        
    def show_account(s):    #function to show data on screen
        print "Account Number. :", s.acno
        print "Account Holder Name: ", s.name
        print "Type of Account", s.type
        print "Balance Amount: ", s.deposit
        print

    def modify(s):          #function to get new data from user
        check=True
        while check:
            name=raw_input("Enter The Name of The Account Holder: ")
            l=name.split(' ')
            n=''.join(l)
            if n.isalpha():
                check=False
            else:
                print "Name Must Contain Only Alphabets"
                print               

        check=True
        while check:
            print "Account Number: ", s.acno
            type=raw_input("Enter Account Type (C/S): ")
            type=type.upper()
            if type=='S' or type=='C':
                check=False
            else:
                print "Invalid Account Type"
                print

            print
            if (type=='S' and s.deposit<500) or (type=='C' and s.deposit<1000):
                if type=='S':
                    print 'Base Amount: 500'
                
                else:
                    print 'Base Amount: 1000'
                print "Minimum Balance Not Present In Account"
                print "Proceed To Deposit Minimum Balance Before Proceeding"
                check=False

            else:
                s.name=name
                s.type=type
                
                

        print

    def dep(s,x):           #FUNCTION TO ACCEPT AMOUNT AND ADD TO BALANCE
        s.deposit+=x
        

    def draw(s,x):          #FUNCTION TO ACCEPT AMOUNT AND SUBTRACT FROM BALANCE
        s.deposit-=x

    def report(s):          #FUNCTION TO SHOW DATA IN TABULAR FORMAT
        print "%-10s"%s.acno,"%-30s"%s.name,"%-10s"%s.type,"%-6s"%s.deposit
        print

    def retacno(s):         #FUNCTION TO RETURN ACCOUNT NUMBER
        return s.acno
        print

    def retdeposit(s):      #FUNCTION TO RETURN BALANCE AMOUNT
        return s.deposit
        print
    def rettype(s):         #FUNCTION TO RETURN TYPE OF ACCOUNT
        return s.type
        print

#FUNCTION TO GENERATE ACCOUNT NUMBER
def gen_acno():
    try:
        inFile=open("account2.dat","rb") #Contains The Previous Account Number
        outFile=open("text2.dat","wb")
        n=inFile.read()
        n=int(n)
        while True:
            n+=1
            outFile.write(str(n))
            inFile.close()
            outFile.close()
            os.remove("account2.dat")
            os.rename("text2.dat","account2.dat")
            yield n
            
            
    except IOError:
        print "I/O error occured"
        print


#FUNCTION TO WRITE RECORD IN BINARY FILE
def write_account():
    print
    try:
        ac=account()
        outFile=open("account.dat","ab")
        ch=gen_acno()
        ac.acno=ch.next()
        ac.create_account()
        pickle.dump(ac,outFile)
        outFile.close()
        print "Account Created Successfully"
        print "YOUR ACCOUNT NUMBER IS: ",ac.retacno()
        print
    except:
        pass


#FUNCTION TO DISPLAY ACCOUNT DETAILS GIVEN BY USER
def display_sp(n):
    flag=0
    try:
        inFile=open("account.dat","rb")
        print "BALANCE DETAILS"
        while True:
            ac=pickle.load(inFile)

            if ac.retacno()==n:
                ac.show_account()
                flag=1
                
    except EOFError:
        inFile.close
        if flag==0:
            print "Account Number Does Not Exist"
            print

    except IOError:
        print "File Open Error!! Press any Key to continue"
        print


#FUNCTION TO MODIFY RECORD OF FILE
def modify_account(n):
    found=0
    try:
        inFile=open("account.dat","rb")
        outFile=open("temp.dat","wb")
        while True:
            ac=pickle.load(inFile)
            if ac.retacno()==n:
                print 30*"-"
                ac.show_account()
                print 30*"-"
                print "Enter The New Details of Account"
                ac.modify()
                pickle.dump(ac,outFile)
                print "Records Updated"
                print
                found=1
            else:
                pickle.dump(ac,outFile)
             
    except EOFError:
        inFile.close()
        outFile.close()
        if found==0:
            print " "
            print

    except IOError:
        print "File Open Error!! Press any Key to continue"
        print

    os.remove("account.dat")
    os.rename("temp.dat","account.dat")



#FUNCTION TO DELETE RECORD FROM FILE
def delete_account(n):
    found=0

    try:
        inFile=open("account.dat","rb")
        outFile=open("temp.dat","wb")
        while True:
            ac=pickle.load(inFile)
            if ac.retacno()==n:
                found=1
                ac.show_account()
                print "Account Deleted"
                print
            else:
                pickle.dump(ac,outFile)
        
            
    except EOFError:
        inFile.close()
        outFile.close()
        if found==0:
            print

    except IOError:
        print "File Open Error!! Press any Key to continue"
        print

    if found==0:
            print "Account Number Does Not Exist"
            print
    os.remove("account.dat")
    os.rename("temp.dat","account.dat")



#FUNCTION TO DISPLAY ALL ACCOUNT DETAILS
def display_all():
    print "\n\n\tACCOUNT HOLDER LIST\n\n"
    print 60*"="
    print "%-10s"%"A/C No.","%-30s"%"Name","%-10s"%"Type","%-6s"%"Balance"
    print 60*"=","\n"
    try:
        inFile=open("account.dat","rb")
        while True:
            ac=pickle.load(inFile)
            ac.report()
    
            
    except EOFError:
        inFile.close()
        
    except IOError:
        print "File Open Error!! Press any Key to continue"
        print

    print 60*"="
    print


#FUNCTION TO DEPOSIT/WITHDRAW AMOUNT FOR GIVEN ACCOUNT
def deposit_withdraw(n,option):
    found=0

    try:
        inFile=open("account.dat","rb")
        outFile=open("temp.dat","wb")
        while True:
            ac=pickle.load(inFile)
            if ac.retacno()==n:
                ac.show_account()
                if option==1:
                    print "DEPOSIT AMOUNT"
                    check=True
                    while check:
                        amt=raw_input("Enter the amount to be deposited: ")
                        if amt.isdigit():
                            ac.dep(int(amt))
                            check=False
                        else:
                            print "Invalid Input"
                            print
                elif option==2:
                    print "TO WITHDRAW AMOUNT"
                    check=True
                    while check:
                        amt=raw_input("Enter amount to be withdrawn: ")
                        if amt.isdigit():
                            check=False
                            amt=int(amt)
                            bal=ac.retdeposit()-amt
                            if((bal<500 and ac.rettype()=="S")or(bal<1000 and ac.rettype()=="C")):
                                print "Insufficient Balance."
                                print "Minimum Balance Not Present In Account"
                                print
                            else:
                                ac.draw(amt)
                        else:
                            print "Invalid Input"
                            print
                pickle.dump(ac,outFile)
                found=1
                print "Records Updated"
                print
            else:
                pickle.dump(ac,outFile)
                
    except EOFError:
        inFile.close()
        outFile.close()
        if found==0:
            print "Record Not Found"
            print
    
    except IOError:
        print "File Open Error!! Press any Key to continue"
        print

    os.remove("account.dat")
    os.rename("temp.dat","account.dat")



#INTRODUCTORY FUNCTION
def intro():
    print "BANK ACCOUNT MANAGEMENT SOFTWARE"
    print "         Version 8.06"
    print

#MAIN PROGRAM BODY

intro()
while True:

    print """MAIN MENU

    1. New Account
    2. Deposit Amount
    3. Withdraw Amount
    4. Balance Enquiry
    5. Account Holder List
    6. Close An Account
    7. Modify An Account
    8. Exit
    """
    ch=raw_input("Enter Your Choice: ")
    if ch.isdigit():
        
        ch=int(ch)
        if ch==1:
            write_account()
        
        elif ch==2:
            check=True
            while check:
                num=raw_input("\n\nEnter Account Number: ")
                if num.isdigit():
                    num=int(num)
                    print
                    deposit_withdraw(num,1)
                    check=False
                else:
                    print "Invalid Input"

        elif ch==3:
            check=True
            while check:
                num=raw_input("\n\nEnter Account Number: ")
                if num.isdigit():
                    num=int(num)
                    print
                    deposit_withdraw(num,2)
                    check=False
                else:
                    print "Invalid Input"

        elif ch==4:
            check=True
            while check:
                num=raw_input("\n\nEnter Account Number: ")
                if num.isdigit():
                    num=int(num)
                    print
                    display_sp(num)
                    check=False
                else:
                    print "Invalid Input"

        elif ch==5:
            display_all()

        elif ch==6:
            check=True
            while check:
                num=raw_input("\n\nEnter Account Number: ")
                if num.isdigit():
                    num=int(num)
                    print
                    delete_account(num)
                    check=False
                else:
                    print "Invalid Input"
        
        elif ch==7:
            check=True
            while check:
                num=raw_input("\n\nEnter Account Number: ")
                if num.isdigit():
                    num=int(num)
                    print
                    modify_account(num)
                    check=False
                else:
                    print "Invalid Input"

        elif ch==8:
            break

        else:
            print "Invalid Choice"
            print

    else:
        print "Invalid Input"
        print



print
raw_input("Press The Enter Key To Exit")

"""*****************************************************************************
				END OF PROJECT
*****************************************************************************"""
