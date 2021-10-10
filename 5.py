from collections import Counter

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

li_count = Counter(src)
unic_li = [k for k, v in li_count.items() if v == 1]
print(unic_li)  # [23, 1, 3, 10, 4, 11]


unic_set = set()
for i in src:
    if i not in unic_set:
        unic_set.add(i)
    else:
        unic_set.discard(i)
unic_li = [i for i in src if i in unic_set]
print(unic_li)  # [23, 1, 3, 10, 4, 11]
