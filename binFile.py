with open('numbers', 'bw') as bin_file:
    bin_file.write(bytes(range(17)))

with open('numbers', 'rb') as bin_file:
    for num in bin_file:
        print(num)
