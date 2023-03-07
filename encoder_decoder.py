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
        output += str(temp % 10)
    return int(output)


def decode(encoded):
    decoded = ""
    for char in str(encoded):
        decoded += str((int(char) - 3) % 10)

    return decoded


def main():
    while True:
        user_input = print_menu()
        if user_input == 1:
            encoded = encode(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")
        elif user_input == 2:
            decoded = decode(encoded)
            print(f"The encoded password is {encoded}, and the original password is {decoded}")
        elif user_input == 3:
            break
        else:
            print("Error, please enter an input of 1, 2, or 3")


main()
