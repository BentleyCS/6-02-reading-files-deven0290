def toString(fileName):

    f = open(fileName)
    out = ""
    for line in f:
        out += line
    return out


def longestLine(fileName):

    f = open(fileName)
    longest = ""
    for line in f:
        line = line.rstrip("\n")  
        if len(line) > len(longest):
            longest = line
    return longest


def toBinary(fileName):
   
    f = open(fileName)
    bits = ""
    for line in f:
        bits += line.strip()  

    result = []
    while len(bits) >= 8:
        result.append(bits[:8])
        bits = bits[8:]
    if bits: 
        result.append(bits)

    return result

