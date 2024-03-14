def main():
    fraction: str = input("Fraction: ")
    percentage: int = convert(fraction)

    # // Print the gauge percentage
    print(gauge(percentage))

# // Convert the fraction to an integer
def convert(fraction: str):
    try:
        # // Split the inputted fraction by "/"
        _split = fraction.split("/")

        # // Get the x and y values
        x: int = int(_split[0])
        y: int = int(_split[1])

        # // Return the percentage integer
        return int(round((x/y)*100))

    # // Except Exceptions, ValueError and ZeroDivisionError
    except ValueError:
        main()
    except ZeroDivisionError:
        main()

# // Convert the percentage integer to a
# // percentage string, E or F
def gauge(percentage):
    try:
        if 0 <= percentage <= 1:
            return "E"
        elif 99 <= percentage <= 100:
            return "F"
        elif 1 < percentage < 99:
            return f"{int(percentage)}%"
        else:
            raise TypeError
    except TypeError:
        main()



# // Run the main function
if __name__ == "__main__":
    main()
