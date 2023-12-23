class py_solution:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))

x=input(99)
print(py_solution().reverse_words(x))