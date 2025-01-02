import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml import SafeLoader


def login():
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)

    stauth.Hasher.hash_passwords(config['credentials'])

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days']
    )

    if "authentication_status" not in st.session_state:
        st.session_state["authentication_status"] = None
    authenticator.login()

    if st.session_state["authentication_status"]:
        authenticator.logout(button_name='Sair',
                             location='main', key='main.py')
        st.write(f'Bem Vindo *{st.session_state["name"]}*')
    elif st.session_state["authentication_status"] is False:
        st.error('Usuário/Senha is inválido')
    elif st.session_state["authentication_status"] is None:
        st.warning('Por Favor, utilize seu usuário e senha!')


def main():
    login()
    if not st.session_state.authentication_status:
        st.info('Por favor, faça login para acessar o sistema.')
        st.stop()

    st.write("### Por favor, navegue pelas páginas no menu lateral.")


if __name__ == "__main__":
    st.set_page_config(
        page_title="Sistema EJEET",
        page_icon="./assets/EJEET for calls.png",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    Home = st.Page(
        page="main.py",
        title="Home",
        default=True
    )
    Dashboard = st.Page(page="views/dashboard.py",
                        title="Dashboard")
    Membros = st.Page(page="views/membros.py", title="Membros")
    Projetos = st.Page(page="views/Projetos.py", title="Projetos")
    PortalBJ = st.Page(page="views/PortalBJ.py", title="PortlBJ")

    pg = st.navigation(pages=[Home, Dashboard, Membros, Projetos, PortalBJ])
    pg.run()

    main()
