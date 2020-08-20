def process(line: str) -> str:
    
    try:
        decimal = int(line[2:],base=16)
    except:
        return "INVALID"
    
    
    if(len(line) != 8):
        return "INVALID"
    
    #print(line)
    res = 0
    while (decimal != 0):
        res += decimal%10
        decimal //= 10
    chk = hex(res)[2:]
    
    if(chk.upper() == line[:2]):
        return "VALID"
    elif(res == 0 and line[:2] == "00"):
        return "VALID"
    else:
        return "INVALID"