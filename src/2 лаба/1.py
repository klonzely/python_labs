nums = [1.5, 2, 2.0, -3.1]
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if nums:
        return min(nums), max(nums)
    else:
        return 'ValueError'
print(min_max(nums))