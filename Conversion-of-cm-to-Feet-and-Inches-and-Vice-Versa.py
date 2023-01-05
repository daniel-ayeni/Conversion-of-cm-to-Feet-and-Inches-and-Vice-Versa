def cm_to_ft_in(cm):
    # Convert cm to inches
    inches = cm / 2.54
    # Convert inches to feet
    feet = int(inches / 12)
    # Calculate remaining inches
    inches = inches % 12
    # Return result as a tuple
    return (feet, inches)


def ft_in_to_cm(feet, inches):
    # Convert feet to inches
    inches += feet * 12
    # Convert inches to cm
    cm = inches * 2.54
    # Return result
    return cm


# Get user input
value = input("Enter a value in cm or ft and inches (e.g. 5ft 2in or 152.4cm): ")

# Check if the input is in cm
if value[-2:] == "cm":
    # Convert cm to feet and inches
    cm = float(value[:-2])
    feet, inches = cm_to_ft_in(cm)
    # Print result
    print(f"{cm}cm is equivalent to {feet}ft {inches:.1f}in")
else:
    # Split the input into feet and inches
    parts = value.split(" ")
    feet = int(parts[0][:-2])
    inches = float(parts[1][:-2])
    # Convert feet and inches to cm
    cm = ft_in_to_cm(feet, inches)
    # Print result
    print(f"{feet}ft {inches}in is equivalent to {cm:.1f}cm")
