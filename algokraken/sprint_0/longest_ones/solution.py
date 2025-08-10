if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        n = int(f.readline().rstrip())
        main_counter = 0
        small_counter = 0
        prev_val = 0
        for _ in range(n):
            item = int(f.readline().rstrip())
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
    with open('output.txt', 'w') as f:
        f.write(str(main_counter))
