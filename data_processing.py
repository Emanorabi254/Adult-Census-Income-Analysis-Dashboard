import os
import pandas as pd
import kagglehub

def get_cleaned_data():
    # Load Dataset
    path = kagglehub.dataset_download("uciml/adult-census-income")
    files = os.listdir(path)
    csv_file = [f for f in files if f.endswith(".csv")][0]
    df = pd.read_csv(os.path.join(path, csv_file))

    # Data Cleaning
    df = df.replace("?", "Unknown")
    data = df.copy()

    # Feature Engineering (Helper Functions)
    def group_education(level):
        if level in ['Preschool','1st-4th','5th-6th','7th-8th','9th','10th','11th','12th']:
            return 'Pre-Secondary'
        elif level == 'HS-grad':
            return 'Secondary-Grad'
        elif level in ['Some-college','Assoc-acdm','Assoc-voc']:
            return 'Higher-Ed'
        elif level == 'Bachelors':
            return 'Bachelors'
        elif level in ['Masters','Prof-school','Doctorate']:
            return 'Post-Grad'
        return 'Other'

    data["education_level"] = data["education"].apply(group_education)

    # ---- Age Range ----
    data["age_range"] = pd.cut(
        data["age"],
        bins=[16,25,45,65,90],
        labels=["Young","Adult","Middle-Aged","Senior"]
    )

    # ---- Work Intensity ----
    data["work_intensity"] = pd.cut(
        data["hours.per.week"],
        bins=[0,35,45,100],
        labels=["Part-Time","Full-Time","Over-Time"]
    )

    # ---- Native Country ----
    data["native"] = data["native.country"].apply(
        lambda x: "US" if x == "United-States" else "Non-US"
    )

    # ---- Marital Status ----
    data["marital_status"] = data["marital.status"].replace({
        "Married-civ-spouse":"Married",
        "Married-AF-spouse":"Married",
        "Divorced":"Previously-Married",
        "Separated":"Previously-Married",
        "Widowed":"Previously-Married",
        "Married-spouse-absent":"Previously-Married",
        "Never-married":"Single"
    })

    # ---- Occupation Grouping ----
    def group_occupation(occ):
        if occ in ['Exec-managerial','Prof-specialty']:
            return 'White-Collar'
        elif occ in ['Craft-repair','Farming-fishing','Machine-op-inspct','Transport-moving','Handlers-cleaners']:
            return 'Blue-Collar'
        elif occ in ['Sales','Tech-support','Protective-serv','Priv-house-serv','Other-service']:
            return 'Service'
        return 'Unknown'

    data["occupation_grouped"] = data["occupation"].apply(group_occupation)

    # ---- Relationship Grouping ----
    data["relationship_group"] = data["relationship"].replace({
        "Husband": "In-Relationship",
        "Wife": "In-Relationship",
        "Own-child": "Family",
        "Not-in-family": "Independent",
        "Other-relative": "Family",
        "Unmarried": "Independent"
    })

    # ---- Income Numeric ----
    data["income_numeric"] = data["income"].apply(lambda x: 1 if x == ">50K" else 0)

    # ---- Race Grouping ----
    data["race"] = data["race"].replace({
        "Amer-Indian-Eskimo": "Other",
        "Asian-Pac-Islander": "Asian"
    })
    return data