import keras
from keras.models import load_model

from agent import Agent
from functions import *
from inputdata import InputData
import sys
from indicators import *
import matplotlib.pyplot as plot

def evaluate(model, stock_name):
  stock_name, model_name = "ELET3", "model_ep_n110"
  # model = load_model("../models/" + model_name)
  # print(model.layers[3].get_weights())
  window_size = model.layers[0].input.shape.as_list()[1]

  bought = []
  sell = []

  # import pdb; pdb.set_trace()

  agent = Agent(10, True, model_name)
  agent.model = model
  indicators = Indicators()
  # data = getStockDataVec(stock_name)
  id = InputData('../data/ibovespa_csv/')
  data_frame = id.data_frame([2016, 2017], stock_name)
  data = np.array(data_frame[['PREULT']])
  data = np.reshape(data, len(data))
  data = data.tolist()

  l = len(data) - 1
  batch_size = 32

  # state = indicators.getState(data_frame, 5)
  state = getState(data, 0, window_size + 1)
  total_profit = 0
  agent.inventory = []

  agent.zero_cash()
  agent.add_cash(1000000)

  for t in range(l):
    action = agent.act(state)
    # import pdb; pdb.set_trace()
    print(action)

    before_cash = agent.get_cash()

    print("state: " + str(state))

    # next_state = indicators.getState(data_frame, t+1)
    next_state = getState(data, t + 1, window_size + 1)
    reward = 0

    if action == 1: # buy
      if agent.get_cash() > data[t]:
        agent.sub_cash(data[t])
        bought.append([data[t], t])
        agent.inventory.append(data[t])
        print("Buy: " + formatPrice(data[t]) + " Carteira: " + formatPrice(agent.get_cash()))
      else:
        print("Carteira vazia: " + formatPrice(agent.get_cash()))

    elif action == 2 and len(agent.inventory) > 0: # sell
      bought_price = agent.inventory.pop(0)
      total_profit += data[t] - bought_price
      sell.append([data[t], t])
      agent.add_cash(bought_price)
      print("Sell: " + formatPrice(data[t]) + " | Profit: " + formatPrice(data[t] - bought_price)  + " Carteira: " + formatPrice(agent.get_cash()))

    reward = math.log((agent.get_cash()/before_cash), 10)

    done = True if t == l - 1 else False
    agent.memory.append((state, action, reward, next_state, done))
    state = next_state

    if done:
      print("--------------------------------")
      print(stock_name + " Total Profit: " + formatPrice(total_profit) + " Carteira: " + formatPrice(agent.get_cash()))
      print("--------------------------------")


  plot.plot(range(len(data)), data, linewidth=0.5, color='blue')

  plot.title("Ações: " + stock_name + " de 2016")

  for b in bought:
    plot.scatter(b[1], b[0], label='skitscat', color='green', s=25, marker="^")

  for s in sell:
    plot.scatter(s[1], s[0], label='skitscat', color='red', s=25, marker="v")

  plot.show()