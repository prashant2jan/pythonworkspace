string = input()
j = len(string)
flag = True
for i in range(0, j//2):
    if(string[i] == string[j-1]):
        i+=1
        j-=1
    else:
        flag = False
if(not flag):
    print(f"{string} is NOT a palindrome!")
else:
    print(f"{string} is a palindrome!")