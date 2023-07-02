square= lambda x: x**2

list1= list(map(int, input("Enter list element separated by space: ").split()))
result= list(map(square, list1))
print("Square of every element: ", result)