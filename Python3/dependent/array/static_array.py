class StaticArray():

    def __init__(self, *args):
        self._len = 0
        self._array = []

        for elem in args:
            self._len += 1
            self._array.append(elem)
    
    def __len__(self):
        return self._len

    def __getitem__(self, idx):
        return self._array[idx]
    
    def __str__(self):
        expand = "["
        expand += ", ".join([str(elem) for elem in self._array])
        expand += "]"

        return expand

    def get(self, idx):
        return self[idx]
