# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 08:20:42 2021

@author: omara
"""

import networkx as nx
import matplotlib.pyplot as plt
from datetime import datetime
from dfs import dfs


G = nx.Graph()

for i in range(100):
    G.add_node(i)

for i in range(0,100, 4):
    for j in range(1,100,1):
        G.add_edge(i, j);
        
for i in range(0,100, 3):
    for j in range(1,100,2):
        G.add_edge(j, i);
        
for i in range(0,100, 7):
    for j in range(1,100,3):
        G.add_edge(i, j);
        
for i in range(0,100, 1):
    for j in range(1,100,2):
        G.add_edge(i, j);
        
for i in range(0,100, 5):
    for j in range(1,100,4):
        G.add_edge(i, j);
for i in range(0,100, 10):
    for j in range(1,100,3):
        G.add_edge(i, j);


GResultado = nx.Graph()
t1 = datetime.now(tz=None)
GResultado = dfs(G, 3)
t2 = datetime.now(tz=None)
plt.figure(1)

nx.draw_networkx(GResultado, pos=nx.spring_layout(GResultado), with_labels=True)
plt.show()
print (t2 - t1)





