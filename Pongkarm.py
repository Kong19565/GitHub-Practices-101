print('pongkarm')
# -*- coding: utf-8 -*-
"""
JobCode : F1C_6710301007
JobDes  : Final Exam. 2567/1 

StudID  : 6710301007
StudName: Darunpop PITAKKITPAISARN
Date    : 2024-10-03 xx:xx  
"""
import math

# *****************************
# ***** class TriangleSet *****
# *****************************
class TriangleSet:
    """class for Triangle Set """
    def __init__(self, triCode, sizeA, sizeB, sizeC, area):
        """Constructor Method to create TriangleSet instance """
        self.triCode = triCode
        self.sizeA = sizeA
        self.sizeB = sizeB
        self.sizeC = sizeC
        self.area = area

    def __str__(self):
        return f'{self.triCode:<9} {self.sizeA:<8} {self.sizeB:<7} {self.sizeC:<10} {self.area:.2f}'
    def showdata(self):
        print(f'triCode :{self.triCode:<8}')
        print(f'sizeA   :{self.sizeA:<8}')
        print(f'sizeB   :{self.sizeB:<8}')
        print(f'sizeC   :{self.sizeC:<8}')
        print(f'area    :{self.area:<8}')
        
        
# ***** Read Triangle File To triangle Memory *****
def triangleFile2TriMem(inFN):
    """ Read inFN(File) return trCol(Column), triMem(Memory) """    
    fin = open(inFN, 'r')
    FNMem = []
    l = 0
    with fin:
        for i in fin:
            triCode, sizeA, sizeB, sizeC, area = i.split()
            if l:
                sizeA = float(sizeA)
                sizeB = float(sizeB)
                sizeC = float(sizeC)
                area = float(area)
                FNMem.append(TriangleSet(triCode, sizeA, sizeB, sizeC, area))          
            else:
                FNCol = f'{triCode:10}{sizeA:7}{sizeB:>7}{sizeC:>8}{area:>11}'

            l += 1

    return FNCol, FNMem


# ***** Show All Triangle Memory *****
def showAlltriMem(trCol, trMem):
    """ Show All trMem(TriangleMem) return Total data, trQty, notrQty """
    notrQty = 0
    trQty = 0
    totData = trMem[-1]
    totData = totData.triCode[1:]
    print(trCol)
    for i in trMem:
        area = allTriangleArea(i.sizeA, i.sizeB, i.sizeC)
        if area > 0:
            trQty += 1
        else:
            notrQty += 1
        i.area = area
        print(f'{i.triCode:<5}     {i.sizeA:<6}   {i.sizeB:<5}   {i.sizeC:<8}   {area:.2f}')
    print(f'Total Date       =  {totData}')
    print(f'Total Triangle   =  {trQty}')
    print(f'Total not Tri.   =  {notrQty}')
    return totData, trQty, notrQty

def totAlltriMem(trMem):
    """ trMem(TriangleMem) return Total data, trQty, notrQty """
    notrQty = 0
    trQty = 0
    totData = trMem[-1]
    totData = totData.triCode[1:]
    for i in trMem:
        area = allTriangleArea(i.sizeA, i.sizeB, i.sizeC)
        if area > 0:
            trQty += 1
        else:
            notrQty += 1
        i.area = area
    
    return totData, trQty, notrQty


# ***** Write Triangle Memory to File *****
def trMemToTriangleFile(trCol, trMem, outFN):
    """ Write trMem to Triangle file """
    fout = open(outFN, 'w')
    with fout:
        fout.write(trCol+'\n')
        notrQty = 0
        trQty = 0
        totData = trMem[-1]
        totData = totData.triCode[1:]
        for i in trMem:
            if i.area > 0:
              trQty += 1
            else:
               notrQty += 1
            fout.write(f'{i.triCode:<9} {i.sizeA:<8} {i.sizeB:<8} {i.sizeC:<10} {i.area:.2f} \n')

        fout.write(f'\n')
        fout.write(f'Total Data       =  {totData}\n')
        fout.write(f'Total Triangle   =  {trQty}\n')
        fout.write(f'Total not Tri.   =  {notrQty}\n')



def showdata_current_trmem(trCol,trMem):
    print(trCol)
    for i in trMem:
        print(i)

