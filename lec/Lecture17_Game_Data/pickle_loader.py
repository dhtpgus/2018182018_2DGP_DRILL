class Npc:
    def __init__(self, name, x, y):
        self.name, self.x, self.y = name, x, y

import pickle

with open('npc.pickle', 'rb') as f:
    npc_list = pickle.load(f)

for npc in npc_list:
    print(npc.name, npc.x, npc.y)