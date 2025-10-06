nums=[3, -1, 5, 5, 0]   
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError("Список ")
    else:
        return min(nums), max(nums)
try:    
    min,max= min_max(nums)  
    print('min='min 'max='max)
except ValueError as e:
    print(f"Ошибка: {e}")