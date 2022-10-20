def get_count_char(str_):
    str_new = str_.lower()
    dict_ = {}
    for value in str_new:
        if value.isalpha():
            if dict_.get(value, None):
                dict_[value] += 1
            else:
                dict_[value] = 1
    return dict_

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))