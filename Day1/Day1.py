with open('part1.csv', 'r') as file: 
    first_vals = []
    second_vals = []
    for line in file:
        [val1, val2] = map(int, line.strip().split())
        first_vals.append(val1)
        second_vals.append(val2)
    first_vals.sort()
    second_vals.sort()
    total_sum = sum(map(lambda a: abs(a[0] - a[1]), zip(first_vals, second_vals)))
    print(total+sum)

        
