#exceptionhandling
try:
    
    even_numbers = [2,4,6,8]
    print(even_numbers[4])

except ZeroDivisionError:
    print("Denominator cannot be 0.")
    
except IndexError:
    print("Index Out of Bound.")

finally:
    print("This is finally block")

#output
Index Out of Bound.
This is finally block


#File Operations
# open a file
file1 = open("test.txt", "r")

# read the file
read_content = file1.read()
print(read_content)

# close the file
file1.close()





