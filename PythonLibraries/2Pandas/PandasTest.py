import os
from datetime import datetime
import pandas as pd # type: ignore

# -------------------------------------------------------------------
# SECTION 0 – Setup Output Folder, Auto-Create Subfolder per Run
# -------------------------------------------------------------------

base_folder = os.path.dirname(os.path.abspath(__file__))

# Main Output folder
output_folder = os.path.join(base_folder, "Output")
os.makedirs(output_folder, exist_ok=True)

# Create unique subfolder for this run
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
run_folder = os.path.join(output_folder, f"Run_{timestamp}")
os.makedirs(run_folder, exist_ok=True)

# Function to save CSV inside the new run folder
def save_csv(df, name):
    filename = f"{name}_{timestamp}.csv"
    path = os.path.join(run_folder, filename)
    df.to_csv(path, index=False)
    print(f"\nSaved CSV: {path}\n")



# -------------------------------------------------------------------
# SECTION 1 – Creating Series and DataFrames
# -------------------------------------------------------------------

print("\n1. Creating Series and DataFrames")
series = pd.Series([10, 20, 30, 40], name="Numbers")
print("\nSeries:")
print(series)

data = {
    "Name": ["John", "Sara", "Amit", "Riya"],
    "Age": [28, 24, 22, 32],
    "Salary": [50000, 60000, 45000, 75000],
    "Department": ["HR", "IT", "IT", "HR"]
}
df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)


# -------------------------------------------------------------------
# SECTION 2 – Inspecting Data
# -------------------------------------------------------------------

print("\n2. Inspecting Data")

print("\nHead():")
print(df.head())

print("\nTail():")
print(df.tail())

print("\nInfo():")
print(df.info())

print("\nDescribe():")
print(df.describe())


# -------------------------------------------------------------------
# SECTION 3 – Selecting Columns and Rows
# -------------------------------------------------------------------

print("\n3. Selecting Columns and Rows")

print("\nSelect 'Name' column:")
print(df["Name"])

print("\nSelect Name & Salary columns:")
print(df[["Name", "Salary"]])

print("\nSelect rows where Age > 25:")
print(df[df["Age"] > 25])

print("\nSelect first 2 rows:")
print(df.iloc[0:2])

print("\nSelect row with index 2:")
print(df.loc[2])


# -------------------------------------------------------------------
# SECTION 4 – Filtering Data
# -------------------------------------------------------------------

print("\n4. Filtering Data")

print("\nSalary > 50000")
print(df[df["Salary"] > 50000])

print("\nAge between 24 and 30")
print(df[(df["Age"] >= 24) & (df["Age"] <= 30)])


# -------------------------------------------------------------------
# SECTION 5 – Sorting Data
# -------------------------------------------------------------------

print("\n5. Sorting Data")

print("\nSort by Salary (ascending):")
print(df.sort_values("Salary"))

print("\nSort by Age (descending):")
print(df.sort_values("Age", ascending=False))


# -------------------------------------------------------------------
# SECTION 6 – Adding and Dropping Columns
# -------------------------------------------------------------------

print("\n6. Adding and Dropping Columns")

df["Tax"] = df["Salary"] * 0.10
print("\nAdded Tax column:")
print(df)

df = df.drop("Tax", axis=1)
print("\nDropped Tax column:")
print(df)


# -------------------------------------------------------------------
# SECTION 7 – Missing Values Handling
# -------------------------------------------------------------------

print("\n7. Missing Values Handling")

df2 = pd.DataFrame({
    "A": [1, None, 3],
    "B": [4, 5, None]
})

print("\nOriginal df2:")
print(df2)

print("\nFill missing values with 0:")
print(df2.fillna(0))

print("\nDrop rows with missing values:")
print(df2.dropna())


# -------------------------------------------------------------------
# SECTION 8 – Grouping and Aggregation
# -------------------------------------------------------------------

print("\n8. Grouping and Aggregation")

print("\nAverage Salary per Department:")
print(df.groupby("Department")["Salary"].mean())

print("\nCount of employees per Department:")
print(df.groupby("Department")["Name"].count())


# -------------------------------------------------------------------
# SECTION 9 – Merging, Joining & Concatenation
# -------------------------------------------------------------------

print("\n9. Merging, Joining & Concatenation")

dept_info = pd.DataFrame({
    "Department": ["HR", "IT"],
    "Location": ["Building A", "Building B"]
})

print("\nMerging df with department info:")
merged = pd.merge(df, dept_info, on="Department", how="left")
print(merged)

print("\nConcatenating two datasets:")
df3 = pd.DataFrame({"Name": ["Sam"], "Age": [29], "Salary": [65000], "Department": ["IT"]})
concat_df = pd.concat([df, df3], ignore_index=True)
print(concat_df)


# -------------------------------------------------------------------
# SECTION 10 – Removing Duplicates
# -------------------------------------------------------------------

print("\n10. Removing Duplicates")

df_dup = pd.DataFrame({"A": [1, 1, 2, 2, 3], "B": [10, 10, 20, 30, 30]})
print("\nOriginal df_dup:")
print(df_dup)

print("\nAfter dropping duplicates:")
print(df_dup.drop_duplicates())


# -------------------------------------------------------------------
# SECTION 11 – Value Counts
# -------------------------------------------------------------------

print("\n11. Value Counts")

print(df["Department"].value_counts())


# -------------------------------------------------------------------
# SECTION 12 – Applying Functions (apply, lambda)
# -------------------------------------------------------------------

print("\n12. Applying Functions (apply, lambda)")

df["Salary_Doubled"] = df["Salary"].apply(lambda x: x * 2)
print("\nSalary Doubled:")
print(df)


# -------------------------------------------------------------------
# SECTION 13 – Working With Dates
# -------------------------------------------------------------------

print("\n13. Working With Dates")

date_df = pd.DataFrame({
    "Event": ["A", "B", "C"],
    "Date": ["2024-01-01", "2024-02-15", "2024-03-10"]
})

date_df["Date"] = pd.to_datetime(date_df["Date"])
print(date_df)

print("\nExtract year:")
print(date_df["Date"].dt.year)


# -------------------------------------------------------------------
# SECTION 14 – Pivot Tables
# -------------------------------------------------------------------

print("\n14. Pivot Tables")

pivot = pd.pivot_table(df, values="Salary", index="Department", aggfunc="mean")
print("\nPivot Table (Avg Salary):")
print(pivot)


# -------------------------------------------------------------------
# SECTION 15 – Write Final DataFrames to Output Folder
# -------------------------------------------------------------------

save_csv(df, "final_dataframe")
save_csv(merged, "merged_data")
save_csv(concat_df, "concat_data")
save_csv(df_dup, "duplicates_example")
save_csv(date_df, "dates_example")

print("\nAll operations completed successfully.")
