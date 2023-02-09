def spy_game(list):
    for i in range(len(list)-1):
        if  list[i] == 0 and list[i+1] == 0 and list[i+2]==7:
            return True
    return False
print(spy_game([1,2,4,0,0,7,5]))