# **Machine Learning Calculator**
## **Summary**
This is a machine learning calculator. On the surface, it may seem to function like a normal calculator. However, it does not actually calculate, but rather predicts what the answer is given the inputs. As a result, any input, especially ones the model was not trained to predict, can be fairly inaccurate.

## **Prerequisites**
- Tensorflow
- Keras
- NumPy

## **How to run**
- Install dependencies (I used a Miniconda env)
- Open and run ml_calculator.py

### **Program Design**
This program was made using Keras, a high-level API for Tensorflow. For each of the operations, I trained a separate model with the given constraints on the dataset:

NOTE: All numbers are integers

#### **Addition:** 
Two numbers between 0 and 1000.
#### **Subtraction:** 
First number between 1000 and 2000, second number between 0 and 1000 (To ensure that result is positive).
#### **Multiplication:** 
Two numbers between 0 and 10.
#### **Division:** 
This is a bit more complicated. Two numbers are chosen, number A between 1 and 10, number B between 1 and 100. For input, the dividend is A * B and the divisor is B. This is to ensure that the quotient is always at least 1, and that the dividend is always divisible by the divisor.

These constraints are mainly in place due to training accuracies being significantly better within these bounds.
