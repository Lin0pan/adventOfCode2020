import re

def importNumbers(file):
    f = open(file, "r")
    pws = f.readlines()
    f.close()
    return pws

def createRex(rule):
    splt = rule.split(' ')
    minmax = splt[0].split('-')
    c = splt[1]
    rx = '^([^'+c+']*'+c+'[^'+c+']*){'+minmax[0]+','+minmax[1]+'}$'
    return rx

def countMatches(pws):
    n = 0
    for pw in pws:
        splt = pw.split(':')
        rx = createRex(splt[0])
        if re.search(rx, splt[1]):
            n+=1
    return n

def main():
    pws = importNumbers('input.txt')
    print(countMatches(pws))

if __name__ == "__main__":
    main()



