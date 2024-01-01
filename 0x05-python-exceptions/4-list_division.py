#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    try:
        for i in range(list_length):
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")
            elif (not isinstance(my_list_1[i], (int, float))
                  or not isinstance(my_list_2[i], (int, float))):
                new_list.append(0)
                print("wrong type")
            elif my_list_2[i] == 0:
                new_list.append(0)
                print("division by 0")
            else:
                new_list.append(my_list_1[i] / my_list_2[i])
    except IndexError as e:
        print(e)
    finally:
        while len(new_list) < list_length:
            new_list.append(0)
        return new_list
