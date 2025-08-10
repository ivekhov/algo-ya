# https://contest.yandex.ru/contest/22450/run-report/134013245/


def find_distance(cur_idx, left_zero_idx, right_zero_idx):
    if right_zero_idx - left_zero_idx == 0:
        return None
    
    dist_to_left = abs(cur_idx - left_zero_idx)
    dist_to_right = abs(cur_idx - right_zero_idx)

    if dist_to_left < dist_to_right:
        return dist_to_left
    return dist_to_right


def solve(houses):
    result = []
    zero_indexes = []
    for idx, item in enumerate(houses):
        if item == 0:
            zero_indexes.append(idx)    
    if len(zero_indexes) == 1:
        for cur_idx in range(len(houses)):
            result.append(abs(zero_indexes[0] - cur_idx))
    else:

        # left part
        if zero_indexes[0] != 0:
            for cur_idx in range(0, zero_indexes[0]):
                result.append(abs(zero_indexes[0] - cur_idx))
        
        # center parts        
        for idx in range(1, len(zero_indexes)):
            left_zero_idx = zero_indexes[idx-1]
            right_zero_idx = zero_indexes[idx]

            for cur_idx in range(left_zero_idx, right_zero_idx):
                dist = find_distance(cur_idx, left_zero_idx, right_zero_idx)
                result.append(dist)
            
        # right part 
        if zero_indexes[-1] < len(houses):
            for cur_idx in range(zero_indexes[-1], len(houses)):
                result.append(abs(zero_indexes[-1] - cur_idx))

    return ' '.join(list(map(str, result)))


if __name__ == '__main__':
    with open('input.txt',  'r' ) as f:
        street = int(f.readline().rstrip())
        houses = f.readline().rstrip()
        houses = list(map(int, houses.split(' ')))
   
    with open('output.txt', 'w') as f:
        f.write(solve(houses))
