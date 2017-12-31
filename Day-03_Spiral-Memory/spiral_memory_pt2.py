import sys


def spiral_memory_pt2(value, verbose = False):

    value = int(value)

    verbose = bool(verbose)

    # list to hold values
    spiral_values = [0] * value
    spiral_values[0] = 1
    spiral_values[1] = 1

    spiral_tile_types = [""] * value
    spiral_tile_types[0] = "start"
    spiral_tile_types[1] = "after_diag"

    tile_type = spiral_tile_types[1]

    # which ring of the spiral we are on
    ring = 1

    # number of elements / tiles in the current ring
    ring_size = 8

    ring_start_index = 1

    # total number of elements in all rings currently in the sprial
    total_sprial_size = 8 + 1

    # number of non-diagonal, non-one-after-diagonal elements on an edge of the current ring
    ring_edge_adj_tiles = 0

    tiles_after_diagonal = 0

    ring_diagonal_counter = 0

    diagonal_indices = []

    #--------------------------------------------------------------------------#
    # Loop through tiles / cells from 3rd onwards
    #--------------------------------------------------------------------------#

    for i in range(2, value, 1):

        #----------------------------------------------------------------------#
        # Determine which type of tile we are on given the previous tile
        #----------------------------------------------------------------------#

        # if the previous tile was daig set the current tile to diagonal
        if tile_type == "diag":

            tile_type = "after_diag"

            tiles_after_diagonal = 0

        # if the previous tile was one after a diagonal set the current tile
        # to either diagonal or adjacent (more than one after diagonal)
        elif tile_type == "after_diag":

            tiles_after_diagonal = 1

            if (ring_edge_adj_tiles > 0) & (tiles_after_diagonal <= ring_edge_adj_tiles):

                tile_type = "adj"

            else:

                tile_type = "diag"

                ring_diagonal_counter = ring_diagonal_counter + 1

                diagonal_indices = diagonal_indices + [i]

        elif tile_type == "adj":

            tiles_after_diagonal = tiles_after_diagonal + 1

            if (ring_edge_adj_tiles > 0) & (tiles_after_diagonal <= ring_edge_adj_tiles):

                tile_type = "adj"

            else:

                tile_type = "diag"

                ring_diagonal_counter = ring_diagonal_counter + 1

                diagonal_indices = diagonal_indices + [i]

        #----------------------------------------------------------------------#
        # Check if the current tile has traversed into a new ring
        #----------------------------------------------------------------------#

        # marks entry onto a new ring
        if i == total_sprial_size:

            new_ring = True

            ring = ring + 1

            ring_size = ring * 8

            ring_edge_adj_tiles = (ring_size - 8) / 4

            total_sprial_size = total_sprial_size + ring_size

            # reset diagonal tiles passed counter
            ring_diagonal_counter = 0

            prev_ring_start_index = ring_start_index

            ring_start_index = i

            if verbose:

                print("new ring:", ring)

        else:

            new_ring = False

        #----------------------------------------------------------------------#
        # Calculate index of tile perpendicular to current tile
        #----------------------------------------------------------------------#

        if ring > 1:

            if tile_type == "adj":

                adj_index_dist = 9 + ((ring - 2) * 4) + (ring_diagonal_counter * 2)

            elif tile_type == "diag":

                adj_index_dist = 0

            elif tile_type == "after_diag":

                if new_ring:

                    adj_index_dist = 1

                else:

                    adj_index_dist = 9 + ((ring - 2) * 4) + (ring_diagonal_counter * 2)

        else:

            adj_index_dist = 1

        if verbose:

            print("i:", i, "-", tile_type, "-", adj_index_dist)

        spiral_tile_types[i] = tile_type

        #----------------------------------------------------------------------#
        # Determine the indices of tiles to add for the current tile
        #----------------------------------------------------------------------#

        # always add the previous tile
        indices_to_add = [i - 1]

        # for diagonals add the previous tile on the same diagonal plus the previous tile (WORKING)
        if tile_type == "diag":

            if ring > 1:

                # get the index of the previous tile on the same diagonal
                indices_to_add = indices_to_add + [diagonal_indices[len(diagonal_indices) - 5]]

            else:

                indices_to_add = indices_to_add + [0]

        # for tiles one after a diagonal sum the same tiles the diagonal summed (plus the diagonal itself)
        elif tile_type == "after_diag":

            # if the tile has moved to a new ring get adjacent + 1 tile up index
            if new_ring:

                indices_to_add = indices_to_add + [prev_ring_start_index]

            else:

                indices_to_add = indices_to_add + [i - 2]

                if ring > 1:

                    indices_to_add = indices_to_add + [diagonal_indices[len(diagonal_indices) - 5]] + [diagonal_indices[len(diagonal_indices) - 5] + 1]

                else:

                    indices_to_add = indices_to_add + [0]

        elif tile_type == "adj":

            # get the index of the adjacent tile from the previous ring (not diagonal)
            indices_to_add = indices_to_add + [i - adj_index_dist]

        if verbose:

            print("indices_to_add:", indices_to_add)

        #----------------------------------------------------------------------#
        # Add together adjacent tiles
        #----------------------------------------------------------------------#



        #----------------------------------------------------------------------#
        # Check exit condition: tile sum gt tile index
        #----------------------------------------------------------------------#





if __name__ == '__main__':

    if len(sys.argv[1:]) > 1:

        spiral_memory_pt2(sys.argv[1], sys.argv[2])

    else:

        spiral_memory_pt2(sys.argv[1])
