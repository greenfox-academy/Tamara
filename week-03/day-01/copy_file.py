# Write a function that copies a file to an other
# It should take the filenames as parameters
# It should return a boolean that shows if the copy was successful


def copy_file(in_file, out_file):
    in_file = open(in_file, "r")
    out_file = open(out_file, "w")
    try:
        for i in in_file:
            out_file.write(i)
            return True
    except:
        print("Something is wrong.")
    in_file.close()
    out_file.close()


copy_file("my-file.txt", "out_file.txt")    
