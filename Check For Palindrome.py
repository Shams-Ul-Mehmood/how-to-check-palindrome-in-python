string = input("Please enter string : ")

def palindrome( string ):
    for index in range( int( len( string ) / 2 ) ):
        if( string[index] == string[ len( string ) - index - 1 ] ):
            return True
    return False

print( palindrome( string ) )