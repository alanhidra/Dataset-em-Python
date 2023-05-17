import pandas as pd
import matplotlib.pyplot as plt

# Importar o arquivo CSV da Tesla e criar o DataFrame
df = pd.read_csv('TSLA.csv')

# Converter a coluna 'Date' para o formato de data do pandas
df['Date'] = pd.to_datetime(df['Date'])

# Gráfico de barras do preço de fechamento
plt.figure()
plt.bar(df['Date'], df['Close'])
plt.xlabel('Data')
plt.ylabel('Preço de Fechamento')
plt.title('Variação do Preço de Fechamento das Ações da Tesla')
plt.xticks(rotation=45)

# Gráfico de linhas do volume de negociação
plt.figure()
plt.plot(df['Date'], df['Volume'])
plt.xlabel('Data')
plt.ylabel('Volume de Negociação')
plt.title('Variação do Volume de Negociação das Ações da Tesla')
plt.xticks(rotation=45)

# Gráfico de dispersão entre o preço de fechamento e o volume de negociação
plt.figure()
plt.scatter(df['Volume'], df['Close'])
plt.xlabel('Volume de Negociação')
plt.ylabel('Preço de Fechamento')
plt.title('Relação entre Volume de Negociação e Preço de Fechamento')
plt.xticks(rotation=45)

# Exibir os gráficos em janelas separadas
plt.show()
