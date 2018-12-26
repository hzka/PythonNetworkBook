# neural network definition
import numpy
import numpy
import scipy.special


class neuralNetwork:

    # initialise the neural network
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        # set number of nodes in each input,hidden,output layer
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        self.lr = learningrate
        # link weight matrices,wih and who
        # weights inside the arrays are w_i_j,where link is from node i to node j in the next layer
        # w11 w21
        # w12 w22 etc
        # self.wih = (numpy.random.random(self.hnodes,self.inodes)-0.5)
        # self.who = (numpy.random.random(self.onodes,self.hnodes)-0.5)
        self.wih = (numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes)))
        self.who = (numpy.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes)))
        self.activation_funcation = lambda x: scipy.special.expit(x)
        pass

    # train the neural network
    def train(self, inputs_list, targets_list):
        inputs = numpy.array(inputs_list, ndmin=2).T
        targes = numpy.array(targets_list, ndmin=2).T
        hidden_inputs = numpy.dot(self.wih, inputs)
        hidden_outputs = self.activation_funcation(hidden_inputs)

        final_inputs = numpy.dot(self.who, hidden_outputs)
        final_ouputs = self.activation_funcation(final_inputs)

        output_errors = targes - final_ouputs
        hidden_errors = numpy.dot(self.who.T, output_errors)
        self.who += self.lr * numpy.dot((output_errors * final_ouputs * (1.0 - final_ouputs)),
                                        numpy.transpose(hidden_outputs))
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)),
                                        numpy.transpose(inputs))
        pass

    # query the neural network
    def query(self, inputs_list):
        inputs = numpy.array(inputs_list, ndmin=2).T
        hidden_inputs = numpy.dot(self.wih, inputs)
        hidden_outputs = self.activation_funcation(hidden_inputs)

        final_inputs = numpy.dot(self.who, hidden_outputs)
        final_ouputs = self.activation_funcation(final_inputs)
        return final_ouputs


# number of input ,hidden and output nodes
input_nodes = 784
hidden_nodes = 200
output_nodes = 10

# learning rate is 0.3
learning_rate = 0.2

# create insrance of neural network
n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

# load csv file
training_data_file = open("E:/postgraduate/PythonCode/IpythonMNIST/mnist_train.csv", 'r')
training_data_list = training_data_file.readlines()
training_data_file.close()
# print(n.query([1.0, 0.5, -1.5]))
# n.train([1.0, 0.5, 1.5],[1.0, 0.5, 1.5])
# n.train([2.0, 0.6, 1.6],[2.0, 0.6, 1.6])
# n.train([1.9, 10.5, 8],[1.9, 10.5, 8])
# n.train([20.0, 0.66, 1.98],[20.0, 0.66, 1.98])

# print(n.query([2.0, 0.5, 1.5]))
# numpy.random.rand(3, 3) - 0.5
epochs = 2
for e in range(epochs):
    for record in training_data_list:
        all_values = record.split(',')
        inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
        targets = numpy.zeros(output_nodes) + 0.01
        targets[int(all_values[0])] = 0.99
        n.train(inputs, targets)
        pass
    pass

# load csv file
test_data_file = open("E:/postgraduate/PythonCode/IpythonMNIST/mnist_test.csv", 'r')
test_data_list = test_data_file.readlines()
test_data_file.close()
# all_values = test_data_list[0].split(',')
# print(all_values[0])
scorecasrd = []
for record in test_data_list:
    all_values = record.split(',')
    correct_label = int(all_values[0])
    print (correct_label, "correct label")
    outputs = n.query((numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01)
    label = numpy.argmax(outputs)
    print (label, "network's answer")
    if (label == correct_label):
        scorecasrd.append(1)
    else:
        scorecasrd.append(0)
        pass
    pass
print (scorecasrd)
scorecasrd_array = numpy.asarray(scorecasrd)
print ("performance=", scorecasrd_array.sum() * 1.0 / scorecasrd_array.size)

# for record in test_data_list:
#     all_values = record.split(',')
#     correct_label = int(all_values[0])
#     print (correct_label , "correct label")
#     inputs = (numpy.asfarray(all_values[1:]) /255.0*0.99)+0.01)
#     outputs = n.query(inputs)
#     label = numpy.argmax(outputs)
#     print (label,"network's answer")
#     pass