import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Архетип", page_icon="🔮", layout="centered"
)


# Fonctions de calcul
def simp(n):
    n = abs(n)
    while n > 22:
        n -= 22
    if n == 0:
        return 22
    return n


def somme_chiffres(n):
    somme = 0
    while n > 0:
        somme += n % 10
        n //= 10
    if somme >= 23:
        somme -= 22
    return somme


# Interface utilisateur Streamlit
st.title("🔮 Архетип")
st.write("Введите дату рождения:")

# Saisie de la date
col_d, col_m, col_y = st.columns(3)

with col_d:
    d = st.number_input("День", min_value=1, max_value=31, value=1)
with col_m:
    m = st.number_input("Месяц", min_value=1, max_value=12, value=1)
with col_y:
    y = st.number_input("Год", min_value=1900, max_value=2100, value=2000)

if st.button("Высчитать", type="primary"):
    # Calculs
    baza1 = simp(d)
    shkola2 = simp(m)
    ekzamen3 = somme_chiffres(y)

    kompleksy4 = simp(baza1 + shkola2)
    myslennya5 = simp(shkola2 + ekzamen3)
    sverhdar6 = simp(myslennya5 + kompleksy4)

    prednaznachenyie7 = simp(baza1 + shkola2 + ekzamen3)
    chto_pomozhet8 = simp(shkola2 + sverhdar6)

    proshlaya_zhyzn9 = (simp(baza1 - shkola2), shkola2, myslennya5)

    strah10 = simp(shkola2 - ekzamen3)
    zadacha11 = simp(proshlaya_zhyzn9[0] - strah10)
    komfort12 = simp(prednaznachenyie7 + chto_pomozhet8)

    kak_sebyia13 = simp(baza1 + kompleksy4 + sverhdar6)
    kak_drugie14 = simp(ekzamen3 + myslennya5 + sverhdar6)
    chto_pomozhet15 = simp(
        (proshlaya_zhyzn9[0] + strah10 + zadacha11) - prednaznachenyie7
    )
    
    detstvoA = simp(baza1 + kompleksy4)
    travmaB = simp(shkola2 + kompleksy4)
    portret_dushiC = simp(shkola2 + myslennya5)
    affektD = simp(ekzamen3 + myslennya5)
    prepyatstvieE = simp(kompleksy4 + sverhdar6)
    syla_ekzamenF = simp(myslennya5 + sverhdar6)
    
    st.markdown("---")
    
    # Section 1 : Bases
    st.subheader("📌 Главные арканы")
    c1, c2, c3 = st.columns(3)
    c1.metric("База (1)", baza1)
    c2.metric("Школа (2)", shkola2)
    c3.metric("Екзамен (3)", ekzamen3)

    c4, c5, c6 = st.columns(3)
    c4.metric("Комплекси (4)", kompleksy4)
    c5.metric("Мислення (5)", myslennya5)
    c6.metric("Сверхдар (6)", sverhdar6)

    # Section 2: Shadow
    st.subheader("🕳️ Тень")
    cA, cB, cC = st.columns(3)
    cA.metric("Детство (А)", detstvoA)
    cB.metric("Травма (B)", travmaB)
    cC.metric("Портрет души в самовыражении (C)", portret_dushiC)

    cD, cE, cF = st.columns(3)
    cD.metric("Афект (D)", affektD)
    cE.metric("Препятствие (E)", prepyatstvieE)
    cF.metric("Сила на экзамене (F)", syla_ekzamenF)
    
    # Section 3 : Destinée et Karmi
    st.subheader("🌟 Карма")
    col_a, col_b = st.columns(2)

    with col_a:
        st.write(f"**Предназначение (7) :** {prednaznachenyie7}")
        st.write(f"**Что в этом поможет (8) :** {chto_pomozhet8}")
        st.write(f"**Прошлая жизнь (9) :** {proshlaya_zhyzn9}")
        st.write(f"**Самый большой страх (10) :** {strah10}")

    with col_b:
        st.write(f"**Кармическая задача (11) :** {zadacha11}")
        st.write(f"**Психологический комфорт (12) :** {komfort12}")
        st.write(f"**Что поможет в задаче (15) :** {chto_pomozhet15}")

    # Section 3 : Perception
    st.subheader("👁️ Восприятие")
    p1, p2 = st.columns(2)
    p1.info(f"**Как я вижу себя (13) :** {kak_sebyia13}")
    p2.success(f"**Как меня видят другие (14) :** {kak_drugie14}")
