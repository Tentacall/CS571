## LAB: 8
#### Team
- Sanskriti Singh [ 2001CS60 ]
- Rupak Biswas [ 2001CS57 ]
---
### How to run ?
```
python main.py
```
- Run above command in the terminal
- It will :
    - train the model
    - Statistics of the prediction on the test data

## Problem Statement:
- The MNIST dataset is a database of handwritten digits. The task is to classify the given handwritten digit into one of the 10 digits (0 to 9)
### Dataset
- mnist_train.csv contains 60,000 instances and mnist_test.csv contains 10,000 instances with 785 features including the label (the digit the input corresponds to). The original dataset contains the handwritten digits in image format (28x28). In the given dataset, the images are already flattened in a single row (that’s why each input will contain 784 features and one target digit that input
corresponds to)
### Task
Given the input data, the logistic regression classifier has to classify the given data into one of the digit (from 0 to 9)


## Analysis

### Logistic Regression

- hypothesis used is:
    - ![hypothesis](image.png)

- where: `g` is the sigmoid function
    - ![sigmoid](image-1.png)

### Training

We ran the model with `epochs = 100` and `lr = 0.001`.

```
100%|███████████████████████████████████████████████████████████████████████████████████████████| 10000/10000 [00:00<00:00, 21690.51it/s]
96/100, error=0.011125
100%|███████████████████████████████████████████████████████████████████████████████████████████| 10000/10000 [00:00<00:00, 21732.46it/s]
97/100, error=0.011105
100%|███████████████████████████████████████████████████████████████████████████████████████████| 10000/10000 [00:00<00:00, 21662.60it/s]
98/100, error=0.011086
100%|███████████████████████████████████████████████████████████████████████████████████████████| 10000/10000 [00:00<00:00, 21471.49it/s]
99/100, error=0.011067
100%|███████████████████████████████████████████████████████████████████████████████████████████| 10000/10000 [00:00<00:00, 21852.69it/s]
100/100, error=0.011048
Evaluating...
...

```

## Testing

- The regression model was tested to predict the labels of the given test data.

### Plot

![Confusion Matrix](confusion_matrix.png)

### Results

- Accuracy: 89.8%



