# Question 5. Create a frozenset named frozen_set_1 containing the elements: 'A', 'B', 'C' and 'D' 
# and combine it using union with a frozenset named frozen_set_2 containing elements 'A', 2, 'C' and 4. 
# The final combined frozenset must be named frozenset_union. Now find the common elements in frozen_set_1 and frozen_set_2 
# and store the result in a variable named frozenset_common. Lastly, in a new forzenset named forzenset_difference store the elements of frozen_set_1 
# which are not in frozen_set_2 and in a new frozenset named frozenset_distinct store the elements which are unique to frozen_set_1 and frozen_set_2.

#Program
#Output:
# Frozenset union: frozenset({2, 4, 'A', 'B', 'C', 'D'})
# Frozenset common: frozenset({'A', 'C'})
# Frozenset difference: frozenset({'B', 'D'})
# Frozenset distinct: frozenset({2, 4, 'B', 'D'})

frozen_set_1 = frozenset(['A', 'B', 'C', 'D'])
frozen_set_2 = frozenset(['A', 2, 'C', 4])

print(frozen_set_1)
print(frozen_set_2)

frozenset_union = frozen_set_1.union(frozen_set_2)
print("Frozenset union:", frozenset_union)

frozenset_common = frozen_set_1.intersection(frozen_set_2)
print("Frozenset common:", frozenset_common)

frozenset_difference = frozen_set_1.difference(frozen_set_2)
print("Frozenset difference:", frozenset_difference)

frozenset_distinct = frozen_set_1.symmetric_difference(frozen_set_2)
print("Frozenset distinct:", frozenset_distinct)