git --version
git config --global user.name "Your Name"
git config --global user.email "you@gmail.com"

mkdir ml_git_project
cd ml_git_project
# create train.py, README.md, requirements.txt (copy the file-creation lines from my last message)

git init
git status
git add .
git commit -m "Initial ML project"
git branch -M main
git log --oneline

git branch model-development
git checkout model-development
# change train.py to the Random Forest code
git add train.py
git commit -m "Added Random Forest model"

git checkout main
git merge model-development

git remote add origin https://github.com/YOUR-USERNAME/ml_git_project.git
git push -u origin main

# merge conflict demo
git checkout -b test-model
sed -i 's/^model = .*/model = RandomForestClassifier(n_estimators=100)/' train.py
git add .
git commit -m "Changed model to Random Forest"
git checkout main
sed -i 's/^model = .*/model = DecisionTreeClassifier()/' train.py
git add .
git commit -m "Changed model to Decision Tree"
git merge test-model
# conflict appears: fix train.py, keep one model line, delete the <<<<<<< ======= >>>>>>> lines
git add train.py
git commit -m "Resolved model merge conflict"

git log --oneline --graph