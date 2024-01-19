def my_function(*args):
    # Function body
    for arg in args:
        print(arg)
my_function("Apple",1,"Monkey","two")

def func(p1,p2,*args,k,**kwargs):
    print("positional or keywords: ... {}".format(p1,p2))
    print("var-positional (*args):.......{}".format(args))
    print("keyword:....................{}".format(k))
    print("var-keyword:.......................{}".format(kwargs))
func(1,2,3,4,59,"Apple",5,k=9,key1=89,key2=90)
    
