import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
# Step 1:DataCollection 
data = {
'Student_ID': [1, 2, 3, 4, 5, 6],
'Hours': [2, 4, 6, 8, 3, 7],
'Attendance': [50, 65, 80, 95, 55, 90],
'Pass': [0, 0, 1, 1, 0, 1]
}
df = pd.DataFrame(data)
# Step 2:Create Feature Store 
feature_store = {}
# Step 3: Register and Store Features 
for i, row in df.iterrows():
   feature_store[row['Student_ID']] = [ 
row['Hours'], row['Attendance']
]
print("Feature Store:") 
print(feature_store)
# Step 4: Retrieve Features
print("\nFeatures of Student 1:") 
print(feature_store[1])
# Step 5: Offline Feature Retrieval 
X = df[['Hours', 'Attendance']]
y = df['Pass']
# Step 6: Reuse Features for Two Models
model1 = DecisionTreeClassifier(random_state=42) 
model1.fit(X, y)
model2 = LogisticRegression() 
model2.fit(X, y)
print("\nDecision Tree Model Trained")
print("Logistic Regression Model Trained")
# Step 7: Online Feature Retrieval 
student = pd.DataFrame(
[feature_store[1]],
columns=['Hours', 'Attendance']
)
print("\nPrediction using Decision Tree:", 
model1.predict(student))
print("Prediction using Logistic Regression:", 
model2.predict(student))