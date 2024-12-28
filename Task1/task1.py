def read_numbers():
    # Запрашиваем ввод чисел у пользователя
    numbers = input("Введите числа, разделенные пробелами: ")
    return list(map(int, numbers.strip().split()))

def calculate_median(nums):
    nums.sort()
    n = len(nums)
    if n % 2 == 1:
        return nums[n // 2]  # Если количество элементов нечетное
    else:
        return (nums[n // 2 - 1] + nums[n // 2]) / 2  # Если четное, возвращаем среднее из двух средних

def calculate_min_moves(nums):
    median = calculate_median(nums)
    moves = sum(abs(num - median) for num in nums)
    return moves

if __name__ == "__main__":
    try:
        nums = read_numbers()
        min_moves = calculate_min_moves(nums)
        print(f"Минимальное количество ходов: {min_moves}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")