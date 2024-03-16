class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            item = self.data[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration
my_list = [1, 2, 3, 4, 5]
my_iterator = MyIterator(my_list)

for item in my_iterator:
    print(item)