def losslessDataCompression(s, width):
    output = s[0]
    i = 1
    while i<len(s):
        window = s[max(0,i-width):i]
        ch = s[i]
        if ch not in window:
            output += ch
            i+=1
        else:
            for length in reversed(range(1,width+2)):
                for startIndex in range(max(0,i-width),i):
                    if s[startIndex:startIndex+length] in window and s[i:i+length]==s[startIndex:startIndex+length]:
                        break
                if s[startIndex:startIndex+length] in window and s[i:i+length]==s[startIndex:startIndex+length]:
                        break
            print i,startIndex,length
            i += length
            line = "("+str(startIndex)+","+str(length)+")"
            output += line
    
    return output
