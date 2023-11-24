import streamlit as st
import random

import numpy as np
import pandas as pd

st.markdown("""# This is a header
## This is a sub header
**This is text**
- this is a list""")

@st.cache
def random_df():
    df = pd.DataFrame({
        'first column': random.sample(range(1, 11), 10),
        'second column': np.arange(10, 101, 10)
        })
    return df

# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
line_count = st.slider('Select a line count', 1, 10, 3)

# and used to select the displayed lines
head_df = random_df().head(line_count)

st.write(head_df)
