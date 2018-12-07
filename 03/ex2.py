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

# Do the same as for part 1, but store the IDs of occupants of each square,
# so we know when they've overlapped
occupied_inches = {}
# Claim IDs stay in here until they're found to overlap with something
non_overlapping_ids = set()

for claim_id, x_start, y_start, x_size, y_size in claims:
    # Start by marking the claim as not overlapping, until we find evidence to the contrary
    non_overlapping_ids.add(claim_id)
    # Go through each inch occupied by this claim
    for x in range(x_start, x_start+x_size):
        for y in range(y_start, y_start+y_size):
            # Add this claim to the list of occupants of this square
            occupied_inches.setdefault((x, y), []).append(claim_id)
            if len(occupied_inches[(x, y)]) > 1:
                # There are multiple occupants of this sqaure
                # Make sure they are all counted as overlapping, including this one
                for cid in occupied_inches[(x, y)]:
                    if cid in non_overlapping_ids:
                        non_overlapping_ids.remove(cid)

if len(non_overlapping_ids) > 1:
    print("Got multiple non-overlapping claims: something's wrong")
else:
    print("Non-overlapping claim: {}".format(list(non_overlapping_ids)[0]))
