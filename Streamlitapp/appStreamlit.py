
import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import altair as alt
from streamlit_echarts import st_echarts
import pyecharts.options as opts
from pyecharts.charts import Line
import pickle
from streamlit_echarts import st_echarts
import plotly.graph_objects as go
import plotly.express as px

path= "./app_data.csv"

app_data = pd.read_csv(path)
app_data=app_data.set_index("SK_ID_CURR")

with open('pad_pkl_model.pkl', 'rb') as f:
    pad_model = pickle.load(f)


features = ['EXT_SOURCE_2', 'PAYMENT_RATE', 'CODE_GENDER', "FLAG_OWN_CAR"]#,
      #"INSTAL_DBD_MEAN"]

# Define a function that accepts input data and returns a prediction
def predict(client_id):
    score = app_data.loc[int(client_id),"SCORE"]
    # Return the prediction as a response
    return round(100-score,2)

# Define the Streamlit app
def main():
    # Set the app title
    st.header(':red[PAD] bank loan scoring')
    # Add a text input for the user to enter input data
    client_id = st.text_input('client id')

  #score_button
    if st.button("SCORE"):
      SCORE = predict(client_id)
      st.write(f"Your score is: {SCORE}")
      st.dataframe(app_data.loc[int(client_id),features])

  #score gauge
      option = {
          "series": [
              {
                  "type": "gauge",
                  "startAngle": 180,
                  "endAngle": 0,
                  "min": 0,
                  "max": 100,
                  "center": ["50%", "80%"],
                  'radius':'120%',
                  "splitNumber": 5,
                  "axisLine": {
                      "lineStyle": {
                          "width": 6,
                          "color": [
                              [0.25, "#FF403F"],
                              [0.5, "#ffa500"],
                              [0.75, "#FDDD60"],
                              [1, "#64C88A"],
                          ],
                      }
                  },
                  "pointer": {
                      "icon": "path://M12.8,0.7l12,40.1H0.7L12.8,0.7z",
                      "length": "12%",
                      "width": 30,
                      "offsetCenter": [0, "-60%"],
                      "itemStyle": {"color": "auto"},
                  },
                  "axisTick": {"length": 10, "lineStyle": {"color": "auto", "width": 2}},
                  "splitLine": {"length": 15, "lineStyle": {"color": "auto", "width": 5}},
                  "axisLabel": {
                      "color": "#464646",
                      "fontSize": 12,
                      "distance": -60,
                  },
                  "title": {"offsetCenter": [0, "-20%"], "fontSize": 20},
                  "detail": {
                      "fontSize": 30,
                      "offsetCenter": [0, "0%"],
                      "valueAnimation": True,
                      "color": "auto",
                      "formatter": SCORE,
                  },
                  "data": [{"value": SCORE, "name": "Client score"}],
              }
          ]
      }

      st_echarts(option, width="450px", height="350px", key="gauge")

    #Important features scores
    if st.button("FEATURES"):
      tab1, tab2 = st.tabs(["📈 Features golbal", "Features detail"])
      with tab1:
        fig1 = go.Figure()
        # Create and style traces
        fig1.add_trace(go.Scatter(x=features, y=app_data.loc[:, features].mean().tolist(), name='MEAN',
                                line=dict(color='firebrick', width=4)))
        fig1.add_trace(go.Scatter(x=features, y=app_data.loc[:, features].max().tolist(),name='MAX',
                                line=dict(color='royalblue', width=4)))
        fig1.add_trace(go.Scatter(x=features, y=app_data.loc[:, features].min().tolist(),name='MIN',
                                line=dict(color='green', width=4))) # dash options include 'dash', 'dot', and 'dashdot'))

        # Edit the layout
        fig1.update_layout(title='Features score',
                          xaxis_title="Features",
                          yaxis_title='Values')
        #tab1.subheader("Features: Mean, Max, Min")
        st.plotly_chart(fig1)

      with tab2:
        fig2 = px.box(app_data.loc[:, features], x=features, color="CODE_GENDER", points="all")
        #tab2.subheader("Features: Details"))  
        st.plotly_chart(fig2)


if __name__ == '__main__':
    main()
