import pandas as pd

class InputData(object):

    def __init__(self, path):
        self.path = path

    def data_frame(self, year, name):
      frames = []

      for i in range(year[0], year[1]+1):
        df = pd.read_csv(self.path + "COTAHIST_A" + str(i) + ".TXT.csv", low_memory=False)
        df = df.drop(df.index[-1])
        df['DATA'] = pd.to_datetime(df['DATA'])
        # df['PREABE'] = df['PREABE']/100
        # df['PREMAX'] = df['PREMAX']/100
        # df['PREMIN'] = df['PREMIN']/100
        # df['PREULT'] = df['PREULT']/100
        df = df[df["CODNEG"] == name]
        df = df[["DATA", "PREABE", "PREMAX", "PREMIN", "PREULT", "VOLTOT"]]

        frames.append(df)

      return pd.concat(frames)