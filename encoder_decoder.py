#  Trevor Sabitsch
def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()
    return int(input("Please enter an option: "))


def encode(to_encode):
    output = ""
    for char in str(to_encode):
        temp = int(char) + 3
        output += str(temp)
    return int(output)


def decode():
    return 123


def main():
    while True:
        encoded = 000000000
        user_input = print_menu()
        if user_input == 1:
            global encoded
            encoded = encode(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")
        elif user_input == 2:
            decoded = decode()
            print(f"The encoded password is {encoded}, and the original password is {decoded}")
        elif user_input == 3:
            break
        else:
            print("Error, please enter an input of 1, 2, or 3")
