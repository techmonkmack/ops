import mlflow
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
X, y = load_iris(return_X_y=True)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Decision Tree
with mlflow.start_run(run_name="DecisionTree"):

    dt = DecisionTreeClassifier(max_depth=3)
    dt.fit(X_train, y_train)

    pred1 = dt.predict(X_test)
    acc1 = accuracy_score(y_test, pred1)

    mlflow.log_param("max_depth", 3)
    mlflow.log_metric("accuracy", acc1)

# Random Forest
with mlflow.start_run(run_name="RandomForest"):

    rf = RandomForestClassifier(n_estimators=100)
    rf.fit(X_train, y_train)

    pred2 = rf.predict(X_test)
    acc2 = accuracy_score(y_test, pred2)

    mlflow.log_param("n_estimators", 100)
    mlflow.log_metric("accuracy", acc2)

print("Decision Tree Accuracy =", acc1)
print("Random Forest Accuracy =", acc2)
if acc1 > acc2:
    print("Best Model : Decision Tree")
else:
    print("Best Model : Random Forest")