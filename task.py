import re
color = "^#[0-9A-Fa-f]{6}$"
input_string = input("Введите проверяемую строку: ")
if re.fullmatch (color, input_string):
  print('Строка является идентификатором цвета')
else:
  print('Введенная строка не является идетификатором цвета')
