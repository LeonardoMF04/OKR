import streamlit as st
import plotly.express as px
from streamlit_gsheets import GSheetsConnection  # type: ignore

if not st.session_state.authentication_status:
    st.info('Por favor, faça seu login na página Home.')
    st.stop()

# Conecta ao Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)
# Adiciona uma barra lateral para selecionar a aba
abas = ["Resumo OKR's 2024", "OKR 1", "OKR 2", "OKR 3", "OKR 4"]
aba_selecionada = st.sidebar.selectbox("Selecione a OKR", abas)

# Carrega os dados da aba selecionada
df = conn.read(worksheet=aba_selecionada)

st.markdown("<h1 style='text-align: center;'>Dashboard de OKR</h1>",
            unsafe_allow_html=True)

if st.sidebar.button('Atualizar Planilha'):
    st.sidebar.success("Planilha atualizada com sucesso!")
    st.cache_data.clear()
    st.rerun()

def plot_pie_chart(progresso, title, col, key):
    if progresso > 100:
        fig = px.pie(
            names=["Progresso", "Excedente"],
            values=[100, progresso - 100],
            title=title,
            width=300,
            height=300,
            color=["Progresso", "Excedente"],
            color_discrete_map={"Progresso": "green", "Excedente": "red"}
        )
    else:
        restante = 100 - progresso
        fig = px.pie(
            names=["Progresso", "Restante"],
            values=[progresso, restante],
            title=title,
            width=300,
            height=300,
            color=["Progresso", "Restante"],
            color_discrete_map={"Progresso": "green", "Restante": "gray"}
        )
    # Adiciona um 'key' único para evitar conflitos no Streamlit
    col.plotly_chart(fig, key=key)


