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
100%|███████████████████████████████████████████████████████████████████████| 60000/60000 [00:45<00:00, 1306.48it/s]
[Epoch 1] loss = 20.281030072144137
100%|███████████████████████████████████████████████████████████████████████| 60000/60000 [00:51<00:00, 1164.10it/s]
[Epoch 2] loss = 20.277578947741596

...

Output is too large... 
```

## Testing

- The regression model was tested to predict the labels of the given test data.

### Plot

![Confusion Matrix](Figure_1_lab8.png)

### Results

- Accuracy: 0.9783041401273885



