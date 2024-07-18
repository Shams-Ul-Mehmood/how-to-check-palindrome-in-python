def palindrome( custom_String ):
    string = ""
    for index in custom_String:
        string = index + string
    return string

custom_String = input("Please enter random string : ")
if custom_String == palindrome( custom_String ):
    print( "Alright it is a palindrome :)\n",palindrome( custom_String ) )
else:
    print( "Sorry, It is not a palindrome :(" )