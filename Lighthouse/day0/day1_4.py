def A_function(number_list):

    max_number = max(number_list) #Ai
    min_number = min(number_list) #Aj

    i = number_list.index(max_number) + 1
    j = number_list.index(min_number) + 1

    mod_number = max_number % min_number

    if mod_number == 0:
        number_list.remove(max_number)
    else:
        number_list[i-1] = mod_number

    return number_list

#input_list = [2, 3, 6]
input_list = [1232, 452, 23491, 34099, 57341, 21488]
count = 0
while len(input_list) > 1:
    A_function(input_list)
    count +=1

print(count)