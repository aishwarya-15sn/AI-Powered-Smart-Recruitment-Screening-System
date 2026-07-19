from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rank_resumes(job_description,resumes):
    documents=[job_description]

    for resume in resumes:
        skills=" ".join(resume["skills"])
        documents.append(skills)

    vectorizer=TfidfVectorizer()
    tfidf_matrix=vectorizer.fit_transform(documents)

    job_vector=tfidf_matrix[0]
    resume_vectors=tfidf_matrix[1:]
    similarity_scores=cosine_similarity(job_vector,resume_vectors)
    ranked_resumes=[]

    for i in range(len(resumes)):
        resume=resumes[i]
        score=round(similarity_scores[0][i]*100,2)
        ranked_resumes.append({
            "id":resume["id"],
            "category":resume["category"],
            "score":score,
            "skills":resume["skills"]
        })
    ranked_resumes.sort(key=lambda x:x["score"],reverse=True)
    return ranked_resumes