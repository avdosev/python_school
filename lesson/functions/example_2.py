def f(x,y):
    return (x+x*x)/y

for x in range(1,5):
    for y in range(1,5):
        res = f(x,y)
        print("x =",x," y =",y," res =",res)