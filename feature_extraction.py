import re

skills_db=[
    "python",
    "java",
    "c",
    "c++",
    "sql",
    "mysql",
    "html",
    "css",
    "javascript",
    "react",
    "node.js",
    "django",
    "flask",
    "fastapi",
    "git",
    "github",
    "linux",
    "docker",
    "kubernetes",
    "aws",
    "azure",
    "machine learning",
    "deep learning",
    "nlp",
    "tensorflow",
    "pytorch",
    "scikit-learn",
    "pandas",
    "numpy",
    "matplotlib",
    "power bi",
    "excel",
    "tableau"
]

def extract_skills(text):
    text=text.lower()
    found_skills=[]

    for skill in skills_db:
        pattern=r"\b"+re.escape(skill)+r"\b"
        if re.search(pattern,text):
            found_skills.append(skill)

    return found_skills