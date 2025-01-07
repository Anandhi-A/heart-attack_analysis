import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
import joblib

# Load dataset
df = pd.read_csv(r"C:\Users\anand\Downloads\heart_attack\heart.csv")

# Prepare features and target
X = df.drop('output', axis=1)
y = df['output']

# Create the pipeline
pipeline = Pipeline([
    ('poly', PolynomialFeatures(degree=2)),
    ('scaler', StandardScaler()),
    ('log_reg', LogisticRegression(max_iter=3000))
])

# Train the model
pipeline.fit(X, y)

# Save the trained model
joblib.dump(pipeline, 'heart_attack_model.pkl')
print("Model saved as heart_attack_model.pkl")
