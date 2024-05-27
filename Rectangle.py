#Roseburrow CIS261 Rectangle
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_perimeter(self):
        return 2 * (self.height + self.width)

    def calculate_area(self):
        return self.height * self.width

    def draw_rectangle(self):
        print("*" * int(self.width))  # Print top side
        for _ in range(int(self.height) - 2):
            print("*" + " " * (int(self.width) - 2) + "*")  # Print sides with spaces in between
        print("*" * int(self.width))  # Print bottom side


def main():
    while True:
        height = float(input("Enter the height of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        perimeter = float(input("Enter the perimeter of the rectangle: "))
        area = float(input("Enter the area of the rectangle: "))

        # Check if provided perimeter and area match the calculated values
        if perimeter != 2 * (height + width) or area != height * width:
            print("Error: Perimeter or area provided is incorrect.")
        else:
            # Create a rectangle object
            rectangle = Rectangle(height, width)

            # Draw the rectangle
            print("Drawing of the rectangle:")
            rectangle.draw_rectangle()


        # Ask if the user wants to continue
        choice = input("Do you want to continue? (yes/no): ").lower()
        if choice not in ['yes', 'y']:
            break


if __name__ == "__main__":
    main()




