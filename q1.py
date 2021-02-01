# Alina Tariq
# 500989574

arr = [9, 13, 21, 4, 11, 7, 1, 3]
size = len(arr)//2 # determines midway point
newarray = arr[size:] # adds second half of original array to new array
newarray.extend(arr[0:size]) # adds first half of original array
print("Switched array: ", newarray)
print("First half average: ", (sum(newarray[0:size])/size))
print("Second half average: ", (sum(newarray[size:])/size))