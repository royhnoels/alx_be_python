# pattern_drawing.py

# Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter for the while loop
row = 0

# Outer loop: while loop to handle rows
while row < size:
    # Inner loop: for loop to print '*' across the columns
    for col in range(size):
        print("*", end="")  # Print * without newline
    print()  # Move to the next line after printing one full row
    row += 1  # Increment row counter
