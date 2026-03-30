from resume_parser import parse_resume
from feature_extraction import extract_skills
from ranking_model import rank_candidate

resume = "sample_resume.txt"

text = parse_resume(resume)
skills = extract_skills(text)
score = rank_candidate(skills)

print("Candidate Score:", score)
