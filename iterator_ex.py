class MyListClass:
    def __init__(self):
        self.my_list = ['hello', 'world', 'this', 'is', 'my', 'list']
        self.index = 0
    def __iter__(self):
        return self
    def next(self):
        if 0 <= self.index < len(self.my_list):
            retval = self.my_list[self.index]
            self.index += 1
            return retval
        else:
            raise StopIteration
            
if __name__ == '__main__':
    my_list_class = MyListClass()
    
    for token in my_list_class:
        print token