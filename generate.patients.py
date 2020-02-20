#!/usr/bin/env python

import pandas as pd
import requests

people = requests.get('https://uinames.com/api/?amount=500&ext').json()

# flatten sub-dictionaries
for person in people:
    person['birthday'] = person['birthday']['mdy']
    person['credit_card'] = person['credit_card']['number']

pd.DataFrame(people)\
    .to_csv('patient-accounts.csv', index=False)
