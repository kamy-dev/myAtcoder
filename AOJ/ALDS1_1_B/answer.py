def gcd(x: int, y: int) -> int:
    while y != 0:
        x, y = y, x % y
    return x

if __name__ == "__main__":
    x, y = input().split()
    x = int(x)
    y = int(y)
    ans = gcd(x,y)
    print(ans)
