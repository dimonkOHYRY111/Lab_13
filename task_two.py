import matplotlib.pyplot as plt
import numpy as np

# Дані для Німеччини про використання даних міжнародними організаціями
years = np.array([2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013,
                  2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])

# Значення показника для Німеччини
germany_data = np.array([0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.6, 0.6, 0.6, 0.6,
                         0.6, 0.8, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])

plt.figure(figsize=(10, 6))
plt.plot(years, germany_data, label='Німеччина', color='green', linewidth=2)

plt.title('Динаміка показника "Використання даних міжнародними організаціями" за 2004-2023 роки', fontsize=14)
plt.xlabel('Рік', fontsize=12)
plt.ylabel('Значення показника', fontsize=12)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

def plot_bar_chart(country_name, country_data, years):
    plt.figure(figsize=(10, 6))
    plt.bar(years, country_data, color='skyblue')
    plt.title(f'Стовпчаста діаграма для {country_name}', fontsize=14)
    plt.xlabel('Рік', fontsize=12)
    plt.ylabel('Значення показника', fontsize=12)
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

plot_bar_chart("Німеччина", germany_data, years)
