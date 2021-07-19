import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import numpy as np
import os

# create model

class Linear_QNet(nn.Module):
    def __init__(self, input_size, hidden_size, hidden_size2, output_size):
        super(Linear_QNet, self).__init__()
        self.linear1 = nn.Linear(input_size, hidden_size)
        self.linear2 = nn.Linear(hidden_size,hidden_size2)
        self.linear3 = nn.Linear(hidden_size2, output_size)

    def forward(self, x):
        x = F.leaky_relu(self.linear1(x),negative_slope=0.01)
        x = F.leaky_relu(self.linear2(x),negative_slope=0.01)
        x = self.linear3(x)
        return x

    def save(self, file_name='model5distance.pth'):
        model_folder_path = './model'
        if not os.path.exists(model_folder_path):
            os.makedirs(model_folder_path)

        file_name = os.path.join(model_folder_path, file_name)
        torch.save(self.state_dict(), file_name)


# criterion = nn.CrossEntropyLoss()
# optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate

class QTrainer:
    def __init__(self, model, lr, gamma):
        self.lr = lr
        self.gamma = gamma
        self.model = model
        self.optimizer = optim.Adam(model.parameters(), lr=self.lr)
        #self.optimizer.load_state_dict(torch.load('./model/model2.pth'))
        #self.optimizer = optim.SGD(model.parameters(), lr=self.lr)
        self.criterion = nn.MSELoss()

    def train_step(self, state, action, reward, next_state, done):
        state = torch.tensor(state,dtype=torch.float)
        next_state = torch.tensor(next_state, dtype=torch.float)
        action = torch.tensor(action, dtype=torch.float)
        reward = torch.tensor(reward, dtype=torch.float)
        # (n, x)

        if len(state.shape) == 1:
            # (1, x)
            state = torch.unsqueeze(state, 0)
            next_state = torch.unsqueeze(next_state, 0)
            action = torch.unsqueeze(action, 0)
            reward = torch.unsqueeze(reward, 0)
            done = (done,)

            # 1: predicted Q values with current state
            pred = self.model(state)
            target = pred.clone()
            for idx in range(len(done)):
                #print(f"Idx: {idx}, Reward[idx]: {reward[idx]} ")
                Q_new = reward[idx]
                if done[idx] == True: #PacMan is still alive
                    Q_new = reward[idx] + self.gamma * torch.max(self.model(next_state[idx]))

                target[idx][torch.argmax(action).item()] = Q_new

            # 2: Q_new = r + y * max( next_predicted Q value) only do this if not done
            #pred.clone()
            # preds[argmax(action)] = Q_new
            self.optimizer.zero_grad()
            #print(f"target: {target}, pred: {pred}")
            loss = self.criterion(target,pred)
            loss.backward()

            self.optimizer.step()




