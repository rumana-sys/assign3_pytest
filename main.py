def calculate_square_area(side_length):
    """
    This function calculates the area of a square.
    
    :param side_length: The length of one side of the square (must be a number).
    :return: The area of the square (rounded to 2 decimal places).
    """
    
    # Check if input is a valid number
    if not isinstance(side_length, (int, float)):
        raise TypeError("Invalid input! Please enter a number.")
    
    # Check if the number is negative
    if side_length < 0:
        raise ValueError("Side length cannot be negative! Please enter a positive number.")

    # Calculate the area (side * side) and round to 2 decimal places
    return round(side_length ** 2, 2)


if __name__ == "__main__":
    print("Welcome! This program calculates the area of a square.")

    try:
        # Ask the user for input
        side = float(input("Please enter the side length of the square: "))

        # Calculate the area and display the result
        area = calculate_square_area(side)
        print(f"The area of the square with side length {side} is: {area}")

    except ValueError as ve:
        print(f"Oops! {ve}")
    except TypeError as te:
        print(f"Oops! {te}")
