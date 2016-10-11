#You are given an array of desired filenames in the order of their creation. Since two files cannot have equal names, the one which comes later will have an addition to its name in a form of (k), where k is the smallest positive integer such that the obtained name is not used yet.

#Return an array of names that will be given to the files.

#Example
#For names = ["doc", "doc", "image", "doc(1)", "doc"], the output should be
#fileNaming(names) = ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"].

#Input/Output
#[time limit] 4000ms (py)

#[input] array.string names
#Constraints:
#5 ≤ names.length ≤ 15,
#1 ≤ names[i].length ≤ 15.

#[output] array.string

def fileNaming(names):
    output = [names[0]]
    for i in range(1,len(names)):
        if names[i] in names[0:i] or names[i] in output[0:i]:
            j = names[0:i].count(names[i])
            k = output[0:i].count(names[i])
            j = max(j,k)
            temp = names[i]+"("+str(j)+")"
            while temp in output[0:i]:
                j+=1
                temp = names[i]+"("+str(j)+")"
            output.append(temp)
        else:
            output.append(names[i])
    return output
