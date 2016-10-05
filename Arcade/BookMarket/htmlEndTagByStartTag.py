＃You are implementing your own HTML editor. To make it more comfortable for developers you would like to add an auto-completion feature to it.

#Given the starting HTML tag, find the appropriate end tag which your editor should propose.

#If you are not familiar with HTML, consult with this note.

#Example

#For startTag = "<button type='button' disabled>", the output should be
#htmlEndTagByStartTag(startTag) = "</button>";
#For startTag = "<i>", the output should be
#htmlEndTagByStartTag(startTag) = "</i>".

#Input/Output
#[time limit] 4000ms (py)

#[input] string startTag
#Constraints:
#3 ≤ startTag.length ≤ 75.

#[output] string

def htmlEndTagByStartTag(startTag):
    starTagSplit = startTag.split()
    if starTagSplit[0][-1]==">":
        return starTagSplit[0][0]+"/"+starTagSplit[0][1:]
    else:
        return starTagSplit[0][0]+"/"+starTagSplit[0][1:]+">"
