import streamlit as st
import pandas as pd

st.set_page_config(page_title="Voto Informado CR 2026", layout="wide")

st.title("🇨🇷 Voto Informado Costa Rica 2026")
st.caption("Análisis ciudadano de planes de gobierno — fuente: TSE")

df = pd.read_csv("planes_scores.csv", encoding="latin1")
df.columns = df.columns.str.replace("ï»¿", "").str.strip()

def semaforo(score):
    if score >= 8.5:
        return "🟢 Alta viabilidad"
    elif score >= 7.5:
        return "🟡 Viabilidad media"
    else:
        return "🔴 Riesgo alto"

df["Viabilidad"] = df["Score"].apply(semaforo)

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["🏆 Ranking", "📊 Comparador", "📄 Fichas por partido", "📖 Metodología", "📚 Fuentes"]
)

# -------- TAB RANKING --------
with tab1:
    st.subheader("📊 Ranking general de planes de gobierno")
    st.dataframe(df.sort_values("Score", ascending=False))

    st.subheader("⚖ Nivel de viabilidad")
    st.dataframe(df[["Partido", "Score", "Viabilidad"]])
    
    import matplotlib.pyplot as plt

    st.subheader("📈 Comparación visual de planes de gobierno")

    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    ax.bar(df["Partido"], df["Score"])
    ax.set_ylabel("Score global")
    ax.set_title("Ranking comparativo de planes")

    st.pyplot(fig)
    
# -------- TAB COMPARADOR --------
with tab2:
    tema = st.selectbox("Elegí un tema", ["Seguridad","Salud","Educacion","Economia","Ambiente"])
    st.bar_chart(df.set_index("Partido")[tema])
    
with tab2:
    st.subheader("Ranking general de planes de gobierno")
    # Gráfico de Matplotlib
    #st.pyplot(fig_ranking)

    # Gráfico de Altair (complemento interactivo)
    import altair as alt
# Comparación de scores por partido
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X("Partido", sort="-y"),
        y="Score",
        color="Partido",
        tooltip=["Partido", "Score", "Viabilidad"]
    ).properties(
        title="Comparación de Score Global por Partido"
    )
    st.altair_chart(chart, use_container_width=True)   

# -------- TAB FICHAS --------
with tab3:
    st.title("📄 Fichas técnicas por partido")

    def ficha(color, partido, enfoque, fortalezas, riesgos, scores, total):
        st.markdown(f"## {color} {partido}")
        st.markdown("### 📌 Enfoque general")
        st.write(enfoque)

        st.markdown("### ✅ Fortalezas principales")
        for f in fortalezas:
            st.write("•", f)

        st.markdown("### ⚠ Riesgos o desafíos")
        for r in riesgos:
            st.write("•", r)

        st.markdown("### 📊 Evaluación técnica")
        for k, v in scores.items():
            st.write(f"**{k}:** {v}")

        st.markdown("### 🧮 Score global")
        st.success(f"{total} / 10")

        st.divider()

    ficha(
        "🟢",
        "PPSO — Partido Pueblo Soberano",
        "Continuidad institucional con foco en ejecución real, seguridad y sostenibilidad.",
        ["Programas activos", "Metas claras", "Bajo riesgo de implementación", "Articulación institucional"],
        ["Presión fiscal moderada", "Dependencia política"],
        {"Factibilidad": "Alta", "Viabilidad": "Alta", "Claridad": "Alta", "Ejecución": "Alta"},
        8.9
    )
    st.divider()
    ficha(
        "🔵",
        "PLN — Partido Liberación Nacional",
        "Desarrollo integral con enfoque clásico en seguridad, economía y servicios públicos.",
        ["Plan estructurado", "Experiencia institucional", "Cobertura amplia país"],
        ["Poca especificidad operativa", "Reformas complejas"],
        {"Factibilidad": "Alta", "Viabilidad": "Media–Alta", "Claridad": "Alta", "Ejecución": "Media"},
        8.2
    )
    st.divider()
    ficha(
        "🟠",
        "CAC — Coalición pro Crecimiento",
        "Reactivación económica con enfoque técnico y empresarial.",
        ["Medidas económicas concretas", "Simplificación trámites", "Atracción inversión"],
        ["Débil eje social", "Reformas estructurales necesarias"],
        {"Factibilidad": "Media–Alta", "Viabilidad": "Media", "Claridad": "Alta", "Ejecución": "Media"},
        7.8
    )
    st.divider()
    ficha(
        "🔴",
        "FA — Frente Amplio",
        "Enfoque social y ambiental con fuerte rol estatal.",
        ["Protección social", "Compromiso ambiental", "Servicios públicos fuertes"],
        ["Riesgo fiscal", "Financiamiento poco claro"],
        {"Factibilidad": "Media", "Viabilidad": "Media–Baja", "Claridad": "Alta", "Ejecución": "Media–Baja"},
        7.6
    )
    st.divider()
    ficha(
        "🟣",
        "PA — Partido Acción",
        "Balance entre crecimiento, eficiencia estatal y sostenibilidad.",
        ["Propuestas moderadas", "Buen equilibrio sectorial", "Riesgo controlado"],
        ["Impacto gradual", "Menor detalle técnico"],
        {"Factibilidad": "Media–Alta", "Viabilidad": "Media–Alta", "Claridad": "Media–Alta", "Ejecución": "Media"},
        8.0
    )

# -------- TAB METODOLOGÍA --------
with tab4:
    st.write("""
Los planes fueron evaluados usando cinco criterios:

• Claridad de objetivos  
• Cómo se ejecutarían las propuestas  
• Financiamiento  
• Continuidad institucional  
• Riesgo de implementación  

Cada criterio se calificó de 0 a 10 por tema:
Seguridad, Salud, Educación, Economía y Ambiente.

El score final es el promedio de todos los temas.
""")

# -------- TAB FUENTES --------
with tab5:
    st.write("### 📚 Fuentes oficiales")

    st.markdown("🔗 [Planes de Gobierno 2026 – TSE (general)](https://www.tse.go.cr/2026/planesgobierno.html)")

    st.markdown("• 📄 [PPSO – Plan de Gobierno (PDF)](https://www.tse.go.cr/2026/docus/planesgobierno/PPSO.pdf)")
    st.markdown("• 📄 [PA – Plan de Gobierno (PDF)](https://www.tse.go.cr/2026/docus/planesgobierno/PA.pdf)")
    st.markdown("• 📄 [FA – Plan de Gobierno (PDF)](https://www.tse.go.cr/2026/docus/planesgobierno/FA.pdf)")
    st.markdown("• 📄 [CAC – Plan de Gobierno (PDF)](https://www.tse.go.cr/2026/docus/planesgobierno/CAC.pdf)")
    st.markdown("• 📄 [PLN – Plan de Gobierno (PDF)](https://www.tse.go.cr/2026/docus/planesgobierno/PLN.pdf)")

    st.write("""
Todos los planes listados aquí son documentos oficiales presentados al Tribunal Supremo de Elecciones — fuente primaria de este portal.
""")


