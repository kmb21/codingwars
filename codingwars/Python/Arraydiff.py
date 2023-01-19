def array_diff(a, b):
   
    for item in b:
        while item in a:
            a.remove(item)
    return a