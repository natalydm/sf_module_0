import numpy as np
def game_core_v1(number):
    '''Просто угадываем на random ни как не используя информацию о больше или меньше.
       Функция Принимает загаданное число и возвращает число попыток'''
    count = 0
    while True:
        count+=1
        predict = np.random.randint(1, 101) # предполагаемое число
        if number == predict: 
            break
    return(count) # выход из цикла, если угадали
        
        
def score_game(game_core_v1):
    '''Запускаем игру 1000 раз, чтоб узнать как быстро игра угадывает число'''
    count_ls = []
    
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(10000))
    for number in random_array:
        count_ls.append(game_core_v1(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

# запускаем
score_game(game_core_v1)

def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его
       в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    predict = np.random.randint(1,100)
    while number != predict:
        count+=1
        if number > predict: 
            predict += 1
        elif number < predict: 
            predict -= 1
    return(count) # выход из цикла, если угадали

# Проверяем
score_game(game_core_v2)




def game_core_v3(number):
    '''Используем метод деления отрезка пополам'''
    count = 0
    left_gr=0
    right_gr=101
    predict = left_gr+((right_gr-left_gr)//2)
    while number != predict:
        
        count+=1
        if number > predict: 
            left_gr=predict
            predict = (predict+(right_gr-predict )// 2)
                    
        elif number < predict: 
            right_gr=predict
            predict = (left_gr+(predict- left_gr)// 2)
  
   
    return(count) # выход из цикла, если угадали

# Проверяем
score_game(game_core_v3)