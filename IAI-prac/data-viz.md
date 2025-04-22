### 1. **Import Data Visualization Object**

To visualize data using Pandas, you’ll often need **Matplotlib** or **Seaborn**.

First, ensure you have them installed:

```bash
pip install matplotlib seaborn
```

Now, import the libraries:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

For example, to plot a simple graph of `Age` from a DataFrame `df`:

```python
# Plot a histogram of the 'Age' column
df['Age'].plot(kind='hist', bins=10, color='blue', alpha=0.7)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.show()
```

### 2. **Inserting and Deleting Columns in Data Structures**

#### Inserting a Column:

```python
# Insert a new column 'Salary' with some values
df['Salary'] = [50000, 60000, 55000, 45000, 48000]
print(df)

# Insert a column at a specific position (e.g., after 'Age' column)
df.insert(2, 'Experience', [3, 5, 2, 8, 4])
print(df)
```

#### Deleting a Column:

```python
# Drop a column by its name
df.drop(columns=['Salary'], inplace=True)
print(df)
```

### 3. **Merging and Joining Data Sets**

Merging combines DataFrames based on a key, while joining can be done directly on the index.

#### Merging:

```python
# Creating another DataFrame for merging
df2 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Department': ['HR', 'Engineering', 'Marketing', 'Sales', 'IT']
})

# Merging on the 'Name' column
merged_df = pd.merge(df, df2, on='Name', how='inner')
print(merged_df)
```

#### Joining:

```python
# Set 'Name' as the index in both DataFrames
df.set_index('Name', inplace=True)
df2.set_index('Name', inplace=True)

# Join DataFrames based on the index
joined_df = df.join(df2)
print(joined_df)
```

### 4. **Reshaping and Pivoting Data Sets**

#### Reshaping with `melt` (wide to long format):

```python
# Sample DataFrame to reshape
df_wide = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Math': [90, 85, 88],
    'Science': [92, 89, 95]
})

# Reshape from wide to long format
df_long = pd.melt(df_wide, id_vars=['Name'], value_vars=['Math', 'Science'], var_name='Subject', value_name='Score')
print(df_long)
```

#### Pivoting (long to wide format):

```python
# Pivot the long format back to wide format
df_pivoted = df_long.pivot(index='Name', columns='Subject', values='Score')
print(df_pivoted)
```

### 5. **Aligning Data and Dealing with Missing Data**

Aligning data is typically useful when you are performing operations on DataFrames with different indices.

#### Align DataFrames (matching index values):

```python
# Create another DataFrame with different index
df3 = pd.DataFrame({
    'Math': [75, 88, 92],
    'Science': [85, 90, 95]
}, index=['Alice', 'Bob', 'Charlie'])

# Align both DataFrames on their indices
aligned_df, aligned_df3 = df.align(df3, join='inner', axis=0)
print(aligned_df)
```

#### Handling Missing Data (fill or drop):

```python
# Fill missing values in 'Age' column with a default value
df['Age'].fillna(30, inplace=True)

# Or drop rows with any missing values
df.dropna(axis=0, inplace=True)

print(df)
```

### 6. **Manipulating Data Using Integrated Indexing for DataFrame Objects**

#### Using `.loc` and `.iloc` for Indexing:

```python
# Use .loc to access data by index labels
print(df.loc[0])  # First row based on label

# Use .iloc to access data by position
print(df.iloc[2])  # Third row by position

# Access specific value
print(df.loc[1, 'Age'])  # Get 'Age' for 'Bob'
```

#### Setting and Resetting Index:

```python
# Set 'Name' as index
df.set_index('Name', inplace=True)
print(df)

# Reset index to default integer-based index
df.reset_index(inplace=True)
print(df)
```

### 7. **Performing Split-Apply-Combine on Data Sets Using the GroupBy Engine**

The `groupby()` function in Pandas allows you to group data, apply some operation, and then combine the results.

#### Example - Grouping by 'Department' and calculating average age:

```python
# Create a DataFrame with departments
df3 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'Department': ['HR', 'Engineering', 'Engineering', 'Sales', 'HR']
})

# Group by 'Department' and calculate average age
grouped = df3.groupby('Department')['Age'].mean()
print(grouped)
```

#### Example - Grouping and applying multiple functions:

```python
# Apply multiple functions on 'Age' grouped by 'Department'
grouped_multiple = df3.groupby('Department').agg({
    'Age': ['mean', 'min', 'max']
})
print(grouped_multiple)
```
