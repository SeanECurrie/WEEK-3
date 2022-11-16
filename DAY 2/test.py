

def check_pali():
    word = input("What do you want to check is a palindrome?")

    if word == word[::-1]:
        print("Thats a Palindome")
    else:
        print("Sorry that isnt one!")

check_pali()




