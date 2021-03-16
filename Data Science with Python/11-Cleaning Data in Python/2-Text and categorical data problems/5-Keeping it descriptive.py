import pandas as pd
survey_response = pd.read_csv("story.txt",sep="\t",index_col=0)
survey_response.index.name = None

airlines = pd.read_csv("airlines_final.csv", index_col=0, chunksize=29)
airlines = next(airlines)

airlines = airlines.join(survey_response)

resp_len = airlines["survey_response"].str.len()
airlines_survey = airlines[resp_len > 40]
print(airlines_survey)
assert airlines_survey["survey_response"].str.len().min() > 40

print(airlines_survey)
print(airlines_survey[airlines_survey["survey_response"].str.contains("personnell|food")])