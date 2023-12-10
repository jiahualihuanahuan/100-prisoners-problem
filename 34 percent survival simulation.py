import random
from statistics import mean 

# create a function to get the value of a given index/key from an existing dictionary
def recursive_dict_value(dict, index, num_loops, start_index):
    # base case: if we've reached the end of the dictionary, return None
    if index >= len(dict):
        return None
    value = dict[index]
#     print(f"found {value} at index {index}")
    # stop recursion when we find a matching key
    if value == start_index:
        if num_loops <=50:
            return 1
        else:
            return 0

    # continue recursing until we reach the end of the dictionary or find a match
    else:
        num_loops += 1
        
        return recursive_dict_value(dict, value, num_loops, start_index)

successes_list = []
for j in range(1,10001):
    boxs_slips_pairs = {boxs[i]: slips_in_box[i] for i in range(len(boxs))}
    for i in range(1,101):
        successes_list.append(recursive_dict_value(boxs_slips_pairs,i,0,i))

mean(successes_list)
