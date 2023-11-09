"""Игра угадай число"""

def guess_the_number(number: int = 1) -> int:
  """
  Функция принимает загаданное число от 1 до 100 и возвращает число попыток.
  
  Args:
      number(int, optional): Загаданное число. Defaults to 1.
      
  Returns:
      int: Количество попыток.
  """

  count = 0 # количество попыток

  low = 0 # левая граница поиска
  high = 100 # правая граница поиска

  while True:
    count += 1
    mid = (low + high) // 2
    
    if mid == number:
      break
    elif mid < number:
      low = mid
    else:
      high = mid
      
  return count
