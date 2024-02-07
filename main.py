"""
Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего
из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без
get_dummies?
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
"""
import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data)

print('________________')

data['tmp'] = 1                                          # Добавляем временный столбец tmp
data.set_index([data.index, 'whoAmI'], inplace=True)     # Устанавливаем индексы по столбцу whoAmI
data = data.unstack(level=-1, fill_value=0).astype(int)  # Удаляем 1 уровень, заполняем пустые  значения нулями,
                                                         # переводим значения в int
data.columns = data.columns.droplevel()                  # Получаем индекс 1-го столбца
data.columns.name = ''                                   # Присваиваем пустое имя
print(data)
