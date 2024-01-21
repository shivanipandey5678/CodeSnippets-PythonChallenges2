//1
tc=int(input())
for i in range(tc):
    n=int(input())
    arr=input()
    dic={}
    count=0
    for i in range(n):
        if arr[i] not in dic:
            dic[arr[i]]=1
        else:
            dic[arr[i]]+=1
    for k in dic:
        if dic[k]%2!=0:
            count+=1
    if count==0 or count==1:
        print("Possible!")
    else:
        print("Not Possible!")
//2
n=int(input())
arr=list(map(int,input().split()))
dic={}
sumi=0
for i in range(len(arr)):
    if arr[i] not in dic:
        dic[arr[i]]=1
    else:
        dic[arr[i]]+=1
for k ,v in dic.items():
    if dic[k]==1:
        sumi+=k
print(sumi)

//3
n=int(input())
mat=[]
for i in range(n):
    arr=list(map(int,input().split()))
    mat.append(arr)
for i in range(n):
    mat[i].reverse()
        
for i in range(n):
    for j in range(n):
        if mat[i][j]==1:
            print(0,end=" ")
        elif mat[i][j]==0:
            print(1,end=" ")
    
    print()
 //4
 tc=int(input())
for i in range(tc):
    n=int(input())
    arr=list(map(int,input().split()))
    dic={}
    for i in range(len(arr)):
        if arr[i] not in dic:
            dic[arr[i]]=1
        else:
            dic[arr[i]]+=1
    for k,v in dic.items():
        if dic[k]==1:
            print(k)
            break

//5
tc=int(input())
for i in range(tc):
    n=int(input())
    arr=list(map(int,input().split()))
    dic={}
    for i in range(len(arr)):
        if arr[i] not in dic:
            dic[arr[i]]=1
        else:
            dic[arr[i]]+=1
    for k,v in dic.items():
        if dic[k]==1:
            print(k)
            break

//6
n=int(input())
arr=list(map(int,input().split()))
for i in arr:
    if i%2==0:
        print(i)
//7
n=int(input())
arr=list(map(int,input().split()))
arr.sort()
print(arr[n-1])
//8
n=int(input())
arr=list(map(int,input().split()))
arr.sort()
print(arr[n-1])
//9
n,m = map(int, input().strip().split())
mat = []
for i in range(n):
    mat.append(list(map(int, input().strip().split())))
R = n//2
C = m//2
# print(C)
# print(n)
sumi1 = 0
sumi2 = 0

for i in range(C) :
    sumi1+=mat[n-1][i]
# print(sumi1)
for i in range(n-1,-1,-1):
    sumi1+=mat[i][C]
# print(sumi1)    
for i in range(C+1,m):
    sumi1+=mat[0][i]
# print(sumi1)
for i in range(0,R) :
    sumi2+=mat[i][0]
# print(sumi2)
for i in range(m):
    sumi2+=mat[R][i]
# print(sumi2)
for i in range(R+1,n):
    sumi2+=mat[i][m-1]
# print(sumi2)


x=abs(sumi1-sumi2)
# print(sumi1,sumi2)   
print (x)
//10
n,m=map(int,input().split())
mat=[]
for i in range(n):
    arr=list(map(int,input().split()))
    mat.append(arr)
for i in range(m):
    product=1
    for j in range(n):
        if mat[j][i]%2!=0:
            product*=mat[j][i]
    print(product)
