#!/usr/bin/python3

claims = []
with open("input.txt", "r") as f:
    for line in f:
        rest = line.rstrip("\n")
        # The first bit is the claim ID
        claim_id, __, rest  = rest.partition(" @ ")
        claim_id = int(claim_id[1:])
        # Then we get the start coordinates
        x_start, __, rest = rest.partition(",")
        y_start, __, rest = rest.partition(": ")
        x_start = int(x_start)
        y_start = int(y_start)
        # Then comes the size
        x_size, __, y_size = rest.partition("x")
        x_size = int(x_size)
        y_size = int(y_size)

        claims.append((claim_id, x_start, y_start, x_size, y_size))

# Everything's in integer inch coordinates, so just make a big list of all the occupied square inches
occupied_inches = set()
doubly_occupied = set()

for claim_id, x_start, y_start, x_size, y_size in claims:
    # Go through each inch occupied by this claim
    for x in range(x_start, x_start+x_size):
        for y in range(y_start, y_start+y_size):
            if (x, y) in occupied_inches:
                # This is already occupied: mark it as now doubly occupied
                doubly_occupied.add((x, y))
            else:
                # Mark this as occupied so we see later whether it overlaps with anything
                occupied_inches.add((x, y))

# Now we can just count up how many sq inches are (at least) doubly occupied
print("{} sq inches doubly occupied".format(len(doubly_occupied)))
