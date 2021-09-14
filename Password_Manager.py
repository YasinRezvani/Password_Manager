from prettytable import PrettyTable

x = PrettyTable()

def view():
    print("")
    with open("password.txt" , "r") as ff:
        for i in ff.readlines():
            data = i.strip()
            acc , user , pas = data.split("|")
            x.add_row([acc, user,pas])
            
    x.field_names = ["Account", "Username", "Password"]
    print(x)
    x.clear_rows()
    
def add():
    account = input("\nEnter Account Name: ")
    user_a = input("\nEnter Username: ")
    pass_a = input("\nEnter Password: ")

    with open("password.txt" , 'a') as qq:
        qq.write(account +" | "+ user_a + " | " + pass_a +"\n")

    print(f"\n--- Successfully add a {account} Account to your Password Manager --- \n")

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
