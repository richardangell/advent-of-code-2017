import sys
import spiral_memory as sm


def ring_size(ring):

    if ring == 0:

        return(1)

    else:

        return(8 * ring)


def non_diag_tiles(ring):

    return((ring_size(ring) - 4) / 4)


def edge_tiles(ring):

    return(2 * ring)


def tiles_adjacent(coord1, coord2):

    if (abs(coord1[0] - coord2[0]) <= 1) & (abs(coord1[1] - coord2[1]) <= 1):

        return(True)

    else:

        return(False)


def spiral_memory_pt2(value, verbose = False):

    value = int(value)

    verbose = bool(verbose)

    current_ring = 0

    current_edge = 1

    current_ring_size = ring_size(current_ring)

    current_ring_edge_tiles = edge_tiles(current_ring)

    # list to store the indices of the current and previous ring tiles
    current_ring_indices = [0]
    previous_ring_indices = []

    coords = [(0, 0)]

    tiles_on_edge = 1

    tiles_on_ring = 1

    # list to store spiral values
    adjacent_sum = [0] * value
    adjacent_sum[0] = 1

    if verbose:

        print(coords[0])

    for i in range(1, value, 1):

        if tiles_on_edge == current_ring_edge_tiles:

            current_edge = current_edge + 1

        # moving to a new ring means moving one tile to the right
        if tiles_on_ring == current_ring_size:

            if verbose:

                print("new ring")

            previous_ring_indices = current_ring_indices

            current_ring = current_ring + 1

            current_ring_size = ring_size(current_ring)

            current_ring_indices = [x for x in range(i, i  + current_ring_size)]

            current_ring_edge_tiles = edge_tiles(current_ring)

            coords = coords + [(coords[i - 1][0] + 1, coords[i - 1][1])]

            tiles_on_edge = 1

            tiles_on_ring = 1

            current_edge = 1

            if verbose:

                print("current_ring_indices:", current_ring_indices)

                print("previous_ring_indices:", previous_ring_indices)

        else:

            if current_edge == 1:

                coords = coords + [(coords[i - 1][0], coords[i - 1][1] + 1)]

            elif current_edge == 2:

                coords = coords + [(coords[i - 1][0] - 1, coords[i - 1][1])]

            elif current_edge == 3:

                coords = coords + [(coords[i - 1][0], coords[i - 1][1] - 1)]

            elif current_edge == 4:

                coords = coords + [(coords[i - 1][0] + 1, coords[i - 1][1])]

            tiles_on_edge = tiles_on_edge + 1

            tiles_on_ring = tiles_on_ring + 1

        if verbose:

            print("i =", i, ":", coords[i], "tiles_on_edge", tiles_on_edge, "tiles_on_ring", tiles_on_ring, "current_edge", current_edge)

        if tiles_on_edge == current_ring_edge_tiles:

            current_edge = current_edge + 1

            tiles_on_edge = 0

        indices_to_add = []

        if verbose:

            print("tiles to check adjacency:", [x for x in previous_ring_indices + current_ring_indices if x <= i - 1])

        # loop through the tiles in the current ring and the previous ring where
        # the tiles are less in index than value - 1 i.e. they appear in the non spiral list before i
        # note i - 1 deals with zero indexing
        for x in [x for x in previous_ring_indices + current_ring_indices if x <= i - 1]:

            if tiles_adjacent(coords[i], coords[x]):

                indices_to_add = indices_to_add + [x]

        if verbose:

            print("tiles to sum:", indices_to_add)

        current_sum = 0

        for k in indices_to_add:

            current_sum = current_sum + adjacent_sum[k]

        adjacent_sum[i] = current_sum

        if current_sum > value:

            print("breaking loop, condition met: current_sum > value")

            print(current_sum)

            return(current_sum)

            break

    if verbose:

        print(adjacent_sum)


if __name__ == '__main__':

    if len(sys.argv[1:]) > 1:

        spiral_memory_pt2(sys.argv[1], sys.argv[2])

    else:

        spiral_memory_pt2(sys.argv[1])
