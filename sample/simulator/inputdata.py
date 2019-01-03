
import pandas as pd


class InputData(object):

    def __init__(self, start_year, end_year):
        self.path = '../data/'
        self.file_prefix = "COTAHIST_A"
        self.file_postfix = ".TXT.csv"

        self.start_year = start_year
        self.end_year = end_year

        # Data do Pregao
        self.date = 'DATA'

        # Codigo de negociacao do papel
        self.codneg = 'CODNEG'

        # Preco de abertura do papel
        self.preabe = 'PREABE'

        # Preco maximo do papel
        self.premax = 'PREMAX'

        # Preco minimo do papel
        self.premin = 'PREMIN'

        # Preco do ultimo negocio do papel mercado
        self.preult = 'PREULT'

        # Volume total de titulos negociados
        self.voltot = 'VOLTOT'

    def stock_df(self, name):
        frames = []

        for i in range(self.start_year, self.end_year + 1):
            file_name = self.path + self.file_prefix + str(i) + self.file_postfix
            df = pd.read_csv(file_name, low_memory=False)

            df = df.drop(df.index[-1])
            df[self.date] = pd.to_datetime(df[self.date])

            df[self.preabe] = df[self.preabe]/100
            df[self.premax] = df[self.premax]/100
            df[self.premin] = df[self.premin]/100
            df[self.preult] = df[self.preult]/100

            df = df[df[self.codneg] == name]

            df = df[[self.date, self.preabe,
                     self.premax, self.premin,
                     self.preult, self.voltot]]

            frames.append(df)

        return pd.concat(frames)
