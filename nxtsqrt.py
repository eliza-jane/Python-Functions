import math
def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    if math.sqrt(sq)==int(math.sqrt(sq)):
        return (math.sqrt(sq)+1)**2
    else:
        return -1