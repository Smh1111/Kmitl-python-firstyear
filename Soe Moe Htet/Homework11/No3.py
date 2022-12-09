
def product(*s):
    result = []
    result = [(i, ) for i in s[0]]
    
    if (len(s)  == 1):
        return result
    
    for i in range(1, len(s)):
        result = [a +(b, ) for a in result for b in s[i]]

    return result

def main():
    s1 = set([1, 2, 3])
    s2 = set(['p', 'q'])
    s3 = set(['a', 'b', 'c'])
    print(product(s1))
    print(product(s1, s2))
    #print(product(s1, s2, s3))

main()