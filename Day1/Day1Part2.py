with open('part1.csv', 'r') as file: 
    score = 0
    first_vals = []
    second_vals = []
    second_val_dict = {}
    for line in file:
        [val1, val2] = map(int, line.strip().split())
        first_vals.append(val1)
        second_vals.append(val2)
    for v in second_vals:
        if v in second_val_dict:
            second_val_dict[v] = second_val_dict[v] + 1
        else:
            second_val_dict[v] = 1

    for x in first_vals:
        if x in second_val_dict:
            score += x * second_val_dict[x]

    print(score)
        
