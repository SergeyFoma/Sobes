from pathlib import Path
from calendar import TextCalendar
# from text_image import TextImage
from hello import hello_world


# created calendar
calendar = TextCalendar()
month = calendar.formatmonth(2025, 1)
print(month)

# created path
home_path = Path("D:/SOBES/Sobes")
calendar_path = home_path/Path("January 2025.png")
print(calendar_path)

# Сохраняем изображение
# ti = TextImage(month)
# ti.save_image(calendar_path)

hello_world('Hello ASDFG')