elements=[3,4,5,63,6,753,64]
for i in range(len(elements)):
    print("index--->",i,"----->",elements[i])

for idx, el in enumerate(elements):
    print(idx,el)

obj1=enumerate(elements)
print(list(obj1))    