# Programmer: Javan Graber
# Date: 2/19/2026
# Program #1: Kilometer Converter
# Write a program that asks the user to enter a distance in kilometers,
# then converts that distance to miles.  The conversion formula is as follows:
# Miles = kilometers x 0.6214.
# The conversion must be done as a function with input and output.


######################
# Create the kilometer conversion function
def kilometer_conversion(kilometers):
    mile_value = kilometers * 0.6214
    return mile_value

# Ask for the kilometer value 
kilometers = float(input('Enter the kilometers: '))

# Substitute in the mile value by calling the function
mile_value = kilometer_conversion(kilometers)

# Print the mile value
print(f'The kilometer value you entered equals {mile_value:,.2f} miles')
######################



#### This piece of the code has been done for you,
#### you only need to worry about the actual kilometer
#### conversion logic in the kilometer_conversion function
if __name__ == '__main__':
    # Get User Input
    print('in main')
    # Call kilometer_conversion, don't forget to pass in the kilometer parameter!

    # Display the miles
