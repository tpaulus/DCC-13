#! /usr/bin/python
#Written By Tom Paulus, @tompaulus, www.tompaulus.com

class Scroller():
    def __init__(self):
        return

    def splitString(self, s, lineLength):
        # s = 'The Quick Brown Fox Jumps Over The Lazy Dog' #Test String

        string = ''
        length = 0
        k = 0       #Counter Variable
        wordLength = list()
        strings = list()
        lines = list()

        words = s.strip().split()

        for k in range(0, len(words)):
            length = len(words[k])
            wordLength.append(length)

        k = 0       #Reset Counter

        while k < len(words):
            if len(string) + len(words[k]) + 1 < lineLength:
                if len(string) == 0:
                    string += words[k]
                else:
                    string = string + ' ' + words[k]
                k += 1

            else:
                strings.append(string)
                string = ''

            if k == len(words):
                strings.append(string)
                string = ''
        k = 0       #Reset Counter

        while k < len(strings):
            if k == len(strings) - 1:
                line = strings[k]
                lines.append(line)
                break
            else:
                line = strings[k] + '\n' + strings[k + 1]
                lines.append(line)
                k += 2
        return lines


if __name__ == '__main__':
    #Library Test
    s = raw_input('Enter the string to be separated\n').replace('\n', '')
    tools = Scroller()
    print tools.splitString(s, 16)