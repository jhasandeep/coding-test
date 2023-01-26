# Write a Python program that finds the longest common substring between two strings.

A = input()
B = input()

if len(A) > len(B) :
    bigger = len(A)
else:
    bigger = len(B)

count = 0
for i in range(bigger):
    
        
    if A[i] == B[i]: 
        count +=1 
    else: 
        count +=0
        break
        
            
print(count)
