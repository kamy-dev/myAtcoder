def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

if __name__ == '__main__':
    data = [3, 2, 2, 1, 5, 10, 9, 7, 8, 6]
    insertion_sort(data)
    print(data)