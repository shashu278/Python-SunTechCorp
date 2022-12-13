x=int(input("Enter number of rows: "))
for i in range(x+1,0,-1):    
    for j in range(0,i-1):  
        print("* ", end=" ")  
    print("\n")
