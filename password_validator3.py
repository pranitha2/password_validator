def instruction():
    print("\nWelcome to Password Validator\n")
    print("Here are set of instructions which \
    you are supposed to follow")
    print("\nPassword length has to be of minimum\
    of 12 character")
    print("Password length has to be of maximum \
    of 20 character")
    print("Password string must consist of Characters \
- Upper Case (A-Z)")
    print("Password string must consist of Characters \
- Lower Case (a-z)")
    print("Passowrd string should consist of \
    Numbers - (0-9)")
    print("Passowrd string should consist of \
    atleast 3 Special Characters.")
    print("Allowed Special Characters are - \
!, @, #, $, %, ^, &, *, (, ), _, -, and ~")
    print("Password string should start with either \
    any special character or 2 digit number")
    print("Password string should have to have at least \
    3 Upper Case and 3 Lower Case characters")
    print("Password string cannot contain  5 same \
    characters or numbers consecutively")
    print("Password string  cannot have the UserName \
into it at any position")
    print("Password string cannot have 3 same special \
charaters consecutively\n")


instruction()


# Function to check for  upper case letter
def uppercase(password, username):
    flag1 = False
    uppercase = 0
    for i in password:
        if i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']:
            uppercase += 1
    if uppercase > 0:
        print("uppercase satisfied")
        flag1 = True
    else:
        print("uppercase not satisfied")

    return flag1


# Function to check lower case letter
def lowercase(password, usename):
    flag2 = False
    lowercase = 0
    for i in password:
        if i in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']:
            lowercase += 1
    if lowercase > 0:
        flag2 = True
        print("lower case satisfied")
    else:
        print("lower case not satisfied")
    return flag2


# Function to check for digits in the password
def digit(password, username):
    flag3 = False
    digit = 0
    for i in password:
        if i in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            digit += 1
    if digit > 0:
        flag3 = True
        print("digit found")
    else:
        print("pls include digit in your passward")

    return flag3


# Function to check for minimum 3 special character
def specialcasecheck(password, username):
    flag4 = False
    special = 0
    for i in password:
        if i in ['~', '!', '@', '#', '$', '%', '&', '^', '', '', '(', ')', '-', '_']:
            special += 1
    if special >= 3:
        flag4 = True
        print("it contains min of three special chars satisfied")
    else:
        print("enter atleast 3 special chars:")
    return flag4


# function to check the allowed special characters
def allow(password, username):
    flag5 = True
    l = ['~', '!', '@', '#', '$', '%', '&', '^', '', '', '(', ')', '-', '_', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
         'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd',
         'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
         '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    for i in password:
        if i not in l:
            print("enter  special characters only in '~','!','@','#','$','%','&','^','','','(',')','-','_'")

            flag5 = False
            break
    return flag5


# Function to check password  starts with number or special #character
def checkstart(password, username):
    flag6 = False

    for i in range(len(password)):
        if password[0] in ['~', '!', '@', '#', '$', '%', '&', '^', '', '', '(', ')', '-', '_']:
            flag6 = True
        if password[0] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'] and password[1] in ['1', '2', '3', '4',
                                                                                                 '5', '6', '7', '8',
                                                                                                 '9', '0']:
            flag6 = True
    if (flag6 == False):
        print("please start your password with special  char or 2 digit number only")
    return flag6


# Function to check for minimum 3 upper/lower case letter
def upperandlowercasemin(password, username):
    flag7 = False
    uppercase = 0
    lowercase = 0
    for i in password:
        if i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']:
            uppercase += 1
        if i in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']:
            lowercase += 1
    if uppercase >= 3 and lowercase >= 3:
        flag7 = True
        print("it contains min of 3 lower case and upper case chars satisfied")
    else:
        print("pls involve atleast 3 uppercase and lower case chars in ypour passwasrd")
    return flag7


# Function to check 5 same characters or numbers
def consecutivecheck5(password, username):
    flag8 = True
    count3 = 0
    for i in range(len(password)):
        if i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8',
                 '9', '0']:
            count3 += 1
        n = i + 5
        count = 0
        for j in range(i, n):
            if j < len(password):
                if (password[j] == password[i]):
                    count += 1

    if count == 5:
        flag8 = False
        print("dont enter 5 same chars or digits consecutively")
    elif count3 < 5:
        print("enter atleast 5 characters")
    else:
        print("consecutive charcters satisfied ")

    return flag8


# Function to check if password consits of username

def usernamecheck(password, username):
    flag9 = False
    if username not in password:
        flag9 = True
    if flag9 == True:
        print("username not found  in passward satisfied")
    else:
        print("dont includde username in passward")
    return flag9


# Function to check 3 consecutive special character

