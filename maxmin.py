list1=[2,4,1,0,2,-1]
list2=[20,50,12,6,14,8]
list3=[100,-100]

def maxmin(list):
    min_value=list[0]
    max_value=list[0]
    for num in list:
        if num < min_value:
            min_value=num
        if num > max_value:
            max_value=num
    return [min_value,max_value]

print(maxmin(list1))
print(maxmin(list2))
print(maxmin(list3))