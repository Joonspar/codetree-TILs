def rectangles_overlap(x1, y1, x2, y2, a1, b1, a2, b2):
    # Check for non-overlapping conditions
    if x2 < a1 or a2 < x1:
        return "nonoverlapping"  # One rectangle is to the left of the other
    if y2 < b1 or b2 < y1:
        return "nonoverlapping"  # One rectangle is above the other
    
    return "overlapping"

x1,y1,x2,y2 = map(int,input().split())
a1,b1,a2,b2 = map(int,input().split())

result = rectangles_overlap(x1, y1, x2, y2, a1, b1, a2, b2)
print(result)