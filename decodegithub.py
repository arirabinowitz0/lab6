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


def decoder(encode):
    decoded = ""
    for element in encode:
        if int(element) >= 3:
            element = str(int(element) - 3)
        elif int(element) == 0:
            element = "7"
        elif int(element) == 1:
            element = "8"
        elif int(element) == 2:
            element = "9"
        decoded += element
    return decoded


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
            print(f"The encoded password is {encoded}, and the original password is {decoder(encoded)}")
        elif choice == 3:
            going = False
            break
