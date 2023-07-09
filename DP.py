# recursion method:
n=5
def fs(n):
    if n<=1:
        return 1

    return fs(n-1)+fs(n-2)
n=5
print(fs(n))

# dynammic programming top down : memoization
memo=[0]* (n+1)
def fs(n):
    if memo[n]:
        return memo[n]

    if n<=1:
        return 1
    else:
        memo[n]=fs(n-1) + fs(n-2)
    return memo[n]
print(fs(n))

#dynammic programming bottom up : tabulation
memo=[0]*(n+1)
def fs(n):
    if memo[n]:
        return memo[n]
    memo[0]=memo[1]=1
    for i in range(2,n+1):
        memo[i]=memo[i-1]+memo[i-2]
    return memo[n]
print(fs(n))
