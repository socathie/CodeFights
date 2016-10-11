'''Morse code is a method of transmitting text information as a series of on-off tones, lights, or clicks. For more information, please read here.

Many of you might have watched a great movie called "The Imitation Game". For those of you who haven't, the movie is about cracking the enigma code during the WWII. In this challenge you're facing a similar problem.

You will be provided the encrypted message in International Morse Code and the encrypted key, which is a code of the "CF" message. Your mission is to build the correct code table and decrypt the message.

Please note that we will use "." for dot and "_" for dah.

Space between letters: 1
Space between words: 2
Example

For message = "_._. ___ _.. . .._. .. __. .... _ ..." and
key = "_._. .._.", the output should be
MorseCode(message, key) = "CODEFIGHTS".

The key stands for the original Morse table, so the message can be decrypted right away. The encrypted message is "CODEFIGHTS".

Input/Output

[time limit] 4000ms (py)
[input] string message

The encrypted message, a string consisting of symbols '_', '.' and ' '. It is guaranteed that the message is written in a correct Morse Code.

Constraints:
1 ≤ message.length ≤ 100.

[input] string key

The key to the Morse Table, a string consisting of symbols '_', '.' and ' '. The key is guaranteed to correctly represent two symbols (C and F) written in Morse Code.

Constraints:
1 ≤ key.length ≤ 20.

[output] string

Decrypted message consisting of uppercase English letters 'A'-'Z'.'''

L2M = {'A': '._',     'B': '_...',   'C': '_._.', 
        'D': '_..',    'E': '.',      'F': '.._.',
        'G': '__.',    'H': '....',   'I': '..',
        'J': '.___',   'K': '_._',    'L': '._..',
        'M': '__',     'N': '_.',     'O': '___',
        'P': '.__.',   'Q': '__._',   'R': '._.',
     	'S': '...',    'T': '_',      'U': '.._',
        'V': '..._',   'W': '.__',    'X': '_.._',
        'Y': '_.__',   'Z': '__..'
       }

M2L= dict((v,k) for (k,v) in L2M.items())

def MorseCode(message, key):
    key = key.split(' ')
    print M2L[key[0]]
    shift = ord(M2L[key[0]])-ord('C')
    print shift
    s = ''
    w = message.split('  ')
    for i in range(len(w)):
        l = w[i].split(' ')
        for j in range(len(l)):
            temp = str(chr((ord(M2L[l[j]])-shift-ord('A'))%26+ord('A')))
            s += temp
        s += ' '
    return s[:-1]
 
