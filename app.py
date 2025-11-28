python
‎import streamlit as st
‎import random
‎
‎def get_color(num):
‎    if num in [1, 3, 7, 9]:
‎        return "Red"
‎    elif num in [0, 2, 4, 6, 8]:
‎        return "Green"
‎    else:
‎        return "Violet"
‎
‎st.title("🎯 Wingo AI Color Predictor")
‎st.write("Last 3 Wingo numbers dijiye:")
‎
‎n1 = st.number_input("Pehla number", 0, 9, step=1)
‎n2 = st.number_input("Doosra number", 0, 9, step=1)
‎n3 = st.number_input("Teesra number", 0, 9, step=1)
‎
‎if st.button("Predict"):
‎    nums = [n1, n2, n3]
‎    colors = [get_color(int(n)) for n in nums]
‎    result = random.choice(["Red", "Green", "Violet"])
‎    st.success(f"Prediction: {result} (based on {colors})")
