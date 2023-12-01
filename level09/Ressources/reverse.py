#!/usr/bin/env python3

import sys

def main():
    encoded_string = sys.argv[1]
    decoded_string = ""

    for index, char in enumerate(encoded_string):
        decoded_string += chr(ord(char) - index)

    print(decoded_string)

if __name__ == "__main__":
    main()