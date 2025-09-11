import streamlit as st
# -------------------------------- SIDEBAR
st.sidebar.image(f'logo.png')
st.sidebar.title('Vieira do Sucesso - Aluguel De Carros')
carros = ['Corsa prisma', 'Parati', 'Peugeot', 'Siena']
modelo = st.sidebar.selectbox('Selecione o Carro Alugado', carros)

# -------------------------------- PRINCIPAL
st.title('Vieira do Sucesso - Aluguel De Carros')
st.markdown(f'## Você Escolheu o Modelo: {modelo}')
st.image(f'{modelo}.png')

if modelo == 'Corsa prisma':
    diaria = 50

elif modelo == 'Parati':
    diaria = 75

elif modelo == 'Peugeot':
    diaria = 40

elif modelo == 'Siena':
    diaria = 30

dias = st.text_input(f'Por quantos dias você alugou o {modelo}')
km = st.text_input(f'Qunatos km você andou?')

if st.button('Calcular'):

    dias = int(dias)
    km = float(km)
    total_dias = dias * diaria
    total_km = km * 0.60
    aluguel = total_dias + total_km
    st.warning(f'Você alugou o {modelo} por {dias} dias e rodou {km} km. O valor do aluguel será R$ {aluguel}')