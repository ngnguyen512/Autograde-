def main():
    print("This program computes the nth Fibonacci number.")
    n = int(input("Enter number for n: "))
    res = 0
    first = 0
    second = 1
    for i in range(2, n+1):
        res = first + second
        first = second
        second = res
    print("The {}th Fibonacci number is {}.".format(n, res))



        


        