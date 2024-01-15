# the code below is used to flatten nested list
# for example input =[1,2,[3,[4,5]]]
# output= [1,2,3,4,5]

def flatten_nested_list(nested_list):
    flattened_list = []
    for item in nested_list:
        if isinstance(item, list):
            flattened_list.extend(flatten_nested_list(item))
        else:
            flattened_list.append(item)
    return flattened_list
