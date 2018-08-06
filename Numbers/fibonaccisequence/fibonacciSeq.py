# @author: Ashish Shetty aka AlphaSierra
# Fibonacci sequence generator my implementation

fibonacci_list = [0, 1]# List created with twi initial numbers hardcoded in it. Now ask user for input for ranging
last = int(input("Please input the limit of Fibonacci series you want to enlist: "))

def fib():# define fibonacci generator function
    m = 0
    n = 1
    i = 0
    for i in range(last):# for loop iterates "last" no of times and appends new fibonacci no. on each loop completion
        p = m + n
        m = n
        n = p
        fibonacci_list.append(p)
    print(fibonacci_list)# once the loop iteration is done. The entire fibonacci sequence list is printed out

fib()# call the fib function
