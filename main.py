from datetime import datetime
from va_courts_tools import VaCourtsTool

import pandas as pd

sess = VaCourtsTool(debug=True)

result = sess.initialize()
if not result[0]:
    print(result)
    exit()

# result = sess.get_cases_for(courtIdx=0, date=datetime(2022, 1, 19))
result = sess.get_all_cases(_from=datetime(2022, 1, 18), _to=datetime(2022, 1, 20))
if not result[0]: exit()

df = pd.DataFrame(result[1])

df.to_csv('vacourt_data.csv')
