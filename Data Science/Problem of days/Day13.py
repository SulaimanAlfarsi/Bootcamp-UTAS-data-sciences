input_nums = [1, 2]
distinct_sums = {0}

for num in input_nums:
    new_sums = set()
    for s in distinct_sums:
        new_sums.add(num + s)
    distinct_sums.update(new_sums)

print(list(distinct_sums))