if aba_selecionada in ["OKR 1", "OKR 2", "OKR 3", "OKR 4"]:
    # PARTE OKR GLOBAL
    # st.markdown("<h1 style='text-align: center;'>Global </h1>",
    # unsafe_allow_html=True)
    # PARTE DPRESS
    # st.markdown("<h1 style='text-align: center;'>Presidência</h1>",
    # unsafe_allow_html=True)
    df_dpres = df[3:21][0:22]
    df_dpres = df_dpres.reset_index(drop=True)
    df_dpres.set_index(df_dpres.columns[0], inplace=True)

    df_dpres_1 = df_dpres.iloc[0:6, 0:21]
    new_header1 = df_dpres_1.iloc[0]
    df_dpres_1 = df_dpres_1[1:]
    df_dpres_1.columns = new_header1

    df_dpres_2 = df_dpres.iloc[6:12, 0:21]
    new_header2 = df_dpres_2.iloc[0]
    df_dpres_2 = df_dpres_2[1:]
    df_dpres_2.columns = new_header2

    df_dpres_3 = df_dpres.iloc[12:18, 0:21]
    new_header3 = df_dpres_3.iloc[0]
    df_dpres_3 = df_dpres_3[1:]
    df_dpres_3.columns = new_header3

    col1, col2, col3 = st.columns(3)
    exibir_df_dpres_1 = col1.checkbox("Exibir Objetivo 1", value=False)
    exibir_df_dpres_2 = col2.checkbox("Exibir Objetivo 2", value=False)
    exibir_df_dpres_3 = col3.checkbox("Exibir Objetivo 3", value=False)

    if exibir_df_dpres_1:
        st.write("### Objetivo 1")
        st.write(df_dpres_1)

    if exibir_df_dpres_2:
        st.write("### Objetivo 2")
        st.write(df_dpres_2)

    if exibir_df_dpres_3:
        st.write("### Objetivo 3")
        st.write(df_dpres_3)

    col1, col2, col3 = st.columns(3)

    # Extração dos dados de progresso
    progresso1 = float(str(df_dpres_1.iloc[0]["Progresso do Objetivo"]).replace(
        '%', '').replace(',', '.')) * 100
    progresso2 = float(str(df_dpres_2.iloc[0]["Progresso do Objetivo"]).replace(
        '%', '').replace(',', '.')) * 100
    progresso3 = float(str(df_dpres_3.iloc[0]["Progresso do Objetivo"]).replace(
        '%', '').replace(',', '.')) * 100

    # Plotando os gráficos de progresso com chaves únicas
    plot_pie_chart(progresso1, "Progresso do Objetivo 1",
                   col1, key="objetivo_1_dpres")
    plot_pie_chart(progresso2, "Progresso do Objetivo 2",
                   col2, key="objetivo_2_dpres")
    plot_pie_chart(progresso3, "Progresso do Objetivo 3",
                   col3, key="objetivo_3_dpres")

    # Calcula a média dos progressos dos objetivos
    media_progresso_dp = (progresso1 + progresso2 + progresso3) / 3.0
    temp = media_progresso_dp
    if media_progresso_dp > 100:
        temp = media_progresso_dp
        media_progresso_dp = 100
    st.markdown("<h2 style='text-align: center;'>Média dos Progressos dos Objetivos</h2>",
                unsafe_allow_html=True)
    st.progress(media_progresso_dp / 100.0)
    st.markdown(
        f"<h3 style='text-align: center;'>{temp:.2f}% de sucesso</h3>", unsafe_allow_html=True)

    # PARTE VP
    st.markdown("<h1 style='text-align: center;'>Vice-Presidência</h1>",
                unsafe_allow_html=True)
    df_vp = df[23:41][0:22]
    df_vp = df_vp.reset_index(drop=True)
    df_vp.set_index(df_vp.columns[0], inplace=True)

    df_vp_1 = df_vp.iloc[0:6, 0:21]
    new_header1_vp = df_vp_1.iloc[0]
    df_vp_1 = df_vp_1[1:]
    df_vp_1.columns = new_header1_vp

    df_vp_2 = df_vp.iloc[6:12, 0:21]
    new_header2_vp = df_vp_2.iloc[0]
    df_vp_2 = df_vp_2[1:]
    df_vp_2.columns = new_header2_vp

    df_vp_3 = df_vp.iloc[12:22, 0:21]
    new_header3_vp = df_vp_3.iloc[0]
    df_vp_3 = df_vp_3[1:]
    df_vp_3.columns = new_header3_vp

    col1_vp, col2_vp, col3_vp = st.columns(3)
    exibir_df_vp_1 = col1_vp.checkbox(
        "Exibir Objetivo 1", value=False, key="vp_objetivo_1")
    exibir_df_vp_2 = col2_vp.checkbox(
        "Exibir Objetivo 2", value=False, key="vp_objetivo_2")
    exibir_df_vp_3 = col3_vp.checkbox(
        "Exibir Objetivo 3", value=False, key="vp_objetivo_3")

    if exibir_df_vp_1:
        st.write("### Objetivo 1")
        st.write(df_vp_1)

    if exibir_df_vp_2:
        st.write("### Objetivo 2")
        st.write(df_vp_2)

    if exibir_df_vp_3:
        st.write("### Objetivo 3")
        st.write(df_vp_3)

    col1_vp, col2_vp, col3_vp = st.columns(3)

    # Extração dos dados de progresso
    progresso1_vp = float(str(df_vp_1.iloc[0]["Progresso do Objetivo"]).replace(
        '%', '').replace(',', '.')) * 100
    progresso2_vp = float(str(df_vp_2.iloc[0]["Progresso do Objetivo"]).replace(
        '%', '').replace(',', '.')) * 100
    progresso3_vp = float(str(df_vp_3.iloc[0]["Progresso do Objetivo"]).replace(
        '%', '').replace(',', '.')) * 100

    # Plotando os gráficos de progresso com chaves únicas
    plot_pie_chart(progresso1_vp, "Progresso do Objetivo 1",
                   col1_vp, key="objetivo_1_vp")
    plot_pie_chart(progresso2_vp, "Progresso do Objetivo 2",
                   col2_vp, key="objetivo_2_vp")
    plot_pie_chart(progresso3_vp, "Progresso do Objetivo 3",
                   col3_vp, key="objetivo_3_vp")

    # Calcula a média dos progressos dos objetivos
    media_progresso_vp = (progresso1_vp + progresso2_vp + progresso3_vp) / 3.0
    temp = media_progresso_vp
    if media_progresso_vp > 100:
        temp = media_progresso_vp
        media_progresso_vp = 100
    st.markdown("<h2 style='text-align: center;'>Média dos Progressos dos Objetivos</h2>",
                unsafe_allow_html=True)
    st.progress(media_progresso_vp / 100.0)
    st.markdown(
        f"<h3 style='text-align: center;'>{temp:.2f}% de sucesso</h3>", unsafe_allow_html=True)

    # PARTE PROJ
    st.markdown("<h1 style='text-align: center;'>Projetos</h1>",
                unsafe_allow_html=True)
    df_proj = df[43:61][0:22]
    df_proj = df_proj.reset_index(drop=True)
    df_proj.set_index(df_proj.columns[0], inplace=True)

    df_proj_1 = df_proj.iloc[0:6, 0:21]
    new_header1_proj = df_proj_1.iloc[0]
    df_proj_1 = df_proj_1[1:]
    df_proj_1.columns = new_header1_proj

    df_proj_2 = df_proj.iloc[6:12, 0:21]
    new_header2_proj = df_proj_2.iloc[0]
    df_proj_2 = df_proj_2[1:]
    df_proj_2.columns = new_header2_proj

    df_proj_3 = df_proj.iloc[12:22, 0:21]
    new_header3_proj = df_proj_3.iloc[0]
    df_proj_3 = df_proj_3[1:]
    df_proj_3.columns = new_header3_proj

    col1_proj, col2_proj, col3_proj = st.columns(3)
    exibir_df_proj_1 = col1_proj.checkbox(
        "Exibir Objetivo 1", value=False, key="proj_objetivo_1")
    exibir_df_proj_2 = col2_proj.checkbox(
        "Exibir Objetivo 2", value=False, key="proj_objetivo_2")
    exibir_df_proj_3 = col3_proj.checkbox(
        "Exibir Objetivo 3", value=False, key="proj_objetivo_3")

    if exibir_df_proj_1:
        st.write("### Objetivo 1")
        st.write(df_proj_1)

    if exibir_df_proj_2:
        st.write("### Objetivo 2")
        st.write(df_proj_2)

    if exibir_df_proj_3:
        st.write("### Objetivo 3")
        st.write(df_proj_3)

    col1_proj, col2_proj, col3_proj = st.columns(3)

    # Extração dos dados de progresso
    progresso1_proj = float(str(df_proj_1.iloc[0]["Progresso do Objetivo"]).replace(
        '%', '').replace(',', '.')) * 100
    progresso2_proj = float(str(df_proj_2.iloc[0]["Progresso do Objetivo"]).replace(
        '%', '').replace(',', '.')) * 100
    progresso3_proj = float(str(df_proj_3.iloc[0]["Progresso do Objetivo"]).replace(
        '%', '').replace(',', '.')) * 100

    # Plotando os gráficos de progresso com chaves únicas
    plot_pie_chart(progresso1_proj, "Progresso do Objetivo 1",
                   col1_proj, key="objetivo_1_proj")
    plot_pie_chart(progresso2_proj, "Progresso do Objetivo 2",
                   col2_proj, key="objetivo_2_proj")
    plot_pie_chart(progresso3_proj, "Progresso do Objetivo 3",
                   col3_proj, key="objetivo_3_proj")

    # Calcula a média dos progressos dos objetivos
    media_progresso_proj = (progresso1_proj + progresso2_proj +
                            progresso3_proj) / 3.0
    temp = media_progresso_proj
    if media_progresso_proj > 100:
        temp = media_progresso_proj
        media_progresso_proj = 100
    st.markdown("<h2 style='text-align: center;'>Média dos Progressos dos Objetivos</h2>",
                unsafe_allow_html=True)
    st.progress(media_progresso_proj / 100.0)
    st.markdown(
        f"<h3 style='text-align: center;'>{temp:.2f}% de sucesso</h3>", unsafe_allow_html=True)

    # PARTE NEGOCIOS
    st.markdown("<h1 style='text-align: center;'>Negócios</h1>",
                unsafe_allow_html=True)
    df_negocios = df[63:81][0:22]
    df_negocios = df_negocios.reset_index(drop=True)
    df_negocios.set_index(df_negocios.columns[0], inplace=True)

    df_negocios_1 = df_negocios.iloc[0:6, 0:21]
    new_header1_negocios = df_negocios_1.iloc[0]
    df_negocios_1 = df_negocios_1[1:]
    df_negocios_1.columns = new_header1_negocios

    df_negocios_2 = df_negocios.iloc[6:12, 0:21]
    new_header2_negocios = df_negocios_2.iloc[0]
    df_negocios_2 = df_negocios_2[1:]
    df_negocios_2.columns = new_header2_negocios

    df_negocios_3 = df_negocios.iloc[12:22, 0:21]
    new_header3_negocios = df_negocios_3.iloc[0]
    df_negocios_3 = df_negocios_3[1:]
    df_negocios_3.columns = new_header3_negocios

    col1_negocios, col2_negocios, col3_negocios = st.columns(3)
    exibir_df_negocios_1 = col1_negocios.checkbox(
        "Exibir Objetivo 1", value=False, key="negocios_objetivo_1")
    exibir_df_negocios_2 = col2_negocios.checkbox(
        "Exibir Objetivo 2", value=False, key="negocios_objetivo_2")
    exibir_df_negocios_3 = col3_negocios.checkbox(
        "Exibir Objetivo 3", value=False, key="negocios_objetivo_3")

    if exibir_df_negocios_1:
        st.write("### Objetivo 1")
        st.write(df_negocios_1)

    if exibir_df_negocios_2:
        st.write("### Objetivo 2")
        st.write(df_negocios_2)

    if exibir_df_negocios_3:
        st.write("### Objetivo 3")
        st.write(df_negocios_3)

    col1_negocios, col2_negocios, col3_negocios = st.columns(3)

    # Extração dos dados de progresso
    progresso1_negocios = float(
        str(df_negocios_1.iloc[0]["Progresso do Objetivo"]).replace('%', '').replace(',', '.')) * 100
    progresso2_negocios = float(
        str(df_negocios_2.iloc[0]["Progresso do Objetivo"]).replace('%', '').replace(',', '.')) * 100
    progresso3_negocios = float(
        str(df_negocios_3.iloc[0]["Progresso do Objetivo"]).replace('%', '').replace(',', '.')) * 100

    # Plotando os gráficos de progresso com chaves únicas
    plot_pie_chart(progresso1_negocios, "Progresso do Objetivo 1",
                   col1_negocios, key="objetivo_1_negocios")
    plot_pie_chart(progresso2_negocios, "Progresso do Objetivo 2",
                   col2_negocios, key="objetivo_2_negocios")
    plot_pie_chart(progresso3_negocios, "Progresso do Objetivo 3",
                   col3_negocios, key="objetivo_3_negocios")

 # Calcula a média dos progressos dos objetivos
    media_progresso_negocios = (progresso1_negocios +
                                progresso2_negocios + progresso3_negocios) / 3.0
    temp = media_progresso_negocios
    if media_progresso_negocios > 100:
        temp = media_progresso_negocios
        media_progresso_negocios = 100
    st.markdown("<h2 style='text-align: center;'>Média dos Progressos dos Objetivos</h2>",
                unsafe_allow_html=True)
    st.progress(media_progresso_negocios / 100.0)
    st.markdown(
        f"<h3 style='text-align: center;'>{temp:.2f}% de sucesso</h3>", unsafe_allow_html=True)

    # PARTE DAF
    st.markdown("<h1 style='text-align: center;'>Administração e Finanças</h1>",
                unsafe_allow_html=True)
    df_daf = df[83:101][0:22]
    df_daf = df_daf.reset_index(drop=True)
    df_daf.set_index(df_daf.columns[0], inplace=True)

    df_daf_1 = df_daf.iloc[0:6, 0:21]
    new_header1_daf = df_daf_1.iloc[0]
    df_daf_1 = df_daf_1[1:]
    df_daf_1.columns = new_header1_daf

    df_daf_2 = df_daf.iloc[6:12, 0:21]
    new_header2_daf = df_daf_2.iloc[0]
    df_daf_2 = df_daf_2[1:]
    df_daf_2.columns = new_header2_daf

    df_daf_3 = df_daf.iloc[12:22, 0:21]
    new_header3_daf = df_daf_3.iloc[0]
    df_daf_3 = df_daf_3[1:]
    df_daf_3.columns = new_header3_daf

    col1_daf, col2_daf, col3_daf = st.columns(3)
    exibir_df_daf_1 = col1_daf.checkbox(
        "Exibir Objetivo 1", value=False, key="daf_objetivo_1")
    exibir_df_daf_2 = col2_daf.checkbox(
        "Exibir Objetivo 2", value=False, key="daf_objetivo_2")
    exibir_df_daf_3 = col3_daf.checkbox(
        "Exibir Objetivo 3", value=False, key="daf_objetivo_3")

    if exibir_df_daf_1:
        st.write("### Objetivo 1")
        st.write(df_daf_1)

    if exibir_df_daf_2:
        st.write("### Objetivo 2")
        st.write(df_daf_2)

    if exibir_df_daf_3:
        st.write("### Objetivo 3")
        st.write(df_daf_3)

    col1_daf, col2_daf, col3_daf = st.columns(3)

    # Extração dos dados de progresso
    progresso1_daf = float(str(df_daf_1.iloc[0]["Progresso do Objetivo"]).replace(
        '%', '').replace(',', '.')) * 100 if df_daf_1.iloc[0]["Progresso do Objetivo"] else 0.0
    progresso2_daf = float(str(df_daf_2.iloc[0]["Progresso do Objetivo"]).replace(
        '%', '').replace(',', '.')) * 100 if df_daf_2.iloc[0]["Progresso do Objetivo"] else 0.0
    progresso3_daf = float(str(df_daf_3.iloc[0]["Progresso do Objetivo"]).replace(
        '%', '').replace(',', '.')) * 100 if df_daf_3.iloc[0]["Progresso do Objetivo"] else 0.0

    # Plotando os gráficos de progresso com chaves únicas
    plot_pie_chart(progresso1_daf, "Progresso do Objetivo 1",
                   col1_daf, key="objetivo_1_daf")
    plot_pie_chart(progresso2_daf, "Progresso do Objetivo 2",
                   col2_daf, key="objetivo_2_daf")
    plot_pie_chart(progresso3_daf, "Progresso do Objetivo 3",
                   col3_daf, key="objetivo_3_daf")

 # Calcula a média dos progressos dos objetivos
    media_progresso_daf = (
        progresso1_daf + progresso2_daf + progresso3_daf) / 3.0
    temp = media_progresso_daf
    if media_progresso_daf > 100:
        temp = media_progresso_daf
        media_progresso_daf = 100
    st.markdown("<h2 style='text-align: center;'>Média dos Progressos dos Objetivos</h2>",
                unsafe_allow_html=True)
    st.progress(media_progresso_daf / 100.0)
    st.markdown(
        f"<h3 style='text-align: center;'>{temp:.2f}% de sucesso</h3>", unsafe_allow_html=True)

