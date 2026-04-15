import sys
import os

# FIX IMPORT PATH (VERY IMPORTANT)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import plotly.graph_objects as go

from src.data_loader import load_data
from src.preprocessing import preprocess
from src.features import add_features
from src.anomaly import detect_anomalies
from src.forecast import forecast
from src.satellite_ingestion import load_satellite_data
from src.data_merge import merge_data

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Climate Intelligence System", layout="wide")

st.title("🌍 Climate Intelligence System")

# ---------------- LOAD DATA ----------------
df = load_data()
df = preprocess(df)

# ---------------- LOAD SATELLITE DATA ----------------
sat_df = load_satellite_data(df['date'])

# ---------------- MERGE DATA ----------------
df = merge_data(df, sat_df)

# ---------------- FEATURE ENGINEERING ----------------
df = add_features(df)

# REMOVE ALL NULLS (IMPORTANT FIX)
df = df.dropna()

# ---------------- ANOMALY DETECTION ----------------
df = detect_anomalies(df)

# ---------------- FORECAST ----------------
pred = forecast(df)

# ====================================================
# 📊 KPI SECTION
# ====================================================
st.subheader("📊 Key Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Avg Temp (°C)", round(df['temperature'].mean(), 2))
col2.metric("Max Temp (°C)", round(df['temperature'].max(), 2))
col3.metric("Anomalies", int(df['anomaly'].sum()))
col4.metric("Avg NDVI", round(df['NDVI'].mean(), 2))

# ====================================================
# 📈 TEMPERATURE TREND
# ====================================================
st.subheader("📈 Temperature Trend")

fig1 = go.Figure()

fig1.add_trace(go.Scatter(
    y=df['temperature'],
    name="Temperature",
    line=dict(color="blue")
))

fig1.add_trace(go.Scatter(
    y=df['rolling_mean'],
    name="Trend",
    line=dict(color="orange")
))

st.plotly_chart(fig1, use_container_width=True)

# ====================================================
# ⚠️ ANOMALY DETECTION
# ====================================================
st.subheader("⚠️ Anomaly Detection")

fig2 = go.Figure()

fig2.add_trace(go.Scatter(
    y=df['temperature'],
    name="Temperature"
))

anomalies = df[df['anomaly'] == 1]

fig2.add_trace(go.Scatter(
    x=anomalies.index,
    y=anomalies['temperature'],
    mode='markers',
    name="Anomalies",
    marker=dict(color='red', size=8)
))

st.plotly_chart(fig2, use_container_width=True)

# ====================================================
# 🛰 SATELLITE DATA
# ====================================================
st.subheader("🛰 Satellite Climate View")

fig3 = go.Figure()

fig3.add_trace(go.Scatter(
    y=df['NDVI'],
    name="NDVI (Vegetation)",
    line=dict(color="green")
))

fig3.add_trace(go.Scatter(
    y=df['LST'],
    name="Land Surface Temp",
    line=dict(color="red")
))

st.plotly_chart(fig3, use_container_width=True)

# ====================================================
# 🔮 FORECASTING
# ====================================================
st.subheader("🔮 Climate Forecast (Next 30 Days)")

fig4 = go.Figure()

fig4.add_trace(go.Scatter(
    y=df['temperature'],
    name="Historical"
))

fig4.add_trace(go.Scatter(
    y=pred,
    name="Forecast",
    line=dict(color="purple")
))

st.plotly_chart(fig4, use_container_width=True)

# ====================================================
# 📥 EXPORT
# ====================================================
df.to_csv("outputs/climate_report.csv", index=False)

st.success("✅ Dashboard Loaded Successfully | Report saved in outputs/")