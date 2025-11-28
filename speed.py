# speed.py
# Program to calculate Speed
import sys

def calculate_speed(distance, time):
    """Calculate speed given distance and time."""
    return distance / time


if __name__ == "__main__":
    print("=== Speed Calculator ===")

    try:
        # Case 1: When arguments are passed through CLI (Jenkins or terminal)
        if len(sys.argv) == 3:
            d = float(sys.argv[1])     # distance
            t = float(sys.argv[2])     # time
        else:
            # Case 2: User input from console
            d = float(input("Enter the distance travelled (in km): "))
            t = float(input("Enter the time taken (in hours): "))

        print("\n=== Program parameters ===")
        print("Distance: ", d)
        print("Time: ", t)

        speed = calculate_speed(d, t)
        print(f"\nSpeed = {speed:.2f} km/h")

    except ValueError:
        print("Invalid input! Please enter numeric values only.")
    except ZeroDivisionError:
        print("Time cannot be zero!")
