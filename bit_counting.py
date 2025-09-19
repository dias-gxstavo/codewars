
""""
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
"""
def count_bits(n):
    arr = []

    if(n >= 1):
        bnry = bin(n)[2:]
        for i in bnry:
            if(i == '1'):
                count = arr.append(i)
                total = arr.count(i)
        return total
    return 0