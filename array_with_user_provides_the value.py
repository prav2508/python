import array as a
x = int(input("Enter the size of array"))
arr = a.array('i',[])
for i in range(x):
    e = int(input("Enter the number.."))
    arr.append(e)
print("--------------")
print("the entered items are ..")
for t in range(x):
    print(arr[t])
print("--------------")

g = int(input("enetr the element to e]get index num"))
for i in range(x):
    if arr[i]==g:
        print("the index is ",i)
        break
    else:
        continue
print(arr.index(g))