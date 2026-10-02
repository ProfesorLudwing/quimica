import streamlit as st
import os

# Configuración del Pizarrón Escolar
st.set_page_config(page_title="FluidoVital: Aire y Agua", page_icon="💧", layout="wide")

st.title("💧 FluidoVital: Capas y Química del Aire y Agua")
st.markdown("### CBTIS 303 | Ciencias Naturales, Experimentales y Tecnología III")
st.write("Explora la química, las propiedades físicas y los ciclos biogeoquímicos de los dos grandes fluidos planetarios.")

# --- RUTAS DE IMÁGENES ---
IMAGENES = {
    "Hidrosfera_Estados": "hidrosfera_estados.png",
    "Agua_Polaridad": "agua_polaridad.png",
    "Agua_Puentes": "agua_puentes.png",
    "Agua_Iones": "agua_iones.jpg",
    "Atmosfera_Composicion": "atmosfera_composicion.png",
    "Atmosfera_Funciones": "atmosfera_funciones.jpg",
    "CicloAgua_Etapas": "agua_etapas.jpg",
    "CicloAgua_Alteraciones": "agua_alteraciones.jpg",
    "Fotosintesis_Proceso": "fotosintesis_proceso.png",
    "Fotosintesis_Fases": "fotosintesis_fases.jpg",
    "Quimiosintesis_Proceso": "quimiosintesis_proceso.jpg",
    "Quimiosintesis_Ambientes": "quimiosintesis_ambientes.jpg"
}

# --- BANCO DE PREGUNTAS ---
CUESTIONARIO = {
    "hidrosfera": [
        {
            "id": "hid1",
            "pregunta": "¿Qué cambio de estado ocurre cuando el agua pasa de líquido a gas?",
            "opciones": ["Evaporación", "Condensación", "Solidificación"],
            "correcta": "Evaporación",
            "pista": "Revisa la subpestaña 'Estados de Agregación'."
        },
        {
            "id": "hid2",
            "pregunta": "¿Por qué la molécula de agua es considerada polar?",
            "opciones": [
                "Porque tiene cargas parciales δ+ y δ−",
                "Porque tiene carga neutra",
                "Porque no tiene electrones"
            ],
            "correcta": "Porque tiene cargas parciales δ+ y δ−",
            "pista": "Revisa la subpestaña 'Propiedades Moleculares'."
        },
        {
            "id": "hid3",
            "pregunta": "¿Cuál es el ion más abundante en el agua de mar?",
            "opciones": ["Cloruro (Cl⁻)", "Sodio (Na⁺)", "Calcio (Ca²⁺)"],
            "correcta": "Cloruro (Cl⁻)",
            "pista": "Revisa la subpestaña 'Iones Disueltos'."
        }
    ],
    "atmosfera": [
        {
            "id": "atm1",
            "pregunta": "¿Cuál es el gas más abundante en la atmósfera terrestre?",
            "opciones": ["Nitrógeno (N₂)", "Oxígeno (O₂)", "Dióxido de carbono (CO₂)"],
            "correcta": "Nitrógeno (N₂)",
            "pista": "Representa el 78.08% del aire seco."
        },
        {
            "id": "atm2",
            "pregunta": "¿En qué proporción aproximada se encuentra el oxígeno (O₂) en el aire seco?",
            "opciones": ["20.95%", "50%", "5%"],
            "correcta": "20.95%",
            "pista": "Revisa la subpestaña 'Composición Química'."
        },
        {
            "id": "atm3",
            "pregunta": "¿Qué función cumple la capa de ozono?",
            "opciones": [
                "Absorbe la radiación ultravioleta (UV)",
                "Aumenta la gravedad terrestre",
                "Genera el campo magnético"
            ],
            "correcta": "Absorbe la radiación ultravioleta (UV)",
            "pista": "Revisa la subpestaña 'Funciones y Protección'."
        }
    ],
    "ciclo_agua": [
        {
            "id": "cic1",
            "pregunta": "¿Qué proceso del ciclo del agua convierte el vapor en gotas líquidas?",
            "opciones": ["Condensación", "Evaporación", "Infiltración"],
            "correcta": "Condensación",
            "pista": "Es el proceso que forma las nubes."
        },
        {
            "id": "cic2",
            "pregunta": "¿Cuál de las siguientes actividades humanas altera más el ciclo del agua?",
            "opciones": [
                "La deforestación y la contaminación",
                "La fotosíntesis de las plantas",
                "La respiración de los animales"
            ],
            "correcta": "La deforestación y la contaminación",
            "pista": "Revisa la subpestaña 'Importancia y Alteraciones'."
        }
    ],
    "fotosintesis": [
        {
            "id": "fot1",
            "pregunta": "¿Cuál es la ecuación general de la fotosíntesis?",
            "opciones": [
                "6 CO₂ + 6 H₂O + luz → C₆H₁₂O₆ + 6 O₂",
                "C₆H₁₂O₆ + 6 O₂ → 6 CO₂ + 6 H₂O",
                "H₂O + NaCl → HCl + NaOH"
            ],
            "correcta": "6 CO₂ + 6 H₂O + luz → C₆H₁₂O₆ + 6 O₂",
            "pista": "Revisa la subpestaña 'Proceso y Ecuación'."
        },
        {
            "id": "fot2",
            "pregunta": "¿En qué parte del cloroplasto ocurre el ciclo de Calvin?",
            "opciones": ["En el estroma", "En los tilacoides", "En el núcleo"],
            "correcta": "En el estroma",
            "pista": "La fase oscura ocurre en el líquido interno del cloroplasto."
        }
    ],
    "quimiosintesis": [
        {
            "id": "qui1",
            "pregunta": "¿Qué tipo de organismos realizan la quimiosíntesis?",
            "opciones": [
                "Bacterias y arqueas",
                "Plantas y algas",
                "Animales y hongos"
            ],
            "correcta": "Bacterias y arqueas",
            "pista": "Revisa la subpestaña 'Proceso y Organismos'."
        },
        {
            "id": "qui2",
            "pregunta": "¿En qué ambiente extremo es fundamental la quimiosíntesis?",
            "opciones": [
                "En las fuentes hidrotermales del fondo oceánico",
                "En los desiertos cálidos",
                "En las selvas tropicales"
            ],
            "correcta": "En las fuentes hidrotermales del fondo oceánico",
            "pista": "Donde no llega la luz solar."
        }
    ]
}

