def mix_lists(list1, list2, list3, list4):
    return [{v1:{"key_2":v2, "key_3":v3,"key_4":v4}}  for v1, v2,v3,v4 in zip(list1,list2, list3, list4)]





list1=["my_key_name_1",3]
list2=["green","brown","blue"]
list3=[1,2,3,4]
list4=["string","float",-1,0]

print(mix_lists(list1,list2,list3,list4))