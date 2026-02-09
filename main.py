def addmultiplenumbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def multiplymultiplenumbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


def isitaninteger(num):
    if isinstance(num, int):
        return True
    if isinstance(num, float) and num.is_integer():
        return True
    return False


def isiteven(num):
    if isitaninteger(num) and num % 2 == 0:
        return True
    return False


def get_numbers_from_user():
    numbers = input("Enter numbers separated by spaces: ")
    number_list = []

    for n in numbers.split():
        number_list.append(float(n))

    return number_list


def main():
    print("Hello learners!")
    print("Welcome to the calculator test")
    print("-------------------------")
    print("1. Add multiple numbers")
    print("2. Multiply multiple numbers")
    print("3. Check if a number is an integer")
    print("4. Check if a number is even")
    print("5. Exit")

    while True:
        choice = input("\nChoose an option (1-5): ")

        if choice == "1":
            numbers = get_numbers_from_user()
            print("Result:", addmultiplenumbers(numbers))

        elif choice == "2":
            numbers = get_numbers_from_user()
            print("Result:", multiplymultiplenumbers(numbers))

        elif choice == "3":
            num = float(input("Enter a number: "))
            print("Is it an integer?", isitaninteger(num))

        elif choice == "4":
            num = float(input("Enter a number: "))
            print("Is it even?", isiteven(num))

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
