import streamlit as st
import pandas as pd 

# Sample data
data = {"name": ["asha", "rahul", "meera"], "score": [70, 80, 80]}
df = pd.DataFrame(data)

st.title("📊 Streamlit Data Display Examples")

# 1. Interactive dataframe (scrollable, sortable)
st.subheader("1. Interactive DataFrame")
st.dataframe(df)

# 2. Static table (non-editable, fixed)
st.subheader("2. Static Table")
st.table(df)

# 3. JSON format (structured data view)
st.subheader("3. JSON Format")
person ={"name": "asha","age":22,"skills":["python","ml","data science"]}

st.json(person)

# 4. Metrics (useful for single values / KPIs)
st.subheader("4. kpi Metrics")
st.metric(label="revenue",value="$1.2M",delta="+5%")
st.metric(label="users",value="350",delta="-10")
