def safe_descent(a, b):
    return a - b >= 1 and a - b <= 3
def safe_ascent(a, b):
    return b - a >= 1 and b - a <= 3
def is_safe(li):
    is_safe = True
    if safe_ascent(li[0], li[1]):
        for i in range(1, len(li) - 1):
            if not safe_ascent(li[i], li[i+1]):
                is_safe = False
                break
    elif safe_descent(li[0], li[1]):
        for i in range(1, len(li) - 1):
            if not safe_descent(li[i], li[i+1]):
                is_safe = False
                break

    else: 
        is_safe = False;
    return is_safe
    

with open('part1.csv', 'r') as file: 
    safe_count = 0
    for line in file:
        list_vals = list(map(int, line.strip().split()))
        safe = False
        for i in range(0, len(list_vals)):
            copy_trunc = list_vals.copy()
            del copy_trunc[i]
            if is_safe(copy_trunc):
                safe = True
                break
        if safe:
            safe_count = safe_count + 1

    print(safe_count)
            
        
