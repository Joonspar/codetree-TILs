n, m, d, s = map(int, input().split())

cheese_eaten = []
for _ in range(d):
    p, c, t = map(int, input().split())
    cheese_eaten.append((p, c, t))

sick_records = []
for _ in range(s):
    p, t = map(int, input().split())
    sick_records.append((p, t))

max_medicine = 0

for cheese in range(1, m + 1):
    potential_sick = set()
    valid_cheese = True
    
    for person, sick_time in sick_records:
        ate_in_time = False
        for eater, eaten_cheese, eaten_time in cheese_eaten:
            if eater == person and eaten_cheese == cheese and eaten_time < sick_time:
                ate_in_time = True
                break
        if not ate_in_time:
            valid_cheese = False
            break
    
    if valid_cheese:
        for eater, eaten_cheese, eaten_time in cheese_eaten:
            if eaten_cheese == cheese:
                potential_sick.add(eater)
        
        max_medicine = max(max_medicine, len(potential_sick))

print(max_medicine)