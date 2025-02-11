# 1. создайте класс прямоугольника.
# a. атрибуты - прямоугольнику можно задать ширину и высоту
# b. методы - реализуйте 2 метода:
# i. расчет площади прямоугольника
# ii. расчет периметра прямоугольника
# c. создайте 3 объекта, рассчитайте площадь и периметр для каждого. Результаты выводить в консоль.

class rectangle:

    def __init__(self, width, height): # width - ширина, height - высота
        self.width = width
        self.height = height

    def square(self): # метод расчета площади
        return self.width*self.height

    def perimeter(self): # метод расчета периметра
        return (self.width+self.height)*2

rect1 = rectangle(7, 5)
rect2 = rectangle(8, 4)
rect3 = rectangle(20, 6)

print(f"Площадь прямоугольника-{rect1.square()}")
print(f"Периметр прямоугольника-{rect1.perimeter()}")
print(f"Площадь прямоугольника-{rect2.square()}")
print(f"Периметр прямоугольника-{rect2.perimeter()}")
print(f"Площадь прямоугольника-{rect3.square()}")
print(f"Периметр прямоугольника-{rect3.perimeter()}")


# 2. Создайте класс Math.
# a. Создайте два атрибута — a и b.
# b. Напишите методы
# i. addition — сложение,
# ii. multiplication — умножение,
# iii. division — деление,
# iv. subtraction — вычитание.
# При передаче в методы параметров a и b с ними нужно производить соответствующие действия и печатать ответ.

print('\n')

class Math:

    def __init__(self, a, b): # a, b - числа
        self.a = a
        self.b = b

    def addition(self): # метод сложение
        print(f"Сложение чисел: {self.a+self.b}")

    def multiplication(self): # метод умножение
        print(f"Умножение чисел: {self.a*self.b}")

    def division(self): # метод деление
        if self.b==0:
            print("Деление на ноль невозможно")
        else:
            print(f"Деление чисел: {self.a/self.b}")

    def subtraction(self): # метод вычитание
        print(f"Вычитание чисел: {self.a-self.b}")

calculator = Math(10, 5)
calculator.addition()
calculator.multiplication()
calculator.division()
calculator.subtraction()

print('\n')

# 3. откройте страницу https://demoqa.com/text-box
# На странице присутствует сайдбар (меню слева)
# a. Создайте объекты для каждой кнопки 2-го уровня вложенности (“Text Box” и т.п.)
# Для этого опишите класс.
# Каждый объект должен содержать в себе:
# - текст кнопки (пример: “Text Box”)
# - тип - одинаковый для всех “Кнопка”
# - локатор - не заполнять, сделать по умолчанию пустой строкой
# Также на кнопку можно нажать - реализуйте метод. Метод возвращает текст “Клик по кнопке { ТЕКСТ КНОПКИ }”
# b. выведите текст для каждой кнопки
# c. вызовите “Клик” для каждой кнопки

class Button:

    def __init__(self, button_text, type='Кнопка', loc=''): # button_text - текст кнопки, type - тип "кнопка", loc - локатор
        self.button_text = button_text
        self.type = type
        self.loc = loc

    def ButtonText(self): # метод вывода текста кнопки
        return f"Текст кнопки: {self.button_text}"

    def click(self): # метод нажатия кнопки
        return f"Клик по кнопке {self.button_text}"

BtnTextBox = Button('Text Box')
BtnCheckBox = Button('Check Box')
BtnRadioButton = Button('Radio Button')
BtnWebTables = Button('Web Tables')
BtnButtons = Button('Buttons')
BtnLinks = Button('Links')
BtnBrokenLinksImages = Button('Broken Links - Images')
BtnUploadAndDownload = Button('Upload and Download')
BtnDynamicProperties = Button('Dynamic Properties')

print(BtnTextBox.ButtonText())
print(BtnTextBox.click())
print(BtnCheckBox.ButtonText())
print(BtnCheckBox.click())
print(BtnRadioButton.ButtonText())
print(BtnRadioButton.click())
print(BtnWebTables.ButtonText())
print(BtnWebTables.click())
print(BtnButtons.ButtonText())
print(BtnButtons.click())
print(BtnLinks.ButtonText())
print(BtnLinks.click())
print(BtnBrokenLinksImages.ButtonText())
print(BtnBrokenLinksImages.click())
print(BtnUploadAndDownload.ButtonText())
print(BtnUploadAndDownload.click())
print(BtnDynamicProperties.ButtonText())
print(BtnDynamicProperties.click())