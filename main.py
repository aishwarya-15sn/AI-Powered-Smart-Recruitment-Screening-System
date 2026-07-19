from resume_parser import load_resumes
from ranking_model import rank_resumes
from save_results import save_results
from feature_extraction import extract_skills

job_description="Looking for a Data Analyst with SQL, Excel, Power BI, Pandas and Tableau."
resumes=load_resumes()
job_skills=extract_skills(job_description)
job_description=" ".join(job_skills)

ranked_resumes=rank_resumes(job_description,resumes)

save_results(ranked_resumes)

print("Top 10 Candidates\n")

for i in range(10):
    print(f"Rank {i+1}")
    print("Resume ID:",ranked_resumes[i]["id"])
    print("Category:",ranked_resumes[i]["category"])
    print("Score:",ranked_resumes[i]["score"])
    print("Skills:",", ".join(ranked_resumes[i]["skills"]))
    print("-"*30)