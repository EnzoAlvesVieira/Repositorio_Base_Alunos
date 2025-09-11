import streamlit as st

#-----------------------------SIDEBAR

st.sidebar.image(f'logo.png')
st.sidebar.title('Sonus - Playlists')

estilo_de_musica = ['Sertanejo', 'Samba', 'Gospel', 'Pagode']
estilo_escolhido = st.sidebar.selectbox('Selecione o estilo de música', estilo_de_musica)

#----------------------------PRINCIPAL

st.title('Sonus - Playlists ')
st.markdown(f'### O seu estilo de música selecionado foi {estilo_escolhido}' )

if estilo_escolhido == 'Sertanejo':
    artistas = ['Gusttavo Lima' , 'Henrique & Juliano' , 'Ana Castela']
    artista = st.sidebar.selectbox('Escolha um artista', artistas)

elif estilo_escolhido == 'Samba':
    artistas = ['Zeca Pagodinho' , 'Alcione' , 'Arlindo Cruz']
    artista = st.sidebar.selectbox('Escolha um artista', artistas)

elif estilo_escolhido == 'Gospel':
    artistas = ['Tales Roberto' , 'Aline Barros' , 'Fernandinho']
    artista = st.sidebar.selectbox('Escolha um artista', artistas)

elif estilo_escolhido == 'Pagode':
    artistas = ['Ferrugem', 'Sorriso Maroto', 'Pericles']
    artista = st.sidebar.selectbox('Escolha um artista', artistas)

if artista == 'Gusttavo Lima':
    st.video('https://youtu.be/-UUe7g8-E0k?si=4Tmzn6oUqSWnE_-u')
    st.markdown(f'### Bom gosto músical, Parabéns pela escolha! 😁')
    

elif artista == 'Henrique & Juliano':
    st.video('https://youtu.be/9Vt4XguN2-A?si=dk3zA23ydHv173VH')
    st.markdown(f'### Bom gosto músical, Parabéns pela escolha! 😁')

elif artista == 'Ana Castela':
    st.video('https://youtu.be/f58W_FVXBLg?si=mcM5wPO981ahqECU')
    st.markdown(f'### Bom gosto músical, Parabéns pela escolha! 😁')

elif artista == 'Zeca Pagodinho':
    st.video('https://youtu.be/Nm5N4iFLU0g?si=j1DbuDJL-aOl2LuZ')
    st.markdown(f'### Bom gosto músical, Parabéns pela escolha! 😁')

elif artista == 'Alcione':
    st.video('https://youtu.be/fwkANwQSELU?si=fdIgIHRpkfKGlqr9')
    st.markdown(f'### Bom gosto músical, Parabéns pela escolha! 😁')

elif artista == 'Arlindo Cruz':
    st.video('https://youtu.be/vNK58tL6J70?si=7yy0ZTlua6Wtba0b')
    st.markdown(f'### Bom gosto músical, Parabéns pela escolha! 😁')

elif artista == 'Tales Roberto':
    st.video('https://youtu.be/mJJmHaitgVc?si=dRrnRMv51DErLhI-')
    st.markdown(f'### Bom gosto músical, Parabéns pela escolha! 😁')

elif artista == 'Aline Barros':
    st.video('https://youtu.be/YyFd_dXy494?si=_ke7c1VzQCl8Z2Fd')
    st.markdown(f'### Bom gosto músical, Parabéns pela escolha! 😁')

elif artista == 'Fernandinho':
    st.video('https://youtu.be/SdkWBHLHTgg?si=gQVPYr0ZOGnZM1Kj')
    st.markdown(f'### Bom gosto músical, Parabéns pela escolha! 😁')

elif artista == 'Ferrugem':
    st.video('https://youtu.be/o3dknP3jclw?si=lJtdzcddVP-f_mmZ')
    st.markdown(f'### Bom gosto músical, Parabéns pela escolha! 😁')

elif artista == 'Sorriso Maroto':
    st.video('https://youtu.be/QDMJVNG2MtM?si=XPxOK826Fkd4bgnd')
    st.markdown(f'### Bom gosto músical, Parabéns pela escolha! 😁')

elif artista == 'Pericles':
    st.video('https://youtu.be/T3Y6RRSDm4o?si=9F5ABPX3nLQbVy-H')
    st.markdown(f'### Bom gosto músical, Parabéns pela escolha! 😁')