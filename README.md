### STEP 1: Create and activate an evironment

```
conda create -n winequality python=3.10 -y
```

```
conda activate requirements.txt
```

### Step 2: Create the project template

### Step 3: Create requirements.txt file and install dependencies

```
touch requirements.txt
```

```
pip install -r requirements.txt
```

### Step 3: Create the project template

```
touch template.py
```

### Step 4: Download the dataset

```
https://drive.google.com/drive/folders/1xw0XX-WK74uxtFFLySbtnX-ODdmdK5Ec
```

### Step 5: Intitalize Git and DVC

```
git init
```

```
dvc init
```

### Step 6: Add the dataset to DVC

```
dvc add data_given/winequality.csv
```

### Step 7: Add and Commit the Code with Git and remote repository

```
git add . && git commit -m "first commit"
```

```
git remote add origin https://github.com/AcheampongStephen/Wine-Quality.git
```

```
git branch -M main
```

```
git push origin main
```

### Step 8: Update the params.yaml

### Step 9: Update get_data.py

### Step 10: Update load_data.py

### Step 11: Update the load_data stages in dvc.yaml

### Step 12: Reproduce the load stage with dvc.yaml

```
dvc repro
```

### Step 13: Push the changes to the repository

```
git add . && git commit -m "Stage 1 completed" && git push origin main
```

### Step 14: Update split_data.py

### Step 15: Update the split_data stage in dvc.yaml

### Step 16: Reproduce the split data with dvc.yaml

```
dvc repro
```

### Step 17: Push the changes to the repository

```
git add . && git commit -m "Stage 2 completed" && git push origin main
```

### Step 18: Update train_and_evaluate_data.py

### Step 19: Update the strain_and_evaluate stage in dvc.yaml

### Step 20: Reproduce the train_and_evaluate with dvc.yaml

```
dvc repro
```

### Step 21: Push the changes to the repository

```
git add . && git commit -m "Stage 2 completed" && git push origin main
```

### Basic commands for experimentations

```
dvc metrics show
```

```
dvc metrics diff
```

### Step 22: Update test_config.py

```
you can run pytest -v to check if the test is correct.
However, you can also run it using tox.ini
```

### Step 23: Update tox.ini and run

```
tox

NB: tox -r ifrequirements are updated
```

### Step 24: Update setup.py to build the packages.

```
pip install -e .
```
