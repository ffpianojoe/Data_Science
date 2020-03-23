import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def calc_data(country):
    cases = country['total_cases'][-1]
    deaths = country['total_deaths'][-1]
    rate = country['total_deaths'][-1] / country['total_cases'][-1]
    location = country['location'][0]
    return cases, deaths, rate, location


def print_data(data):
    output = calc_data(data)
    print(output[3])
    print('Total Cases: ', output[0])
    print('Total Deaths: ', output[1])
    print('Mortality Rate: ', output[2])


df = pd.read_csv('new_data.csv')

df['datetime'] = pd.to_datetime(df['date'])
df = df.set_index('datetime')
df.drop(['date'], axis=1, inplace=True)

print(df.head())
print(df.info())

us = df[df['location'] == 'United States']
italy = df[df['location'] == 'Italy']
china = df[df['location'] == 'China']
spain = df[df['location'] == 'Spain']
germany = df[df['location'] == 'Germany']
france = df[df['location'] == 'France']
uk = df[df['location'] == 'United Kingdom']
iran = df[df['location'] == 'Iran']
world = df[df['location'] == 'World']

print_data(world)
print_data(us)
print_data(italy)
print_data(china)
print_data(spain)
print_data(germany)
print_data(france)
print_data(uk)
print_data(iran)

print(china.tail())
print(us.tail())
print(italy.tail())

sns.set()
x = us['2020-03-05':].index
y = us['2020-03-05':].total_cases
x2 = italy['2020-03-05':].index
y2 = italy['2020-03-05':].total_cases
x3 = china['2020-03-05':].index
y3 = china['2020-03-05':].total_cases
plt.plot(x, y, marker='.', linestyle='-')
plt.plot(x2, y2, marker='.', linestyle='-')
plt.plot(x3, y3, marker='.', linestyle='-', color='red')
plt.legend(['US', 'Italy', 'China'])
plt.title('COVID-19 Total Cases - US/Italy/China')
plt.xlabel('Month')
plt.ylabel('# of Cases')
# plt.show()