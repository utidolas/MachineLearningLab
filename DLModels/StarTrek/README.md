# How to Run
deploy in development ~ 

# Evaluation

## Custom model
### Classification Report

| Class           | Precision | Recall | F1-score | Support |
|-----------------|-----------|--------|----------|---------|
| commandRed      | 0.83      | 0.88   | 0.85     | 60      |
| operationGold   | 0.95      | 0.95   | 0.95     | 43      |
| scienceBlue     | 0.88      | 0.81   | 0.85     | 54      |

**Accuracy:** 0.88 (157 samples)

| Average Type   | Precision | Recall | F1-score | Support |
|---------------|-----------|--------|----------|---------|
| Macro Avg     | 0.89      | 0.88   | 0.88     | 157     |
| Weighted Avg  | 0.88      | 0.88   | 0.88     | 157     |


### Confusion Matrix
![alt text](imgs/customModelEval.png)
### Acc/Loss curve
![alt text](imgs/customModelEval2.png)

*****

## MobileNetV2
### Classification Report

| Class           | Precision | Recall | F1-score | Support |
|-----------------|-----------|--------|----------|---------|
| commandRed      | 0.69      | 0.83   | 0.76     | 60      |
| operationGold   | 0.85      | 0.91   | 0.88     | 43      |
| scienceBlue     | 0.77      | 0.56   | 0.65     | 54      |

**Accuracy:** 0.76 (157 samples)

| Average Type   | Precision | Recall | F1-score | Support |
|---------------|-----------|--------|----------|---------|
| Macro Avg     | 0.77      | 0.77   | 0.76     | 157     |
| Weighted Avg  | 0.76      | 0.76   | 0.75     | 157     |


### Confusion Matrix
![alt text](imgs/mobNetEval.png)
### Acc/Loss Curve
![alt text](imgs/mobNetEval2.png)
***

## EfficientNetB0
### Classification Report


| Class           | Precision | Recall | F1-score | Support |
|-----------------|-----------|--------|----------|---------|
| commandRed      | 0.79      | 0.83   | 0.81     | 60      |
| operationGold   | 0.82      | 0.95   | 0.88     | 43      |
| scienceBlue     | 0.84      | 0.69   | 0.76     | 54      |

**Accuracy:** 0.82 (157 samples)

| Average Type   | Precision | Recall | F1-score | Support |
|---------------|-----------|--------|----------|---------|
| Macro Avg     | 0.82      | 0.82   | 0.82     | 157     |
| Weighted Avg  | 0.82      | 0.82   | 0.81     | 157     |


### Confusion Matrix
![alt text](imgs/effNetEval.png)
### Acc/Loss Curve
![alt text](imgs/effNetEval2.png)

# Validation
## K-foll Cross validation
### K-Fold Cross-Validation Results (k=5)

| Model           | Mean Accuracy  | Std Dev | 
|-----------------|-----------|--------|
| **Custom CNN**      | 85.90%       | ± 1.69%   | 
| **MobileNetV2**  | 75.73%      | ± 2.07%   | 
| **EfficientNetB0**     | 83.99%      | ± 4.87%   | 