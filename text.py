from screen import drawScreen

x = 'ieaieha'
y = 'faovao'

string = 'vwoiwi', x + y + 'owijwp', 618
string2 = 'Twas brillig and the slithy tothes did gire and gimble in the wabe, all mimsy were the borogroves and the momeraths outgabe!'
string3 = 'Please include the code that produced the message. Please include the smallest sample of code that actually produces this error message'

def splitIntoLines(string):
    output = []
    length = 52
    lastSpace = length + 1
    firstCount = 0
    while firstCount == 0:
        lastSpace = length
        if len(string) > length:
            secondCount = 0
            while secondCount == 0:
                endCharacter = string[lastSpace]
                if endCharacter == ' ':
                    output.append(string[:lastSpace])
                    string = string[lastSpace + 1:]
                    secondCount += 1
                else:
                    lastSpace -= 1
        else:
            output.append(string)
            return output

def getExtraSpace(line):
    spaces = 52 - len(line)
    extraSpace = ''
    for _ in range(spaces):
        extraSpace += ' '
    return extraSpace

def turnIntoOneString(therest):
    results = [] 
    for t in therest: 
        t = str(t)
        for x in t: 
            results.append(x)
        results.append(' ') 
    totalString = ''
    count = 0
    for string in results:
        if count == 0:
            totalString += str(string)
            count += 1
        else:
            totalString += str(string)
    return (totalString[:-1])

    
    


def text(data, *therest):
    drawScreen(data)
    newString = turnIntoOneString(therest)
    lines = splitIntoLines(newString)
#    print ('/------------------------------------------------------\\')
    for line in lines:
        extraSpace = getExtraSpace(line)
        print('| ' + line + extraSpace + ' |')
    print ('\\------------------------------------------------------/')
    input()

#text(string)

(('vwoiwi ', 'ieaiehafaovaoowijwp', 618),)