# *************************************
# ***** subroutine from FlowChart *****
# *************************************
def bigAndSmall(a, b):
    """ return small, big"""
    if a < b :
        big = b
        small = a
    else :
        big = a
        small = b
            
    return (small, big)

def biggestOfThree(a, b, c):
    """ return s1,s2,s3 that s3 is the biggest """   
    s1, s2 = bigAndSmall(a, b)
    s2, s3 =  bigAndSmall(s2, c)
    
    return (s1, s2, s3)

def isZero(a, b, c):
    """ return iz is qty of zero """   
    iz = 0
    if a == 0 :
        iz += 1
    if b == 0 :
        iz += 1
    if c == 0 :
        iz += 1
           
    return iz

def isNotTriangle(a, b, c):
    """ return ierr, errcode = 1,2,3,4 is not triangle """
    ierr = isZero(a, b, c)
    if ierr == 0 :
        s1, s2, s3 = biggestOfThree(a, b, c)
        if s3 >= (s1 + s2):
            ierr = 4
    return ierr

def trueTriangleArea(a, b, c):
    """ return Cal. Triang;e Area from a, b, c """
    s = (a + b + c)/2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
 
    return area

def allTriangleArea(a, b, c):
    """ return Cal. Triang;e Area from a, b, c """
    ierr = isNotTriangle(a, b, c)
    if ierr == 0:
        area = trueTriangleArea(a, b, c)
    else:
        if ierr == 1:
            area = -991
        elif ierr == 2:
            area = -992
        elif ierr == 3:
            area = -993
        elif ierr == 4:
            area = -994
        else:
            area = -999
        
    return area

if __name__ == "__main__":
#********************
#*** Main Program ***
#********************
#     inFN = 'InputData.txt'
    
    
# #**** Test def bigAndSmall(a,b) ***
#     x = 10
#     y = 2 
#     sm, bg = bigAndSmall(x, y)
#     print(f'    x,   y = {x:8.2f},{y: 8.2f}')
#     print(f'Small, Big = {sm:8.2f},{bg:8.2f}')
# #**** end  Test ****

# #**** Test def biggestOfThree(a, b, c) ***
#     x = 15
#     y = 10
#     z = 25
#     s1, s2, s3 = biggestOfThree(x, y, z)
#     print(f' x,  y,  z = {x:8.2f},{y: 8.2f},{z: 8.2f}')
#     print(f's1, s2, s3 = {s1:8.2f},{s2:8.2f},{s3:8.2f}')
# #**** end  Test ****

# #**** Test def isZero(a, b, c) ***
#     x = 20
#     y = 0.0
#     z = 0.15
#     izero = isZero(x, y, z)
#     print(f' x,  y,  z = {x:8.2f},{y: 8.2f},{z: 8.2f}')
#     print(f'There are {izero}')
# #**** end  Test ****

# #**** Test def isNotTriangle(a, b, c)  ***
#     a = 3
#     b = 4
#     c = 5
#     ierr = isNotTriangle(a, b, c)
#     print(f'a,  b,  c = {a:8.2f},{b: 8.2f},{c: 8.2f}')
#     if ierr == 0:
#         print(f'This is Triangle')
#     else:
#         print(f'This is not Triangle')
        
#     print(f'ierr = {ierr}')
# #**** end  Test ****

# #**** Test def allTriangleArea(a, b, c)  ***
#     a = 1
#     b = 2
#     c = 3
#     area = allTriangleArea(a, b, c)
#     print(f'a,  b,  c = {a:8.2f},{b: 8.2f},{c: 8.2f}')
#     if area > 0:
#         print(f'\nThis is Triangle')
#     else:
#         print(f'\nThis is not Triangle')
        
#     print(f'area = {area:8.2f}')
#**** end  Test ****

# **** Test Input, Output File from class TriangleSet:
    inFN = 'InputDataA.txt'
    trCol, trMem = triangleFile2TriMem(inFN)
    totData, trQty, notrQty = showAlltriMem(trCol, trMem)
    print(f'------ end ------')
    print()
    print()
    showdata_current_trmem(trCol, trMem)
    outFN = 'OutputData.txt'
    trMemToTriangleFile(trCol, trMem, outFN)
    print('sucessfully')
# **** end  Test ****
