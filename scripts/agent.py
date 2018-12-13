import keras
from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense
from keras.layers import Embedding
from keras.layers import LSTM
from keras.layers import Dropout
# from keras.layers import Flatten
from keras.layers.wrappers import TimeDistributed

from keras.optimizers import Adam

import numpy as np
import random
from collections import deque

class Agent:
  def __init__(self, state_size, is_eval=False, model_name=""):
    self.state_size = state_size # normalized previous days
    self.action_size = 3 # sit, buy, sell
    self.memory = deque(maxlen=1000)
    self.cash = 0
    self.inventory = []
    self.model_name = model_name
    self.is_eval = is_eval

    self.gamma = 0.1
    self.epsilon = 1.0
    self.epsilon_min = 0.01
    self.epsilon_decay = 0.995

    self.model = load_model("../models/" + model_name) if is_eval else self._model()

  def _model(self):
    model = Sequential()
    model.add(Dense(units=64, input_dim=self.state_size, activation="relu", 
                    kernel_initializer='random_uniform'))
    # model.add(Dropout(0.5))
    model.add(Dense(units=16, activation="relu", kernel_initializer='random_uniform'))
    # model.add(Dropout(0.5))
    model.add(Dense(units=8, activation="relu", kernel_initializer='random_uniform'))
    # model.add(Dropout(0.5))
    model.add(Dense(units=3, activation="linear", kernel_initializer='random_uniform'))
    model.compile(loss="mse", optimizer=Adam(lr=0.001))

    # model = Sequential()
    # model.add(Dense(units=256, activation="linear", input_dim=50))
    # model.add(Dense(units=256, activation="elu"))
    # model.add(Embedding(256, 256))
    # model.add(LSTM(units=256))
    # model.add(Dense(3))
    # model.compile(loss="categorical_crossentropy", optimizer=Adam(lr=0.001))

    return model

  def zero_cash(self):
    self.cash = 0

  def add_cash(self, cash):
    self.cash = self.cash + cash

  def sub_cash(self, cash):
    self.cash = self.cash - cash

  def get_cash(self):
    return self.cash

  def act(self, state):
    if not self.is_eval and random.random() <= self.epsilon:
      return random.randrange(self.action_size)
    options = self.model.predict(state)
    return np.argmax(options[0])

  def expReplay(self, batch_size):
    mini_batch = []
    l = len(self.memory)
    for i in range(l - batch_size + 1, l):
      mini_batch.append(self.memory[i])

    for state, action, reward, next_state, done in mini_batch:
      target = reward
      if not done:
        target = reward + self.gamma * np.amax(self.model.predict(next_state)[0])

      target_f = self.model.predict(state)
      target_f[0][action] = target

      # import pdb; pdb.set_trace()
      self.model.fit(state, target_f, epochs=1, verbose=0)

    if self.epsilon > self.epsilon_min:
      self.epsilon *= self.epsilon_decay