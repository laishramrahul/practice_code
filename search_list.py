old_list=["aaa a a","aaa","bbb","ccc"]
new_list=["aaa","bb"]
for i in range(len(new_list)):
    for j in range(len(old_list)):
        if new_list[i]==old_list[j]:
            print("same")