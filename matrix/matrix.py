class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string.split("\n")
        
    def row(self, index):
        rows = [int(i) for i in self.matrix_string[index-1].split(" ")]
        return rows

    def column(self, index):
        columns = [int(i.split(" ")[index - 1]) for i in self.matrix_string]
        return columns
