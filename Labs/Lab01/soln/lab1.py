def max_list_iter(tlist):  # must use iteration not recursion
    """ finds the max of a list of numbers and returns it, not the index"""
    if tlist is None:
        raise ValueError('empty list')
    if (len(tlist) == 0):
        return None
    maxnum = tlist[0]
    for num in tlist:
        if num > maxnum:
            maxnum = num
    return maxnum

def reverse_rec(int_list):   #must use recursion
    """ recursively reverses the integers in a list """
    if int_list is None:
        raise ValueError
    if len(int_list) <= 1:
        return int_list
    #length = len(int_list)
    #return int_list[length - 1:] + reverse_rec(int_list[:length - 1])  # length-1:length, 0:length-1
    return reverse_rec(int_list[1:]) + [int_list[0]]

def bin_search(target, low, high, int_list):  #must use recursion
    """ searches for target in list_val[low..high] and returns index if found"""
    if int_list is None:
        raise ValueError
    if low > high:
        return None
    mid = (low+high)//2
    if target > int_list[mid]:
        return bin_search(target,mid+1,high,int_list)
    elif target < int_list[mid]:
        return bin_search(target,low,mid-1,int_list)
    else:
        return mid
