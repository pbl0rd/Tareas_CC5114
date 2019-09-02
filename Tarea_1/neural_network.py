import numpy as np
from neuron_layer import NeuronLayer
from tanh import Tanh
from sigmoid import Sigmoid


# Clase Red Neuronal
class NeuralNetwork(object):

    # Método constructor para la clase Red Neuronal que recibe un entero con el número capas ocultas de la red, una
    # lista de enteros que se corresponden con el número de neuronas de cada capa oculta de la red, un entero con la
    # catidad de inputs/features del dataset a ocupar y un entero con la cantidad de neuronas que debe tener la capa de
    # salida de la red. Opcionalmente puede recibir un diccionario con los diccionarios de pesos de las neuronas de cada
    # capa, un diccionario con los diccionarios de los sesgos de las neuronas de cada capa, un diccionario con las
    # funciones de activación a ser ocupadas por cada capa de la red (debe ser Sigmoid() o Tanh() para cada capa) y un
    # float con la tasa de aprendizaje de la red completa.
    def __init__(self, hlayers: int, neurons_per_layer: list, entrada: int, salida: int, weights=None, bias=None,
                 ac_functions=None, lrate=0.1):
        if type(hlayers) != int:
            raise ValueError("El número de capas ocultas debe ser un número entero positivo")
        elif hlayers < 1:
            raise ValueError("El número de capas ocultas debe ser un número entero positivo")
        elif type(neurons_per_layer) != list:
            raise ValueError("neurons_per_layer debe ser una lista de números enteros positivos")
        elif len(neurons_per_layer) != hlayers:
            raise ValueError("El largo de neurons_per_layer debe coincidir con el número de capas ocultas")
        elif type(entrada) != int:
            raise ValueError("El número de inputs debe ser un número entero positivo")
        elif entrada < 1:
            raise ValueError("El número de inputs debe ser un número entero positivo")
        elif type(salida) != int:
            raise ValueError("El número de neuronas en la capa de salida debe ser un número entero positivo")
        elif salida < 1:
            raise ValueError("El número de neuronas en la capa de salida debe ser un número entero positivo")
        else:
            self.__lrate = lrate
            self.__hlayers = hlayers
            if ac_functions is None:
                ac_functions = {}
                for j in range(hlayers+1):
                    ac_functions[j] = Sigmoid()
                self.__acfunctions = ac_functions
            elif type(ac_functions) != dict:
                raise ValueError("Input ac_functions debe ser un diccionario con las fuciones de activación "+
                                 "de cada capa")
            elif len(list(ac_functions.keys())) != hlayers+1:
                raise ValueError("Número de entradas del diccionario ac_functions debe ser igual al numero de capas")
            else:
                self.__acfunctions = ac_functions
            self.__layers = {}
            if weights is None and bias is None:
                for i in range(hlayers + 1):
                    if i == 0:
                        self.__layers[i] = NeuronLayer(neurons=neurons_per_layer[i], n_weights=entrada,
                                                       ac_function=ac_functions[i], lrate=lrate)
                    elif i == hlayers:
                        self.__layers[i] = NeuronLayer(neurons=salida, n_weights=neurons_per_layer[i - 1],
                                                       ac_function=ac_functions[i], lrate=lrate)
                    else:
                        self.__layers[i] = NeuronLayer(neurons=neurons_per_layer[i], n_weights=neurons_per_layer[i - 1],
                                                       ac_function=ac_functions[i], lrate=lrate)
            elif bias is None:
                if type(weights) is not dict:
                    raise ValueError("Input weights debe ser un diccionario con los diccionarios con las listas de " +
                                     "pesos de cada capa")
                elif len(list(weights.keys())) != hlayers+1:
                    raise ValueError("Número de entradas del diccionario weights debe ser igual al número de capas")
                else:
                    for i in range(hlayers + 1):
                        if i == 0:
                            self.__layers[i] = NeuronLayer(neurons=neurons_per_layer[i], n_weights=entrada,
                                                           weights=weights[i], ac_function=ac_functions[i], lrate=lrate)
                        elif i == hlayers:
                            self.__layers[i] = NeuronLayer(neurons=salida, n_weights=neurons_per_layer[i - 1],
                                                           weights=weights[i], ac_function=ac_functions[i], lrate=lrate)
                        else:
                            self.__layers[i] = NeuronLayer(neurons=neurons_per_layer[i],
                                                           n_weights=neurons_per_layer[i - 1], weights=weights[i],
                                                           ac_function=ac_functions[i], lrate=lrate)
            elif weights is None:
                if type(bias) is not dict:
                    raise ValueError("Input bias debe ser un diccionario con los diccionarios con los bias de cada " +
                                     "capa")
                elif len(list(bias.keys())) != hlayers+1:
                    raise ValueError("Número de entradas del diccionario bias debe ser igual al número de capas")
                else:
                    for i in range(hlayers + 1):
                        if i == 0:
                            self.__layers[i] = NeuronLayer(neurons=neurons_per_layer[i], n_weights=entrada,
                                                           biass=bias[i], ac_function=ac_functions[i], lrate=lrate)
                        elif i == hlayers:
                            self.__layers[i] = NeuronLayer(neurons=salida, n_weights=neurons_per_layer[i - 1],
                                                           biass=bias[i], ac_function=ac_functions[i], lrate=lrate)
                        else:
                            self.__layers[i] = NeuronLayer(neurons=neurons_per_layer[i],
                                                           n_weights=neurons_per_layer[i - 1], biass=bias[i],
                                                           ac_function=ac_functions[i], lrate=lrate)
            else:
                if type(weights) is not dict or type(bias) is not dict:
                    raise ValueError("El input weights y bias deben ser diccionarios con los diccionarios con las " +
                                     "listas de pesos y bias de cada capa de la red respectivamente")
                elif len(list(weights.keys())) != hlayers+1 or len(list(bias.keys())) != hlayers+1:
                    raise ValueError("El número de entradas de los diccionario weights y bias debe ser igual al " +
                                     "número de capas de la red")
                else:
                    for i in range(hlayers + 1):
                        if i == 0:
                            self.__layers[i] = NeuronLayer(neurons=neurons_per_layer[i], n_weights=entrada,
                                                           weights=weights[i], bias=bias[i],
                                                           ac_function=ac_functions[i], lrate=lrate)
                        elif i == hlayers:
                            self.__layers[i] = NeuronLayer(neurons=salida, n_weights=neurons_per_layer[i - 1],
                                                           weights=weights[i], bias=bias[i],
                                                           ac_function=ac_functions[i], lrate=lrate)
                        else:
                            self.__layers[i] = NeuronLayer(neurons=neurons_per_layer[i],
                                                           n_weights=neurons_per_layer[i - 1], weights=weights[i],
                                                           bias=bias[i], ac_function=ac_functions[i], lrate=lrate)

    # Métodos get para obtener los atributos de la red.

    # Función para obtener un diccionario con los diccionarios de pesos de cada capa de la red
    def get_weights(self):
        weights = {}
        for i in range(self.__hlayers+1):
            weights[i] = self.__layers[i].get_weights().copy()
        return weights

    # Función para obtener un diccionario con los diccionarios de sesgos de cada capa de la red
    def get_bias(self):
        bias = {}
        for i in range(self.__hlayers+1):
            bias[i] = self.__layers[i].get_bias().copy()
        return bias

    # Métodos set para modificarr los atributos de la red.

    # Función para modificar los pesos de las neuronas de la red.
    # Recibe un diccionario con los diccionarios con los nuevos arreglos de pesos para las neuronas de cada capa
    def set_weights(self, new_weights: dict):
        if type(new_weights) is not dict:
            raise ValueError("Input new_weights debe ser un diccionario con los diccionarios con las listas de " +
                             "pesos de cada capa")
        elif len(list(new_weights.keys())) != self.__hlayers + 1:
            raise ValueError("Número de entradas del diccionario weights debe ser igual al número de capas")
        else:
            for i in range(self.__hlayers+1):
                self.__layers[i].set_weights(new_weights[i])

    # Función para modificar los sesgos de las neuronas de la red.
    # Recibe un diccionario  con los diccionarios con los nuevos sesgos para las neuronas de cada capa
    def set_bias(self, new_bias: dict):
        if type(new_bias) is not dict:
            raise ValueError("Input new_bias debe ser un diccionario con los diccionarios con los bias de cada " +
                             "capa")
        elif len(list(new_bias.keys())) != self.__hlayers + 1:
            raise ValueError("Número de entradas del diccionario bias debe ser igual al número de capas")
        else:
            for i in range(self.__hlayers+1):
                self.__layers[i].set_bias(new_bias[i])

    # Función para alimentar a la red neuronal con un arreglo de inputs (x) cuyo tamaño coincide con el número de
    # pesos de cada neurona de la capa de entrada. Retorna un arreglo con la respuesta dada por cada neurona de la
    # capa de salida y un diccionario con los arreglos correspondientes a las respuestas de cada capa de la red.
    def feed(self, x: np.ndarray):
        in_aux = x.copy()
        layers_out = {}  # diccionario en el que guardaremos las salidas de cada capa de la red
        for i in range(self.__hlayers+1):  # Recorremos las capas de la red comenzando por la primera
            res = self.__layers[i].feed(in_aux).copy()  # Obtenemos la salida de la capa i
            layers_out[i] = res.copy()  # guardamos la respuesta de la capa i en el diccionario
            in_aux = res.copy()  # actualizamos el valor del input para alimentar la siguiente capa
        return res, layers_out

    # método para propagar el error, recibe los outputs de cada capa y la etiqueta correspondiente al input que generó
    # los outputs. Retorna un diccionario con los vectores deltas de cada capa.
    def back_prop(self, layers_out: dict, y: np.ndarray):
        pos = self.__hlayers  # posición (empezamos en la última capa)
        grads = {}  # guardaremos los vectores con los delta en este diccionario
        for i in range(self.__hlayers+1):  # Recorremos las capas de la red (lo haremos en orden inverso usando pos)
            if pos-i == self.__hlayers:  # si estamos en la capa de salida
                error = y - layers_out[pos-i]  # calculamos un vector de errores
                delta = []  # arreglo donde guardaremos los deltas de cada neurona de la capa de salida
                for j in range(len(error)):
                    # agregamos al arreglo de deltas, el delta correspondiente a la neurona j
                    delta.append(error[j]*self.__layers[pos-i].get_acfunction().derivative(layers_out[pos-i][j]))
                delta = np.array(delta)
                grads[pos-i] = delta.copy()  # guardamos una copia del vector delta de la capa de salida
            else:  # para las otras capas
                # calculamos el vector de errores de la capa (pos-i)
                error = [np.dot(self.__layers[pos-i+1].get_weights_pos_i(j),
                                grads[pos-i+1]) for j in range(self.__layers[pos-i].get_length())]
                delta = []  # arreglo donde guardaremos los deltas de cada neurona de la capa
                for j in range(len(error)):
                    # agregamos al arreglo de deltas, el delta correspondiente a la neurona j
                    delta.append(error[j] * self.__layers[pos - i].get_acfunction().derivative(layers_out[pos - i][j]))
                delta = np.array(delta)
                grads[pos - i] = delta.copy()  # guardamos una copia del vector delta de la capa
        return grads

    # método para actualizar los parámetros de la red, recibe el input de la red, los outputs de cada capa y los
    # deltas de cada neurona. Retorna un diccionario con los nuevos pesos de la red y otro con los nuevos bias
    def upd_params(self, x: np.ndarray, layers_out: dict, grads: dict):
        new_weights_net = {}  # diccionario donde se guardarán los nuevos pesos de la red
        new_bias_net = {}  # diccionario donde se guardarán los nuevos bias de la red
        lr = self.__lrate  # obtenemos el learning rate de la red
        for i in range(self.__hlayers+1):  # Recorremos las capas de la red
            old_weights = self.__layers[i].get_weights().copy()  # diccionario con los pesos actuales de la capa i
            old_bias = self.__layers[i].get_bias().copy()  # diccionario con los bias actuales de la capa i
            new_weights = {}  # diccionario para guardar los pesos nuevos de la capa i
            new_bias = {}  # diccionario para guardar los bias nuevos de la capa i
            for j in range(self.__layers[i].get_length()):  # Recorremos las neuronas de la capa
                new_weights_neuron = []  # lista para guardar los nuevos pesos de la neurona j
                for k in range(self.__layers[i].get_neurons()[j].get_length()):  # Recorremos los pesos de la neurona j
                    if i == 0:  # si la capa es la inicial debemos usar el input de la red para recalcular pesos
                        new_weights_neuron.append(old_weights[j][k] + x[k] * lr * grads[i][j])
                    else:  # si la capa no es la inicial ocupamos la salida de la capa anterior para recalcular pesos
                        new_weights_neuron.append(old_weights[j][k] + layers_out[i-1][k] * lr * grads[i][j])
                new_weights[j] = np.array(new_weights_neuron).copy()  # guardamos una copìa del nuevo vector de pesos
                                                                      # de la neurona j
                new_bias[j] = old_bias[j] + lr * grads[i][j]  # guardamos en nuevo bias de la neurona j
            new_weights_net[i] = new_weights.copy()  # guardamos una copia del diccionario de nuevos pesos de la capa i
            new_bias_net[i] = new_bias.copy()  # guardamos una copia del diccionario de nuevos sesgos de la capa i
        return new_weights_net, new_bias_net

    # método para entrenar a la red con un ejemplo. Recibe el input de la red (x) y la respuesta/etiqueta
    # correspondiente a ese input. Retorna  la respuesta dada por la red, el error comentido y si se considera como
    # acierto tal respuesta.
    def train(self, x: np.ndarray, y: np.ndarray):
        res, layers_out = self.feed(x)  # obtenemos las salidas del codigo
        grads = self.back_prop(layers_out, y)
        new_weights, new_bias = self.upd_params(x, layers_out, grads)
        self.set_weights(new_weights)
        self.set_bias(new_bias)
        ans = np.array(y)
        ans_hat = np.array(res)
        diff = ans-ans_hat
        error = np.dot(diff, diff)/len(diff)
        ans_hat_acc = np.eye(1, len(ans), int(np.argmax(res)))[0]
        diff_acc = ans - ans_hat_acc
        error_acc = np.dot(diff_acc, diff_acc)/len(diff_acc)
        if error_acc == 0.0:
            acierto = 1
        else:
            acierto = 0
        return res, error, acierto

    # método para entrenar a la red con un dataset completo. Recibe una lista de vectores de inputs (x) y una lista
    # con las respuestas/etiquetas correspondientes a esos inputs. Retorna un vector con la respuesta dada por la red
    # a cada uno de los ejemplos, el error total promedio y el porcentaje de aciertos logrado.
    def train_w_set(self, x, y):
        preds = []
        epoch_error = 0
        accuracy = 0
        for j in range(len(x)):  # para cada ejemplo en el dataset de entrenamiento
            res, error, acierto = self.train(x[j], y[j])  # entrenamos la red con el ejemplo j del dataset
            preds.append(res[:])
            epoch_error += error
            accuracy += acierto
        epoch_error = epoch_error/len(x)
        accuracy = accuracy/len(x)
        return preds, epoch_error, accuracy

    # método para entrenar a la red con un dataset completo un determinado número de épocas. Recibe una lista de
    # vectores de inputs (x) y una lista con las respuestas/etiquetas correspondientes a esos inputs.
    # Retorna un diccionario con un vector con la respuesta dada por la red a cada uno de los ejemplos por cada época,
    # un diccionario con el error total promedio por cada época y un diccionario con el porcentaje de aciertos logrado
    # por cada época.
    def train_network(self, x, y, epochs=100):
        preds_per_epoch = {}  # diccionario donde guardaremos las predicciones por época
        error_per_epoch = {}  # diccionario donde guardaremos los errores por época
        accuracy_per_epoch = {}  # diccionario donde guardaremos los accuracy por época
        for i in range(epochs):  # para cada época
            preds, epoch_error, accuracy = self.train_w_set(x, y)  # entrenamos la red con el dataset
            preds_per_epoch[i] = preds[:]  # guardamos las predicciones de la época
            error_per_epoch[i] = epoch_error  # guardamos el error de la época
            accuracy_per_epoch[i] = accuracy  # guardamos el accuracy de la época
        return preds_per_epoch, error_per_epoch, accuracy_per_epoch

    # método para evaluar a la red con un dataset de testeo. Recibe una lista de
    # vectores de inputs (test_x) y una lista con las respuestas/etiquetas correspondientes a esos inputs (test_y).
    # Retorna un vector con la respuesta dada por la red a cada uno de los ejemplos, el error total promedio y
    # el porcentaje de aciertos logrado.
    def eval(self, test_x, test_y):
        preds = []  # arreglo donde guardaremos las predicciones de la red
        error_final = 0
        accuracy = 0
        for i in range(len(test_x)):  # para cada ejemplo del dataset de testeo
            res, layers_out = self.feed(test_x[i])  # obtenemos la predicción
            preds.append(res)
            ans = np.array(test_y[i])
            ans_hat = np.array(res)
            diff = ans - ans_hat  # calculamos la diferencia entre la etiqueta y la predicción
            error = np.dot(diff, diff) / len(diff)  # calculamos el error MSE
            ans_hat_acc = np.eye(1, len(ans), int(np.argmax(res)))[0]  # obtenemos la interpretación de la predicción
            diff_acc = ans - ans_hat_acc
            error_acc = np.dot(diff_acc, diff_acc) / len(diff_acc)  # calculamos el error para la accuracy
            if error_acc == 0.0:
                acierto = 1
            else:
                acierto = 0
            error_final += error
            accuracy += acierto
        error_final = error_final/len(test_x)
        accuracy = accuracy/len(test_x)
        return preds, error_final, accuracy








