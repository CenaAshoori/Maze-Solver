import copy
from collections import deque
import random
import datetime
print("Enter the number of your Choice:\n1-Solve Matrix From File\n2-Random Matrix\n3-Full Random")
num=int(input(">>>"))
if num==1:
    f = open("E:\\Uni\Maze\Maze","r")
    n=int(f.readline())
    print(n)
    matrix=[[0]*n for i in range(n)]
    for i in range(n):
        string=f.readline()
        j=0
        for word in string:
            if word == '0':
                matrix[i][j]=1
                j+=1
            elif word=='1':
                matrix[i][j]=0
                j+=1
    for row in matrix:
        for col in row:
            print(col, end=" ")
        print()
elif num==2:
    n=int(input("Enter number of row and col matrix:"))
    matrix=[[0]*n for i in range(n)]
    for i in range(n):
        matrix[i][i]=1
    for i in range(n):
        matrix[random.randrange(0,n)][random.randrange(0,n)]=1
elif num==3:
    fr = open('E:\\Uni\Maze\Random Maze',"w")
    n=int(input("Enter number of row and col matrix:"))
    matrix=[[0]*n for i in range(int(n))]
    matrix[0][0] = 1
    matrix[n - 1][n - 1] = 1
    for i in range(n):
        shape=random.randrange(1,3)
        # matrix[random.randrange(0,n)][random.randrange(0,n)]=0
        if shape==1:
            for m in range(int(n/4)):
                i,j=random.randrange(0,n),random.randrange(0,n)
                if i+1<n and j+2<n:
                    matrix[i][j]=1
                    matrix[i][j+1]=1
                    matrix[i][j+2]=1
                    matrix[i+1][j+2]=1

        elif shape==2:
            i,j=random.randrange(0,n),random.randrange(0,n)
            if i+1<n and j+1<n:
                matrix[i][j]=1
                matrix[i][j+1]=1
                matrix[i+1][j]=1
                matrix[i][j-1]=1
                matrix[i-1][j]=1
        elif shape==3:
            pass
    for row in matrix:
        for col in row:
            print(col, end=" ")
            fr.write(str(col))
            fr.write(" ")
        fr.write("\n")
        print()
# Show matrix on Console

# class Path():
stack = deque()
path=deque()
r=matrix.__len__() #سطر
c=matrix[0].__len__() #ستون
class Data():
    #Dir's
    #    5 6 7
    #    4 # 0
    #    3 2 1

    def __init__(self):
        self.dirs = [0] * 8
        self.isDir = [0] * 8
        self.visit=False
    def isVisited(self):
        if self.visit:
            return True
        else :
            return False
    def visited(self):
        self.visit=True
    def unVisited(self):
        self.visit=False
    def setInfo(self,row,col,val):
        self.row=row
        self.col=col
        self.val=val
        if not val:
            self.visit=True
    def getDirs(self):
        sum=0
        for i in self.dirs:
            sum +=i
        # print(sum)
        return sum
    def setDir(self, mat) :
        self.dirs = [0] * 8
        mat[row][col].dirs[1] = 1 if row + 1 < r and col + 1 < c and not mat[row + 1][col + 1].isVisited() and mat[row + 1][col + 1].val else 0
        mat[row][col].dirs[2] = 1 if row + 1 < r and col < c and not mat[row + 1][col].isVisited() and mat[row + 1][col].val else 0
        mat[row][col].dirs[0] = 1 if row < r and col + 1 < c and not mat[row][col + 1].isVisited() and mat[row][col + 1].val else 0
        mat[row][col].dirs[3] = 1 if row + 1 < r and col - 1 >= 0 and not mat[row + 1][col - 1].isVisited() and mat[row + 1][col - 1].val else 0
        mat[row][col].dirs[7] = 1 if row - 1 >= 0 and col + 1 < c and not mat[row - 1][col + 1].isVisited() and mat[row - 1][col + 1].val else 0
        mat[row][col].dirs[6] = 1 if row - 1 >= 0 and col < c and not mat[row - 1][col].isVisited() and mat[row - 1][col].val else 0
        mat[row][col].dirs[4] = 1 if row < r and col - 1 >= 0 and not mat[row][col - 1].isVisited() and mat[row][col - 1].val else 0
        mat[row][col].dirs[5] = 1 if row - 1 >= 0 and col - 1 >= 0 and not mat[row - 1][col - 1].isVisited() and mat[row - 1][col - 1].val else 0
mat= [[Data() for j in range(c)] for i in range(r)]
#initializing array of object(NODE)
for i in range(r):
    for j in range(c):
        mat[i][j].setInfo(i,j,matrix[i][j])
