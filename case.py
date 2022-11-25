#место для твоего кода
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('StudentsPerformance.csv')
df.info()


female_math = df[df['gender']=='female']['math score'].mean()
male_math = df[df['gender']=='male']['math score'].mean()
female_reading = df[df['gender']=='female']['reading score'].mean()
male_reading = df[df['gender']=='male']['reading score'].mean()
female_write = df[df['gender']=='female']['writing score'].mean()
male_write = df[df['gender']=='male']['writing score'].mean()

female_free = 0
female_standart = 0

def lunch_counter(row):
    global female_free, female_standart
    if fow['gender'] == 'femali' and row['lunch'] == 'standart':
        female_standart+=1
    if fow['gender'] == 'femali' and row['lunch'] == 'free/reduced':
        female_free+=1
    return False

df.apply(lunch_counter, axis = 1)
print(female_free, female_standart)

print('Результаты по математике:', 'Девочки:', round(female_math, 2), 'Мальчики:', round(male_math, 2))
print('Результаты по чтению:',  'Девочки:', round(female_reading, 2), 'Мальчики:', round(male_math, 2))
print('Результаты по письму:', 'Девочки:',  round(female_write, 2), 'Мальчики:', round(male_math, 2))

print('Девочки сильнее в гуманитарных науках, а мальчики в точных науках')

print('Влияет ли качество питания на результаты по тестов?')
standart_math = df[df['lunch']=='standart']['math score'].mean()
free_math = df[df['lunch']=='free/reduced']['math score'].mean()
standart_reading = df[df['lunch']=='standart']['reading score'].mean()
free_reading = df[df['lunch']=='free/reduced']['reading score'].mean()
standart_write = df[df['lunch']=='standart']['writing score'].mean()
free_write = df[df['lunch']=='free/reduced']['writing score'].mean()

print('Результаты по математике:', 'Стандарт:', round(standart_math, 2), 'Бесплатное:', round(free_math, 2))
print('Результаты по чтению:',  'Стандарт:', round(standart_reading, 2), 'Бесплатное:', round(free_reading, 2))
print('Результаты по письму:', 'Стандарт:',  round(standart_write, 2), 'Бесплатное:', round(free_write, 2))

print('Гипотеза подтверждена. Питание влияет на качество обучение')

s = pd.Series(data=[female_math, male_math, female_readin, male_readin, female_write, male_write],
index = ['Мат.Девочки', 'Мат.Мальчики', 'Чт.Девочки', 'Чт.Мальчики', 'Письмо ', 'Письмо '])
s.plot(king='barh')
plt.show()

df['gender'].value_counts.plot(king='pie')
plt.show()                                                          