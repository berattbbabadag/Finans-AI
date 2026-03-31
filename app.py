import streamlit as st
import pandas as pd
from database import init_db, add_expense, get_expenses
from ai_agent import FinanceAgent

# Sayfa Ayarı
st.set_page_config(page_title="2026 Finans Asistanı", page_icon="💰")
init_db()
agent = FinanceAgent()

st.title("💰 AI Agent Finans Asistanı")

# Veri Girişi
with st.sidebar:
    st.header("Harcama Ekle")
    kategori = st.selectbox("Kategori", ["Gıda", "Ulaşım", "Eğlence", "Kira", "Diğer"])
    miktar = st.number_input("Miktar (TL)", min_value=0.0)
    not_ekle = st.text_input("Not")
    if st.button("Kaydet"):
        add_expense(kategori, miktar, not_ekle)
        st.success("Kaydedildi!")

# Harcamaları Listele
data = get_expenses()
if data:
    df = pd.DataFrame(data, columns=["ID", "Kategori", "Miktar", "Not", "Tarih"])
    st.subheader("Harcama Geçmişi")
    st.dataframe(df)

    # AI Analiz Butonu
    if st.button("AI Asistanına Sor"):
        summary = df.groupby("Kategori")["Miktar"].sum().to_string()
        with st.spinner("Agent analiz ediyor..."):
            advice = agent.analyze_spending(summary)
            st.info(advice)
else:
    st.write("Henüz harcama eklenmemiş.")