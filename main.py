
def view():
    with open("password.txt" , 'r') as qq:
        data = qq.readlines()
        print(data)

def add():
    account = input("Enter Account Name: ")
    user_a = input("Enter Username: ")
    pass_a = input("Enter Password: ")

    with open("password.txt" , 'a') as qq:
        qq.write(account +": "+ user_a + " | " + pass_a +"\n")
    

while True:
    mode = input("Would you like to add a new password or view use ones(add , view), press q to quit()? ")
    if mode == 'q':
        break
    elif mode == 'add':
        add()
    elif mode == 'view':
        view()
    else: 
        print("Invalid mode. try again")
        continue