def specialchar3check(password, username):
    flag10 = True
    for i in range(len(password)):
        count2 = 0
        if i in ['~', '!', '@', '#', '$', '%', '&', '^', '', '', '(', ')', '-', '_']:
            count2 += 1
        n = i + 3
        count1 = 0
        for j in range(i, n):
            if j < len(password) - 1:
                temp = password[j]
                if temp == password[j + 1]:
                    count1 += 1
        if count1 == 2:
            flag10 = False
            break

    if (flag10 == False):
        print("do not enter 3 same special chars consecutively")
    elif count2 < 3:
        print("special  chars not found")
    else:
        print("conseccutive special chars satisfied")
    return flag10


# Function to check the  length of password

def length(password, username):
    if (12 <= len(password) <= 20):
        print("length matches")
    else:
        print("length doesnt matches")


def main():
    s = input("enter passward:")
    username = input("enter username:")

    if s in ['password', 'password', '123456', '123456', '123456', '123456', '123456', '123456', '123456'
                                                                                                 '123456', '123456',
             'password', 'password', 'password', 'password', 'password', 'password', '123456789',
             '12345678', '12345678', '12345678', '12345', '1234567812345', '12345678', '123456789', 'qwerty',
             'qwerty', 'abc123', 'qwerty', '12345678', 'qwerty', '12345678', 'qwerty', '12345678', 'password',
             'abc123', 'qwerty', 'abc123', 'qwerty', '12345', 'football', '12345', '12345', '1234567',
             'monkey', 'monkey', '123456789', '123456789', '123456789', 'qwerty', '123456789', '111111', '12345678',
             '1234567', 'letmein', '111111', '1234', 'football', '1234567890', 'letmein', '1234567', '12345',
             'letmein', 'dragon', '1234567', 'baseball', '1234', '1234567', '1234567', 'sunshine', 'iloveyou',
             'trustno1', '111111', 'iloveyou', 'dragon', '1234567', 'princess', 'football', 'qwerty', '111111',
             'dragon', 'baseball', 'adobe123', 'football', 'baseball', '1234', 'iloveyou', 'iloveyou', '123123',
             'baseball', 'iloveyou', '123123', ' 1234567', 'welcome', 'login', 'admin', ' princess', 'abc123', '111111',
             'trustno1', 'admin', 'monkey', '1234567890', ' welcome', ' welcome', 'admin', 'qwerty123', 'iloveyou',
             '1234567', ' 1234567890', 'letmein', ' abc123', 'solo', 'monkey', 'welcome', ' 1q2w3e4r',
             'master', 'sunshine', 'letmein', 'abc123', '111111', 'abc123', 'login', '666666', 'admin',
             'sunshine', 'master', 'photoshop', '111111', '1qaz2wsx', ' admin', 'abc123', 'abc123', 'qwertyuiop',
             'ashley', ' 123123', '1234', 'mustang', 'dragon', '121212', 'starwars', 'football', '654321', 'bailey',
             'welcome', 'monkey', 'access', 'master', 'flower', '123123', '123123', '555555',
             'passw0rd', 'shadow', 'shadow', ' shadow', 'monkey', 'passw0rd', 'dragon', 'monkey', 'lovely',
             'shadow', 'ashley', 'sunshine', 'master', 'letmein', 'dragon', 'passw0rd', '654321', '7777777',
             '123123', 'football', '12345', 'michael', 'login', 'sunshine', 'master', '!@#$%^&*', 'welcome', '654321',
             'jesus', 'password1', 'superman', 'princess', 'master', 'hello', 'charlie', '888888',
             'superman', 'michael', 'princess', '696969', 'qwertyuiop', 'hottie', 'freedom', 'aa123456', 'princess',
             'qazwsx', 'ninja', 'azerty', '123123', 'solo', 'loveme', 'whatever', 'donald', 'dragon', 'michael',
             'mustang', 'trustno1', 'batman', 'passw0rd', 'zaq1zaq1', 'qazwsx', 'password1', 'password1', 'Football',
             'password1', '000000', 'trustno1', 'starwars', 'password1', 'trustno1', 'qwerty123', '123qwe']:
        print("it is common passward")
        main()
    else:
        print("it is not a common passward:", s)
    flag11 = length(s, username)
    flag1 = uppercase(s, username)
    flag2 = lowercase(s, username)
    flag3 = digit(s, username)
    flag4 = specialcasecheck(s, username)
    flag5 = allow(s, username)
    flag6 = checkstart(s, username)
    flag7 = upperandlowercasemin(s, username)
    flag8 = consecutivecheck5(s, username)
    flag9 = usernamecheck(s, username)
    flag10 = specialchar3check(s, username)

    # print("flag1:",flag1,"flag2:",flag2,"flag3:",flag3,"flag4:",flag4,"flag5:",flag5,"flag6:",flag6,"flag7:",flag7,"flag8;",flag8,"flag9:",flag9,"flag10:",flag10)

    if (flag1 == flag2 == flag3 == flag4 == flag5 == flag6 == flag7 == flag8 == flag9 == flag10 == flag11 == True):
        print("your passward is valid")
    else:
        print("invalid passward")


main()