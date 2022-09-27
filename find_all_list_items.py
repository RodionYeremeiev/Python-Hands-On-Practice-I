def get_all_list_items_indexes(search_list, item):
    result_list = list()
    for i in range(len(search_list)):
        if search_list[i] == item:
            result_list.append([i])
        elif isinstance(search_list[i], list):
            for index in get_all_list_items_indexes(search_list[i], item):
                result_list.append([i]+index)
    return result_list
