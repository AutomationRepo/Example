def changeList1( mylist ):
    mylist.append([1, 2, 3, 4])
    print("Values inside function:", mylist)


mylist = [5, 6, 7, 8]
changeList( mylist )
print("Values outside function:", mylist)
g = lambda x: x**2
print(g(5))
