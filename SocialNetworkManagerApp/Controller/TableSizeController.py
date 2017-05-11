class TableSizeController():
    def __init__(self):
        self.count = 0

    def __str__(self):
        return str(self.count)

    def increment(self):
        self.count += 1
        return ''

    def pair(self):
        return self.count % 2 == 0