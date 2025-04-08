def gnome_sort(data: list) -> list:
    idx = 0
    while idx < len(data):
        if idx == 0 or data[idx] >= data[idx-1]:
            idx += 1
        else:
            data[idx], data[idx-1] = data[idx-1], data[idx]
            idx -= 1
    return data

if __name__ == "__main__":
    data = [5, 3, 2, 4, 1]
    print(gnome_sort(data))  # [1, 2, 3, 4, 5]