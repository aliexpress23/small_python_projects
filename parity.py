def main():
    x = int(input("what's X? "))
    if is_even(x):
        print("Even")
    else:
        print("odd")

def is_even(n):
    return n % 2 == 0
main()