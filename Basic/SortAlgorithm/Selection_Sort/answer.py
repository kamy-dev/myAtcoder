def selection_sort(data):
    for i in range(len(data)-1):
        min_idx = i
        for j in range(i+1, len(data)):
            if data[j] < data[min_idx]:
                min_idx = j                 # 最小値を持つ要素のインデックスを更新するために必要
        data[i], data[min_idx] = data[min_idx], data[i]

    return data

if __name__ == '__main__':
    data = [5, 3, 8, 4, 2, 1, 9]
    selection_sort(data)
    print(data)  # [1, 2, 3, 4, 5, 8, 9]