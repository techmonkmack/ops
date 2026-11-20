import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Step 1: Data Collection
data = {
    'Hours': [2, 4, 6, 8, 3, 7],
    'Marks': [30, 45, 65, 80, 35, 75],
    'Pass': [0, 0, 1, 1, 0, 1]
}
df = pd.DataFrame(data)
print("Original Data:")
print(df)

# Step 2: Data Preprocessing
df = df.fillna(0)

# Step 3: Feature Engineering
df['Total'] = df['Hours'] + df['Marks']

# Step 4: Data Validation
print("\nMissing Values:")
print(df.isnull().sum())

# Step 5: Separate Input and Output
X = df[['Hours', 'Marks', 'Total']]
y = df['Pass']

# Step 6: Pipeline Design
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression())
])

# Step 7: Execute Pipeline
pipeline.fit(X, y)

# Step 8: Prediction
prediction = pipeline.predict(
    pd.DataFrame({
        'Hours': [5],
        'Marks': [60],
        'Total': [65]
    })
)
print("\nPrediction:", prediction[0])
print("Pipeline Executed Successfully")