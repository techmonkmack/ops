python --version
git --version

cd ~
mkdir Student_ML_Project
cd Student_ML_Project
python -m venv .venv
source .venv/Scripts/activate
python -m pip install dvc scikit-learn pandas pyyaml
dvc --version

mkdir data
# create data/students.csv (version 1) and .gitignore (copy from lab3_dvc.txt)

git init
dvc init

dvc add data/students.csv
git add data/students.csv.dvc data/.gitignore .gitignore
git commit -m "Track student dataset"
git tag data-v1

# add 4 new rows to data/students.csv (version 2)
dvc add data/students.csv
git add data/students.csv.dvc
git commit -m "Dataset Version 2"
git tag data-v2

dvc diff data-v1 data-v2
git log --oneline

dvc remote add -d storage ../dvc-storage
dvc push
git add .dvc/config
git commit -m "Configure DVC remote"
dvc status

# create params.yaml, train.py and dvc.yaml (copy from lab3_dvc.txt)
dvc repro
git add .
git commit -m "Create reproducible pipeline"

dvc exp run -S model.max_depth=5
dvc exp show
dvc metrics show