#finding Dirs per Nodes
row, col= 0, 0
mat[0][0].setDir(mat)
counter=0
time=datetime.datetime.now()
print(time.minute,":",time.second,":",time.microsecond)
while(True):
    if not row and not col and not mat[row][col].getDirs():
        break
    if row==r-1 and col==c-1 :
        counter += 1
        stack.append(mat[r-1][c-1])
        if counter >1 and stack.__len__()<path[0].__len__():
            path.clear()
            path.append(copy.deepcopy(stack))
        elif counter==1:
            path.append(copy.deepcopy(stack))
            for item in stack:
                print(item.row, item.col)
        stack.remove(stack[-1])
        row=stack[-1].row
        col=stack[-1].col
        stack.remove(stack[-1])


    if mat[row][col].getDirs() == 0:
        # print("if 2 main")
        mat[row][col].unVisited()
        row = stack[-1].row
        col = stack[-1].col
        stack.pop()
    elif row+1 <r and col+1 <c and mat[row+1][col+1].val and  mat[row][col].dirs[1]==1 and not mat[row+1][col+1].isVisited():
        # print("==" * 7, "\n", row, col)
        # print("Down Right")
        mat[row][col].visited()
        stack.append(mat[row][col])
        mat[row][col].dirs[1]=0
        # print(mat[row][col].getDirs())
        row+=1
        col+=1
        mat[row][col].setDir(mat)
        #moving down Right
    elif row < r and col + 1 < c and mat[row][col + 1].val and mat[row][col].dirs[0] == 1 and not mat[row][col + 1].isVisited():
        # print("==" * 7, "\n", row, col)
        # print("Right")
        stack.append(mat[row][col])
        mat[row][col].visited()
        mat[row][col].dirs[0] = 0
        col += 1
        mat[row][col].setDir(mat)
        # moving Right
    elif row+1 <r and col <c and mat[row+1][col].val and mat[row][col].dirs[2]==1 and not mat[row+1][col].isVisited():
        # print("==" * 7, "\n", row, col)
        # print("Down")
        stack.append(mat[row][col])
        mat[row][col].visited()
        mat[row][col].dirs[2] = 0
        row+=1
        mat[row][col].setDir(mat)
        #moving down
    elif row - 1 >= 0 and col + 1 < c and mat[row - 1][col + 1].val and mat[row][col].dirs[7] == 1 and not mat[row - 1][col + 1].isVisited():
        # print("==" * 7, "\n", row, col)
        # print("Up Rigth")
        stack.append(mat[row][col])
        mat[row][col].visited()
        mat[row][col].dirs[7] = 0
        row -= 1
        col += 1
        mat[row][col].setDir(mat)
        # moving up Right
    elif row+1 <r and col-1>=0 and mat[row+1][col-1].val and mat[row][col].dirs[3]==1and not mat[row+1][col-1].isVisited():
        # print("==" * 7, "\n", row, col)
        # print("Down Left")
        stack.append(mat[row][col])
        mat[row][col].visited()
        mat[row][col].dirs[3]=0
        row+=1
        col-=1
        mat[row][col].setDir(mat)
        #moving down Left
    elif row-1 >=0 and col <c and mat[row-1][col].val and mat[row][col].dirs[6]==1 and not mat[row-1][col].isVisited():
        # print("==" * 7, "\n", row, col)
        # print("Up")
        stack.append(mat[row][col])
        mat[row][col].visited()
        mat[row][col].dirs[6]=0
        row -= 1
        mat[row][col].setDir(mat)
        #moving up
    elif row < r and col-1 >=0 and mat[row][col-1].val and mat[row][col].dirs[4]==1 and not mat[row][col-1].isVisited():
        # print("==" * 7, "\n", row, col)
        # print("Left")
        stack.append(mat[row][col])
        mat[row][col].visited()
        mat[row][col].dirs[4]=0
        col -= 1
        mat[row][col].setDir(mat)
        #moving left
    elif row-1 >=0 and col-1 >=0 and mat[row-1][col-1].val and mat[row][col].dirs[5]==1 and not mat[row-1][col-1].isVisited():
        # print("==" * 7, "\n", row, col)
        # print("Up Left")
        stack.append(mat[row][col])
        mat[row][col].visited()
        mat[row][col].dirs[5]=0
        row -= 1
        col -= 1
        mat[row][col].setDir(mat)
        #moving up Left


print('\n\n\n\t\t',counter,"direction Founded\n")
for item in path:
    print ("BEST DIRECTION IS:")
    for ite in item:
        print(f"({ite.row},{ite.col})",end="")
        if ite != item[-1]:
            print(" , ",end="")
print()
if len(path):
    for row in matrix:
        for col in row:
            print (col,end=" ")
        print()
    matrix=[[0]*n for i in range(n)]
    print("AND THE MATRIX IS :")
    for elment in path:
        for item in elment:
            matrix[item.row][item.col]=1
    for row in matrix:
        for col in row:
            print (col,end=" ")
        print()
else :
    print("NO DIRECTION !!")
new_time=datetime.datetime.now()
print("RunTime:",int(new_time.minute)-int(time.minute),":",int(new_time.second)-int(time.second),":",float(new_time.microsecond)-float(time.microsecond))
