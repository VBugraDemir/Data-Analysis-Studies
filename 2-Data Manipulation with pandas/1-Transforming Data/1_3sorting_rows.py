import pickle
import pandas as pd
# data serilerinde birden fazla column yazılamaz [[]] ile square bracket liste oluşturmak için

newfile = open("homeless_data.pkl","rb")
homelessness = pickle.load(newfile)
homelessness_ind = homelessness.sort_values("individuals")
print(homelessness_ind.head())
print()

homelessness_fam = homelessness.sort_values("family_members", ascending = False)
print(homelessness_fam.head())
print()

homelessness_rag_fam = homelessness.sort_values(["region", "family_members"],ascending = [True, False])
print(homelessness_rag_fam)

