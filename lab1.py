import numpy as np 


def print_seq_sum(begin, end):
    seq_sum = np.array(range(begin, end)).sum()
    print(f"Сумма ряда {begin}-{end}: {seq_sum}")


if __name__ == "__main__":
    print_seq_sum(0, 100)
    print_seq_sum(0, int(input("Введите правую границу:")))

    mean_rand_seq = np.random.randint(100, size=100).mean()
    print(f"Среднее значение 100 случайных чисел: {mean_rand_seq}")