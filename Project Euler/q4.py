"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009
Find the largest palindrome made from the product of two 3-digit numbers
"""

my_list = list(range(100, 1000))
my_list2 =  list(range(100, 1000))
zarb_list = []

for number in my_list:
    for sec_number in my_list2:
        zarb = number * sec_number
        if str(zarb) == str(zarb)[::-1]:
            zarb_list.append(zarb)

print(max(zarb_list))