# --- FUNCIÓN PARA MOSTRAR IMÁGENES ---
def mostrar_imagen(nombre_archivo, texto_alternativo):
    if os.path.exists(nombre_archivo):
        st.image(nombre_archivo, caption=texto_alternativo, use_container_width=True)
    else:
        st.warning(f"⚠️ Guarda una imagen llamada '{nombre_archivo}' en tu carpeta para verla aquí.")

# --- PESTAÑAS PRINCIPALES ---
tab_hidro, tab_atmo, tab_ciclo, tab_foto, tab_quimio, tab_glosario = st.tabs([
    "💧 Hidrósfera",
    "🌤️ Atmósfera",
    "🔄 Ciclo del Agua",
    "🌿 Fotosíntesis",
    "⚗️ Quimiosíntesis",
    "📖 Glosario"
])

# ============================================================
# PESTAÑA 1: HIDRÓSFERA
# ============================================================
with tab_hidro:
    st.header("💧 La Hidrósfera: El Fluido Vital")

    sub1, sub2, sub3 = st.tabs([
        "🌡️ Estados de Agregación",
        "🔬 Propiedades Moleculares",
        "⚡ Iones Disueltos"
    ])

    with sub1:
        col1, col2 = st.columns([1.2, 1])
        with col1:
            mostrar_imagen(IMAGENES["Hidrosfera_Estados"], "Cambios de estado del agua en el planeta.")
        with col2:
            st.success("### 🌡️ Los Tres Estados del Agua")
            st.markdown("""
            El agua es la única sustancia natural que se encuentra en los **tres estados 
            de agregación** de forma simultánea en la Tierra.
            """)
            st.info("### 📊 Cambios de Estado")
            st.markdown("""
            - **Fusión:** Sólido → Líquido (hielo → agua).
            - **Solidificación:** Líquido → Sólido (agua → hielo).
            - **Evaporación:** Líquido → Gas (agua → vapor).
            - **Condensación:** Gas → Líquido (vapor → nubes).
            - **Sublimación:** Sólido → Gas (hielo → vapor, sin pasar por líquido).
            """)
            st.warning("### 🔄 Conexión con el Ciclo del Agua")
            st.markdown("""
            Estos cambios son la base del **ciclo hidrológico**: el agua se evapora 
            del océano, se condensa en nubes, precipita como lluvia y regresa a los ríos.
            """)

    with sub2:
        col1, col2 = st.columns([1.2, 1])
        with col1:
            mostrar_imagen(IMAGENES["Agua_Polaridad"], "Distribución de cargas en la molécula de agua.")
            mostrar_imagen(IMAGENES["Agua_Puentes"], "Red de puentes de hidrógeno entre moléculas de agua.")
        with col2:
            st.success("### 🔬 Polaridad de la Molécula")
            st.markdown("""
            La molécula de agua (**H₂O**) es **polar** porque el oxígeno atrae los 
            electrones con más fuerza que el hidrógeno.
            """)
            st.info("### 📊 Cargas Parciales")
            st.markdown("""
            - **Oxígeno (O):** Carga parcial **negativa (δ−)**.
            - **Hidrógenos (H):** Carga parcial **positiva (δ+)**.
            """)
            st.warning("### 🌉 Puentes de Hidrógeno")
            st.markdown("""
            La atracción entre el **H (δ+)** de una molécula y el **O (δ−)** de otra 
            forma los **puentes de hidrógeno**. Son más débiles que un enlace químico, 
            pero le dan al agua propiedades únicas:
            """)
            st.markdown("""
            - **Alto punto de ebullición (100 °C).**
            - **Alto calor específico** (regula el clima).
            - **Tensión superficial alta** (insectos caminan sobre ella).
            - **Capilaridad** (el agua sube por las raíces).
            - **El hielo flota** (red hexagonal menos densa).
            """)
            st.error("### 🧠 Analogía")
            st.markdown("""
            Imagina que cada molécula de agua tiene **dos manos positivas** (H) y 
            **dos bolsillos negativos** (O). Todas se toman de las manos y se meten 
            en los bolsillos de las vecinas: esa red es el puente de hidrógeno.
            """)

    with sub3:
        col1, col2 = st.columns([1.2, 1])
        with col1:
            mostrar_imagen(IMAGENES["Agua_Iones"], "Cationes y aniones presentes en el agua de mar.")
        with col2:
            st.success("### ⚡ ¿Qué son los Iones?")
            st.markdown("""
            Los **iones** son átomos o moléculas que han **ganado o perdido electrones**, 
            adquiriendo carga eléctrica neta.
            """)
            st.info("### 📊 Tipos de Iones")
            st.markdown("""
            - **Catión (+):** Perdió electrones. Ejemplo: **Na⁺, Ca²⁺, Mg²⁺, K⁺**.
            - **Anión (−):** Ganó electrones. Ejemplo: **Cl⁻, SO₄²⁻, HCO₃⁻**.
            """)
            st.warning("### 🌊 Los 6 Iones Principales del Agua de Mar")
            st.markdown("""
            | Ion | Fórmula | % en sales |
            |---|---|---|
            | Cloruro | Cl⁻ | 55.0% |
            | Sodio | Na⁺ | 30.6% |
            | Sulfato | SO₄²⁻ | 7.7% |
            | Magnesio | Mg²⁺ | 3.7% |
            | Calcio | Ca²⁺ | 1.2% |
            | Potasio | K⁺ | 1.1% |
            """)
            st.error("### 💡 ¿Por qué importan?")
            st.markdown("""
            Los iones son los responsables de la **conductividad eléctrica** del agua. 
            El agua pura (destilada) **no conduce electricidad**; el agua de mar sí, 
            porque los iones libres transportan carga eléctrica.
            """)

    st.write("---")
    with st.expander("📝 Pon a prueba tus conocimientos sobre la Hidrósfera"):
        for q in CUESTIONARIO["hidrosfera"]:
            ans = st.radio(q["pregunta"], q["opciones"], key=q["id"])
            if st.button("Validar Respuesta", key=f"btn_{q['id']}"):
                if ans == q["correcta"]:
                    st.success("🎉 ¡Excelente! Respuesta correcta.")
                else:
                    st.error(f"❌ Incorrecto. Pista: {q['pista']}")

