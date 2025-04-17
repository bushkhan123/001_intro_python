#01_add_two_number........................................................................

def main():
    print("This program adds two numbers.")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    total = num1 + num2
    print(f"The total is {total}.")

if __name__ == '__main__':
    main()

#02_agreement_bot.............................................................................
def main():
    favorite_animal = input("What's your favorite animal? ")
    print(f"My favorite animal is also {favorite_animal}!")

if __name__ == '__main__':
    main()


#03_fahrenheit_to_celsius.........................................................................


# 🌡️ Temperature Converter: Fahrenheit to Celsius
# 📝 This script converts temperature from Fahrenheit to Celsius.

def fahrenheit_to_celsius(fahrenheit):
    """
    📌 Convert Fahrenheit to Celsius.
    
    🔢 Formula: (°F - 32) × 5/9 = °C
    """
    return (fahrenheit - 32) * 5.0 / 9.0

def main():
    # 🏁 Prompt user for input
    try:
        fahrenheit = float(input("❄️ Enter temperature in Fahrenheit: "))
        
        # 🔄 Convert temperature
        celsius = fahrenheit_to_celsius(fahrenheit)
        
        # 📢 Display the result
        print(f"✅ Temperature: {fahrenheit}°F = {celsius:.2f}°C 🌡️")
    
    except ValueError:
        print("⚠️ Please enter a valid number! 🚫")

# 🚀 Run the script when executed
if __name__ == '__main__':
    main()


#04_how_old_are_they..............................................................................

    # 🎂 Age Calculator Program
# 📝 This program calculates and displays the ages of five individuals based on a given pattern.

def calculate_ages():
    """
    📌 This function assigns and calculates ages based on a given sequence.
    """
    # 🎭 Assign initial ages
    alex = 21  
    bella = alex + 6  
    charlie = bella + 20  
    dylan = charlie + alex  
    emma = charlie  

    # 📢 Display the calculated ages
    print(f"🎈 Alex is {alex} years old.")
    print(f"🎈 Bella is {bella} years old.")
    print(f"🎈 Charlie is {charlie} years old.")
    print(f"🎈 Dylan is {dylan} years old.")
    print(f"🎈 Emma is {emma} years old.")

# 🚀 Run the program
if __name__ == '__main__':
    calculate_ages()


#05_triangle_perimeter...............................................................................


def main():
    # Get the 3 side lengths of the triangle
    side1 = float(input("What is the length of side 1? "))
    side2 = float(input("What is the length of side 2? "))
    side3 = float(input("What is the length of side 3? "))

    # Calculate perimeter
    perimeter = side1 + side2 + side3

    # Print the perimeter
    print(f"The perimeter of the triangle is {perimeter}")

if __name__ == '__main__':
    main()

#06_square_number.....................................................................


# 🟢 Square Calculator 🟢
# 🎯 This script calculates and displays the square of a given number.

def calculate_square():
    """
    📌 Function to calculate the square of a user-input number.
    """
    try:
        # 🔢 Get the number from the user
        num = float(input("🔢 Type a number to see its square: "))

        # 🧮 Calculate the square
        square = num ** 2

        # 📢 Display the result
        print(f"✅ {num} squared is {square} 🎯")

    except ValueError:
        print("⚠️ Please enter a valid numeric value! 🚫")

# 🚀 Run the program
if __name__ == '__main__':
    calculate_square()