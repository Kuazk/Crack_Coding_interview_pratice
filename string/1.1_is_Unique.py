# implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

# solution 1 hash table (On On):

def is_unique(str):
    hset = set()
    for ch in str:
        if ch in hset:
            return False 
        hset.add(ch)
    return True 
# solution 2 sort string and compare time (O(nlogn)) space(O1):

def is_unique2(string):
    sort_str = sorted(string)
    pre = sort_str[0]
    for ch in sort_str[1:]:
        if ch is pre:
            return False 
        else:
            pre = ch 
    return True

print(is_unique2('helisoo'))