# ============================================================
# PESTAÑA 2: ATMÓSFERA
# ============================================================
with tab_atmo:
    st.header("🌤️ La Atmósfera: El Escudo Gaseoso")

    sub1, sub2 = st.tabs([
        "🧪 Composición Química",
        "🛡️ Funciones y Protección"
    ])

    with sub1:
        col1, col2 = st.columns([1.2, 1])
        with col1:
            mostrar_imagen(IMAGENES["Atmosfera_Composicion"], "Gráfica de composición del aire seco.")
        with col2:
            st.success("### 🧪 El Aire es una Mezcla")
            st.markdown("""
            El aire **no es un solo gas**, es una mezcla de varios gases que 
            varía su proporción según la altitud, temperatura y humedad.
            """)
            st.info("### 📊 Composición del Aire Seco (Nivel del Mar)")
            st.markdown("""
            | Gas | Fórmula | % Volumen |
            |---|---|---|
            | Nitrógeno | N₂ | 78.08% |
            | Oxígeno | O₂ | 20.95% |
            | Argón | Ar | 0.93% |
            | Dióxido de carbono | CO₂ | 0.042% (420 ppm) |
            | Neón | Ne | 18.2 ppm |
            | Helio | He | 5.24 ppm |
            | Metano | CH₄ | ~1.9 ppm |
            | Kriptón | Kr | 1.14 ppm |
            """)
            st.warning("### 💧 Vapor de Agua")
            st.markdown("""
            A diferencia de los gases anteriores, el **vapor de agua (H₂O)** es 
            **variable**: puede representar entre **0% y 4%** del aire total.
            Es el gas de efecto invernadero más abundante.
            """)
            st.error("### 🌍 Gases de Efecto Invernadero")
            st.markdown("""
            - **Vapor de agua (H₂O):** Variable, hasta 4%.
            - **Dióxido de carbono (CO₂):** 420 ppm y en aumento.
            - **Metano (CH₄):** ~1.9 ppm, 25× más potente que el CO₂.
            - **Óxido nitroso (N₂O):** 0.33 ppm, 300× más potente que el CO₂.
            """)

    with sub2:
        col1, col2 = st.columns([1.2, 1])
        with col1:
            mostrar_imagen(IMAGENES["Atmosfera_Funciones"], "Funciones protectoras de la atmósfera.")
        with col2:
            st.success("### 🛡️ Funciones Esenciales")
            st.markdown("""
            La atmósfera no es solo una capa de gas: es un **escudo activo** que 
            permite la vida en la Tierra.
            """)
            st.info("### 📊 Las 4 Funciones Principales")
            st.markdown("""
            1. **Filtro UV:** La capa de ozono (O₃) absorbe la mayor parte de la 
               radiación ultravioleta del Sol.
            2. **Destrucción de meteoritos:** La fricción con el aire incinera 
               a la mayoría de meteoritos antes de que toquen el suelo.
            3. **Regulación térmica:** Distribuye el calor solar, evita extremos 
               de temperatura entre el día y la noche.
            4. **Base del clima:** Los vientos y el vapor de agua permiten el 
               ciclo hidrológico y los patrones climáticos.
            """)
            st.warning("### ⚙️ Fenómenos Asociados")
            st.markdown("""
            - **Incandescencia:** La fricción convierte la energía cinética del 
              meteorito en calor, generando una "estrella fugaz".
            - **Efecto invernadero natural:** Los gases traza retienen parte del 
              calor, manteniendo la temperatura media en 15 °C en lugar de -18 °C.
            """)
            st.error("### 🧠 Dato Clave")
            st.markdown("""
            Sin atmósfera no habría sonido, no habría clima, no habría 
            respiración aerobia y los meteoritos golpearían la superficie 
            sin frenar, como ocurre en la Luna.
            """)

    st.write("---")
    with st.expander("📝 Pon a prueba tus conocimientos sobre la Atmósfera"):
        for q in CUESTIONARIO["atmosfera"]:
            ans = st.radio(q["pregunta"], q["opciones"], key=q["id"])
            if st.button("Validar Respuesta", key=f"btn_{q['id']}"):
                if ans == q["correcta"]:
                    st.success("🎉 ¡Excelente! Respuesta correcta.")
                else:
                    st.error(f"❌ Incorrecto. Pista: {q['pista']}")

