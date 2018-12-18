fname = input("Enter file name: ")
num of lines = 0
with open(fname, 'r') as f:
    for line in f:
        num of lines += 1
print("Number of lines:")
print(num of lines)
