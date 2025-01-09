import streamlit as st
import calendar
import pandas as pd

st.title("Calendário EJEET")
year = 2025

# Inicializa o estado da sessão para descrições se não existir
if 'descriptions' not in st.session_state:
    st.session_state.descriptions = {
        # (Mes, Dia) : "Descrição"
        (9, 19): "Aniversário Leonardo Moreto",
        (4, 7): "Festa",
        # Adicione outras datas e descrições aqui
    }
descriptions = st.session_state.descriptions


# Função para adicionar descrições aos dias
def add_descriptions(cal, month):
    desc_list = []
    for week in cal:
        for i, day in enumerate(week):
            if day != 0 and (month, day) in descriptions:
                desc_list.append(f"Dia {day} -> {descriptions[(month, day)]}")
    return cal, desc_list


# Itera sobre os meses e exibe em uma única coluna
for month in range(1, 12 + 1):
    cal = calendar.monthcalendar(year, month)
    cal, desc_list = add_descriptions(cal, month)
    st.header(calendar.month_name[month])
    
    # Cria um DataFrame com os dias da semana como colunas
    df = pd.DataFrame(cal, columns=["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"])
    st.table(df)
    
    for desc in desc_list:
        st.write(desc)
