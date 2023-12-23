class CapitalIterable:
    def __init__ (self, string):
        self.string=string
    def __iter__ (self):
        return CapitalIterator(self.string)

class CapitalIterator:
    def __init__(self, string):
        self.words=[w.capitalize() for w in string.split()]
        self.index=0
    def __next__ (self):
        if self.index==len(self.words):
            raise StopIteration()
        word=self.words [self.index]
        self.index += 1
        return word
    def __iter__ (self):
        return self

itble=CapitalIterable(
    'the quick brown fox jumps over the dog')
it=iter(itble)
while True:
    try:
        print(next(it))
    except StopIteration:
        break