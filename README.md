# Refactoring Code

Refactoring means improving the structure and readability of code without changing what the program does.

## What is refactoring?

When we refactor code, we reorganize it to make it cleaner, easier to understand, and easier to maintain. The goal is not to change the behavior of the program, but to make the code better.

## Example

Before refactoring:

```python
n = int(input("Enter a number: "))
result = n * n
print("The square of", n, "is", result)
```

After refactoring:

```python
def square_number(number: int) -> int:
    return number * number


def main() -> None:
    n = int(input("Enter a number: "))
    result = square_number(n)
    print(f"The square of {n} is {result}")


if __name__ == "__main__":
    main()
```

## Why refactor code?

- Makes the code easier to read
- Reduces repetition
- Improves organization
- Helps future changes and debugging
- Makes the code more professional and reusable

## Important point

Refactoring is about improving quality, not changing output. A refactored program should still do the same task, but in a cleaner and better-structured way.

## In simple words

Refactoring is like cleaning a room: you are not changing the room's purpose, but you are making it more organized, easier to use, and easier to maintain.
