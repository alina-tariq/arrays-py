# Alina Tariq
# 500989574

arr = [1, 4, 14, 2, 1, 3, 5, 6, 23]
rearr = [] # rearranged array
for num in arr:
    # inserts even numbers at the front and odd numbers at the end
    rearr.insert(0, num) if num % 2 == 0 else rearr.insert(len(rearr), num)
print(rearr)