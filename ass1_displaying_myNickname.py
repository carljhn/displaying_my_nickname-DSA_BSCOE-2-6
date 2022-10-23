# Assignment 1:
# Create a program that will print your nickname using only asterisk character (*)
# Your program should be uploaded to github before 11:59 pm on Oct 22, 2022

nickname="CARL"
print_C=[[" " for i in range (7)] for j in range (7)] 
print_A=[[" " for i in range (7)] for j in range (7)]
print_R=[[" " for i in range (7)] for j in range (7)] 
print_L=[[" " for i in range (7)] for j in range (7)]

#code for C
for row in range (7):
    for col in range (7):
        if (col==0 and (row!=0 and row!=6)) or ((row==0 or row==6) and (col>0)):
            print_C[row][col]= "*"

#code for A
for row in range(7):
    for col in range(7):
        if ((col==0 or col==6) and row!=0) or row==3 or (row==0 and (col!=0 and col!=6)):
            print_A[row][col]= "*"

#code for R
for row in range(7):
    for col in range(7):
        if col==0 or (col==6 and (row!=0 and row!=3)) or ((row==0 or row==3) and (col>0 and col<6)):
            print_R[row][col]= "*"

#code for L
for row in range(7):
    for col in range(7):
        if col==0 or row==6:
            print_L[row][col]= "*"

#combine
for i in range(7):
    for j in range(7):
        print(print_C[i][j],end="")
    print(end="  ")
    for j in range(7):
        print(print_A[i][j],end="")
    print(end="  ")
    for j in range(7):
        print(print_R[i][j],end="")
    print(end="  ")
    for j in range(7):
        print(print_L[i][j],end="")
    print()

#Other Algorithm that can be used. 
print(" ******   ******   *******   *")
print("*        *      *  *      *  *")
print("*        *      *  *      *  *")
print("*        ********  *******   *")
print("*        *      *  *      *  *      ")
print(" ******  *      *  *      *  *******")