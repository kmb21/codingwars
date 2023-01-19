def array_diff(a, b):
    #your code here
    for item in b:
        while item in a:
            a.remove(item)
    return a