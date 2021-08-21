
from beautifultable import BeautifulTable

table = BeautifulTable()

def view():
    with open("password.txt" , "r") as ff:
        for i in ff.readlines():
            data = i.strip()
            acc , user , pas = data.split("|")
            table.rows.append([acc, user,pas])
            continue
                
    table.set_style(BeautifulTable.STYLE_BOX_ROUNDED)  
    table.columns.header = ["Account", "Username", "Password"]
    print(table)
    
def add():
    add.account = input("Enter Account Name: ")
    add.user_a = input("Enter Username: ")
    add.pass_a = input("Enter Password: ")

    with open("password.txt" , 'a') as qq:
        qq.write(add.account +" | "+ add.user_a + " | " + add.pass_a +"\n")
    

while True:
    mode = input("\nWould you like to add new password or view passwords,\nplease enter ones(add , view), press q to quit()? ")
    if mode == 'q':
        break
    elif mode == 'add':
        add()
    elif mode == 'view':
        view()
    else: 
        print("\n--Invalid mode. try again--")
        continue

# Made By Yasin Rezvani