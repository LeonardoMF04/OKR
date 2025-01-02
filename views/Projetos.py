import streamlit as st
from streamlit_gsheets import GSheetsConnection  # type: ignore

# Check authentication status
if not st.session_state.authentication_status:
    st.info('Por favor, faça seu login na página Home.')
    st.stop()

# Connect to Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)

# Sidebar for selecting the year tab
abas = ["Projetos 2024", "Projetos 2025"]
aba_selecionada = st.sidebar.selectbox("Selecione o ano", abas)

if st.sidebar.button('Atualizar Planilha'):
    st.sidebar.success("Planilha atualizada com sucesso!")
    st.cache_data.clear()
    st.rerun()

# Load data from the selected tab
df = conn.read(worksheet=aba_selecionada)

# Create a summarized dataframe with selected columns
colunas_desejadas = ["Empresa", "Data de início",
                     "Data de término", "Status", "Valor do projeto"]
df_resumido = df.iloc[1:, [df.columns.get_loc(
    col) for col in colunas_desejadas]]


# Display the summarized data table
st.dataframe(df_resumido, use_container_width=True)


numero_ao_lado_meta = df.iloc[4][15]
numero_ao_lado_total = df.iloc[5][15]

# Calculate the progress towards the annual goal
meta_do_ano = float(str(numero_ao_lado_meta).replace(
    'R$', '').replace('.', '').replace(',', '.').strip())
total_obtido = float(str(numero_ao_lado_total).replace(
    'R$', '').replace('.', '').replace(',', '.').strip())
progresso_meta = (total_obtido / meta_do_ano) * 100

st.markdown("<h2 style='text-align: center;'>Progresso da Meta do Ano</h2>",
            unsafe_allow_html=True)
st.progress(min(progresso_meta, 100) / 100.0)

if progresso_meta > 100:
    st.markdown(f"<h3 style='text-align: center;'>{
                progresso_meta:.2f}% de sucesso (excedido)</h3>", unsafe_allow_html=True)
else:
    st.markdown(f"<h3 style='text-align: center;'>{
                progresso_meta:.2f}% de sucesso</h3>", unsafe_allow_html=True)
