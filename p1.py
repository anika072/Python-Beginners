Generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)-->

n=int(input(">"))
dic={x:x**2 for x in range(1,n)}
dic
