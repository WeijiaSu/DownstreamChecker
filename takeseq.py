def twoSum(numbers, target):
    i, j = 0, len(numbers) - 1
    while (i < j):
        sum = numbers[i] + numbers[j]
        if (sum == target):
            return i + 1, j + 1
        elif (sum > target):
            j = j - 1
        else:
            i = i + 1


print(twoSum([1,2,3,4],7))