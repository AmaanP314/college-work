### 1. **Library Install**

If you don’t have Pandas installed, you can install it via pip:

```bash
pip install pandas
```

### 2. **Object Creation**

You can create a Pandas DataFrame from a dictionary (as an example):

```python
import pandas as pd

# Creating an example DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, None],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}

df = pd.DataFrame(data)
print(df)
```

### 3. **Import File**

You can import a CSV file by specifying the file path:

```python
df = pd.read_csv('your_file_path.csv')
print(df)
```

### 4. **Read CSV File**

Read the CSV file into a DataFrame, using the `read_csv` method:

```python
# Assuming you have a CSV file at 'your_file_path.csv'
df = pd.read_csv('your_file_path.csv')
print(df.head())  # Shows first 5 rows by default
```

### 5. **Understand the CSV File**

You can use various functions to understand the structure of the CSV file:

```python
# Show first 5 rows of the DataFrame
print(df.head())

# Show summary of DataFrame
print(df.info())

# Show basic statistics about numerical columns
print(df.describe())
```

### 6. **Handling Missing Values**

You can handle missing data by filling or dropping them:

#### Drop rows with missing values:

```python
df.dropna(inplace=True)
```

#### Fill missing values with a specific value (e.g., mean of the column):

```python
df['Age'].fillna(df['Age'].mean(), inplace=True)
```

### 7. **Read 1st & Last 5 Lines**

To read the first row and last 5 rows:

```python
# First row (index 0)
print(df.iloc[0])

# Last 5 rows
print(df.tail())
```

### 8. **Identify Duplicate Data**

To identify duplicate rows:

```python
duplicates = df[df.duplicated()]
print(duplicates)

# To drop duplicates
df.drop_duplicates(inplace=True)
```

### 9. **Find Null Values**

To find rows with missing values:

```python
# Check for null values in each column
print(df.isnull().sum())

# Find rows with any null values
print(df[df.isnull().any(axis=1)])
```

---
