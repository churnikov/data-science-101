import numpy as np

class CrossEntropy:

    def forward(self, probs, ground_truth):
        m = probs.shape[1]
        cost = -(1 / m) * np.sum(np.log(probs[ground_truth.flatten(), np.arange(m)] + 0.001))
        return cost


class Optimizer:

    def __init__(self, model, lr=0.0001, decrease=0.98):
        self.decrease = decrease
        self.model = model
        self.lr = lr

    def optimize(self, ground_truth, pred):
        dw, dvec = self.model.grad(ground_truth, pred)
        self.model.backward({
            "embedding": -dvec.T * self.lr,
            "linear": -dw * self.lr
        })

    def decrease_lr(self, prod=None):
        if prod is not None:
            self.lr *= prod
        else:
            self.lr *= self.decrease


def train(X, Y, model, optimizer: Optimizer, loss, epochs, batch_size=256,
          print_cost=True):
    costs = []
    m = X.shape[1]

    for epoch in range(epochs):
        epoch_cost = 0
        batch_inds = list(range(0, m, batch_size))
        np.random.shuffle(batch_inds)
        for i in batch_inds:
            X_batch = X[:, i:i + batch_size]
            Y_batch = Y[:, i:i + batch_size]

            softmax_out = model.forward(X_batch)
            optimizer.optimize(Y_batch, softmax_out)
            cost = loss.forward(softmax_out, Y_batch)
            epoch_cost += np.squeeze(cost)

        costs.append(epoch_cost)
        if print_cost and epoch % (epochs // 500) == 0:
            print("Cost after epoch {}: {}".format(epoch, epoch_cost))
        if epoch % (epochs // 100) == 0:
            optimizer.decrease_lr()

    return costs
