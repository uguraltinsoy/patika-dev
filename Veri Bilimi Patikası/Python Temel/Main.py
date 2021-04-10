# Question 1
input1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flatten_list = []

def flattenUnList(input):
    for item in input:        
        if type(item) != list:
            flatten_list.append(item)
        else:
            flattenUnList(item) 

for item in input1:
    if type(item) != list:
        flatten_list.append(item)
    else:
        flattenUnList(item)      

print("Question 1 Result =>",flatten_list)

# Question 2 
input2 = [[1, 2], [3, 4], [5, 6, 7]]
reverse_list = []
input2.reverse()
for item in input2:
    item.reverse()
    reverse_list.append(item)
    
print("Question 2 Result =>",reverse_list)
