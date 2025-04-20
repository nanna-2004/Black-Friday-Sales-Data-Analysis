# 🛍️ Black Friday Sales Analysis (EDA Project)

This project presents an **Exploratory Data Analysis (EDA)** on the Black Friday dataset, aimed at uncovering customer purchasing behavior based on demographics and other features. This type of analysis is commonly used in market segmentation and recommendation system pipelines.

## 📁 Dataset Information

- **Rows**: ~550,000  
- **Columns**: 12 (after preprocessing)
- **Features**:
  - 'User_ID`, `Product_ID`
  - 'Gender', 'Age`, `Occupation`, `City_Category`
  - 'Stay_In_Current_City_Years`, `Marital_Status`
  - 'Product_Category_1`, `Purchase` *(target variable)*

## 🔍 Objective

To understand:
- Demographic trends in purchasing
- Spending behavior across different age groups, cities, genders, and occupations
- Popular product categories
- Correlation between numerical variables

## 🛠️ Tools & Libraries Used

- Python
- Pandas
- Matplotlib
- Seaborn

## 📊 Key Visualizations

- **Pie Charts**: Gender & Marital Status Distribution
- **Bar Charts**: Age-wise, Gender-wise, Occupation-wise purchases
- **Box Plot**: Purchase distribution by Age
- **Correlation Heatmap**: Relationship between numerical features

## 🧼 Data Cleaning

- Dropped 'Product_Category_2` and `Product_Category_3` due to many nulls
- No imputation applied to focus purely on EDA
- Non-numeric columns excluded from correlation matrix
