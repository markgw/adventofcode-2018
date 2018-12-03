#!/usr/bin/python3

# Start the frequency on 0
freq = 0
# Read in the file line by line
with open("input.txt", "r") as f:
    for line in f:
        # Get the frequency change and apply it
        freq += int(line.strip("\n"))
        print("Change: {}".format(freq))

print("Final frequency: {}".format(freq))
