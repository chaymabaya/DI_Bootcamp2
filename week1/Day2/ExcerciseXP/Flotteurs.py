numbers = []
start = 1.5
end = 5
step = 0.5
while start <= end:
    if start.is_integer():
        numbers.append(int(start))
    else:
        numbers.append(start)
    start += step
print(numbers)