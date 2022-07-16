'''12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print'''

num=int(input("enter the number :"))
list=[]
for i in range(0,num):
    n=input().split()

    if n[0]=='insert':
        list.insert(int(n[1]),int(n[2]))
    elif n[0]=='print':
        print(list)
    elif n[0]=='remove':
        list.remove(int(n[1]))
    elif n[0]=='append':
        list.append(int(n[1]))
    elif n[0]=='sort':
        list.sort()
    elif n[0]=='print':
        print(list)
    elif n[0]=='pop':
        list.pop()
    elif n[0]=='reverse':
        list.reverse()
    elif n[0]=='print':
        print(list)
        
