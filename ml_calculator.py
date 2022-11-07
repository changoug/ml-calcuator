from tensorflow.keras.models import load_model
import numpy as np
import os

if __name__ == '__main__':
    # Load the models
    model_add = load_model('./trained models/ml_add.h5')
    model_subtract = load_model('./trained models/ml_sub.h5')
    model_multiply = load_model('./trained models/ml_mult.h5')
    model_divide = load_model('./trained models/ml_div.h5')

    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    while True:
        num1 = input('Type first number: ')
        num2 = input('Type second number: ')
        operation = input('Type operation (+, -, *, /): ')
        np_arr = np.array([[int(num1), int(num2)]])

        if operation == '+':
            print('predicted result: ', round(model_add.predict(np_arr, verbose=0)[0][0]))
            print('actual result: ', int(num1) + int(num2))
        elif operation == '-':
            print('predicted result: ', round(model_subtract.predict(np_arr, verbose=0)[0][0]))
            print('actual result: ', int(num1) - int(num2))
        elif operation == '*':
            print('predicted result: ', round(model_multiply.predict(np_arr, verbose=0)[0][0]))
            print('actual result: ', int(num1) * int(num2))
        elif operation == '/':
            print('predicted result: ', round(model_divide.predict(np_arr, verbose=0)[0][0]))
            print('actual result: ', round(int(num1) / int(num2)))
