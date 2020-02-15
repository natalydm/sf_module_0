import numpy as np
def game_core_v1(number):
    '''������ ��������� �� random �� ��� �� ��������� ���������� � ������ ��� ������.
       ������� ��������� ���������� ����� � ���������� ����� �������'''
    count = 0
    while True:
        count+=1
        predict = np.random.randint(1, 101) # �������������� �����
        if number == predict: 
            break
    return(count) # ����� �� �����, ���� �������
        
        
def score_game(game_core_v1):
    '''��������� ���� 1000 ���, ���� ������ ��� ������ ���� ��������� �����'''
    count_ls = []
    
    np.random.seed(1)  # ��������� RANDOM SEED, ����� ��� ����������� ��� �������������!
    random_array = np.random.randint(1, 101, size=(10000))
    for number in random_array:
        count_ls.append(game_core_v1(number))
    score = int(np.mean(count_ls))
    print(f"��� �������� ��������� ����� � ������� �� {score} �������")
    return(score)

# ���������
score_game(game_core_v1)

def game_core_v2(number):
    '''������� ������������� ����� random �����, � ����� ��������� ��� ����������� ���
       � ����������� �� ����, ������ ��� ��� ������ �������.
       ������� ��������� ���������� ����� � ���������� ����� �������'''
    count = 0
    predict = np.random.randint(1,100)
    while number != predict:
        count+=1
        if number > predict: 
            predict += 1
        elif number < predict: 
            predict -= 1
    return(count) # ����� �� �����, ���� �������

# ���������
score_game(game_core_v2)




def game_core_v3(number):
    '''���������� ����� ������� ������� �������'''
    count = 0
    left_gr=0
    right_gr=101
    predict = int((right_gr-left_gr)/2)
    while number != predict:
        
        count+=1
        if number > predict: 
            left_gr=predict
            predict = int(predict+(right_gr-predict )/ 2)
                    
        elif number < predict: 
            right_gr=predict
            predict = int(left_gr+(predict- left_gr)/ 2)
  
   
    return(count) # ����� �� �����, ���� �������

# ���������
score_game(game_core_v3)