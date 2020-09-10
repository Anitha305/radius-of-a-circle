#Python program of the file name of the user and their extensions

fn= input("Enter filename:")
f = fn.split(".")
print("Extension of the file is: " + f[-1])
