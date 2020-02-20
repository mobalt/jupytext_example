# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.3.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
import pandas as pd

# %%
patients = pd.read_csv('patient-accounts.csv')
patients.head()

# %%
patients['paranoia'] = patients.password.str.len()
patients.paranoia.hist()

# %%
patients.age.hist()

# %%
patients.plot.scatter('age','paranoia')

# %%
patients.corr()

# %%
