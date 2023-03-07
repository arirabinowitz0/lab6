def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def encoder(password):
    encoded = ''
    password = str(password)
    for a in password:
        a = int(a)
        if a < 7:
            a += 3
        elif a == 7:
            a = 0
        elif a == 8:
            a = 1
        elif a == 9:
            a = 2
        encoded += str(a)
    return encoded

print(encoder(12345555))
print(encoder('00009962'))

if __name__ == '__main__':
    going = True
    while going == True:
        print_menu()
        choice = int(input("Please enter an option: "))
        if choice == 1:
            choice2 = int(input("Please enter your password to encode: "))
            encoded = encoder(choice2)
            print("Your password has been encoded and stored!")
        elif choice == 2:
            print(f"The encoded password is {encoded}, and the original password is {choice2}")
        elif choice == 3:
            going = False
            break

