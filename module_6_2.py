class Vehicle:
  __COLOR_VARIANTS = ['white', 'orange', 'black', 'red', 'yellow', 'green']
  def __init__(self, owner: str, _model: str, _color: str, _engine_power: int):
      self.owner = owner
      self.__model = _model
      self.__engine_power = _engine_power
      self.__color = _color


  def get_model(self):
     return f"Модель: {self.__model}"
  def get_horsepower(self):
     return f"Мощьность двигателя: {self.__engine_power}"
  def get_color(self):
      return f'Цвет: {self.__color}'
  def print_info(self):
      print(self.get_model(),self.get_horsepower(), self.get_color(), f'Владелец: {self.owner}')
  def set_color(self, new_color: str):
      if new_color.lower() in self.__COLOR_VARIANTS:
          self.__color = new_color
      else:
          print(f'Нельзя сменить цвет на {new_color}')
class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()





