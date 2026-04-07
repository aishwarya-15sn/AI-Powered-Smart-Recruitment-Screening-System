# RecruitAI – AI Recruitment Intelligence System

An NLP-based system that automatically analyzes resumes and ranks candidates
based on job descriptions using text similarity techniques.

## Features
- Resume text parsing and preprocessing
- Skill and keyword extraction from candidate resumes
- Candidate ranking based on similarity with job descriptions
- Automated screening support for recruiters

## Methods Used
- TF-IDF vectorization to represent resume and job description text
- Cosine similarity scoring to measure candidate-job relevance
- NLP preprocessing including tokenization and stop-word removal

## Tech Stack
Python, Scikit-learn, NLP (TF-IDF, Cosine Similarity)

## Project Structure
resume_parser.py     # Extracts and preprocesses resume text  
ranking_model.py     # Computes TF-IDF vectors and similarity scores  
main.py              # Runs the candidate ranking pipeline  

## Future Improvements
- Integration with real recruitment datasets
- Semantic matching using transformer-based embeddings
- Web interface for recruiter interaction
