from numpy import exp, array, dot

class NeuralNetwork:
    def __init__(self, row=6, col=5, max_moves=50):
        self.weight_count = row * col + max_moves
        self.hidden_count = self.weight_count / 2
        self.w1 = [array([0.0 for i in range(self.weight_count)]) for i in range(self.hidden_count)]
        self.w2 = array([0.0 for i in range(self.hidden_count)])

        self.l1 = None
        self.l2 = None
        self.output = None

    def sigmoid(self, x, deriv=False):
        if deriv:
            return self.sigmoid(x, deriv=False) * (1 - self.sigmoid(x, deriv=False))
        return 1 / (1 + exp(-x))

    def loss(self, actual, expected):
        return (actual - expected) ** 2

    def train(self, _in, _out):
        # forward pass
        self.l1 = _in
        h_sums = [dot(self.l1, self.w1[i]) for i in range(self.hidden_count)]
        #self.l2 = array([sigmoid(dot(self.l1, self.w1[i])) for i in range(hidden_count)])
        self.l2 = array([self.sigmoid(h_sums[i]) for i in range(self.hidden_count)])
        sum = dot(self.l2, self.w2)
        self.output = self.sigmoid(sum)

        loss = self.loss(self.output, _out)

        # backpropagation
        # delta output sum = loss * S'(sum)
        d_osum = loss * self.sigmoid(sum, deriv=True)
        # type(d_w2) = array
        d_w2 = d_osum / self.l2
        # update w2: w2 <- w2 + d_w2
        self.w2 = self.w2 + d_w2

        # delta hidden sum = d_osum / self.w1 * S'(hidden sum)
        # warning: divide by zero error!
        d_hsums = array([d_osum / self.w1[i] * self.sigmoid(h_sums[i], deriv=True) for i in range(self.hidden_count)])
        #d_w1 = d_hsum / input data
        d_w1 = d_hsums / _in
        # update w1: w1 <- w1 + d_w1
        self.w1 = self.w1 + d_w1

        #print self.w1
        #print self.w2

nn = NeuralNetwork(row=2, col=2, max_moves=5)
test = ([0, 1, 2, 3, 0, 0, 0, 0, 0], 1)
nn.train(test[0], test[1])
# divide by zero
# init, end case
# drops
# for some reason current pos isn't in the state
# Eric's new year gift https://www.facebook.com/edgyteensmemes/videos/368292056896333/?hc_ref=NEWSFEED
