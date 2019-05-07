def devisible_by_2(my_list=[]):
    bi_list = []
    for index in my_list:
        if index % 2 != 0:
            bi_list.apend(False)
        else:
            bi_list.appen(True)
    return bi_list
