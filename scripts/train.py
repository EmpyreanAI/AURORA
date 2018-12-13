from agent import Agent
from functions import *
from inputdata import InputData
import sys
from indicators import *
import math
from evaluate_test import *
from random import randint
import matplotlib.pyplot as plot
      
stock_name, window_size, episode_count = "VALE3", 10, 0


agent = Agent(window_size)

indicators = Indicators()
id = InputData('../data/ibovespa_csv/')

data_frame = id.data_frame([2010, 2014], stock_name)
data = np.array(data_frame[['PREULT']])
data = np.reshape(data, len(data))
data = data.tolist()

l = len(data) - 1
batch_size = 32
history = []
bought = []
sell = []

for e in range(episode_count + 1):
  print("Episode " + str(e) + "/" + str(episode_count))
  state = getState(data, 0, window_size + 1) # Aqui será a retirada dos indicadores
  # state = indicators.getState(data_frame, 5) # Aqui será a retirada dos indicadores

  agent.zero_cash()
  agent.add_cash(1000000)

  total_profit = 0
  agent.inventory = []

  for t in range(l):
    action = agent.act(state)
    next_state = getState(data, t + 1, window_size + 1)

    reward = 0

    before_cash = agent.get_cash()

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
      agent.add_cash(bought_price)
      sell.append([data[t], t])
      print("Sell: " + formatPrice(data[t]) + " | Profit: " + formatPrice(data[t] - bought_price)  + " Carteira: " + formatPrice(agent.get_cash()))

    # reward = max(data[t] - bought_price, 0)
    reward = math.log((agent.get_cash()/before_cash), 10)
    # reward = randint(-7, 8)
    
    done = True if t == l - 1 else False
    agent.memory.append((state, action, reward, next_state, done))
    state = next_state

    if done:
      print("--------------------------------")
      print("Total Profit: " + formatPrice(total_profit))
      print("--------------------------------")

    if len(agent.memory) > batch_size:
      history = agent.expReplay(batch_size)

    if e % 10 == 0:
      agent.model.save("../models/model_ep_teste"+ stock_name + str(e))

# plt.plot(history.history['loss'])
# plt.plot(history.history['val_loss'])
# plt.title('model loss')
# plt.ylabel('loss')
# plt.xlabel('epoch')
# plt.legend(['train', 'test'], loc='upper left')
# plt.show()

plot.plot(range(len(data)), data, linewidth=0.5, color='blue')

for b in bought:
  plot.scatter(b[1], b[0], label='skitscat', color='green', s=25, marker="^")

for s in sell:
  plot.scatter(s[1], s[0], label='skitscat', color='red', s=25, marker="v")

plot.show()

agent.zero_cash()
agent.add_cash(1000000)
evaluate(agent.model, "VALE3")
