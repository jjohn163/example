
def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""
    q = num // b
    r = num % b
    str_r = str(r)
    if r >= 10:
        str_r = chr(ord("A") + r - 10)
    if q == 0:
        return str_r
    else:
        return convert(q,b) + str_r

#print(convert(0, 2))