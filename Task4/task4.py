import sys

def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        return list(map(int, file.read().strip().split()))

def calculate_median(nums):
    nums.sort()
    n = len(nums)
    if n % 2 == 1:
        return nums[n // 2]  # Если количество элементов нечетное
    else:
        return nums[n // 2 - 1]  # Если четное, выбираем меньший из двух средних

def calculate_min_moves(nums):
    median = calculate_median(nums)
    moves = sum(abs(num - median) for num in nums)
    return moves

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python script.py <имя_файла>")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        nums = read_numbers_from_file(filename)
        min_moves = calculate_min_moves(nums)
        print(f"Минимальное количество ходов: {min_moves}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
