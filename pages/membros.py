import streamlit as st
from streamlit_gsheets import GSheetsConnection  # type: ignore

# Authentication check
if not st.session_state.authentication_status:
    st.info('Por favor, faça login para acessar o sistema.')
    st.stop()

# Conecta ao Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)
# Adiciona uma barra lateral para selecionar a aba e o ano
anos = ["2024", "2025"]
ano_selecionado = st.sidebar.selectbox("Selecione o Ano", anos)
if st.sidebar.button('Atualizar Planilha'):
    st.sidebar.success("Planilha atualizada com sucesso!")
    st.cache_data.clear()
    st.rerun()

# Carrega os dados da aba e ano selecionados
df = conn.read(worksheet=f"{ano_selecionado}")

st.markdown("<h1 style='text-align: center;'>Dashboard de OKR</h1>",
            unsafe_allow_html=True)


# Layout de duas colunas
col1, col2 = st.columns(2)

# Título da página com o número total de membros
with col1:
    st.title("Membros da Empresa")

with col2:
    st.write(f"<div style='text-align: right;'>{len(df)
                                                } membros atuais</div>", unsafe_allow_html=True)


# Campo de busca
nome_pesquisa = st.text_input("Buscar membro")

# Filtrar membros com base na busca
# Filtrar membros com base na busca, ignorando a primeira linha (cabeçalho)
membros_filtrados = df[1:][df[1:][0].str.contains(
    nome_pesquisa, case=False, na=False)] if nome_pesquisa else df[1:]

# Exibir membros
for index, row in membros_filtrados.iterrows():
    st.subheader(row[0])
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.text(f'Email: {row[1]}')
    with col2:
        st.text(f'Telefone: {row[2]}')
    with col3:
        st.text(f'Diretoria: {row[3]}')
    with col4:
        st.text(f'Cargo: {row[4]}')
    st.write("---")
