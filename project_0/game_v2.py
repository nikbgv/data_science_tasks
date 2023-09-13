"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    predict_current = np.random.randint (1, 101)
    
    predict_max = 101
    predict_min = 0
    
    count = 1 #не ноль, что-бы при угадывании с первой попытки функция вернула 1
        
    while True:
        if predict_current == number:
            break
        elif predict_current > number:
            predict_max = predict_current
            predict_current -= int((predict_max - predict_min) // 2)
        else:
            predict_min = predict_current
            predict_current += int((predict_max - predict_min) // 2)
        count += 1   
    
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
