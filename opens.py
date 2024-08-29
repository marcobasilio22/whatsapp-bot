import pandas as pd

class ReadArchive:
    def __init__(self, file_path):
        self.df = pd.read_excel(file_path, dtype={'numero': str})
        self.nome = self.df['nome'].tolist()
        self.numero = self.df['numero'].tolist()
        self.valor = self.df['valor'].tolist()

    def get_name(self):
        return self.nome

    def get_number(self):
        return self.numero

    def get_value(self):
        return self.valor

