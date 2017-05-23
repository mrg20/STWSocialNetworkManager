class TableSizeController():
    def __init__(self):
        self.count = 0
        self.newbox = True

    def __str__(self):
        return str(self.count)

    def increment(self):
        self.count += 1
        return ''

    def pair(self):
        return self.count % 2 == 0

    def is_less_than_eight(self):
        return self.count < 8

    def get_box_num(self):
        return self.count+1

    def not_new_box(self):
        self.newbox = False
        return ''

    def new_box(self):
        self.newbox = True
        return ''

    def is_new_box(self):
        return self.newbox