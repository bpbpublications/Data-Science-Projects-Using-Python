set1 = {12,24,13}
set2 = {23,24,25}
print(set1.union(set2))# Combines both sets->{12,24,13,23,24,25}
print(set1.intersection(set2))#Common elements->{24}
print(set1.difference(set2))# Items in set1 but not in set2->{12,13}
