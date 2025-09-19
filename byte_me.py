# return the total byte size of the object. 
import sys
def total_bytes(obj):
    bsz = sys.getsizeof(obj)
    return bsz

