'''There are several ways to join two set 
    1. union() or | 
    2. update()
    3. intersection() or &
    4. difference()
'''

set1= {"red", "black", "blue", "green",1}
set2 ={1, 2, 3, 4}

set3 = set1 | set2
print(set3)

set4 = set1.union(set2)
print(set4)

set5 = set1 & set2; print(set5) #intersection

