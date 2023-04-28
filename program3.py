#jasmin ericka a. celebre
#bscpe 1-4

#define a function
def line_write():
#open file
    with open("mylife.txt", "w") as my_file:
#ask for user input of line
        line = input("Enter line:")
        my_file.write(line + "\n")
