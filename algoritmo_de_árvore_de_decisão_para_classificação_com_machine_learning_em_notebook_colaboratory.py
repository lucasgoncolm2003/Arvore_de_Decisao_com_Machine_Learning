# -*- coding: utf-8 -*-
"""Algoritmo de Árvore de Decisão para Classificação com Machine Learning em Notebook Colaboratory.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Qbj9aTRmROAXeoRTtM1KdQJH4HvVLi2p

# **Conceito de Árvore de Decisão em Machine Learning**
> A Árvore de Decisão possui uma Composição semelhante a um Fluxograma, com Etapas e Condições. É uma boa técnica pois oferece uma boa Compreensão para o Usuário e para a Machine Learning. Uma Árvore de Decisão é um Algoritmo de Aprendizado Supervisionado de Máquina usado para Classificação e Regressão, tanto para a Previsão de Categorias Discretas quanto para Valores Numéricos.

> Em um Fluxograma, a Árvore estabelece Nós de Decisão que se relacionam por Hierarquia. Existe também o Nó-Raiz, o mais importante e inicial, e os Nós-Folha, que são os resultados finais. O Nó-Raiz é um dos Atributos da Base de Dados e o Nó-Folha é a Classe de Resposta.
*   **Nó-Raiz**: Atributo Inicial da Base de Dados.
*   **Nó-Folha**: Atributo Final ou Resposta da Base de Dados.

> A Relação entre os Nós consiste em uma Condicional "se-então". Ao chegar em um Nó A, se a Condição dele for Verdadeira, ele vai para um lado da Árvore, se não for, vai para outro lado da Árvore. Esse Algoritmo opera com Recursividade, replicando Padrões na medida em que entra em Novos Níveis de Profundidade. Para encontrar os Nós e encaixá-los em suas Posições, Cálculos são fundamentais.
"""

# Importando o pandas
import pandas as pd

# Importando o dataset iris
from sklearn.datasets import load_iris

"""# **O Ganho de Informação e a Entropia**
> Uma abordagem comum é o Ganho de Informação e a Entropia. Essas Variáveis falam sobre a Desorganização e a Falta de Uniformidade em Dados. Quanto maior a Entropia, maior é o Caos e a Mistura entre os Dados. É preciso portanto, calcular a Entropia das Classes de Saída e o Ganho de Informação dos Atributos da Base de Dados. Quem tiver o Maior Ganho de Informação entre os Atributos deve ser o Nó-Raiz.

> Para dividir a Base de Dados em uma Árvore, existem Condições, dividindo a Base em Caminhos com Análise de Registros que satisfazem certa Condição. O Ganho de Informação é baseado nisso, pois quando os Registros Separados pela Condição tornam-se Homogêneos, há Alto Ganho de Informação, ou seja, é mais provável saber a Saída Esperada em relação à Base de Dados organizada da forma tal qual estava antes.
"""

# Retornando os dados
data = load_iris()

# Transformando em um DataFrame
iris = pd.DataFrame(data.data)
iris.columns = data.feature_names
iris['target'] = data.target
iris.head(100)

"""# **Aplicação e Conceito de Random Forest**
> As Árvores servem para Classificação ou Regressão, ambos tipos de Tarefas da Aprendizado Supervisionado. Essa Versatilidade explica o sucesso do algoritmo em comparação com o Naive-Bayes ou outros Algoritmos. Outra aplicação é quando existem Problemas de Diversos Rótulos. Ou seja, quando as Categorias de Classificação são Múltiplas, e não só duas. Outros Algoritmos apresentam Problemas com mais Complexidade, ao passo que com as Árvores, Cientistas de Dados podem lidar com isso de uma forma fácil.


> Com as Árvores, os Valores fora do Padrão (Outliers) ou Valores Atípicos não são prejudiciais, e poucos Tratamentos são precisos. O Algoritmo também funciona para Informações Categóricas ou Nominais, ou seja, não é preciso realizar a Conversão de Tipos de Dados. As Random Forests (Florestas Aleatórias) são casos usados para Classificação e Regressão, sendo um Conjunto de Árvores de Decisão que oferecem Predição sobre um Conjunto de Dados. A Categoria mais Recorrente nos Resultados das Árvores influencia na Avaliação da mesma para Tomada de Decisão.
"""

# Selecionando apenas as colunas de pétala e esses targets
iris1 = iris.loc[iris.target.isin([1,2]),['petal length (cm)', 'petal width (cm)', 'target']]

# Separando X e y
X = iris1.drop('target',axis=1)
y = iris1.target
X.head(100)

"""# **Montagens de Algoritmos de Árvore de Decisão**
> Existem Bibliotecas Auxiliares com Implementações prontas. É útil entender alguns conceitos como Entropia e Ganho de Informação, pois esses são passados para as Funções. Existem métodos fáceis e intuitivos para gerar o Algoritmo para conduzir Classificação ou Regressão:
*   **Python**: com Módulo DecisionTreeClassifier, da Sci-Kit Learn, com Funções fit e score para Treinamento e Configuração. Para ver se um Modelo conseguiu fazer o Aprendizado, usa-se o Método predict. O Matplotlib pode ser usado para Plotagem de Grafos.
*   **R**: No R, também pode-se ter facilidade para a Árvore Decisória. Bibliotecas como cTree, RPart e Tree podem conseguir criar esse Modelo com poucas linhas e de forma intuitiva. Também existe o Método "fit".
"""

# Fazendo o train_test_split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1, random_state=42)

# Visualizando os dados de treino
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.scatter(X_train['petal length (cm)'],
           X_train['petal width (cm)'],
           c=y_train)
