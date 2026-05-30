import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from pathlib import Path

# Load dataset (resolve path relative to this script, with cwd fallback)
here = Path(__file__).resolve().parent
candidates = [here / "sales_data_sample.csv", Path("sales_data_sample.csv")]
for p in candidates:
	if p.exists():
		csv_path = p
		break
else:
	raise FileNotFoundError(
		f"sales_data_sample.csv not found in {here!s} or current working directory ({Path.cwd()!s})"
	)

df = pd.read_csv(csv_path, encoding="latin1")

# Show first 5 rows
print(df.head())
#Dataset information

print("\nDataset Information:")
print(df.info())

# Check missing values

print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()
print("\nDuplicates removed successfully.")

# Handle missing values

df = df.fillna(0)
print("\nMissing values handled.")

# Input feature
X = df[["QUANTITYORDERED"]]

# Target/output

y = df["SALES"]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = LinearRegression()

model.fit(X_train, y_train)

print("\nModel trained successfully.")

predictions = model.predict(X_test)

print("\nFirst 5 Predictions:")
print(predictions[:5])

score = r2_score(y_test, predictions)

print("\nModel Accuracy:", score)

comparison = pd.DataFrame({"Actual Sales": y_test.values,"Predicted Sales": predictions})

print("\nPrediction Comparison:")
print(comparison.head())
comparison.to_csv("prediction_report.csv", index=False)
print("\nPrediction report saved successfully.")

future_quantity = [[50]]
future_prediction = model.predict(future_quantity)
print("\nPredicted Sales for Quantity 50:")
print(future_prediction)

plt.figure(figsize=(10, 6))
plt.scatter(X_test,y_test,label="Actual Sales")

plt.plot(X_test,predictions,linewidth=2,label="Predicted Trend")
plt.title("Predictive Analytics - Sales Forecasting")
plt.xlabel("Quantity Ordered")
plt.ylabel("Sales")
plt.legend()
plt.tight_layout()
plt.savefig("sales_prediction.png")
print("\nPrediction graph saved successfully.")
plt.show()
