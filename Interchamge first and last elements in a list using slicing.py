def swap_first_last_3(lst):
    if len(lst)>=2:
        lst = lst[-1:] + lst[1:-1] + lst[:1]
        return lst
inp=[2,4,6,8]
print("The original input is:",inp)
result=swap_first_last_3(inp)
print("The output after swap first and last is:",result)