# ============================================================
# PESTAÑA 3: CICLO DEL AGUA
# ============================================================
with tab_ciclo:
    st.header("🔄 El Ciclo del Agua: El Motor Hidrológico")

    sub1, sub2 = st.tabs([
        "💧 Etapas del Ciclo",
        "⚠️ Importancia y Alteraciones"
    ])

    with sub1:
        col1, col2 = st.columns([1.2, 1])
        with col1:
            mostrar_imagen(IMAGENES["CicloAgua_Etapas"], "Etapas del ciclo hidrológico.")
        with col2:
            st.success("### 💧 ¿Qué es el Ciclo del Agua?")
            st.markdown("""
            Es el movimiento continuo del agua entre la **hidrósfera**, la **atmósfera**, 
            la **litósfera** y la **biósfera**. No tiene principio ni fin: es un ciclo 
            cerrado con una duración estimada de **9 a 10 días** por vuelta completa.
            """)
            st.info("### 📊 Las 5 Etapas Principales")
            st.markdown("""
            1. **Evaporación:** El Sol calienta el agua de océanos, ríos y lagos, 
               convirtiéndola en vapor que sube a la atmósfera.
            2. **Transpiración:** Las plantas liberan vapor de agua por sus hojas 
               (junto con la evaporación se llama **evapotranspiración**).
            3. **Condensación:** El vapor sube, se enfría y forma nubes.
            4. **Precipitación:** El agua cae como lluvia, nieve o granizo.
            5. **Infiltración y Escorrentía:** El agua penetra en el suelo 
               (recarga acuíferos) o corre por la superficie hacia ríos y mares.
            """)
            st.warning("### 🌍 Reservorios de Agua")
            st.markdown("""
            - **Océanos:** 97% del agua total.
            - **Glaciares y casquetes:** 2% (la mayor parte del agua dulce).
            - **Agua subterránea:** ~0.6%.
            - **Ríos y lagos:** ~0.01% (¡el agua que usamos!).
            - **Atmósfera:** 0.001% (vapor de agua).
            """)

    with sub2:
        col1, col2 = st.columns([1.2, 1])
        with col1:
            mostrar_imagen(IMAGENES["CicloAgua_Alteraciones"], "Alteraciones humanas del ciclo hidrológico.")
        with col2:
            st.success("### ⚠️ Importancia del Ciclo")
            st.markdown("""
            El ciclo del agua es **vital** porque:
            - Distribuye agua dulce a todos los ecosistemas.
            - Regula el clima global (transporte de calor).
            - Modela el relieve (erosión y sedimentación).
            - Permite la fotosíntesis y la vida en general.
            """)
            st.error("### 🚨 Alteraciones Humanas")
            st.markdown("""
            - **Deforestación:** Reduce la transpiración de las plantas y, por 
              tanto, la formación de nubes y lluvias (ej. Amazonía).
            - **Contaminación:** Fertilizantes, pesticidas y desechos 
              industriales contaminan ríos, lagos y acuíferos.
            - **Urbanización:** El asfalto y concreto impiden la infiltración; 
              el agua corre rápido y provoca inundaciones.
            - **Cambio climático:** Altera los patrones de precipitación y 
              provoca sequías o lluvias extremas.
            - **Sobreexplotación de acuíferos:** Se extrae más agua de la que 
              se recarga naturalmente.
            """)
            st.warning("### 💡 Reflexión")
            st.markdown("""
            Cuidar el ciclo del agua **no es solo ahorrar agua en casa**: implica 
            proteger bosques, evitar la contaminación y planear ciudades que 
            respeten el ciclo natural.
            """)

    st.write("---")
    with st.expander("📝 Pon a prueba tus conocimientos sobre el Ciclo del Agua"):
        for q in CUESTIONARIO["ciclo_agua"]:
            ans = st.radio(q["pregunta"], q["opciones"], key=q["id"])
            if st.button("Validar Respuesta", key=f"btn_{q['id']}"):
                if ans == q["correcta"]:
                    st.success("🎉 ¡Excelente! Respuesta correcta.")
                else:
                    st.error(f"❌ Incorrecto. Pista: {q['pista']}")

