list1 = []
num = int(input("Enter number of elements in list: "))
for i in range(1, num+1):
    elm =input("Enter element "+str(i)+" :")
    list1.append(elm)
print(list1)    
print("Largest element in list1 is: ",list1[-1])

