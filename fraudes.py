# =========================================================
# PROJETO DE MACHINE LEARNING - DETECÇÃO DE FRAUDES
# USANDO DATASET ONLINE DO TENSORFLOW
# =========================================================

# =========================
# IMPORTAÇÃO DAS BIBLIOTECAS
# =========================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    accuracy_score
)

# =========================================================
# CARREGANDO DATASET ONLINE
# =========================================================

url = "https://storage.googleapis.com/download.tensorflow.org/data/creditcard.csv"

# Lendo o dataset online
df = pd.read_csv(url)

# =========================================================
# MOSTRANDO BASE DE DADOS
# =========================================================

print("\nBASE DE DADOS:")
print(df.head())

# =========================================================
# INFORMAÇÕES DO DATASET
# =========================================================

print("\nINFORMAÇÕES:")
print(df.info())

# =========================================================
# ESTATÍSTICAS
# =========================================================

print("\nESTATÍSTICAS:")
print(df.describe())

# =========================================================
# QUANTIDADE DE FRAUDES
# =========================================================

print("\nQUANTIDADE DE FRAUDES:")
print(df['Class'].value_counts())

# =========================================================
# GRÁFICO DE FRAUDES
# =========================================================

df['Class'].value_counts().plot(kind='bar')

plt.title('Quantidade de Fraudes')

plt.xlabel('Classe')

plt.ylabel('Quantidade')

plt.show()

# =========================================================
# SEPARANDO ENTRADAS E SAÍDA
# =========================================================

# X = dados de entrada
X = df.drop('Class', axis=1)

# y = resultado esperado
y = df['Class']

print("\nENTRADAS:")
print(X.head())

print("\nSAÍDAS:")
print(y.head())

# =========================================================
# DIVISÃO TREINO E TESTE
# =========================================================

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.2,

    random_state=42
)

# =========================================================
# CRIANDO MODELO
# =========================================================

modelo = RandomForestClassifier(

    n_estimators=100,

    random_state=42,

    class_weight='balanced'
)

# =========================================================
# TREINANDO MODELO
# =========================================================

print("\nTREINANDO MODELO...")

modelo.fit(X_train, y_train)

print("\nMODELO TREINADO COM SUCESSO!")

# =========================================================
# PREVISÕES
# =========================================================

previsoes = modelo.predict(X_test)

print("\nPREVISÕES:")
print(previsoes)

# =========================================================
# RELATÓRIO
# =========================================================

print("\nRELATÓRIO DE CLASSIFICAÇÃO:")

print(classification_report(y_test, previsoes))

# =========================================================
# MATRIZ DE CONFUSÃO
# =========================================================

print("\nMATRIZ DE CONFUSÃO:")

print(confusion_matrix(y_test, previsoes))

# =========================================================
# ACCURACY
# =========================================================

accuracy = accuracy_score(y_test, previsoes)

print("\nACURÁCIA:")

print(f"{accuracy * 100:.2f}%")

# =========================================================
# IMPORTÂNCIA DAS VARIÁVEIS
# =========================================================

importancias = modelo.feature_importances_

resultado_importancia = pd.DataFrame({

    'Variável': X.columns,
    'Importância': importancias

})

print("\nIMPORTÂNCIA DAS VARIÁVEIS:")

print(resultado_importancia.sort_values(
    by='Importância',
    ascending=False
).head(10))

# =========================================================
# TESTE MANUAL
# =========================================================

print("\nTESTE MANUAL")

# IMPORTANTE:
# O dataset possui 30 colunas de entrada
# Precisamos criar uma transação com 30 valores

nova_transacao = X.iloc[0:1].copy()

# Alterando alguns valores para simular fraude
nova_transacao['Amount'] = 5000

print("\nNOVA TRANSAÇÃO:")
print(nova_transacao)

# =========================================================
# PREVISÃO
# =========================================================

resultado = modelo.predict(nova_transacao)

probabilidade = modelo.predict_proba(nova_transacao)

print("\nPROBABILIDADE:")

print(probabilidade)

# =========================================================
# RESULTADO FINAL
# =========================================================

if resultado[0] == 1:

    print("\nRESULTADO:")
    print("Transação Fraudulenta")

else:

    print("\nRESULTADO:")
    print("Transação Normal")

# =========================================================
# FIM DO PROJETO
# =========================================================