# ============================================================
# PESTAÑA 4: FOTOSÍNTESIS
# ============================================================
with tab_foto:
    st.header("🌿 La Fotosíntesis: La Fábrica de la Vida")

    sub1, sub2 = st.tabs([
        "🌞 Proceso y Ecuación",
        "⚙️ Fases (Luminosa y Calvin)"
    ])

    with sub1:
        col1, col2 = st.columns([1.2, 1])
        with col1:
            mostrar_imagen(IMAGENES["Fotosintesis_Proceso"], "Esquema general de la fotosíntesis.")
        with col2:
            st.success("### 🌞 ¿Qué es la Fotosíntesis?")
            st.markdown("""
            Es el proceso mediante el cual **plantas, algas y cianobacterias** 
            convierten la **energía solar** en **energía química** (glucosa), 
            liberando oxígeno como subproducto.
            """)
            st.info("### 📊 Ecuación General")
            st.markdown("""
            **6 CO₂ + 6 H₂O + Luz solar → C₆H₁₂O₆ + 6 O₂**
            
            - **Reactivos:** Dióxido de carbono (CO₂) + Agua (H₂O) + Luz.
            - **Productos:** Glucosa (C₆H₁₂O₆) + Oxígeno (O₂).
            """)
            st.warning("### 🌍 Importancia Global")
            st.markdown("""
            - **Libera el oxígeno** que respiramos (todo el O₂ atmosférico 
              proviene de la fotosíntesis).
            - **Captura el CO₂** atmosférico, regulando el clima.
            - **Es la base de la cadena trófica** en casi todos los ecosistemas.
            - **Produce biomasa:** el 99.9% de la materia orgánica del planeta.
            """)
            st.error("### 🌱 Organismos Fotosintéticos")
            st.markdown("""
            - **Plantas terrestres:** árboles, pastos, cultivos.
            - **Algas:** verdes, rojas, pardas.
            - **Cianobacterias:** bacterias fotosintéticas ancestrales.
            - **Fitoplancton:** responsable del **50%** del oxígeno del planeta.
            """)

    with sub2:
        col1, col2 = st.columns([1.2, 1])
        with col1:
            mostrar_imagen(IMAGENES["Fotosintesis_Fases"], "Fase luminosa (tilacoides) y Ciclo de Calvin (estroma).")
        with col2:
            st.success("### ⚙️ Las Dos Fases de la Fotosíntesis")
            st.markdown("""
            La fotosíntesis ocurre en dos etapas complementarias dentro del **cloroplasto**.
            """)
            st.info("### ☀️ Fase Luminosa (en los Tilacoides)")
            st.markdown("""
            - Ocurre **en presencia de luz**.
            - La **clorofila** capta fotones y los convierte en energía química.
            - Se produce la **fotólisis del agua:** H₂O → 2H⁺ + ½O₂ + 2e⁻.
            - Se generan **ATP** y **NADPH** (moléculas energéticas).
            - **Producto clave:** Oxígeno (O₂) liberado a la atmósfera.
            """)
            st.warning("### 🌑 Ciclo de Calvin (en el Estroma)")
            st.markdown("""
            - Ocurre **sin necesidad de luz directa** (fase oscura).
            - Usa el **ATP** y **NADPH** de la fase luminosa.
            - Fija el **CO₂** y lo convierte en glucosa mediante 3 etapas:
                1. **Fijación de carbono:** El CO₂ se une a la RuBP.
                2. **Reducción:** Se forman moléculas de G3P.
                3. **Regeneración:** Se reconstruye la RuBP.
            - **Producto clave:** Glucosa (C₆H₁₂O₆).
            """)
            st.error("### 🧠 Dato Clave")
            st.markdown("""
            Cada año, la fotosíntesis global **captura ~120 mil millones de toneladas 
            de carbono** y libera ~130 mil millones de toneladas de oxígeno. 
            ¡Sin ella, la vida en la Tierra no existiría!
            """)

    st.write("---")
    with st.expander("📝 Pon a prueba tus conocimientos sobre la Fotosíntesis"):
        for q in CUESTIONARIO["fotosintesis"]:
            ans = st.radio(q["pregunta"], q["opciones"], key=q["id"])
            if st.button("Validar Respuesta", key=f"btn_{q['id']}"):
                if ans == q["correcta"]:
                    st.success("🎉 ¡Excelente! Respuesta correcta.")
                else:
                    st.error(f"❌ Incorrecto. Pista: {q['pista']}")

