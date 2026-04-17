import pandas as pd

# -------------------------------
# Helper function to standardize dataset
# -------------------------------
def process_dataset(df, text_col, label_col, label_map):
    # Rename columns
    df = df.rename(columns={
        text_col: "text",
        label_col: "label"
    })

    # Keep only required columns
    df = df[["text", "label"]]

    # Convert labels
    df["label"] = df["label"].map(label_map)

    return df


# -------------------------------
# Load datasets
# -------------------------------
print("Loading datasets...")

# Dataset 1: Spam dataset
d1 = pd.read_csv("spam.csv", encoding="latin-1")

d1 = process_dataset(
    d1,
    text_col="message",   # change if needed
    label_col="label",
    label_map={"spam": 1, "ham": 0}
)

# -------------------------------
# Dataset 2: Phishing emails
# -------------------------------
d2 = pd.read_csv("phishing.csv")

d2 = process_dataset(
    d2,
    text_col="email",     # change if needed
    label_col="type",
    label_map={"phishing": 1, "legitimate": 0}
)

# -------------------------------
# Dataset 3: Another email dataset
# -------------------------------
d3 = pd.read_csv("emails.csv")

d3 = process_dataset(
    d3,
    text_col="content",   # change if needed
    label_col="class",
    label_map={1: 1, 0: 0}
)

# -------------------------------
# Dataset 4 (Optional): Custom dataset
# -------------------------------
try:
    d4 = pd.read_csv("extra.csv")

    d4 = process_dataset(
        d4,
        text_col="text",
        label_col="label",
        label_map={"phishing": 1, "safe": 0}
    )

    datasets = [d1, d2, d3, d4]

except:
    datasets = [d1, d2, d3]

# -------------------------------
# Merge all datasets
# -------------------------------
print("Merging datasets...")

data = pd.concat(datasets, ignore_index=True)

# -------------------------------
# Cleaning
# -------------------------------

# Remove missing values
data = data.dropna()

# Remove duplicates
data = data.drop_duplicates()

# Shuffle data
data = data.sample(frac=1).reset_index(drop=True)

# -------------------------------
# Save final dataset
# -------------------------------
data.to_csv("dataset.csv", index=False)

print("✅ Final dataset created: dataset.csv")
print(f"Total rows: {len(data)}")
