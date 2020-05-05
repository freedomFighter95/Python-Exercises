#Define function that take one word in string as input and return True if it is palindrome else return False
#palinedrome - Word that reads same backwards as forwards


def is_palindrome(word):       #definning Function 
    reverse_word = word[::-1]  #store the Reverse string
    if word == reverse_word:  
        return True            #return value if word is palindrome
    return False               #return value if word is not palindrome

a = input("enter a word :")
is_palindrome(a)