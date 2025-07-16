import numpy as np
import os
import torch
import torch.nn as nn
from torch.nn import functional as F

# Hyperparameters
batch_size = 32 # how many independent sequences will we process in parallel?
block_size = 8 # what is the maximum context length for predictions?
max_iters = 3000
eval_interval = 300
learning_rate = 1e-3
device = 'cuda' if torch.cuda.is_available() else 'cpu'
eval_iters = 200

torch.manual_seed(1337)

with open('input.txt', 'r') as file:
    text = file.read()

# all the characters in the text
chars = sorted(list(set(text)))
vocab_size = len(chars)

# create a mapping (encoding) from characters to ints

stoi = {ch:i for i,ch in enumerate(chars)}
stoi = {i:ch for i,ch in enumerate(chars)}
# String -> list of ints
encode = lambda x: 
# list of ints -> string
