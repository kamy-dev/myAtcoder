def shaker_sort(data):
    begin = 0
    end = len(data) - 1

    while begin < end:
        for i in range(begin, end):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
        end -= 1

        for i in range(end, begin, -1):
            if data[i] < data[i-1]:
                data[i], data[i-1] = data[i-1], data[i]
        begin += 1

    return data

if __name__ == "__main__":
    data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
    print(shaker_sort(data))