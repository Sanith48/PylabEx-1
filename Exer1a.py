my_list=[5,7,8,4,3,9]
total_sum=sum(my_list)
print(f"The sum of the digits in the list is: {total_sum}")

from functools import reduce
from operator import mul

total_product = reduce(mul, my_list, 1)
print(f"The product of all items in the list is: {total_product}")

largest_number=max(my_list)
print(f"The largest number in the list is: {largest_number}")

smallest_number=min(my_list)
print(f"The smallest number in the list is: {smallest_number}")