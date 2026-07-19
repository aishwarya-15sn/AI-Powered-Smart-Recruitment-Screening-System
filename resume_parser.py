import pandas as pd
from feature_extraction import extract_skills

def load_resumes():
    df=pd.read_csv("Resume.csv")
    resumes=[]
    for _,row in df.iterrows():
        text=str(row["Resume_str"])

        resume={
            "id":row["ID"],
            "category":row["Category"],
            "text":text,
            "skills":extract_skills(text)
        }
        resumes.append(resume)
    return resumes