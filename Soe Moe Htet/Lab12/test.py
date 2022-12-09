class A:
    def __init__(self, i):
        self.i = i
    
    def __str__(self):
        return "A"

    def __eq__(self, other):
        return self.i == other.i


def main():
    print((2 ** 19) - 1 )

main()