import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('BlackFriday.csv')

# Drop unnecessary columns
df.drop(['Product_Category_2', 'Product_Category_3'], axis=1, inplace=True)

# Handle missing values if any
df.fillna({'Product_Category_1': df['Product_Category_1'].mode()[0]}, inplace=True)  # Filling missing Product Category with mode
df.fillna({'Age': df['Age'].mode()[0]}, inplace=True)  # Filling missing Age with mode
df.fillna({'Occupation': df['Occupation'].mode()[0]}, inplace=True)  # Filling missing Occupation with mode

# --- Basic Info ---
print("Shape:", df.shape)
print("Null values:\n", df.isnull().sum())

# --- Gender Distribution (Pie Chart) ---
plt.figure(figsize=(6,6))
df['Gender'].value_counts().plot.pie(autopct="%.1f%%", colors=['lightpink', 'lightblue'], title="Gender Distribution")
plt.ylabel('')
plt.show()

# --- Marital Status Distribution (Pie Chart) ---
plt.figure(figsize=(6,6))
df['Marital_Status'].value_counts().plot.pie(autopct='%.1f%%', colors=['gold', 'lightgreen'], title='Marital Status Distribution')
plt.ylabel('')
plt.show()

# --- Age Distribution (Bar Chart) ---
plt.figure(figsize=(10,6))
df['Age'].value_counts().sort_index().plot(kind='bar', color='lightcoral', title="Purchase Count by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Count")
plt.show()

# --- Purchase by Gender (Bar Chart) ---
df.groupby('Gender')['Purchase'].sum().plot(kind='bar', title='Total Purchase by Gender', color=['lightblue', 'pink'])
plt.ylabel("Total Purchase")
plt.show()

# --- Average Purchase by Gender (Bar Chart) ---
df.groupby('Gender')['Purchase'].mean().plot(kind='bar', title='Average Purchase by Gender', color=['purple', 'orange'])
plt.ylabel("Average Purchase")
plt.show()

# --- Purchase by Age (Bar Chart) ---
df.groupby('Age')['Purchase'].sum().plot(kind='bar', figsize=(10,6), title='Total Purchase by Age Group', color='lightgreen')
plt.ylabel("Total Purchase")
plt.show()

# --- Average Purchase by Age (Bar Chart) ---
df.groupby('Age')['Purchase'].mean().plot(kind='bar', figsize=(10,6), title='Average Purchase by Age Group', color='skyblue')
plt.ylabel("Average Purchase")
plt.show()

# --- Occupation vs Average Purchase (Bar Chart) ---
plt.figure(figsize=(12,6))
sns.barplot(data=df.groupby('Occupation')['Purchase'].mean().reset_index(), x='Occupation', y='Purchase', palette='magma')
plt.title("Average Purchase by Occupation")
plt.xlabel("Occupation")
plt.ylabel("Average Purchase")
plt.show()

# --- City Category vs Purchase (Bar Chart) ---
plt.figure(figsize=(8,6))
sns.barplot(data=df.groupby('City_Category')['Purchase'].mean().reset_index(), x='City_Category', y='Purchase', palette='Set2')
plt.title("Average Purchase by City Category")
plt.xlabel("City Category")
plt.ylabel("Average Purchase")
plt.show()

# --- Stay In Current City Years vs Purchase (Bar Chart) ---
plt.figure(figsize=(8,6))
sns.barplot(data=df.groupby('Stay_In_Current_City_Years')['Purchase'].mean().reset_index(), 
            x='Stay_In_Current_City_Years', y='Purchase', palette='Set3')
plt.title("Average Purchase by Stay Duration in City")
plt.xlabel("Stay in Current City Years")
plt.ylabel("Average Purchase")
plt.show()

# --- Product Category Distribution (Bar Chart) ---
plt.figure(figsize=(10,6))
df['Product_Category_1'].value_counts().sort_index().plot(kind='bar', color='lightseagreen', title="Product Category 1 Distribution")
plt.xlabel("Product Category 1")
plt.ylabel("Count")
plt.show()

# --- Correlation Heatmap (Correlation Matrix) ---
plt.figure(figsize=(10,8))
corr = df.select_dtypes(include='number').corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=1)
plt.title("Correlation Heatmap")
plt.show()


# --- Box Plot for Purchase by Age (Boxplot) ---
plt.figure(figsize=(10,6))
sns.boxplot(x='Age', y='Purchase', data=df, palette='Set1')
plt.title("Boxplot of Purchase by Age Group")
plt.show()
