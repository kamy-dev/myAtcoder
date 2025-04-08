# シェルソートはgapの値によって計算量が大きく変わる。サンプルコードではgapの値を配列の長さ//2とする。
def shell_sort(data: list) -> list:
    n = len(data)
    gap = n // 2  # gapの初期化

    while gap > 0:
        for i in range(gap, n):
            tmp = data[i]   # インデックスgapの値をtmpに代入
            j = i
            while j >= gap and data[j-gap] > tmp:
                data[j] = data[j-gap]
                j -= gap
            data[j] = tmp
        gap //= 2

    return data 

if __name__ == '__main__':
    data = [1, 5, 2, 8, 7, 3, 4, 6, 9, 0]
    print(shell_sort(data))  # [1, 2, 3, 4, 5, 7, 8]