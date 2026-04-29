ast.set_page_config(page_title="Aviation Risk Predictor")

st.title("✈️ Aviation Risk Predictor")

st.write("This app predicts aviation risk level (Demo version)")

altitude = st.number_input("Enter altitude (feet)")
weather = st.selectbox("Weather condition", ["Clear", "Cloudy", "Storm"])

if st.button("Predict Risk"):
if altitude > 30000 and weather == "Storm":
st.error("High Risk ✈️⚠")
elif altitude > 20000:
st.warning("Medium Risk ⚠")
else:
st.success("Low Risk ✅")
