from getpass import getpass
import pyperclip


def signup():
    user_name_sign_up = input("Enter your username to sign up :")
    password_sign_up = input("Enter your password to sign up :")
    Hash = hash()
    error = 0
    try:
        if user_name_sign_up in Hash.keys():
            error = 1
    except:
        error = 0 
    if error == 1:
        if user_name_sign_up in Hash.keys():
            print("This username Already exist")
            print('-'*30)
            signup()
        else:
            with open("{}.csv".format(user_name_sign_up),'w') as file, open("files.txt","a") as write_file:
                file.write(user_name_sign_up + ' ' + password_sign_up + "\n")
                write_file.write(user_name_sign_up+' '+"{}.csv".format(user_name_sign_up)+'\n')
                file.write("s.no.,username,Password,app_or_website\n")
                print('Data is Saved..!\n'+'-'*30)
                print("Please Login :")
    else:
        with open("{}.csv".format(user_name_sign_up),'w') as file, open("files.txt","a") as write_file:
            file.write(user_name_sign_up + ' ' + password_sign_up + "\n")
            write_file.write(user_name_sign_up+' '+"{}.csv".format(user_name_sign_up)+'\n')
            file.write("s.no.,username,Password,app_or_website\n")
            print('Data is Saved..!\n'+'-'*30)
            print("Please Login :")
    login()

def hash():
    try:
        with open("files.txt","r") as f_read:
            dic = {}
            for line in f_read:
                words = line.split()
                dic[words[0]] = words[1]
            return dic
    except :
        print()

def Read(user_name_login):
    with open("{}.csv".format(user_name_login),'r') as file:
        for line in file:
            out = line.split(',')
            print("     ".join(out))
        ques1 = input("Do you want to copy password (y/n):")
        if ques1 == 'y':
            edit_line = int(input("Enter the s.no of password :"))
            a_file = open("{}.csv".format(user_name_login),'r')
            list_of_lines = a_file.readlines()
            copy_text = list_of_lines[edit_line+1].split(',')
            pyperclip.copy(copy_text[2])
            spam = pyperclip.paste()
            print("your password is copied..!")
            a_file.close()
    print('-'*30)
    login_input(user_name_login)

def Read2(user_name_login):
    with open("{}.csv".format(user_name_login),'r') as file:
        for line in file:
            out = line.split(',')
            print("     ".join(out))

def Edit(user_name_login):
    Read2(user_name_login)
    a_file = open("{}.csv".format(user_name_login),'r')
    list_of_lines = a_file.readlines()
    print('-'*30)
    edit_line = int(input("Enter the s.no :"))
    username = input("Enter the website_Username :")
    password = input("Enter the website_password :")
    name = input("Enter the app or website :")
    list_of_lines[edit_line+1] = "{},{},{},{}\n".format(edit_line,username,password,name)

    a_file = open("{}.csv".format(user_name_login),'w')
    a_file.writelines(list_of_lines)
    a_file.close()
    print("Your Password is Edited..!")
    print('-'*30)
    login_input(user_name_login)

def add(user_name_login):
    with open("{}.csv".format(user_name_login),'a') as file, open("{}.csv".format(user_name_login),'r') as out:
        next(out)
        next(out)
        s_no = 1
        for line in out:
            s_no += 1
        username = input("Enter the website_Username :")
        password = input("Enter the website_password :")
        name = input("Enter the App_or_website :")
        print('-'*30)
        file.write(str(s_no) + ',' + username + ',' + password + "," + name + "\n")
    login_input(user_name_login)

def login_input(user_name_login):
    print('-'*13+'menu'+'-'*13)
    print("-"*30)
    Input = input("Enter 1 to Read \nEnter 2 to Edit \nEnter 3 to add \nEnter 4 to logout\n")
    if Input == '1':
        print('-'*30)
        Read(user_name_login)
    elif Input == '2':
        print('-'*30)
        Edit(user_name_login)
    elif Input == '3':
        print('-'*30)
        add(user_name_login)
    elif Input == '4':
        main()
    else:
        login_input(user_name_login)

def login():
    user_name_login = input("Enter your username to login :")
    password_login = getpass("Enter your password to login :")
    Hash = hash()
    error = 0
    try:
        if user_name_login in Hash.keys():
            error = 1
    except:
        error = 0

    if error == 1:
        with open("{}.csv".format(user_name_login),'r') as pass_file:
            password = pass_file.readline().split()
            if password_login == password[1]:
                print("-"*30)
                login_input(user_name_login)
            else:
                print("Incorrect Password..!")
                print('-'*30)
                login()
    else:
        print("This username does not exist..!")  
        print("-"*30)      
        login()

     
def main():
    print("-"*30)
    print('-'*5+'WELCOME TO THE VAULT'+'-'*5)
    print("-"*30)
    choice = input("Enter 1 to Sign Up \nEnter 2 to login \nEnter 3 to exit\n")
    print("-"*30)
    if choice == '1':
        signup()
    elif choice == '2':
        login()
    elif choice == '3':
        exit()
    else:
        main()

if __name__ == "__main__":
    main()