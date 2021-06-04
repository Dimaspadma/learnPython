class Stack(list):

    def tambah(self, data):
        self.append(data)
    
    def hapus(self):
        if not self.is_empty():
            self.pop()
        else:
            print("can't pop")
    
    def is_empty(self):
        return len(self) == 0


test = Stack()
test.hapus()

print(test)