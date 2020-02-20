# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import pandas as pd

patients = pd.read_csv('patient-accounts.csv')
patients.head()

# # Does drug x cause an age-dependent increase in patient paranoia?
#
# To answer this question we use a marker of paranoia, password length.

patients['paranoia'] = patients.password.str.len()
patients.paranoia.hist()

patients.age.hist()

patients.plot.scatter('age','paranoia')

patients.corr()

# # Results
#
# Nope, sorry.
#
# ![](https://media.ldscdn.org/images/media-library/book-of-mormon-seminary-curriculum-images/boy-sad-840560-mobile.jpg)