ax.set(xlim=(2.9, 7), xticks=[3,4,5,6,7],
       ylim=(0.9, 2.7), yticks=[1,1.5,2,2.5])
plt.show()

# Importando a árvore de decisão
from sklearn import tree

# Criando o classificador
clf = tree.DecisionTreeClassifier(random_state=42)

"""# **Exemplos de Árvore de Decisão**
## Diagnóstico de Doenças
> Uma decision tree pode ser aplicada para identificar doenças a partir de informações cedidas ao algoritmo como treinamento — uma classificação. Nesse caso, o sistema apreende os dados, entende suas relações, realiza os cálculos a fim de entender quais são os nós mais importantes e ajusta as condições. 
## Previsão de Empréstimo 
> Outro tipo de uso é para previsão de um valor de empréstimo que pode ser concedido a um usuário do banco. Esse é um problema de regressão, pois requer uma informação numérica como saída. O sistema vai entender como a base de dados está organizada de acordo com os atributos e criar um modelo capaz de fazer essa previsão. 
## Análise de Sentimentos
> Não é incomum ver também aplicações na área da análise de sentimentos, subcategoria do campo de processamento de linguagem natural. O modelo entende os dados e tenta prever se um texto deve ser categorizado como positivo ou negativo, por exemplo. Para melhores resultados, a random forest é aplicada também.
## Previsão de Saída de Funcionários
> Outro uso muito específico é para o RH saber quando um funcionário está quase saindo da empresa por insatisfação. Com a análise de dados sobre cada um, o modelo entende a base de dados e consegue realizar uma predição, ou seja, uma classificação.


"""

# Fazendo o fit com os dados de treino
clf = clf.fit(X_train, y_train)

# Verificando o score
clf.score(X_train, y_train)

# Visualizando essa árvore
fig, ax = plt.subplots(figsize=(10,10))
tree.plot_tree(clf)
plt.show()

# Podemos adicionar essas regras no nosso gráfico
fig, ax = plt.subplots()
ax.scatter(X_train['petal length (cm)'], 
           X_train['petal width (cm)'], 
           c=y_train)
ax.plot([5.2,5.2],[0.9,1.45],'--r')
ax.plot([5.2,5.2],[1.58,1.75,],'--r')
ax.plot([2.9,4.95],[1.65,1.65],'--r')
ax.plot([4.95,5.2],[1.55,1.55],'--r')
ax.plot([4.95,4.95],[1.45,1.55],'--r')
ax.plot([4.95,5.2],[1.45,1.45],'--r')
ax.plot([4.95,5.2],[1.45,1.45],'--r')
ax.plot([4.95,4.95],[1.65,1.75],'--r')
ax.plot([4.95,5.2],[1.75,1.75],'--r')
ax.set(xlim=(2.9, 7), xticks=[3,4,5,6,7,8],
       ylim=(0.9, 2.7), yticks=[1,1.5,2,2.5,3])
plt.show()

"""# **Matriz de Confusão: Conceito e Aplicação**
> A Matriz de Confusão é uma Tabela que permite a Visualização do Desempenho de um Algoritmo de Classificação por meio de uma Tabela de Contingência 2x2 Especial, chamada de **Matriz de Erro**. Cada Linha da Matriz representa Instâncias de uma Classe Prevista enquanto cada Coluna representa Instâncias da Classe Atual. Isso ocorre para verificar se o Sistema confunde Duas Classes.

> A Tabela de Erro carrega Duas Dimensões (Atual e Prevista), e conjuntos de Classes Idênticos em ambas as Dimensões (cada Combinação das Dimensões e Classe é uma Variável na Tabela de Contingência). Em Análise Preditiva, a Matriz de Confusão é uma Tabela que relata:
*   **Verdadeiros Positivos**: Elemento 1x1 da Matriz.
*   **Falsos Positivos**: Elemento 1x2 da Matriz.
*   **Falsos Negativos**: Elemento 2x1 da Matriz.
*   **Verdadeiros Negativos**: Elemento 2x2 da Matriz.

> Isso permite uma Análise Detalhada do que a mera Proporção de Classificações Corretas (Precisão). A Precisão produzirá Resultados Enganosos se o Conjunto de Dados estiver desequilibrado; isto é, quando o Número de Observações em Diferentes Classes variam muito. Por exemplo, se houver 95 gatos e apenas 5 cachorros nos dados, um determinado Classificador pode classificar todas as observações como gatos. 

> A Precisão Geral seria de 95%, mas com mais detalhes o Classificador teria uma Taxa de Reconhecimento de 100% para a Classe de Gatos, mas uma Taxa de Reconhecimento de 0% para a Classe de Cães. O **F1 Score (ou F-Measure)** é ainda mais confiável em tais casos, e aqui renderia mais de 97,4%, enquanto remove o viés e produz 0 como a Probabilidade de uma Decisão Informada para qualquer forma de Suposição (aqui sempre supondo gato).








 
"""

# Fazendo a previsão e avaliando o erro
y_pred = clf.predict(X_test)
from sklearn.metrics import confusion_matrix
confusion_matrix(y_test,y_pred)

# Separando X e y da base completa
X = iris.drop('target',axis=1)
y = iris.target

# Fazendo o train_test_split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Criando o classificador e fazendo o fit
clf2 = tree.DecisionTreeClassifier(random_state=42).fit(X_train,y_train)

# Verificando o score
clf2.score(X_train,y_train)

# Visualizando essa árvore
fig, ax = plt.subplots(figsize=(10,8))
tree.plot_tree(clf2)
plt.show()

# Fazendo a previsão
y_pred2 = clf2.predict(X_test)

# Avaliando o modelo
confusion_matrix(y_test,y_pred2)