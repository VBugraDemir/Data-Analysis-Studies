from fuzzywuzzy import process

import numpy as np

unique = ['america', 'merican', 'amurican', 'americen', 'americann',
       'asiane', 'itali', 'asiann', 'murican', 'italien', 'italian',
       'asiat', 'american', 'americano', 'italiann', 'ameerican',
       'asianne', 'italiano', 'americin', 'ammericann', 'amerycan',
       'aamerican', 'ameriican', 'italiaan', 'asiian', 'asiaan',
       'amerrican', 'ameerrican', 'ammereican', 'asian', 'italianne',
       'italiian', 'itallian']
unique_types = np.array(unique)
print(process.extract("assian", unique_types, limit = len(unique_types)))
print(process.extract("american", unique_types, limit = len(unique_types)))
print(process.extract("italian", unique_types, limit = len(unique_types)))

# 80 as a cutoff values seems ok.
