# Titanic Data Cleaning and Preprocessing

Is project mein Titanic dataset ko clean aur preprocess kiya gaya hai. 

Steps followed:
- Dataset load kiya
- Missing values ko median/mode se fill kiya
- Cabin column ko drop kiya kyunki usme bahut missing data tha
- Duplicate records ko remove kiya
- Categorical variables (Sex, Embarked) ko one-hot encoding se numerical banaya
- Age aur Fare columns ko standardize kiya
- Fare column ke outliers ko detect aur remove kiya
- Final cleaned data ko CSV file mein save kiya
