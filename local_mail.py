import mysql.connector as sqltor
import sys
import getpass

#------------- first_page ------------#

def login_page():
    global user_active
    global passwd_active
    global type_active
    global id_active
    
    mycursor.execute("select * from user_info")
    data=mycursor.fetchall()
    if data == [] :
        print("No accounts are registered yet.")
        sys.exit()
    else:
        while True:
            while True:
                u1 = input("\nEnter Username :")
                if u1 in block:
                    print("Username not found.")
                    choice_1 = input("Press 1 to try again or anything to exit :")
                    if choice_1 == "1":
                        continue
                    else:
                        sys.exit()
                else:
                    break
            
            for i in ulist:
                if u1 == i:
                    pin = ulist.index(i)
                    break
                else:
                    if i == ulist[len(ulist)-1]:
                        print("Username not found.")
                        choice_1 = input("Press 1 to try again or anything to exit :")
                        if choice_1 == "1":
                            continue
                        else:
                            sys.exit()
                    else:
                        continue
            else:
                continue
            break
        while True:
            p1=input("Enter password :")
            if p1 == plist[pin]:
                t1=input("Enter Type :")
                if t1 == tlist[pin]:
                    id_active = idlist[pin]
                    user_active = ulist[pin]
                    passwd_active = plist[pin]
                    type_active = tlist[pin]
                    print("Login Successful\n\n")
                    break
                
                else:
                    print("Username, password, and type of account doesn't match.")
            else:
                print("Username and password doesn't match !")

def register_page():
    if bcon.is_connected() == True:
        mycursor.execute("use ymail")
        mycursor.execute("select * from user_info")
        data=mycursor.fetchall()
        if data == [] :
            y_id = "#1"
        else:
            x = data[len(data)-1]
            y = str(x)
            z = int(y[3])+1
            y_id = "#"+str(z)
            
        fn = input("Enter First Name :")
        mn = input("Enter Middle Name :")
        ln = input("Enter Last Name :")
        dob = input("Enter DOB (yyyy-mm-dd) :")
        un = input("Enter desired username :")
        pwd = input("Enter password :")
        ty = input("Enter type of Account (N - Normal/B - Buisness) :")
        print("\nAccount Registered Successfully")
        qwery = "insert into user_info values('"+y_id+"', '"+fn+"', '"+mn+"', '"+ln+"', '"+dob+"', '"+un+"', '"+pwd+"', '"+ty+"', now(), now(), NULL, NULL)"
        qwery_2 = "insert into mailbox values('"+y_id+"', 0,0,0,0)"
        mycursor.execute(qwery)
        mycursor.execute(qwery_2)
        bcon.commit()
        fi = open("C:\\Users\\"+ask_pc+"\\Desktop\\project\\inbox\\"+y_id+".txt","a")
        fi.close()
        fd = open("C:\\Users\\"+ask_pc+"\\Desktop\\project\\drafts\\"+y_id+".txt","a")
        fd.close()
        fs = open("C:\\Users\\"+ask_pc+"\\Desktop\\project\\sent\\"+y_id+".txt","a")
        fs.close()
        ft = open("C:\\Users\\"+ask_pc+"\\Desktop\\project\\trash\\"+y_id+".txt","a")
        ft.close()
    else:
        print("MySQL Connection Unsuccessful")

def report():
    print("1. Generate Mailbox")
    print("2. Users' info")
    choice = input("Choose :")
    if choice == "1":
        mycursor.execute("select count(*) from mailbox")
        num = mycursor.fetchone()
        if num:
            num = num[0]
        mycursor.execute("select * from mailbox")
        table = mycursor.fetchall()
        print("+------+---------+--------+----------+---------+")
        print("|  id  |   inbox |   sent |  drafts  |  trash  |")
        print("+------+---------+--------+----------+---------+")
        for i in range(num):
            a = table[i][0]
            b = str(table[i][1])
            c = str(table[i][2])
            d = str(table[i][3])
            e = str(table[i][4])
            print("| ",a," | ",b," "*(5-len(b)),"| ",c," "*(4-len(c)),"|",d," "*(7-len(d)),"|",e," "*(6-len(e)),"| ")
            print("+------+---------+--------+----------+---------+")
    elif choice == "2":
        mycursor.execute("select count(*) from user_info where closing_date IS NULL")
        no = mycursor.fetchone()
        if no:
            no = no[0]
        mycursor.execute("select count(*) from user_info")
        num = mycursor.fetchone()
        if num:
            num = num[0]
        mycursor.execute("select * from user_info")
        table = mycursor.fetchall()
        print("No of active users :",no)
        print("+------+-----------------------------+--------------------------+-----------------------------+--------------------------+")
        print("|  id  |   account opening date      |    account opening time  |   account closing date      |    account closing time  |")
        print("+------+-----------------------------+--------------------------+-----------------------------+--------------------------+")
        for i in range(num):
            a = table[i][0]
            b = str(table[i][8])
            c = str(table[i][9])
            d = str(table[i][10])
            e = str(table[i][11])
            print("| ",a," |        ",b,"        ","|        ",c,"       ","|        ",d,"        ","|        ",e,"        |")
            print("+------+-----------------------------+--------------------------+-----------------------------+--------------------------+")
    else:
        sys.exit()

                
