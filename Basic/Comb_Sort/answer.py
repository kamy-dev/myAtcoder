def comb_sort(data: list) -> list:
    gap = len(data)
    swap = False

    while gap != 1 or swap:
        gap = int(gap / 1.3)
        if gap < 1:
            gap = 1
        swap = False

        for i in range(len(data) - gap):
            if data[i] > data[i+gap]:
                data[i], data[i+gap] = data[i+gap], data[i]
                swap = True
    
    return data

if __name__ == '__main__':
    data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(comb_sort(data)) 