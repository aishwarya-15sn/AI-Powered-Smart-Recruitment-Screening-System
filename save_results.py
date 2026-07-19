import pandas as pd

def save_results(ranked_resumes):
    df=pd.DataFrame(ranked_resumes)
    df.to_csv("outputs/ranked_candidates.csv",index=False)
    print("\nResults saved to outputs/ranked_candidates.csv")