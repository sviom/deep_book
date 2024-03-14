import numpy as np


def ANDGate(x1, x2):
    zz = np.array([x1, x2])
    kk = np.array([0.5, 0.5])
    gg = np.sum(zz * kk)
    b = -0.7
    tmp = gg + b
    if tmp <= 0:
        print(str(0))
        return 0
    elif tmp > 0:
        print(str(1))
        return 1


def NANDGate(x1, x2):
    zz = np.array([x1, x2])
    kk = np.array([-0.5, -0.5])
    gg = np.sum(zz * kk)
    b = 0.7
    tmp = gg + b
    if tmp <= 0:
        print(str(0))
        return 0
    elif tmp > 0:
        print(str(1))
        return 1


def ORGate(x1, x2):
    zz = np.array([x1, x2])
    kk = np.array([0.5, 0.5])
    gg = np.sum(zz * kk)
    b = -0.2
    tmp = gg + b
    if tmp <= 0:
        print(str(0))
        return 0
    elif tmp > 0:
        print(str(1))
        return 1


ANDGate(0, 0)
ANDGate(0, 1)
ANDGate(1, 0)
ANDGate(1, 1)

NANDGate(0, 0)
NANDGate(0, 1)
NANDGate(1, 0)
NANDGate(1, 1)

ORGate(0, 0)
ORGate(0, 1)
ORGate(1, 0)
ORGate(1, 1)

# x = np.array([0, 1])
# w = np.array([0.5, 0.5])
# b = -0.7

# z = x * w
# y = np.sum(z)
# k = y + b
# print(k)
