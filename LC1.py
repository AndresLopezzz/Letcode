nums = [2,7,11,15]
target = 9
for i in range(len(nums)):
    for j in range(i + i, len(nums)):
        if nums[i] + nums[j] == target:
            op = (i, j) 

print(f"los datos son = {nums}")
print(f"el objetivo es = {target}")
print(f"los datos que su suma dan {target} están en {op}")


