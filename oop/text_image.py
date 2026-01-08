from PIL import Image, ImageDraw, ImageFont
from pathlib import Path


class TextImage:
    paddings = 20
    font_size = 26
    line_height = 2

    # Задаём путь до файла со шрифтами.
    # Шрифты должны лежать в каталоге fonts рядом с программой
    font_path = Path("fonts/pt-mono_regular.ttf")

    def __init__(self, text: str):
        self.text = text

        # Начальные позиции (x, y)
        self.y = TextImage.paddings
        self.x = TextImage.paddings

        # Максимальная ширина текста
        max_line = self._get_text_max_line()

        # Задаём шрифт
        self.font = ImageFont.truetype(TextImage.font_path, size=TextImage.font_size)

        # Создаём базовое изображение
        self.image = Image.new("RGB", (100, 100), color="white")
        self.draw = ImageDraw.Draw(self.image)

        # Вычисляем длину текста в px
        text_length = self.draw.textlength(max_line, font=self.font)

        # Меняем размер изображения (чтобы влез весь текст) и пересоздаём ImageDraw
        self.image = self.image.resize((int(text_length + TextImage.paddings * 2), self._get_image_height()))
        self.draw = ImageDraw.Draw(self.image)

    def _get_image_height(self) -> int:
        """
        Возвращает высоту изображения с учетом текста и отступов.
        """

        # Чистая высота текста
        text_height = len(self.text.splitlines()) * TextImage.font_size

        # Высота с учетом отступов
        text_height *= TextImage.line_height

        # Убираем последний отступ
        text_height -= TextImage.line_height

        # Добавляем внутренние отступы сверху и снизу
        image_height = text_height + TextImage.paddings * 2

        return int(image_height)

    def _get_text_max_line(self):
        """
        Возвращает самую длинную строку в тексте
        """
        max_line = ""
        max_line_length = 0
        for line in self.text.splitlines():
            line = line.strip("\n")
            if len(line) > max_line_length:
                max_line_length = len(line)
                max_line = line
        return max_line

    def _draw_text_line(self, line):
        """
        Записывает в изображение одну строку и смещает y-координату
        """
        print((self.x, self.y), line)
        self.draw.text((self.x, self.y), line, font=self.font, fill="black")
        self.y += int(TextImage.font_size * TextImage.line_height)

    def _draw_text(self):
        """
        Вставляет весь текст
        """
        for line in self.text.splitlines():
            self._draw_text_line(line.strip("\n"))

    def save_image(self, path: Path) -> None:
        self._draw_text()
        self.image.save(path)
        # self.image.show("Тест")