#------------- mail_box ------------#


def compose():
    while True:
        receiver = input("\nEnter recepient's username :")
        if receiver in block:
            print("Username not in database")
            choice_1 = input("Press 1 to try again or anything else to exit :")
            if choice_1 == "1":
                continue
            else:
                sys.exit()
        elif receiver in ulist:
            break
        else:
            print("Username not in database")
            choice_1 = input("Press 1 to try again or anything else to exit :")
            if choice_1 == "1":
                continue
            else:
                sys.exit()
    pin = ulist.index(receiver)
    id_receiver = idlist[pin]
    sub = input("Enter subject :")
    body = input("Enter body :")
    sender = "Sender's Email Address :"+user_active+"@ymail.com"+"\n"
    receiver = "Receiver's Email Address :"+receiver+"@ymail.com"+"\n"
    sub = "Subject :"+sub+"\n"
    body = "Body :"+body+"\n"
    qwery = sender + receiver + sub + body + "\n"
    
    while True:
        print("1. Save as Draft")
        print("2. Send it")
        print("3. Discard")
        confirm = input("\nEnter choice :")
        if confirm == "1":
            mycursor.execute("update mailbox set drafts = drafts + 1 where id = '"+id_active+"'")
            bcon.commit()
            with open("C:\\Users\\"+ask_pc+"\\Desktop\\project\\drafts\\"+id_active+".txt","a") as x:
                x.write(qwery)
                print("Saved in Draft")
                break
        elif confirm == "2":
            mycursor.execute("update mailbox set sent = sent + 1 where id = '"+id_active+"'")
            mycursor.execute("update mailbox set inbox = inbox + 1 where id = '"+id_receiver+"'")
            bcon.commit()
            with open("C:\\Users\\"+ask_pc+"\\Desktop\\project\\sent\\"+id_active+".txt","a") as y, open("C:\\Users\\"+ask_pc+"\\Desktop\\project\\inbox\\"+id_receiver+".txt","a") as q:
                y.write(qwery)
                q.write(qwery)
                print("Sent successfully...")
                break
        elif confirm == "3":
            print("Discarded")
            break
        else:
            print("Invalid Input")
            choice_2 = input("Press 1 to try again or anything to exit :")
            if choice_2 == "1":
                continue                        
            else:
                sys.exit()

def inbox():
    ct = 0
    nlist=[0]
    senderlist = []
    x = open("C:\\Users\\"+ask_pc+"\\Desktop\\project\\inbox\\"+id_active+".txt","r")
    data = x.readlines()
    for i in range(len(data)):
        if data[i] == '\n':
            ct = ct + 1
            pin = i
            nlist.append(pin)
        else:
            continue
    ultimate = []
    for u in range(len(nlist)-1):
        if u == 0:
            record = data[nlist[u]:nlist[u+1]]
            ultimate.append(record)   
        else:
            record = data[nlist[u]+1:nlist[u+1]]
            ultimate.append(record)

    if ct == 0:
        print("\nZero Mails in Inbox")
    else:
        print("\nNo of received emails :",ct)
        print("1. View all Mails")
        print("2. View mails by particular sender")
        print("3. Delete Mails")
        print("Press anything else to exit")
        while True:
            choice = input("\nEnter choice :")
            if choice == "1":
                print()
                for j in data:
                    print(j[:len(j)-1])
            elif choice == "2":
                print()
                count_sender = 0
                user_list = []
                user_sender = input("Enter username of a sender :")
                
                for k in range(len(ultimate)):
                    if ultimate[k][0] == "Sender's Email Address :"+user_sender+"@ymail.com"+"\n":
                        count_sender = count_sender + 1
                        user_list.append(ultimate[k])
                    else:
                        continue
                print()
                print("Emails received by "+user_sender+":",count_sender)
                for m in user_list:
                    print()
                    for n in m:
                        print(n[:len(n)-1])
            elif choice == "3":
                print()
                x = open("C:\\Users\\"+ask_pc+"\\Desktop\\project\\inbox\\"+id_active+".txt","r")
                data = x.readlines()
                for j in data:
                    print(j[:len(j)-1])
                num = int(input("Enter the No. of the email to delete:"))
                x.close()
                mycursor.execute("update mailbox set trash = trash + 1 where id = '"+id_active+"'")
                mycursor.execute("update mailbox set inbox = inbox - 1 where id = '"+id_active+"'")
                bcon.commit()
                if num == 1:
                    with open("C:\\Users\\"+ask_pc+"\\Desktop\\project\\trash\\"+id_active+".txt","a") as r, open("C:\\Users\\"+ask_pc+"\\Desktop\\project\\inbox\\"+id_active+".txt","w") as q:
                        for p in data[:nlist[num]+1]:
                            r.write(p)
                        for y in data[nlist[num]+1:]:
                            q.write(y)
                else:
                    with open("C:\\Users\\"+ask_pc+"\\Desktop\\project\\trash\\"+id_active+".txt","a") as r, open("C:\\Users\\"+ask_pc+"\\Desktop\\project\\inbox\\"+id_active+".txt","w") as q:
                        for p in data[nlist[num-1]+1:nlist[num]+1]:
                            r.write(p)
                    
                        for y in data[:nlist[num-1]+1]+data[nlist[num]+1:]:
                            q.write(y)
                print("Deleted Mail Successfully.....")
            else:
                sys.exit()
    x.close()


