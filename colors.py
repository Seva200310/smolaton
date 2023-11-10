import colorsys


def generate_colors(num_colors):
    # Начальное значение оттенка (от 0 до 1)
    hue_start = 0.0

    # Шаг изменения оттенка для каждого цвета
    hue_step = 1.0 / num_colors

    # Генерация цветов
    colors = []
    for i in range(num_colors):
        # Получаем RGB значения из HSV
        rgb = colorsys.hsv_to_rgb(hue_start, 0.8, 0.8)  # Насыщенность и значение оставляем постоянными
        # Масштабируем значения от 0-1 до 0-255 и преобразуем в целые числа
        colors.append(tuple(int(val * 255) for val in rgb))

        # Увеличиваем оттенок для следующего цвета
        hue_start += hue_step

    return colors


# Генерация 100 цветов
colors = generate_colors(100)

# Вывод значений RGB для каждого цвета
for i, color in enumerate(colors):
    print(f"Color {i + 1}: RGB({color[0]}, {color[1]}, {color[2]})")
