
def int2addr(number):
    """converts an integer to addr_hi and addr_lo bytes"""
    return number >> 8, number & 255

def addr2int(addr):
    """converts addr_hi and addr_lo into single number address"""
    hi, lo = addr
    return hi << 8 | lo & 255