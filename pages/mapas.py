import streamlit as st

# Título centralizado
st.markdown("<h1 style='text-align: center;'>Mapas Mentais da EJEET</h1>",
            unsafe_allow_html=True)

# CSS personalizado para estilo
st.markdown("""
    <style>
    .main-column {
        display: flex;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        border: 2px solid #fff;
        padding: 10px;
        margin: 10px;
        border-radius: 5px;
        background-color: #001f27; /* Cor mais escura */
        text-align: center;
        flex-direction: column;
        align-items: center; /* Alinha os itens ao centro */
    }

    .link-item {
        display: block;
        margin: 5px auto;
        text-align: center;
        padding: 10px;
        border-radius: 5px;
        background-color: #003545; /* Azul escuro */
        color: white;
        text-decoration: none;
        width: 80%;
    }

    .link-item:hover {
        background-color: #005f73; /* Tom mais claro ao passar o mouse */
    }

    .full-width {
        width: 100%;
    }

    .stColumn {
        flex: 1 !important;
        padding: 10px !important;
    }
        
    </style>
    """, unsafe_allow_html=True)

mapas_links = {
    "EJEET": [("Mapa Mental 1", "https://example.com/ejeet1")],
    "DPRES": [("Mapa Mental 2", "https://example.com/presidencia2"),
              ("Mapa Mental 3", "https://example.com/presidencia3")],
    "VP": [("Mapa Mental 4", "https://example.com/vp4"),
           ("Mapa Mental 5", "https://example.com/vp5")],
    "PROJ": [("Mapa Mental 6", "https://example.com/projetos6"),
             ("Mapa Mental 7", "https://example.com/projetos7")],
    "NEG": [("Mapa Mental 8", "https://example.com/negocios8"),
            ("Mapa Mental 9", "https://example.com/negocios9")],
    "DAF": [("Mapa Mental 10", "https://example.com/daf10"),
            ("Mapa Mental 11", "https://example.com/daf11")]
}

st.markdown(f"<div class='main-column'>"
            f"<h1>EJEET</h1>", unsafe_allow_html=True)

for name, link in mapas_links["EJEET"]:
    st.markdown(
        f"<a href='{link}' class='link-item'>{name}</a>", unsafe_allow_html=True)

# Remover EJEET do dicionário para não duplicar
del mapas_links["EJEET"]

# Distribuir as diretorias restantes entre as colunas
cols = st.columns(5)
for col, (diretoria, links) in zip(cols, mapas_links.items()):
    with col:
        # Div principal para a diretoria
        st.markdown(f"<div class='main-column'>"
                    f"<h2>{diretoria}</h2>", unsafe_allow_html=True)

        # Adicionar os links dentro da div principal
        st.markdown("<div class='links'>", unsafe_allow_html=True)
        for name, link in links:
            st.markdown(
                f"<a href='{link}' class='link-item'>{name}</a>", unsafe_allow_html=True)
        st.markdown("</div></div>", unsafe_allow_html=True)
