import streamlit as st

st.title("Juega con Magic Calculator")

# Ask for user's name
name = st.text_input("Cuál es tu nombre?")

# Continue only if the user writes their name
if name:
    st.write(f"Hola, {name}! vamos ha hacer algo de mates básicas")

    num_1 = st.number_input("Elige un número del 1 al 7", step=1)
    num_2 = st.number_input(f"Que número 1-7 quieres sumarle a {num_1}?", step=1)

    if st.button("Calcula El Resultado"):
        result = int(num_1) + int(num_2)
        st.success(f"Boom!!! La Suma es: {result}")

        if result == 0:
            st.info(f"Y por eso {name}, SE LA CHUPAS AL PORTERO")
        elif result == 1:
            st.info(f"Y por eso {name}, TE LA COMES DE DESAYUNO")
        elif result == 2:
            st.info(f"Y por eso {name}, TE DOY POR CULO Y TE DA TOSS")
        elif result == 3:
            st.info(f"Y por eso {name}, TE DOY POR CULO OTRA VEZ")
        elif result == 4:
            st.info(f"Y por eso {name}, PARA TU CULO MI APARATO")
        elif result == 5:
            st.info(f"Y por eso {name}, POR EL CULO TE LA HINCO")
        elif result == 6:
            st.info(f"Y por eso {name}, MENOS 1 Y POR EL CULO TE LA HINCO")
        elif result == 7:
            st.info(f"Y por eso {name}, EN EL CULO SE TE METE")
        elif result == 8:
            st.info(f"Y por eso {name}, POR EL CULO TE LA ENTOCHO")
        elif result == 9:
            st.info(f"Y por eso {name}, EN EL CULO SE TE MUEVE")
        elif result == 10:
            st.info(f"Y por eso {name}, TE DOY POR EL CULO Y NO ME VEZ")
        elif result == 11:
            st.info(f"Y por eso {name}, CHUPALA ENTONCES")
        elif result == 12:
            st.info(f"Y por eso {name}, EN EL CULO TE GUSTA EL ROCE")
        elif result == 13:
            st.info(f"Y por eso {name}, AGARRAMELA QUE ME CRECE")
        elif result > 13:
            st.info(f"NO ES 5 PERO... {name}, POR EL CULO TE LA HINCO")
