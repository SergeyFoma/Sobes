class Counter:
    # def __init__(self):
    #     self._count = 0

    def __init__(self, start=0): # variant2 добавили возможность задания начального значения
        self._count=start

    def get(self): # метод добавления порядкового номера
        return self._count

    def inc(self):
        self._count += 1

    def __str__(self):
        return str(self._count)