#!/usr/bin/env python
# coding: utf-8

# In[1]:


try:
 
    from enum import Enum
    from io import BytesIO, StringIO
    from typing import Union
 
    import pandas as pd
    import streamlit as st
except Exception as e:
    print(e)
 
STYLE = """
<style>
img {
    max-width: 100%;
}
</style>
"""
 
def main():
    """Run this function to display the Streamlit app"""
    st.info(__doc__)
    st.markdown(STYLE, unsafe_allow_html=True)
 
    file = st.file_uploader("Upload file", type=["csv"])
    show_file = st.empty()
 
    if not file:
        show_file.info("Please upload a file of type: " + ", ".join(["csv"]))
        return
 
    content = file.getvalue()
    else:
        data = pd.read_csv(file)
        st.dataframe(data.head(10))
    file.close()
 
main()


# In[ ]:




