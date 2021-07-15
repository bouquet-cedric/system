from sys import argv
import os

print("\n\t\t\t Système d'équation")

def vars(line):
    lesX = ""
    lesY = ""
    leR = ""
    xFound = False
    yFound = False
    rFound = False
    cpt = 0
    charX = "x"
    charY = "y"
    for i in line:
        if not xFound:
            if i.isdigit() or i == '-':
                lesX+=str(i)
        elif not yFound:
            if i.isdigit() or i == '-':
                lesY+=str(i)
        elif not rFound:
            if i != '=' and i != ' ':
                leR+=str(i)
        if i != '-' and i.isdigit()==False and i!= ' ' and i!='+' and i != '=':
            if cpt==0:
                charX = str(i)
                xFound = True
            elif cpt == 1:
                charY = str(i)
                yFound = True
            cpt += 1
    lesY = backPossible(lesY)
    lesX = backPossible(lesX)
    return [int(lesX),int(lesY),int(leR),charX,charY]

def backPossible(laVar):
        if laVar == "-":
            return -1
        if laVar == "":
            return 1
        return laVar

def ppcm(a,b):
    x = abs(a)
    y = abs(b)
    cpt = 1
    while 1:
        tmp = x * cpt
        if tmp % y == 0:
            return tmp
        cpt += 1
    return -1


def checkV1IsNotDividendeOfV2(v1,v2):
    lesX = (v1[0] % v2[0] == 0)
    if lesX:
        coeffX = v1[0] / v2[0]
        lesY = (v1[1] % v2[1] == 0)
        if lesY:
            coeffY = v1[1] / v2[1]
            lesR = (v1[2] % v2[2] == 0)
            if lesR and (coeffX == coeffY):
                coeffR = v1[2] / v2[2]
                if coeffR == coeffX:
                    return False
    return True



def calcul(t1,t2):
    if t1[3] != t2[3] or t1[4] != t2[4]:
        return ["ERREUR","<VariableError> : 2 inconnues attendues"]
    if t1[0] == t2[0] and t1[1] == t2[1]:
        return ["ERREUR","<SolutionNotFound> : Les droites sont parallèles"]
    if checkV1IsNotDividendeOfV2(t1,t2):
        coeff = ppcm(t1[0],t2[0])
        x = int(coeff / t1[0])
        y = int(coeff / t2[0])
        y1 = t1[1] * int(x)
        r1 = t1[2] * int(x)
        y2 = t2[1] * int(y)
        r2 = t2[2] * int(y)
        Y = y1 - y2
        R = r1 - r2
        Y = (R/Y)
        X = (t1[2] - Y*t1[1])/t1[0]
        return [f"{t1[3]} = {X}", f"{t1[4]} = {Y}"]
    return ["ERREUR","<InfinityError> : Les deux droites sont confondues"]


if len(argv) == 2:
    f= open(argv[1], 'r')
    l = f.readlines()
    cpt = 0
    tmp = []
    sn = 0
    for i in l:
        if i != "\n":
            if cpt == 0:
                tmp.append(i[:-1])
                cpt = 1
            else:
                tmp.append(i[:-1])
                sn += 1
                print("\n __________________________________________________________________________\n/ Système S"+str(sn)+"\n| {\n| \t"+tmp[0]+"\n| \t"+tmp[1]+"\n| }")
                v1 = vars(tmp[0])
                v2 = vars(tmp[1])
                res = calcul(v1,v2)
                print("| Solution : "+res[0]+", "+res[1]+"\n\\__________________________________________________________________________")
                tmp=[]
                cpt = 0
else:
    l1 = input("> ")
    v1 = vars(l1)
    l2 = input("> ")
    v2 = vars(l2)
    res = calcul(v1,v2)
    print("Solution : "+res[0]+", "+res[1])
    os.system("pause > nul")
