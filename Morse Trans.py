# this is a Morse Code Translator
"""
Function Planned:
1. encoding string into morse code,
2. decoding morse code into string,
3. replace . OR - with different singals.
"""
# Dictionary of encoding and decoding
encodedict = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    ' ': ' ',
    '': '',
    ".": ".-.-.-",
    ",": "--..--",
    ":": "---...",
    "?": "..--..",
    "'": ".----.",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "=": "-...-"
}
decodedict = {v: k for k, v in encodedict.items()}

# Context includes alpha 'A' to 'Z' adn number 0 to 9
# Code includes '.' for DIT, and '-' for DAH

# encoding function to translate normal text to morse code


def replaceChar(s, old, new):
    if old != new:
        print('old is', old, ', new is', new)
        return s.replace(old, new)
    return s


def encoding(text, sep='/', DIT='.', DAH='-'):
    encode = sep.join(encodedict.get(c.upper()) for c in text)
    encode = replaceChar(encode, '.', DIT)
    encode = replaceChar(encode, '-', DAH)
    return encode


def decoding(morcod, sep='/', DIT='.', DAH='-'):
    morcod = replaceChar(morcod, DIT, '.')
    morcod = replaceChar(morcod, DAH, '-')
    decode = ''.join(decodedict.get(s) for s in morcod.split(sep))
    return decode


print('Please choose which function would you need:')
print('1. Encoding -- from normal text to morse code')
print('2. Decoding -- from morse code to normal text')
fc = input('Please type in 1 OR 2 and press Enter\n')
if fc == '1':
    msg = input('Please in put your normal text\n')
elif fc == '2':
    msg = input('Please in put your morse code\n')
else:
    print('Please check your input')
rep = input('Use other char instead of .-/ ? y/n\n')
if rep == 'y':
    sep = input('Separator is?\t')
    DIT = input('DIT is?\t')
    DAH = input('DAH is?\t')
else:
    sep = '/'
    DIT = '.'
    DAH = '-'
repdict = {'sep': sep, 'DIT':  DIT, 'DAH': DAH}
if fc == '1':
    print(encoding(msg, **repdict))
else:
    print(decoding(msg, **repdict))
print('Translation work done')
