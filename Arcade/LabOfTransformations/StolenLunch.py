#When you recently visited your little nephew, he told you a sad story: there's a bully at school who steals his lunch every day, and locks it away in his locker. He also leaves a note with a strange, coded message. Your nephew gave you one of the notes in hope that you can decipher it for him. And you did: it looks like all the digits in it are replaced with letters and vice versa. Digit 0 is replaced with 'a', 1 is replaced with 'b' and so on, with digit 9 replaced by 'j'.

#The note is different every day, so you decide to write a function that will decipher it for your nephew on an ongoing basis.

#Example
#For note = "you'll n4v4r 6u4ss 8t: cdja", the output should be
#stolenLunch(note) = "you'll never guess it: 2390".

#Input/Output

#[time limit] 4000ms (py)

#[input] string note
#A string consisting of lowercase English letters, digits, punctuation marks and whitespace characters (' ').
#Constraints:
#0 ≤ note.length ≤ 500.

#[output] string
#The deciphered note.

def stolenLunch(note):
    newNote = []
    for i in range(0,len(note)):
        print i
        if '0'<=note[i]<='9':
            newNote.append(chr(int(note[i])+ord('a')))
        elif 'a'<=note[i]<='j':
            newNote.append(str(ord(note[i])-ord('a')))
        else:
            newNote.append(note[i])

        return "".join(newNote)
