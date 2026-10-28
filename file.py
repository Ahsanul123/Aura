def square_number(number: int) -> int:
    return number * number


def main() -> None:
    n = int(input("Enter a number: "))
    result = square_number(n)
    print(f"The square of {n} is {result}")


if __name__ == "__main__":
    main()