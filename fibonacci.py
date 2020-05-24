def get_fibonacci(n):
    i = 0
    j = 1
    l = []     #empty list
    l.extend([i,j])
    while len(l)!=n :
        temp = j
        j= i+j
        i= temp
        l.append(j)
    return l

if __name__ == "__main__":
    n = int(input("Enter number: "))
    result= get_fibonacci(n)
    print("Fibonacci series = {}".format(result))