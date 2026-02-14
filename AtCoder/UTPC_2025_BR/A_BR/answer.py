

if __name__ == "__main__":
    T = int(input())
    for _ in range(0, T):
        x, y, z = input().split()
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        C = list(map(int, input().split()))
        # print(f'{A}, {B}, {C}')
        # A ⊂ C の確認
        for i in range(0, len(C)):
            # A[0]がC[何]から始まってるか
            # もしあれば、A[1]がC[何+1]か
            # これ以降もAの要素がなくなるか、Cの連続した要素ではなくなるかで検査
        # B ⊂ C の確認
