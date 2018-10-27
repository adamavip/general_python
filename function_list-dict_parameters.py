def print_my_list(title_list, title_dict, *my_list, **my_dict):
    # Dans ce namespace, my_dict est un dictionnaire et my_list une liste
    
    print('ici les elements de la liste %s' % (title_list))
    for idx,value in enumerate(my_list):
        print('Index %02d: %s' % (idx, value))

    print('voici les elements du dictionnaire %s' % (title_dict))
    for key,value in my_dict.items():
        print('Element %s: %s' % (key, value))

if __name__ == '__main__':
    print_my_list('liste 0', 'dict 0', 0, 1, 2, 3, zero=0, un=1, deux=2, trois=3, quatre=4, cinq=5)