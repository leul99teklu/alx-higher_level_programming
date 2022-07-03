#!/use/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)

    copy_my_list = my_list.copy()
    if 0 <= idx < length:
        copy_my_list[idx] = element
    return(copy_my_list)
