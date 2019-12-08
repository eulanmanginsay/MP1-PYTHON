# Problem 1
import matplotlib.pyplot as plt
x=[ ]
y=[ ]
n=list(range(100))

def f(n):
    if n <= 9:
        fy=(n**(2)-7)
        return fy
    return f(n-10)

for m in n:
    x.append(m)
    y.append(f(m))
 
plt.stem(x,y, use_line_collection=True )
plt.show()