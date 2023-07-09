# recursion method:
def fs(n):
    if n<=1:
        return 1

    return fs(n-1)+fs(n-2)
n=5
print(fs(n))