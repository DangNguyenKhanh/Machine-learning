import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def relu(x, derivative=False):
    if derivative:
        if x > 0:
            return 1
        else:
            return 0
    return max(x, 0)


class SGD:
    def __init__(self, learning_rate=0.1):
        self.learning_rate = learning_rate

    def update(self, params, gradients):
        for i in range(len(params)):
            params[i] -= self.learning_rate * gradients[i]
        return params


class BasicNN:
    def __init__(self):
        np.random.seed(42)
        self.w00 = np.random.normal(loc=0, scale=1)
        self.b00 = np.random.normal(loc=0, scale=1)
        self.w01 = np.random.normal(loc=0, scale=1)

        self.w10 = np.random.normal(loc=0, scale=1)
        self.b10 = np.random.normal(loc=0, scale=1)
        self.w11 = np.random.normal(loc=0, scale=1)

        self.final_bias = 0

    def forward_prop(self, input):
        # 1st neuron - hidden layer 1
        input_y00 = input * self.w00 + self.b00
        output_y00 = relu(input_y00)
        scaled_output_y00 = output_y00 * self.w01

        # 2nd neuron - hidden layer 1
        input_y10 = input * self.w10 + self.b10
        output_y10 = relu(input_y10)
        scaled_output_y01 = output_y10 * self.w11

        # input to last neuron
        output_final = scaled_output_y00 + scaled_output_y01 + self.final_bias

        return output_final

    def backward_prop(self, input, predicted, observed):
        loss = (predicted - observed) ** 2
        output_gradient = 2 * (predicted - observed)

        input_y00 = input * self.w00 + self.b00
        input_y10 = input * self.w10 + self.b10

        final_bias_gradient = output_gradient * 1
        w01_gradient = output_gradient * relu(input_y00, derivative=False)
        w11_gradient = output_gradient * relu(input_y10, derivative=False)

        b00_gradient = output_gradient * self.w01 * relu(input_y00, derivative=True) * 1
        w00_gradient = output_gradient * self.w01 * relu(input_y00, derivative=True) * input

        b10_gradient = output_gradient * self.w11 * relu(input_y10, derivative=True) * 1
        w10_gradient = output_gradient * self.w11 * relu(input_y10, derivative=True) * input

        # Package gradients into a list
        gradients = [w00_gradient, b00_gradient, w01_gradient, w10_gradient, b10_gradient, w11_gradient, final_bias_gradient]

        # Update parameters
        optimizer = SGD()
        self.w00, self.b00, self.w01, self.w10, self.b10, self.w11, self.final_bias = optimizer.update([self.w00, self.b00, self.w01, self.w10, self.b10, self.w11, self.final_bias], gradients)

        return loss

    def fit(self, x_train, y_train, max_epoch=100):
        for epoch in range(max_epoch):
            total_loss = 0

            for i, row in enumerate(x_train):
                output = self.forward_prop(row[0])
                total_loss += self.backward_prop(row[0], output, y_train[i])

            print("Epoch " + str(epoch+1) + '/' + str(max_epoch))
            print('Total loss: ', total_loss)

            if total_loss < 0.0001:
                break

        print('final bias: ', self.final_bias)

    def predict(self, x_test):
        return relu(self.forward_prop(x_test), derivative=False)


X_train = np.array([[0.], [0.5], [1.]])
y_label = np.array([0., 1., 0.])
model = BasicNN()
model.fit(X_train, y_label, max_epoch=150)
X_test = np.linspace(0, 1, num=10)
y_pred = []
for x in X_test:
    y_pred.append(model.predict(x))
sns.set(style='whitegrid')
sns.lineplot(x=X_test, y=y_pred, color='green', linewidth=2.5)
plt.ylabel('Effectiveness')
plt.xlabel('Dose')
plt.show()




