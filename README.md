# Password validator
This  code is used to validate if the  password entered is valid or invalid.
## Requirements ##
To Run the Source Code of password validator we  need Python3 Installed in our computer
## Introduction ##
Password Validators are responsible for determining whether a proposed password is acceptable for use and could include checks like ensuring it meets minimum length requirements, that it has an appropriate range of characters.
## Instructions ##
1)Password length has to be of minimum of 12 character

2)Password length has to be of maximum of 20 character

3)Password string must consist of minimum 3 characters - Upper Case (A-Z)

4)Password string must consist of minimum 3 characters - Lower Case (a-z)

5)Passowrd string should consist minimum 3 of Numbers - (0-9)

6)Passowrd string should consist of atleast 3 Special Characters.

7)llowed Special Characters are - !, @, #, $, %, ^, &, *, (, ), _, -, and ~

8)assword string should start with either any special character or 2 digit number

9)assword string cannot contain 5 same characters or numbers consecutively

10)assword string cannot have 3 same special charaters consecutively

11)assword string cannot have the UserName into it at any position

## Functions used in source code ##

* def instructions():  - This function displays the set of instructions after starting the game.

* def main(): -This is main function of the Code

* def length(): -This function is used to find the length of the password and checks wheather the given password match the length or not.

* def specialchar3check(): -  Function to check 3 consecutive special character and returns wheather the password satisfies the special characters and says not to enter 3 special characters  consecutively.

* def usernamecheck(): - This function will check wheather the password contains username in it or not.

* def consecutivecheck5(): - This function will check the password string 5 same characters or numbers consecutively.

* def upperandlowercasemin(): -This function will rcheck if the password string contains min of 3 lower case and upper case characters.

* def checkstart(): - This function will check wheather the password string starts with number or the special character.

* def allow(): - This function will allows the given special characters

* def specialcasecheck(): -This function checks that the given password string contains 3 special characters.

* def digit(): -This function checks wheather the password string consists of digit included in it or not. If not the it will ask to include  digit  in it.

* def lowercase(): -This will check wheather the password string consists of lower case in it or not.

* def uppercase(): - This will check wheather the password string consists of upper case in it or not.