def drafts():
    ct = 0
    nlist = [0]
    w = open("C:\\Users\\"+ask_pc+"\\Desktop\\project\\drafts\\"+id_active+".txt","r")
    data = w.readlines()
    for i in range(len(data)):
        if data[i] == '\n':
            ct = ct + 1
            pin = i
            nlist.append(pin)
        else:
            continue
    if ct == 0:
        print("\nZero emails in Drafts")
    else:
        print("\nNo of drafted emails :",ct)
        print("1. View drafts")
        print("2. Send a draft")
        print("Press anything else to exit")
        while True:
            choice = input("\nEnter choice :")
            print()
            if choice == "1":
                for j in data:
                    print(j[:len(j)-1])
            elif choice == "2":
                print()
                for j in data:
                    print(j[:len(j)-1])
                num = int(input("Enter the No. of the email to send :"))
                w.close()
                if num == 1:
                    receiver = data[1]
                    receiver = receiver[26:]
                    receiver = receiver[:len(receiver)-11]
                    pin = ulist.index(receiver)
                    id_receiver = idlist[pin]
                    mycursor.execute("update mailbox set inbox = inbox + 1 where id = '"+id_receiver+"'")
                    mycursor.execute("update mailbox set sent = sent + 1 where id = '"+id_active+"'")
                    mycursor.execute("update mailbox set drafts = drafts - 1 where id = '"+id_active+"'")
                    bcon.commit()
                    with open("C:\\Users\\"+ask_pc+"\\Desktop\\project\\sent\\"+id_active+".txt","a") as x, open("C:\\Users\\"+ask_pc+"\\Desktop\\project\\inbox\\"+id_receiver+".txt","a") as y, open("C:\\Users\\"+ask_pc+"\\Desktop\\project\\drafts\\"+id_active+".txt","w") as z:
                        for p in data[:nlist[1]+1]:
                            y.write(p)
                        for q in data[:nlist[1]+1]:
                            x.write(q)
                        for r in data[nlist[1]+1:]:
                            z.write(r)
                else:
                    receiver = data[nlist[num-1]+2]
                    receiver = receiver[26:]
                    receiver = receiver[:len(receiver)-11]
                    pin = ulist.index(receiver)
                    id_receiver = idlist[pin]
                    mycursor.execute("update mailbox set inbox = inbox + 1 where id = '"+id_receiver+"'")
                    mycursor.execute("update mailbox set sent = sent + 1 where id = '"+id_active+"'")
                    mycursor.execute("update mailbox set drafts = drafts - 1 where id = '"+id_active+"'")
                    bcon.commit()
                    with open("C:\\Users\\"+ask_pc+"\\Desktop\\project\\sent\\"+id_active+".txt","a") as x, open("C:\\Users\\"+ask_pc+"\\Desktop\\project\\inbox\\"+id_receiver+".txt","a") as y, open("C:\\Users\\"+ask_pc+"\\Desktop\\project\\drafts\\"+id_active+".txt","w") as z:
                        for p in data[nlist[num-1]+1:nlist[num]+1]:
                            y.write(p)
                        for q in data[nlist[num-1]+1:nlist[num]+1]:
                            x.write(q)
                        for r in data[:nlist[num-1]+1]+data[nlist[num]+1:]:
                            z.write(r)
                print()
                break
            else:
                sys.exit()

