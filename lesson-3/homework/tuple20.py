original_tuple = (1, 2, 3, 4, 5, 6, 7, 8)
group_size = 3


start = 0
sub1 = original_tuple[start : start + group_size]
start = group_size
sub2 = original_tuple[start : start + group_size]
start = 2 * group_size
sub3 = original_tuple[start : start + group_size]

nested_tuple = (sub1, sub2, sub3)
print(nested_tuple)
