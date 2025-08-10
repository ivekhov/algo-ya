## В задаче добавление в файл выхода присходит сразу
## так как при сборе списка и выгрузке в конце его целиком
## не проходит требование по используемой памяти


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        with open('output.txt', 'w') as f_out:
            n = int(f.readline().rstrip())
            if n > 0:
                prev_val = int(f.readline().rstrip())
                f_out.write(str(prev_val))
                f_out.write('\n')
                for _ in range(n-1):
                    cur_val = int(f.readline().rstrip())
                    if cur_val != prev_val:
                        f_out.write(str(cur_val))
                        f_out.write('\n')
                        prev_val = cur_val
                    else:
                        res = []
