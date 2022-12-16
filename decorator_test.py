def func(msg):
    print(msg)
    return func
hi_func = func("hi")
bye_func = func("bye")    
print(hi_func)
bye_func()