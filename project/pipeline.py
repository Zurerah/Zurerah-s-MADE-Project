# %% [markdown]
# # Import Library

# %%
import pandas as pd

# %% [markdown]
# # Load the Data

# %%
df = pd.read_csv('https://data.humdata.org/dataset/469a7757-302c-4176-bf82-4a4523feb586/resource/5419549c-8d27-497c-8a7a-9d849a86cbca/download/climate-change_deu.csv')
df

# %%
df = pd.read_csv('https://data.humdata.org/dataset/469a7757-302c-4176-bf82-4a4523feb586/resource/5419549c-8d27-497c-8a7a-9d849a86cbca/download/climate-change_deu.csv')
df

# %%
df.dropna()

# %%
df.to_csv("../data/output.csv")