# ============================================================
# PESTAÑA 5: QUIMIOSÍNTESIS
# ============================================================
with tab_quimio:
    st.header("⚗️ La Quimiosíntesis: Vida Sin Luz Solar")

    sub1, sub2 = st.tabs([
        "🔬 Proceso y Organismos",
        "🌋 Importancia en el Planeta"
    ])

    with sub1:
        col1, col2 = st.columns([1.2, 1])
        with col1:
            mostrar_imagen(IMAGENES["Quimiosintesis_Proceso"], "Proceso de quimiosíntesis en bacterias.")
        with col2:
            st.success("### ⚗️ ¿Qué es la Quimiosíntesis?")
            st.markdown("""
            Es el proceso mediante el cual **bacterias y arqueas** obtienen energía 
            **oxidando compuestos inorgánicos** (sin necesidad de luz solar), 
            y usan esa energía para producir materia orgánica.
            """)
            st.info("### 🔬 Organismos Quimiosintéticos")
            st.markdown("""
            - **Bacterias nitrificantes:** *Nitrosomonas*, *Nitrobacter*.
            - **Bacterias sulfurosas:** *Thiobacillus*.
            - **Arqueas metanogénicas:** productoras de metano.
            - **Bacterias del hierro:** oxidan Fe²⁺ a Fe³⁺.
            """)
            st.warning("### ⚡ Reacciones Típicas")
            st.markdown("""
            - **Nitrificación:** NH₄⁺ → NO₂⁻ → NO₃⁻.
            - **Oxidación de azufre:** H₂S → S → SO₄²⁻.
            - **Oxidación de hierro:** Fe²⁺ → Fe³⁺.
            - **Metanogénesis:** CO₂ + H₂ → CH₄.
            """)
            st.error("### 🧠 Diferencia con la Fotosíntesis")
            st.markdown("""
            - **Fotosíntesis:** Usa **luz solar** como fuente de energía.
            - **Quimiosíntesis:** Usa **energía química** de compuestos inorgánicos.
            - Ambas producen **materia orgánica** a partir de CO₂.
            """)

    with sub2:
        col1, col2 = st.columns([1.2, 1])
        with col1:
            mostrar_imagen(IMAGENES["Quimiosintesis_Ambientes"], "Ambientes donde ocurre la quimiosíntesis.")
        with col2:
            st.success("### 🌋 ¿Dónde Ocurre?")
            st.markdown("""
            La quimiosíntesis se da en **ambientes extremos** donde no llega la luz solar.
            """)
            st.info("### 📍 Ambientes Principales")
            st.markdown("""
            1. **Fuentes hidrotermales:** Fumarolas negras en el fondo oceánico 
               (hasta 4,000 m de profundidad).
            2. **Subsuelo terrestre:** Hasta 10 km de profundidad en rocas.
            3. **Suelo agrícola:** Bacterias nitrificantes que producen nitratos.
            4. **Aguas termales y volcanes:** Ambientes sulfurosos.
            5. **Intestinos de animales:** Microbiota metanogénica.
            """)
            st.warning("### 🌍 Importancia Ecológica")
            st.markdown("""
            - **Base de ecosistemas abisales:** En las fuentes hidrotermales, la 
              quimiosíntesis sostiene comunidades enteras (gusanos tubícolas, 
              almejas gigantes, cangrejos yeti) sin necesidad de luz solar.
            - **Fertilidad del suelo:** La nitrificación produce los **nitratos** 
              que las plantas absorben. ¡Sin ella, la agricultura no existiría!
            - **Ciclos biogeoquímicos:** Participa en el ciclo del nitrógeno, 
              azufre y carbono.
            - **Origen de la vida:** Se cree que los primeros seres vivos fueron 
              quimiosintéticos, en las profundidades oceánicas.
            """)
            st.error("### 🧠 Dato Clave")
            st.markdown("""
            La quimiosíntesis representa solo el **0.1%** de la producción primaria 
            global, pero es **esencial** en los ecosistemas donde la luz no llega. 
            ¡Demuestra que la vida se abre camino incluso en la oscuridad total!
            """)

    st.write("---")
    with st.expander("📝 Pon a prueba tus conocimientos sobre la Quimiosíntesis"):
        for q in CUESTIONARIO["quimiosintesis"]:
            ans = st.radio(q["pregunta"], q["opciones"], key=q["id"])
            if st.button("Validar Respuesta", key=f"btn_{q['id']}"):
                if ans == q["correcta"]:
                    st.success("🎉 ¡Excelente! Respuesta correcta.")
                else:
                    st.error(f"❌ Incorrecto. Pista: {q['pista']}")

