
import matplotlib.pyplot as plot

class Plotter(object):

    def __init__(self):
        print("Ploter Initted")

    def plot_one(self, data, buy, sell):
        plot.plot(range(len(data)), data, linewidth=0.5, color='blue')
        self.plot_buy_marks(buy)
        self.plot_sell_marks(sell)
        plot.show()

    @classmethod
    def _plot_buy_marks(cls, buy):
        for b in buy:
            plot.scatter(b[1], b[0], label='skitscat', color='green', s=25, marker="^")

    @classmethod
    def _plot_sell_marks(cls, sell):
        for s in sell:
            plot.scatter(s[1], s[0], label='skitscat', color='red', s=25, marker="v")
