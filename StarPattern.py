""" 
program to prints the below pattern 

*
**
***
****
*****
******
*******
********
*********
**********

"""
for i in range(0,10,1):
    for i in range(0,i+1,1):
        print("*",end="")
    print("") 
