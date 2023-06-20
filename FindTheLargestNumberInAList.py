##Find the largest Number in a list-->
numbers=[4,6,43,768,24,68]
max=numbers[0]
for item in range(1,len(numbers)):
    if max<numbers[item]:
        max = numbers[item]
print(max)
