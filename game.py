import torch
import torch.nn as nn
import numpy as np
from os import environ
import Graphics
import Grid_init
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import Ghost_PathFinding

gridhard = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
grideasy = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
gridhard2 = [
    [1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1],
    [1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1],
    [1,1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,1],
    [1,1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1,1],
    [1,1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1,1],
    [1,1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,1],
    [1,1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1,1],
    [1,1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1,1],
    [1,1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1,1],
    [1,1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1,1],
    [1,1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1,1],
    [1,1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1,1],
    [1,1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1,1],
    [1,1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1,1],
    [1,1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1,1],
    [1,1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1,1],
    [1,1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1,1],
    [1,1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1,1],
    [1,1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1,1],
    [1,1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1,1],
    [1,1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,1],
    [1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1],
    [1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1],
]
gridhard3 = [
    [1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1],
    [1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1],
    [1,1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,1],
    [1,1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1,1],
    [1,1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1,1],
    [1,1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1,1],
    [1,1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1,1],
    [1,1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1,1],
    [1,1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1,1],
    [1,1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1,1],
    [1,1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1,1],
    [1,1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1,1],
    [1,1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1,1],
    [1,1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1,1],
    [1,1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1,1],
    [1,1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1,1],
    [1,1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1,1],
    [1,1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1,1],
    [1,1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1,1],
    [1,1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1,1],
    [1,1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,1],
    [1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1],
    [1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1],
]
gridhard4 = [
    [1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1],
    [1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1],
    [1,1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1,1],
    [1,1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1,1],
    [1,1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1,1],
    [1,1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1,1],
    [1,1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1,1],
    [1,1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1,1],
    [1,1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1,1],
    [1,1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1,1],
    [1,1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1,1],
    [1,1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 4, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1,1],
    [1,1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1,1],
    [1,1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1,1],
    [1,1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1,1],
    [1,1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1,1],
    [1,1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1,1],
    [1,1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1,1],
    [1,1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1,1],
    [1,1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1,1],
    [1,1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,1],
    [1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1],
    [1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1],
]
class PacManGame:
    def __init__(self):
        self.screen_size_x, self.screen_size_y = 960, 1400
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.screen_size_x, self.screen_size_y))
        self.reset()
        self.reward

    def reset(self):
        self.a = gridhard2
        self.level_grid = np.array(self.a)
        Grid_init.RandGhost(self.level_grid)
        self.n_rows, self.n_col = np.shape(self.level_grid)
        self.PacMan_row, self.PacMan_col = Grid_init.LocatePacMan(self.level_grid)
        self.pellet_grid = Grid_init.PelletGrid(self.level_grid)
        self.pellet_count = 0
        self.ghost2_row, self.ghost2_col = Grid_init.LocateGhost2(self.level_grid)
        self.game = True
        self.pacman_alive = True
        self.path2 = []
        self.direction = [0, 0, 0, 0]
        self.counter = 0
        self.score = 0
        self.ghost2_map = False
        self.frame_iteration = 0
        self.reward = 0
        self.distance = 0
        self.distance2 = 0

    def softreset(self):
        self.a = gridhard2
        self.level_grid = np.array(self.a)
        Grid_init.RandGhost(self.level_grid)
        self.n_rows, self.n_col = np.shape(self.level_grid)
        self.PacMan_row, self.PacMan_col = Grid_init.LocatePacMan(self.level_grid)
        self.pellet_grid = Grid_init.PelletGrid(self.level_grid)
        self.pellet_count = 0
        self.ghost2_row, self.ghost2_col = Grid_init.LocateGhost2(self.level_grid)
        self.game = True
        self.pacman_alive = True
        self.path2 = []
        self.direction = [0, 0, 0, 0]
        self.counter = 0
        self.ghost2_map = False
        self.frame_iteration = 0
        self.reward = 0
        self.distance = 0
        self.distance2 = 0

    def play_step(self, action):
        self.distance = Ghost_PathFinding.Distance(self.level_grid)
        self.reward = 0
        self.frame_iteration = self.frame_iteration + 1
        self.counter = self.counter + 1
        if self.counter == 3:
            self.counter = 0
        self.clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
        # could also create self.frame_iteration > 100*len9self.

        self.direction = action

        if self.pacman_alive == True:

            if self.direction == [0, 0, 1, 0] and (
                    self.level_grid[self.PacMan_row][self.PacMan_col + 1] == 0 or self.level_grid[self.PacMan_row][self.PacMan_col + 1] == 2):
                self.level_grid[self.PacMan_row][self.PacMan_col] = 2
                self.pellet_grid[self.PacMan_row][self.PacMan_col] = 2
                self.level_grid[self.PacMan_row][self.PacMan_col + 1] = 4
                self.PacMan_col = self.PacMan_col + 1
                if self.level_grid[self.PacMan_row][self.PacMan_col + 1] == 0:
                    self.score = self.score + 10
                    self.reward = 10

            elif self.direction == [1, 0, 0, 0] and (
                    self.level_grid[self.PacMan_row][self.PacMan_col - 1] == 0 or self.level_grid[self.PacMan_row][self.PacMan_col - 1] == 2):
                self.level_grid[self.PacMan_row][self.PacMan_col] = 2
                self.pellet_grid[self.PacMan_row][self.PacMan_col] = 2
                self.level_grid[self.PacMan_row][self.PacMan_col - 1] = 4
                self.PacMan_col = self.PacMan_col - 1
                if self.level_grid[self.PacMan_row][self.PacMan_col + 1] == 0:
                    self.score = self.score + 10
                    self.reward = 10

            elif self.direction == [0, 1, 0, 0] and (
                    self.level_grid[self.PacMan_row - 1][self.PacMan_col] == 0 or self.level_grid[self.PacMan_row - 1][self.PacMan_col] == 2):
                self.level_grid[self.PacMan_row][self.PacMan_col] = 2
                self.pellet_grid[self.PacMan_row][self.PacMan_col] = 2
                self.level_grid[self.PacMan_row - 1][self.PacMan_col] = 4
                self.PacMan_row = self.PacMan_row - 1
                if self.level_grid[self.PacMan_row][self.PacMan_col + 1] == 0:
                    self.score = self.score + 10
                    self.reward = 10

            elif self.direction == [0, 0, 0, 1] and (
                    self.level_grid[self.PacMan_row + 1][self.PacMan_col] == 0 or self.level_grid[self.PacMan_row + 1][self.PacMan_col] == 2):
                self.level_grid[self.PacMan_row][self.PacMan_col] = 2
                self.pellet_grid[self.PacMan_row][self.PacMan_col] = 2
                self.level_grid[self.PacMan_row + 1][self.PacMan_col] = 4
                self.PacMan_row = self.PacMan_row + 1
                if self.level_grid[self.PacMan_row][self.PacMan_col + 1] == 0:
                    self.score = self.score + 10
                    self.reward = 10
            elif (self.direction == [0, 0, 1, 0] and self.level_grid[self.PacMan_row][self.PacMan_col + 1] == 3) or (self.direction == [1, 0, 0, 0] and self.level_grid[self.PacMan_row][self.PacMan_col - 1] == 3) or (self.direction == [0, 1, 0, 0] and self.level_grid[self.PacMan_row - 1][self.PacMan_col] == 3) or (self.direction == [0, 0, 0, 1] and self.level_grid[self.PacMan_row + 1][self.PacMan_col] == 3):
                self.pacman_alive = False
                self.reward = -15
                return self.reward, self.pacman_alive, self.score
            elif (self.direction == [0, 0, 1, 0] and self.level_grid[self.PacMan_row][self.PacMan_col + 1] == 1) or (self.direction == [1, 0, 0, 0] and self.level_grid[self.PacMan_row][self.PacMan_col - 1] == 1) or (self.direction == [0, 1, 0, 0] and self.level_grid[self.PacMan_row - 1][self.PacMan_col] == 1) or (self.direction == [0, 0, 0, 1] and self.level_grid[self.PacMan_row + 1][self.PacMan_col] == 1):
                 self.reward = -5

            self.pellet_count = Grid_init.PelletCounter(self.level_grid)

            if self.pellet_count != 0:
                self.distance2 = Ghost_PathFinding.Distance(self.level_grid)
            elif self.pellet_count == 0:
                self.softreset()

            if self.ghost2_map == False:
                self.path2, self.ghost2_row, self.ghost2_col = Ghost_PathFinding.Path_init(self.ghost2_row,
                                                                                           self.ghost2_col,
                                                                                           self.level_grid)
                # path2.append(path2[-1])
                self.ghost2_map = True

            if self.ghost2_map == True:
                self.level_grid[self.ghost2_row][self.ghost2_col] = 2

                if self.level_grid[self.path2[0][0]][self.path2[0][1]] == 4 and self.ghost2_map == True:
                    self.level_grid[self.ghost2_row][self.ghost2_col] = 3
                    self.pacman_alive = False
                    self.reward = -15
                    return self.reward, self.pacman_alive, self.score
                elif self.level_grid[self.path2[0][0]][self.path2[0][1]] == 2 and self.ghost2_map == True:
                    self.level_grid[self.path2[0][0]][self.path2[0][1]] = 3
                    self.ghost2_row, self.ghost2_col = self.path2[0][0], self.path2[0][1]
                    self.path2.pop(0)
                    if (self.counter == 2):
                        self.ghost2_map = False
                    if len(self.path2) == 0:
                        self.ghost2_map = False
                elif self.level_grid[self.path2[0][0]][self.path2[0][1]] == 0:
                    self.level_grid[self.ghost2_row][self.ghost2_col] = 0
                    self.level_grid[self.path2[0][0]][self.path2[0][1]] = 3
                    self.ghost2_row, self.ghost2_col = self.path2[0][0], self.path2[0][1]
                    self.path2.pop(0)
                    if (self.counter == 2):
                        self.ghost2_map = False
                    if len(self.path2) == 0:
                        self.ghost2_map = False

            if (self.distance2 < self.distance):
                self.reward = self.reward + 5
            elif (self.distance2 > self.distance):
                self.reward = self.reward - 5


        self.ghost2_row, self.ghost2_col, self.pellet_count = Graphics.LevelCreator(self.level_grid, self.screen, self.counter, self.direction, self.PacMan_row, self.PacMan_col)
        #Graphics.FirstPerson(self.level_grid, self.screen2, self.PacMan_row, self.PacMan_col, self.direction)
        pygame.display.flip()
        return self.reward, self.pacman_alive, self.score



