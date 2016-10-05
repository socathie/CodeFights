#A media access control address (MAC address) is a unique identifier assigned to network interfaces for communications on the physical network segment.

#The standard (IEEE 802) format for printing MAC-48 addresses in human-friendly form is six groups of two hexadecimal digits (0 to 9 or A to F), separated by hyphens (e.g. 01-23-45-67-89-AB).

#Example
#For inputString = "00-1B-63-84-45-E6", the output should be
#isMAC48Address(inputString) = true;
#For inputString = "Z1-1B-63-84-45-E6", the output should be
#isMAC48Address(inputString) = false;
#For inputString = "not a MAC-48 address", the output should be
#isMAC48Address(inputString) = false.

#Input/Output
#[time limit] 4000ms (py)

#[input] string inputString
#Constraints:
#15 ≤ inputString.length ≤ 20.

#[output] boolean
#true if inputString corresponds to MAC-48 address naming rules, false otherwise.

def isMAC48Address(inputString):
    if len(inputString)!=17:
        return False
    
    inputStringSplit = inputString.split('-')
    
    if len(inputStringSplit)!=6:
        return False
    
    for i in range(0,len(inputStringSplit)):
        if len(inputStringSplit[i])!=2:
            return False
        if (("0"<=inputStringSplit[i][0]<="9" or "A"<=inputStringSplit[i][0]<="F") and ("0"<=inputStringSplit[i][1]<="9" or "A"<=inputStringSplit[i][1]<="F")):
            return True
        else:
            return False
