def safe_descent(a, b):
    return a - b >= 1 and a - b <= 3
def safe_ascent(a, b):
    return b - a >= 1 and b - a <= 3

with open('part1.csv', 'r') as file: 
    safe_count = 0
    for line in file:
        list_vals = list(map(int, line.strip().split()))
        is_safe = True
        if safe_ascent(list_vals[0], list_vals[1]):
            for i in range(1, len(list_vals) - 1):
                if not safe_ascent(list_vals[i], list_vals[i+1]):
                    is_safe = False
                    break
        elif safe_descent(list_vals[0], list_vals[1]):
            for i in range(1, len(list_vals) - 1):
                if not safe_descent(list_vals[i], list_vals[i+1]):
                    is_safe = False
                    break

        else: 
            is_safe = False;
        if is_safe:
            safe_count = safe_count + 1

    print(safe_count)
            
        
