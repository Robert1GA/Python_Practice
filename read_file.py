# Read an entire file
read_a_file = open('filename.txt', 'r')
print(read_a_file.read())
read_a_file.close()

# Read a line
read_a_file = open('filename.txt', 'r')
print('first line: ' + read_a_file.readline())
print('second line: ' + read_a_file.readline())
print('third line: ' + read_a_file.readline())
read_a_file.close()

# Or....
read_a_file = open('filename', 'r')
for line in read_a_file:
    print(line)
read_a_file.close()
