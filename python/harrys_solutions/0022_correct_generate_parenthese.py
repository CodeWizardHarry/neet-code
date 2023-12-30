[0,3,5,7,10]
l   
   r 


while l <= r:
    m = (l + r) // 2
    if last_col[m] < target: 
        prev_l = l
        l = m + 1
    elif  target < last_col[m]:
        r = m -1
    else:
        return True