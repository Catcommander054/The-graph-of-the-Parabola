import numpy as np
import matplotlib.pyplot as plt

cell_size = 1.0  #Размер клетки

#Размер графика
fig_width = 10
fig_height = 10

fig, ax = plt.subplots(figsize=(fig_width, fig_height), dpi=100)

fig.patch.set_facecolor('white')  #Цвет фона вокруг
ax.set_facecolor('#f0f0f0')  #Цвет фона с параболой

#Значения(переменные) параболы
a = 1 #Не должно быть равно 0
b = 0
c = -10 #Центральная точка параболы(Точка перегиба)

if a < 1: x = np.linspace(-6 / a, 6 / a, 1000)
else: x = np.linspace(-6, 6, 1000)

y = a * x ** 2 + b * x + c

ax.set_ylim(-10, 10)

ax.grid(True, which='both', linestyle='--', linewidth=0.5)

ax.set_xticks(np.arange(-20, 21, cell_size))  # Деления по оси x от -20 до 20 с шагом 1
ax.set_yticks(np.arange(-20, 21, cell_size))  # Деления по оси y от -20 до 20 с шагом 1

#Начальные пределы осей
x_offset = 0
y_offset = 0
ax.set_xlim(-6 + x_offset, 6 + x_offset)
ax.set_ylim(-10 + y_offset, 10 + y_offset)

ax.plot(x, y, color='black', linewidth=1.5)
# ax.fill_between(x, y, color='red', alpha=0.3)

ax.set_title('График параболы', color='black')
ax.set_xlabel('x', color='black')
ax.set_ylabel('y', color='black')

ax.set_aspect('equal', adjustable='box')

ax.axhline(0, color='blue', linewidth=0.5, ls='--')  #Горизонтальная линия
ax.axvline(0, color='blue', linewidth=0.5, ls='--')  #Вертикальная линия

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_color('black')

def on_key(event):
    global x_offset, y_offset
    x_min = -20
    x_max = 20
    y_min = -20
    y_max = 20

    if event.key == 'up':
        if y_offset < y_max - 10:
            y_offset += 1
    elif event.key == 'down':
        if y_offset > y_min + 10:
            y_offset -= 1
    elif event.key == 'left':
        if x_offset > x_min + 6:
            x_offset -= 1
    elif event.key == 'right':
        if x_offset < x_max - 6:
            x_offset += 1
    update_plot()

def update_plot():
    ax.set_xlim(-6 + x_offset, 6 + x_offset)
    ax.set_ylim(-10 + y_offset, 10 + y_offset)
    plt.draw()

fig.canvas.mpl_connect('key_press_event', on_key)

plt.show()
