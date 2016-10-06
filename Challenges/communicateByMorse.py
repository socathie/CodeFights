L2M = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..'
       }

M2L= dict((v,k) for (k,v) in L2M.items())

def communicateByMorse(signal):
    s = ''
    if '0'<=signal[0]<='1':
        w = signal.split('0000000')
        for i in range(len(w)):
            l = w[i].split('000')
            for j in range(len(l)):
                c = l[j].split('0')
                for k in range(len(c)):
                    if c[k]=='1':
                        c[k]='.'
                    else:
                        c[k]='-'
                c = ''.join(c)
                c = M2L[c]
                s += c
            s += ' '
        return s[:-1]
    else:
        w = signal.split(' ')
        for i in range(len(w)):
            for j in range(len(w[i])):
                c = w[i][j]
                c = L2M[c]
                for k in range(len(c)):
                    if c[k]=='-':
                        tmp='111'
                    else:
                        tmp='1'
                    s += tmp +'0'
                s += '00'
            s += '0000'
        return s[:-7]

'''Probably the most well known Morse Code message is SOS.
The message is made up of three short signals, then three long signals, and then three short signals again (...---...). This is the distress signal that people send out when they need help.

According to Wikipedia, some historians have called the Morse code the first digital code. This is because the Morse code uses just two states (On and Off) that is to flicker the light on/off, turn the sound tone on/off, or analogically set electrical pulse high/low.

To conform to ITU standard, the basic transmission of Morse code must obey the following rules where 1 is On and 0 is Off:

Dot: the signal must be turn on for 1, i.e. 1;
Dash: the signal must be turn on for 3 time units long: 111;
The signal forming the same letter between the dots and dashes should be turned off for 1 time unit long: 0
         Example:       Letter 'X' = '-..-' the signal would be sent as
                                                    '11101010111'

Gap between letters: the signal should be turned off for 3 time units long: 000
         Example:       Word 'MR' = '-- .-.' the signal would be sent as
                                                       '11101110001011101'
                                                                 M                     R

Medium gap between words: the signal should be turned off for 7 times unit long: 0000000
         Example:       Messge 'MR X' = '-- .-. / -..-' the signal would be sent as
                                                               '11101110001011101000000011101010111'

Here's your task. Given the signal string, decode it into a text message if it represents a Morse-decoded text, or encode it with Morse code if it represents a regular text.

Check out this link for the reference: Internations Morse Code.

Hope this challenge will not make you send out the distress SOS signals.
Good Luck and have fun!

Example

For signal = "MR X", the output should be
communicateByMorse(signal) = "11101110001011101000000011101010111".

For signal = "11101110001011101000000011101010111",
the output should be
communicateByMorse(signal) = "MR X".

Input/Output

[time limit] 4000ms (py)
[input] string signal

A string that contains either Morse binary digital code ('0's and '1's) or a regular message (Uppercase Latin letters 'A'-'Z').

Constraints:
4 ≤ input.length ≤ 5000.

[output] string

The decoded/encoded signal.'''