def sent():
    ct = 0
    nlist = []
    x = open("C:\\Users\\"+ask_pc+"\\Desktop\\project\\sent\\"+id_active+".txt","r")
    data = x.readlines()
    for i in range(len(data)):
        if data[i] == '\n':
            ct = ct + 1
            pin = i
            nlist.append(pin)
        else:
            continue
    if ct == 0:
        print("\nZero Sent Mails")
    else:
        print("\nNo of sent emails :",ct)
        choice = input("Do you wish to see all sent mails? (y/n)-(Y/N) :")
        print()
        if choice == 'y' or choice == 'Y':
            for j in data:
                print(j[:len(j)-1])
        else:
            print()
    x.close()

def trash():
    ct = 0
    nlist = []
    x = open("C:\\Users\\"+ask_pc+"\\Desktop\\project\\trash\\"+id_active+".txt","r")
    data = x.readlines()
    for i in range(len(data)):
        if data[i] == '\n':
            ct = ct + 1
            pin = i
            nlist.append(pin)
        else:
            continue
    if ct == 0:
        print("\nZero Trash Mails")
    else:
        print("\nNo of trashed emails :",ct)
        choice = input("Do you wish to see all trashed mails? (y/n)-(Y/N) :")
        print()
        if choice == 'y' or choice == 'Y':
            for j in data:
                print(j[:len(j)-1])
        else:
            print()
    x.close()

def close():
    mycursor.execute("update user_info set closing_date = now() where y_id = '"+id_active+"'")
    mycursor.execute("update user_info set closing_time = now() where y_id = '"+id_active+"'")
    bcon.commit()
    print("\n--- ACCOUNT CLOSED ---")


#------------- main_program ------------#

print("\nWelcome to YMail Services")

ask_pc = getpass.getuser()
ask_user = input("Enter MySQL Username :")
ask_pass = input("Enter MySQL Password :")

bcon=sqltor.connect(host="localhost", user=ask_user, passwd=ask_pass)
mycursor=bcon.cursor()
if bcon.is_connected() == True:
    print("MySQL Connection Successful")
    mycursor.execute("create database if not exists ymail")
    mycursor.execute("use ymail")
    mycursor.execute("create table if not exists user_info (y_id char(10) PRIMARY KEY, first_name char(20) NOT NULL, middle_name char(20), last_name char(20), date_of_birth DATE NOT NULL, user_name char(25) NOT NULL UNIQUE, password char(25) NOT NULL UNIQUE, type char(1) NOT NULL, opening_date DATE NOT NULL, opening_time TIME NOT NULL, closing_date DATE, closing_time TIME)")
    mycursor.execute("create table if not exists mailbox (id char(10) PRIMARY KEY, inbox int(5), sent int(5), drafts int(5), trash int(5));")
else:
    print("MySQL Connection Unsuccessful")

idlist, ulist, plist, tlist = [], [], [] ,[]
mycursor.execute("select * from user_info")
data=mycursor.fetchall()
for x in data:
    idlist.append(x[0])
    ulist.append(x[5])
    plist.append(x[6])
    tlist.append(x[7])
block = []
mycursor.execute("select user_name from user_info where closing_date IS NOT NULL")
data = mycursor.fetchall()
for x in data:
    if x:
        x = x[0]
    block.append(x)
    
count = 0
print("\nChoose an action :-")
print("1. Register")
print("2. Login")
print("3. Reports Generation")
while True:
    choice_1 = input("\nEnter choice :")
    if choice_1 == "1":
        register_page()
        break
    elif choice_1 == "2":
        login_page()
        count = count+1
        break
    elif choice_1 == "3":
        report()
    else:
        print("Invalid Input")
        choice_2 = input("Press 1 to try again or anything to exit :")
        if choice_2 == "1":
            continue                        
        else:
            sys.exit()
            
if count != 0:
    print("This is Your Mail")
    print("1. Compose email")
    print("2. Inbox")
    print("3. Sent Mails")
    print("4. Drafts")
    print("5. Trash")
    print("6. Exit")
    print("7. CLOSE ACCOUNT")
    while True:
        print()
        choice_3 = input("Enter number what to view (6 - exit):")
        if choice_3 == "1":
            compose()
        elif choice_3 == "2":
            inbox()
        elif choice_3 == "3":
            sent()
        elif choice_3 == "4":
            drafts()
        elif choice_3 == "5":
            trash()
        elif choice_3 == "6":
            sys.exit()
        elif choice_3 == "7":
            close()
            break
        else:
            print("Invalid Input")
            choice_4 = input("Press 1 to try again or anything to exit :")
            if choice_4 == "1":
                continue                        
            else:
                sys.exit()
else:
    count = 0


