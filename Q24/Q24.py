import pandas as pd

# Read CSV file
df = pd.read_csv("titanic.csv")

print("===== Original Dataset =====")
print(df.head())

# Display dataset information
print("\n===== Dataset Information =====")
print(df.info())

# Check missing values
print("\n===== Missing Values =====")
print(df.isnull().sum())

# Fill missing Age with mean
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Fill missing Fare with mean
df["Fare"] = df["Fare"].fillna(df["Fare"].mean())

# Fill missing Embarked with mode
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Fill missing Cabin with Unknown
df["Cabin"] = df["Cabin"].fillna("Unknown")

# Remove duplicate rows
df = df.drop_duplicates()

print("\n===== Cleaned Dataset =====")
print(df.head())

# Check missing values again
print("\n===== Missing Values After Cleaning =====")
print(df.isnull().sum())

# Save cleaned dataset
df.to_csv("cleaned_titanic.csv", index=False)

print("\nCleaned dataset saved as cleaned_titanic.csv")