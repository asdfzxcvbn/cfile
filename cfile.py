#!/usr/bin/python3
# written by chatgpt, and i added some extra code too :)

import hashlib
import sys

# Get the filenames of the files to compare from the command-line arguments
if len(sys.argv) == 2:
    print('usage: cfile <file1> <file2>')
    print(f'"{sys.argv[1]}" if your file1, you\'re currently missing file2')
    sys.exit(1)
if len(sys.argv) != 3:
    print('usage: cfile <file1> <file2>')
    sys.exit(1)

try:
    file1 = sys.argv[1]
    file2 = sys.argv[2]

    # Define a function to calculate the SHA256 checksum of a file
    def sha256sum(filename):
        sha256 = hashlib.sha256()
        with open(filename, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                sha256.update(chunk)
        return sha256.hexdigest()

    # Calculate the SHA256 checksums of the two files
    checksum1 = sha256sum(file1)
    checksum2 = sha256sum(file2)

    # Compare the two checksums to determine if the files are identical
    if checksum1 == checksum2:
        print(f'{file1} and {file2} are identical,', 
              f'and their sha256 checksum is {checksum1}')
    else:
        print('these files are not identical.')
        print(f'the sha256 checksum of {file1} is {checksum1}')
        print(f'the sha256 checksum of {file2} is {checksum2}')

except FileNotFoundError as nf:
    print(f'unfortunately, "{str(nf)[38:-1]}" is invalid.', 
          'please try using a file that actually exists.')
