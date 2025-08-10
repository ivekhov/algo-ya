def solution(arr):
    main_counter = 0
    small_counter = 0
    prev_val = 0
    for item in arr:   
        if item == 1:
            prev_val = 1
            small_counter += 1
            if small_counter > main_counter:
                main_counter = small_counter
        elif item == 0:
            if small_counter > main_counter:
                main_counter = small_counter
            small_counter = 0
            prev_val = 0
    return main_counter


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        rows = f.readlines()
        arr = [int(item.rstrip()) for item in rows]
        res = solution(arr[1:])
    with open('output.txt', 'w') as f:
        f.write(str(res))