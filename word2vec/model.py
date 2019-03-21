import numpy as np

class Softmax:

    def forward(self, input):
        return np.exp(input) / (np.sum(np.exp(input), axis=0, keepdims=True) + 0.001)

    def grad(self, ground_truth, pred):
        assert ground_truth.shape == pred.shape

        return ground_truth - pred


class CrossEntropy:

    def forward(self, probs, ground_truth):
        m = probs.shape[1]
        cost = -(1 / m) * np.sum(np.sum(ground_truth * np.log(probs + 0.001), axis=0, keepdims=True), axis=1)
        return cost


class Linear:

    def __init__(self, input_size: int, output_size: int):
        self.output_size = output_size
        self.input_size = input_size

        # В статье не используется bias
        self.W = np.random.randn(output_size, input_size) * 0.01
        self.cache = {"input": None}

    def forward(self, input):

        self.cache['input'] = input
        return self.W @ input

    def grad(self, cost):
        m = self.cache['input'].shape[1]
        dw = (1 / m) * cost @ self.cache['input'].T
        dinp = self.W.T @ cost

        assert (self.W.shape == dw.shape)
        assert (self.cache['input'].shape == dinp.shape)

        return dw, dinp

    def backward(self, step):
        self.W += step

class Embedding:

    def __init__(self, vocab_size: int, emb_size):
        self.embs = np.random.randn(vocab_size, emb_size) * 0.01


    def ind2vecs(self, input):
        m = input.shape[1]
        word_vec = self.embs[input.flatten(), :].T

        assert (word_vec.shape == (self.embs.shape[1], m))

        return word_vec

    def backward(self, step, inds):
        self.embs[inds, :] += step


class Word2Vec:

    def __init__(self, vocab_size: int, emb_size: int):
        self.emb_size = emb_size
        self.vocab_size = vocab_size

        self.embedding = Embedding(vocab_size, emb_size)
        self.linear = Linear(emb_size, vocab_size)
        self.softmax = Softmax()

        self.cache = {'input': None}

    def forward(self, input):
        self.cache['input'] = input

        vec = self.embedding.ind2vecs(input)
        out = self.linear.forward(vec)
        probs = self.softmax.forward(out)

        return probs

    def grad(self, ground_truth, pred):
        dz = self.softmax.grad(ground_truth, pred)
        dw, dvec = self.linear.grad(dz)
        return  dw, dvec

    def backward(self, step):
        self.embedding.backward(step['embedding'], inds=self.cache['input'].flatten())
        self.linear.backward(step['linear'])

class Optimizer:

    def __init__(self, model: Word2Vec, lr=0.0001):
        self.model = model
        self.lr = lr

    def optimize(self, ground_truth, pred):
        dw, dvec = self.model.grad(ground_truth, pred)
        self.model.backward({
            "embedding": - dvec.T * self.lr,
            "linear": - dw * self.lr
        })

