# 1) Заменить "х" на "у"

source = "asjdpxjxoiuuxyyxiuayixyyxiuayxuixyiaxyixuyauixyiuayx"
print(source)
print(''.join(char if char != 'x' else 'y' for char in source))

# 2) Произведение чисел кратных 3 и 5

import random as r
import math
source = r.choices(range(1, 100), k=10)
print(source)
num_to_produce = list(num for num in source if (num % 5 == 0) or (num % 3 == 0))
print(f"ПРоизведение {num_to_produce}: ", math.prod(num_to_produce))