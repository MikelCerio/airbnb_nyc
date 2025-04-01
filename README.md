# Proyecto de Análisis de Precios y Predicción en Airbnb NYC

Este proyecto analiza y predice precios de alojamientos en Airbnb de la ciudad de Nueva York usando técnicas de ciencia de datos, visualización avanzada y modelos de machine learning.

## 📂 Dataset
- Fuente: Kaggle - `AB_NYC_2019.csv`
- Observaciones: 48.000+ alojamientos
- Variables: ubicación (lat/lon), tipo de alojamiento, precio por noche, disponibilidad, reviews, etc.

---

## 📈 Análisis Exploratorio (EDA)
- Limpieza de outliers en precios (>500$)
- Distribución de precios por barrio y tipo de alojamiento
- Comparativa entre índices de disponibilidad y precio

## 🌍 Visualización geoespacial
- **Mapa de calor con `folium`** para mostrar zonas de alto y bajo valor
- **Mapa interactivo con `plotly.express`** usando coordenadas y precios como intensidad

## 🚀 Modelo Predictivo
- **Random Forest Regressor**
- Variables usadas: tipo de alojamiento, barrio, disponibilidad, reviews
- **MAE obtenido**: ~45€ de error promedio

### 🔍 Visualización de resultados
- Gráfico `scatter` con precios reales vs. predichos
- Buena precisión general, especialmente en el rango crítico de 50€ a 200€ por noche

---

## 📄 Tecnologías utilizadas
- Python, Pandas, Seaborn, Matplotlib
- Scikit-learn, Folium, Plotly

---

## 🌐 Reproducibilidad
1. Clona este repo
2. Instala dependencias:
```bash
pip install -r requirements.txt
```
3. Ejecuta `Airbnb_NYC_Analysis.ipynb`

---

## 🚀 Autor
[Mikel Cerio Chinchurreta](https://www.linkedin.com/in/mikelcerio-data-analyst)
> Especialista en Business Intelligence con experiencia real en revenue management, estrategia de datos y automatización.
> "Convierto datos en decisiones rentables."

