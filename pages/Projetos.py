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
st.markdown(
    "<div style='text-align: right;'><a href='https://docs.google.com/spreadsheets/d/1Ne9jgW3gxdcp8GAy4XpMpp255NPM75FVbyIvGAAPLxE/edit?gid=1202155433#gid=1202155433' target='_blank'>Link para a planilha</a></div>",
    unsafe_allow_html=True
)

numero_ao_lado_meta = float(df.iloc[4][15])
numero_ao_lado_total = float(df.iloc[5][15])


progresso_meta = (numero_ao_lado_total / numero_ao_lado_meta) * 100
st.markdown("<h2 style='text-align: center;'>Progresso da Meta do Ano</h2>",
            unsafe_allow_html=True)
st.progress(min(progresso_meta, 100) / 100.0)

if progresso_meta > 100:
    st.markdown(f"<h3 style='text-align: center;'>{
                progresso_meta:.2f}% de sucesso (excedido)</h3>", unsafe_allow_html=True)
else:
    st.markdown(f"<h3 style='text-align: center;'>{
                progresso_meta:.2f}% de sucesso</h3>", unsafe_allow_html=True)
