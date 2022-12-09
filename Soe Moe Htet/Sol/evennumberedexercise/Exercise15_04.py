
def m(i):
    if i == 1:
        return 1
    else:
        return m(i - 1) + 1.0 / i   # m(i - 1) -> m(i - 1 - 1) + 1.0 / i - 1 + 1.0 / i


def main():
    print(m(4))

main()
