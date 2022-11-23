
class SvgGenerate:
    def __init__(self, color, width, height, figure, filename):
        self.color = color
        self.width = width
        self.height = height
        self.figure = figure
        self.filename = filename

    def templates(self, figure):
        """
        В соответствии с типом фигуры вызывает соответствующий метод.
        """
        if figure == 'circle':
            return self.circle()
        elif figure == 'square':
            return self.square()
        elif figure == 'triangle':
            return self.triangle()
        else:
            return 'Figure not found'

    def circle(self):
        """ Возвращает svg-код круга. """
        return f''' 
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
            <circle cx="{self.height/2}" cy="{self.height/2}" r="{self.width/2}" style="fill:{self.color}"/>
        </svg>
        '''

    def square(self):
        """ Возвращает svg-код квадрата. """
        return f''' 
        <svg xmlns="http://www.w3.org/2000/svg" width="{self.width}" height="{self.height}">
            <rect width="{self.width}" height="{self.height}" style="fill:{self.color}"/>
        </svg>
        '''

    def triangle(self):
        """ Возвращает svg-код треугольника. """
        return f''' 
        <svg xmlns="http://www.w3.org/2000/svg" width="{self.width}" height="{self.height}">
            <polygon points="0,0 {self.width},0 {self.width//2},{self.height}" style="fill:{self.color}" />
        </svg>
        '''

    def save(self):
        """ Сохраняет svg-код в файл. """
        with open(self.filename, 'w') as f:
            f.write(self.templates(self.figure))
