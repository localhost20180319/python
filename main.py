import pandas as pd
from keywords import skill_keywords

df = pd.read_csv("data/job_data.csv")
skill_list = df["技能"].dropna().tolist()

all_skills=[]
for i in skill_list:
    skills_in_row = i.split(";")
    cleaned_skills = [skill.strip() for skill in skills_in_row ]
    all_skills.extend(cleaned_skills)

from collections import Counter
skill_counts = Counter(all_skills)


#print(skill_list.split(";"))
# print(df.head(15))
# print(df["技能"].head())
print(skill_counts)
