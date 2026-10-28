def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    return "Odd"


def main():
    try:
        num = int(input("Enter a number: "))
        print(f"The number {num} is {check_even_odd(num)}.")
    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()
