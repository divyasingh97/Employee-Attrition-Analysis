cat > README.md << 'EOF'
# Employee Attrition Analysis

## Project Overview

Employee Attrition Analysis is a machine learning project that predicts whether an employee is likely to leave a company based on employee-related information.

The project includes data analysis, visualization, data preprocessing, machine learning model training, model evaluation, and a Streamlit web application for prediction.

## Objectives

- Analyze employee attrition patterns.
- Perform data cleaning and exploratory data analysis.
- Identify factors related to employee attrition.
- Train and compare multiple machine learning models.
- Evaluate models using Accuracy, Precision, Recall, and F1 Score.
- Build an interactive Streamlit application for employee attrition prediction.

## Dataset

The project uses the IBM HR Analytics Employee Attrition & Performance dataset available on Kaggle.

Dataset source:
https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset

The dataset contains 1,470 employee records and 35 columns.

The dataset is a sample/fictitious HR analytics dataset and does not represent real IBM employee records.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook
- Git & GitHub

## Machine Learning Models

The following classification models were trained and compared:

1. Logistic Regression
2. Decision Tree
3. Random Forest

## Model Results

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---:|---:|---:|---:|
| Logistic Regression | 74.49% | 33.33% | 59.57% | 42.75% |
| Decision Tree | 78.57% | 37.88% | 53.19% | 44.25% |
| Random Forest | 84.01% | 50.00% | 34.04% | 40.51% |

### Final Model

Random Forest was selected for the final Streamlit application because it achieved the highest accuracy of **84.01%**.

Logistic Regression achieved the highest recall of **59.57%**, while Decision Tree achieved the highest F1 score of **44.25%**.

## Project Structure

```text
Employee-Attrition-Analysis/
│
├── data/
│   └── WA_Fn-UseC_-HR-Employee-Attrition.csv
│
├── models/
│   └── employee_attrition_model.pkl
│
├── notebook/
│   └── employee_attrition_analysis.ipynb
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore