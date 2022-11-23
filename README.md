# 🖼🛠🌟 SVG Generate | Простой инструмент для генерации SVG изображений 🖼🛠🌟
### Описание
Данный проект представляет собой простой инструмент для генерации SVG изображений.
Все что вам нужно - это указать размеры изображения и выбрать цвета. 
После этого вы получите SVG код, который вы можете использовать в своих проектах.
### Технологии
* Python (standart library)
### Установка
1. Склонируйте репозиторий

```bash
git clone repository_url
```

2. Выполните команду

```bash
python3 main.py --color hex_color --figure circle --width 100 --height 100 --filename output.svg
```
где:
* `--color` - цвет в формате hex
* `--figure` - фигура (circle, square, triangle)
* `--width` - ширина изображения
* `--height` - высота изображения
* `--filename` - имя файла c расширением .svg
* `--help` - вывод справки

### Примеры
```bash
python3 main.py --color #ff0000 --figure circle --width 100 --height 100 --filename output.svg
```
Результат:
```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="50" fill="#ff0000"/>  
</svg>
```
С изображением можно ознакомиться в папке `examples`

