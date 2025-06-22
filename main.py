#Initialize dictionary
test_dict = {'codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'coding' : 1}
#print original dictionary
print("The original dictionary is : " + str(test_dict))
#Initialize value
K = 2
# Using loop
# Selecting key values in dictionary
res = 0
for key in test_dict:
    if test_dict[key] == K:
        res += 1
# Printing result
print("Frequency of K is : " + str(res))