# ============================================================
# PESTAÑA 6: GLOSARIO
# ============================================================
with tab_glosario:
    st.header("📖 Glosario de Términos Clave")
    st.markdown("Consulta las definiciones de los conceptos más importantes de esta Web. Cada término se despliega al hacer clic.")

    glosario = [
        ("Polaridad",
         "Distribución desigual de carga eléctrica en una molécula. La molécula de agua es polar porque tiene un polo δ+ (hidrógenos) y un polo δ− (oxígeno)."),
        ("Puente de hidrógeno",
         "Atracción intermolecular entre el H (δ+) de una molécula y el O (δ−) de otra. Es más débil que un enlace covalente, pero le da al agua sus propiedades únicas."),
        ("Ion",
         "Átomo o molécula con carga eléctrica neta, resultado de ganar o perder electrones."),
        ("Catión",
         "Ion con carga positiva porque perdió electrones. Ejemplos: Na⁺, Ca²⁺, Mg²⁺, K⁺."),
        ("Anión",
         "Ion con carga negativa porque ganó electrones. Ejemplos: Cl⁻, SO₄²⁻, HCO₃⁻."),
        ("ppm",
         "Partes por millón. 1 ppm = 0.0001% en volumen. Se usa para medir gases traza en la atmósfera."),
        ("Salinidad",
         "Masa total de sales disueltas por kilogramo de agua. La salinidad media del océano es 35 g/kg (3.5%)."),
        ("Capa de ozono",
         "Zona de la estratosfera rica en ozono (O₃) que absorbe la mayor parte de la radiación ultravioleta del Sol."),
        ("Tensión superficial",
         "Propiedad de la superficie del agua que actúa como una 'piel elástica', debido a la cohesión entre moléculas por puentes de hidrógeno."),
        ("Ciclo hidrológico",
         "Movimiento continuo del agua entre la hidrósfera, atmósfera, litósfera y biósfera. Incluye evaporación, condensación, precipitación e infiltración."),
        ("Evapotranspiración",
         "Suma de la evaporación del agua del suelo y la transpiración de las plantas. Es clave en la formación de nubes y lluvias."),
        ("Fotosíntesis",
         "Proceso por el cual plantas, algas y cianobacterias convierten luz solar, CO₂ y H₂O en glucosa y oxígeno. Base de casi todas las cadenas tróficas."),
        ("Cloroplasto",
         "Organelo celular donde ocurre la fotosíntesis. Contiene tilacoides (fase luminosa) y estroma (Ciclo de Calvin)."),
        ("Tilacoide",
         "Membrana interna del cloroplasto donde ocurre la fase luminosa de la fotosíntesis. Produce ATP, NADPH y libera O₂."),
        ("Estroma",
         "Líquido interno del cloroplasto donde ocurre el Ciclo de Calvin (fase oscura). Fija el CO₂ en glucosa."),
        ("Ciclo de Calvin",
         "Conjunto de reacciones de la fase oscura de la fotosíntesis que fijan el CO₂ en glucosa, usando ATP y NADPH."),
        ("Quimiosíntesis",
         "Proceso por el cual bacterias y arqueas obtienen energía oxidando compuestos inorgánicos (sin luz solar) y producen materia orgánica."),
        ("Fuente hidrotermal",
         "Grieta en el fondo oceánico que libera agua caliente rica en minerales. Sostiene ecosistemas quimiosintéticos sin luz solar."),
        ("Nitrificación",
         "Proceso bacteriano que convierte amoniaco (NH₄⁺) en nitritos (NO₂⁻) y luego en nitratos (NO₃⁻). Fundamental para la fertilidad del suelo."),
        ("Biomasa",
         "Masa total de materia orgánica viva en un ecosistema. La fotosíntesis es su principal fuente de producción.")
    ]

    for termino, definicion in glosario:
        with st.expander(f"📌 {termino}"):
            st.markdown(definicion)