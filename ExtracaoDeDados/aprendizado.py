import random
from typing import TypeVar, List, Tuple
X = TypeVar('X') # Tipo genérico para representar um ponto de dados

def split_data(data: List[X], prob: float) -> Tuple[List[X], List[X]]:
    data = data[:]
    random.shuffle(data)
    cut = int(len(data) * prob)
    return data[:cut], data[cut:]

data = [n for n in range(1000)]
train, test = split_data(data, 0.75)

assert len(train) == 750
assert len(test) == 250

assert sorted(train + test) == data

Y = TypeVar('Y')


def train_test_splits(xs: List[X], ys: List[Y], test_pct: float) -> Tuple[List[X], List[X], List[Y], List[Y]]:
    # Gera e divida os indices
    idxs = [i for i in range(len(xs))]
    train_idxs, test_idxs = split_data(idxs, 1 - test_pct)

    return( [xs[i] for i in train_idxs], # x train
            [xs[i] for i in test_idxs], # x test
            [ys[i] for i in train_idxs], # y train
            [ys[i] for i in test_idxs] # y test
        )

xs = [x for x in range(1000)]
ys = [2 * x for x in xs]
x_train, x_test, y_train, y_test = train_test_splits(xs, ys, 0.75)

# assert len(x_train) == len(y_train) == 750
# assert len(x_test) == len(y_test) == 250

# assert all(y == 2 * x for x,y in zip(x_train, y_train))
# assert all(y == 2 * x for x,y in zip(x_test, y_test))

# Prevendo leucemia

def accuracy(true_positive: int, false_positive: int, false_negative: int, true_negative: int) -> float:
    correct = true_negative + true_positive
    total = true_positive + false_negative + false_positive + true_negative
    return correct / total

print(accuracy(70, 4930, 13930, 981070))

# A precisão determina em que medida as previsões positivas são precisas
def precision(true_positive, false_positive ) -> float:
    return true_positive / (true_positive + false_positive)
print(precision
(70, 4930))

# A sensibilidade determina a fração dos positivos identificados pelo modelo
def recall(true_positive, false_negative ) -> float:
    return true_positive / (true_positive + false_negative)
print(recall(70, 13930))