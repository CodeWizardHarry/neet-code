def outer():
    res=[1,2,3]


    def helper():
        # res.append(0)
        res = [0,0,0,0]
        
    helper()
    print(res)
    
outer()