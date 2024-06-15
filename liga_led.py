import pyfirmata
import time
import streamlit as st

porta = '/dev/ttyACM1'




try:
    board = pyfirmata.Arduino(porta)
    st.warning("Comunicação Iniciada com sucesso")

    st.title('Manipulando um LED com Arduíno UNO')
    bt = st.radio('LED',['On','Off'],index=1)

    if bt =='On':
        board.digital[8].write(1)
    else:
        board.digital[8].write(0)
except:
    st.warning('Erro na comunicação!!')      
