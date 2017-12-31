import sys


def spiral_memory(value, verbose = False):

    value = int(value)

    verbose = bool(verbose)

    if value == 1:

        print(0)

        return(0)

    i = 0

    ring_size = 1

    total_elements = 1

    prev_ring_total_elements = 0

    while total_elements < value:

        # increment ring counter
        i = i + 1

        # number of elements in ring
        ring_size = 2 * i * 4

        # record the total elements in sprial excluding the current (outermost) ring
        prev_ring_total_elements = total_elements

        # accumulate total elements in spiral
        total_elements = total_elements + ring_size

        if total_elements > 1000000:

            print("breaking loop at 10^6 total elements")

            break

    if verbose:

        print("i:", i)

        print("total_elements:", total_elements)

    elements_into_ith_ring = value - prev_ring_total_elements

    if verbose:

        print("elements_into_ith_ring:", elements_into_ith_ring)

    # manhattan distance for the first element in the current ring
    ring_start_value = (2 * i) - 1

    # manhattan distance for the last element in the current ring
    ring_end_value = 2 * i

    # min manhattan distance in the current ring
    ring_min_value = i

    # max manhattan distance in the current ring
    ring_max_value = 2 * i

    eighth_step_size = i

    desc_eighth = [x for x in range(ring_max_value - 1, ring_min_value - 1, -1)]

    assert len(desc_eighth) == eighth_step_size, "desc_eighth incorrect length"

    asce_eighth = [x for x in range(ring_min_value + 1, ring_max_value + 1, 1)]

    assert len(asce_eighth) == eighth_step_size, "asce_eighth incorrect length"

    current_ring_mh_dist = []

    # construct the ring value would fall into by appending repeating
    # descending and ascending 1/8 segments of the ring
    for a in range(4):

        # this step constructs the ring value would land in
        # the elements of the ring are the manhattan distance to the center
        current_ring_mh_dist = current_ring_mh_dist + desc_eighth + asce_eighth

        # if ith ring has been constructed more elements than is needed for value
        if len(current_ring_mh_dist) > elements_into_ith_ring:

            break

    if verbose:

        print("current_ring_mh_dist:", current_ring_mh_dist)

    # extract the mh dist for the element value
    manhattan_distance = current_ring_mh_dist[elements_into_ith_ring - 1]

    print(manhattan_distance)

    return(manhattan_distance)




if __name__ == '__main__':

    if len(sys.argv[1:]) > 1:

        spiral_memory(sys.argv[1], sys.argv[2])

    else:

        spiral_memory(sys.argv[1])
