#jasmin ericka a. celebre
#bscpe 1-4

#define a function
def line_write():
#open file
    with open("mylife.txt", "w") as my_file:
#ask for user input of line
        line = input("Enter line:")
        my_file.write(line + "\n")
#set a conditon for lines
        while True:
            answer = input("Are there more lines? y/n:")
            if answer == "y":
                line = input("enter line:")
                my_file.write(line + "\n")
            else:
                break
line_write()