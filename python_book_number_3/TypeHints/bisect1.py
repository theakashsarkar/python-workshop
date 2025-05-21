# import bisect

# def sorted_insert_example():
#     nums = [2, 4, 6, 8, 10]
#     bisect.insort(nums, 5)
#     bisect.insort(nums, 4)
#     print(nums)
# def find_insertion_point():
#     nums = [2, 4, 6, 8, 10]
#     index = bisect.bisect_left(nums, 5)
#     bisect.insort(nums, 5)
#     print(nums)
# def price_lookup():
#     price_breaks = [1000, 5000, 10000]
#     discounts = [0, 10, 20, 30]

#     def get_discount(amount):
#         i = bisect.bisect_right(price_breaks, amount)
#         return discounts[i]
#     orders = [500, 2500, 7000, 12000]
#     print([(amount, get_discount(amount)) for amount in orders])
# # sorted_insert_example()
# # find_insertion_point()
# price_lookup()
