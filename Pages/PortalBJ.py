import streamlit as st

if not st.session_state.authentication_status:
    st.info('Por favor, faça seu login na página Home.')
    st.stop()

# Títulos
st.title("Painel de Indicadores da EJ")

# Colunas para organização
col1, col2, col3 = st.columns(3)

# Indicadores da "EJ de Alto Crescimento"
with col1:
    st.subheader("EJ DE ALTO CRESCIMENTO")
    st.metric(label="Faturamento", value="12.5 mil", delta="114.60%")
    st.metric(label="Membros que executam", value="82.6%", delta="121.48%")

# Indicadores da "EJ Colaborativa"
with col2:
    st.subheader("EJ COLABORATIVA")
    st.metric(label="Membros colaborativos", value="65.2%", delta="10.9 mil")
    st.metric(label="Taxa de colaboração", value="66.7%", delta="26.66%")

# Indicadores da "EJ Inovadora"
with col3:
    st.subheader("EJ INOVADORA")
    st.metric(label="% de Membros minorizados", value="45%", delta="100%")
    st.metric(label="Nº de Soluções Inovadoras", value="1", delta="100%")
    st.metric(label="NPS", value="100", delta="125%")

# Estilo básico com barra de progresso
st.progress(100)  # Exemplo para uma barra de progresso
