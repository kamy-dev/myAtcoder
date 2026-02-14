def is_prime(x: int) -> bool:
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(x**0.5)+1,2):
        if x % i == 0:
            return False
    return True

if __name__ == "__main__":
    cnt = int(input())
    ans = 0
    for _ in range(cnt):
        x = int(input())
        if is_prime(x):
            ans += 1
    print(ans)