if aba_selecionada == "Resumo OKR's 2024":

    x = ["OKR 1", "OKR 2", "OKR 3", "OKR 4"]
    med_dpres = df.iloc[4][5:11].astype(str)
    
    med_vp = df.iloc[8][5:11].astype(str)
    med_proj = df.iloc[12][5:11].astype(str)
    med_negocios = df.iloc[16][5:11].astype(str)
    med_daf = df.iloc[20][5:11].astype(str)
    med_okr = df.iloc[1][5:11].astype(str)

    fig_med_okr = px.bar(
        x=x,
        y=[float(value.replace('%', '').replace(',', '.'))
           for value in med_okr],
        labels={'x': 'OKRs', 'y': 'Média de Progresso %'},
        title='Média de Progresso dos OKRs - Diretorias',
        color_discrete_sequence=['#19D3F3']
    )
    st.plotly_chart(fig_med_okr, use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
        fig_dpres = px.bar(
            x=x,
            y=[float(value.replace('%', '').replace(',', '.'))
               for value in med_dpres],
            labels={'x': 'OKRs', 'y': 'Média de Progresso'},
            title='Média de Progresso dos OKRs - Presidência',
            color_discrete_sequence=['#636EFA']
        )
        st.plotly_chart(fig_dpres)

    with col2:
        fig_vp = px.bar(
            x=x,
            y=[float(value.replace('%', '').replace(',', '.'))
               for value in med_vp],
            labels={'x': 'OKRs', 'y': 'Média de Progresso'},
            title='Média de Progresso dos OKRs - Vice-Presidência',
            color_discrete_sequence=['#EF553B']
        )
        st.plotly_chart(fig_vp)

    col3, col4, col5 = st.columns(3)

    with col3:
        fig_proj = px.bar(
            x=x,
            y=[float(value.replace('%', '').replace(',', '.'))
               for value in med_proj],
            labels={'x': 'OKRs', 'y': 'Média de Progresso'},
            title='Média de Progresso dos OKRs - Projetos',
            color_discrete_sequence=['#00CC96']
        )
        st.plotly_chart(fig_proj)

    with col4:
        fig_negocios = px.bar(
            x=x,
            y=[float(value.replace('%', '').replace(',', '.'))
               for value in med_negocios],
            labels={'x': 'OKRs', 'y': 'Média de Progresso'},
            title='Média de Progresso dos OKRs - Negócios',
            color_discrete_sequence=['#AB63FA']
        )
        st.plotly_chart(fig_negocios)

    with col5:
        fig_daf = px.bar(
            x=x,
            y=[float(value.replace('%', '').replace(',', '.'))
               for value in med_daf],
            labels={'x': 'OKRs', 'y': 'Média de Progresso'},
            title='Média de Progresso dos OKRs - Administração e Finanças',
            color_discrete_sequence=['#FFA15A']
        )
        st.plotly_chart(fig_daf)


