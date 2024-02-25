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

#### Add and Commit the Code with Git and remote repository

```
git add . && git commit -m "first commit"
```
