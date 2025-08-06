n=int(input("enter the no of the list"))
nums=[]
for i in range(n):
    num=int(input("enter element{i+1}:"))
    nums.append(num)
unique=set(nums)
print("unique elements:",unique)
