numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # List of numbers to be checked
evenCount = 0 # Variable to keep track of even numbers
oddCount = 0 # Variable to keep track of odd numbers
for num in numbers: # Loop through numbers
    if(num % 2 == 1): # Check if the number is odd
        oddCount += 1 # Increment the odd number counter
    else: # Check if the number is not odd
        evenCount += 1 # Increment the even number counter
    
print(f"Number of Even Numbers: {evenCount}") # Print the number of even numbers
print(f"Number of Odd Numbers: {oddCount}") # Print the number of odd numbers