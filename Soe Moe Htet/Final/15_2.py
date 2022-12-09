def main():
    index = eval(input("Enter an index for a Fibonacci number: "))
    # Find and display the Fibonacci number
    print("The Fibonacci number at index", index, "is",  fib(index))

    # The function for finding the Fibonacci number 
def fib(index):
    if index == 0: # Base case
        return 0
    elif index == 1: # Base case
        return 1
    else: # Reduction and recursive calls
        print(f"fib(index - 1) at {index - 1} ", fib(index - 1))
        print(f"fib(index - 2) at {index - 2} ", fib(index - 2))
        print()
        return fib(index - 1) + fib(index - 2)
    
main() # Call the main function