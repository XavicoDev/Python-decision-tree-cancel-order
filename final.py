# -*- coding: utf-8 -*-
"""
Created on Wed May  3 22:04:42 2023

@author: Xavico
"""
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.tree import export_graphviz
import graphviz
from sklearn.tree import export_text
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
# Cargar datos
data = pd.read_csv('C:\\Users\\Xavico\\Documents\\MCD\\5. MINERIA DE DATOS\\DT.csv', encoding="UTF-8", sep=';')
#X = data.iloc[:, 1:]
X = data
X = X.drop('Fe_Factura', axis=1)
X = X.drop('Resp_Pago', axis=1)
X = X.drop('DenominaciOn', axis=1)
X = X.drop('Cl_Factura', axis=1)

# Seleccionar las columnas a transformar
cols_to_transform = ['T_doc_Com','Desc_tipo_doc','Material', 'Desc_tipo_doc', 'Desc_tipo_doc', 'Canal', 'tipo_persona', 'Poblacion',  'Segmento', 'Marca']
df=X
encoders = {}
le = LabelEncoder()
for col in cols_to_transform:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = {"encoder": le, "labels": le.classes_}

encoders["Canal"]["encoder"]
encoders["Poblacion"]["labels"]

df['F_Pedido'] = pd.to_datetime(df['F_Pedido'])
# crea las nuevas columnas
df['dia'] = df['F_Pedido'].dt.day
df['mes'] = df['F_Pedido'].dt.month
df['anio'] = df['F_Pedido'].dt.year
# elimina la columna original
df.drop('F_Pedido', axis=1, inplace=True)
df = df.replace(',', '.', regex=True)
df['Vendedor'] = pd.factorize(df['Vendedor'])[0] + 1
df.isna()
df.isna().sum()
df = df.dropna()

# Separar variables independientes y dependiente
#datos = datos.drop('x2', axis=1)
X = df.iloc[:, 1:]
# Codificar variable dependiente
y = df.iloc[:, :1]
#label_encoder = LabelEncoder()
#y = label_encoder.fit_transform(y)

# Construir el árbol de decisión
clf = DecisionTreeClassifier(random_state=0,max_depth=3)
clf.fit(X, y)

# Visualizar el árbol de decisión
plot_tree(clf)


# Exportar el árbol de decisión en formato SVG
#dot_data = export_graphviz(clf, out_file=None, filled=True, rounded=True, special_characters=True)
#graph = graphviz.Source(dot_data)
#graph.format = 'svg'
#graph.render("C:\\Users\\Xavico\\Documents\\MCD\\5. MINERIA DE DATOS\\arbol_decision1")

# Exportar el árbol de decisión en formato PDF
#dot_data = export_graphviz(clf, out_file=None, filled=True, rounded=True, special_characters=True)
#graph = graphviz.Source(dot_data)
#graph.format = 'pdf'
#graph.render("C:\\Users\\Xavico\\Documents\\MCD\\5. MINERIA DE DATOS\\arbol_decision2")

dt = DecisionTreeClassifier(max_depth=3)
dt.fit(X, y)
plot_tree(dt, feature_names=X.columns, class_names=['NO ANULADO', 'ANULADO'], filled=True, proportion=True)
#plt.figure(figsize=(16, 12))
plt.figure(figsize=(20, 16))
plot_tree(dt, feature_names=X.columns, class_names=['NO ANULADO', 'ANULADO'], filled=True, proportion=True, impurity=False, node_ids=True, fontsize=12)


tree_text = export_text(dt, feature_names=X.columns.tolist())
print(tree_text)

