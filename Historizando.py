import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

# Leitura dos dados do arquivo CSV
data = pd.read_csv('dados.csv')

# Plotagem dos dados
plt.figure(figsize=(10, 5))
plt.plot(data['tempo'], data['temperatura'], label='Temperatura')
plt.xlabel('Tempo (ms)')
plt.ylabel('Temperatura (°C)')
plt.title('Temperatura ao longo do tempo')
plt.legend()
plt.grid(True)
plt.savefig('relatorio.png')
plt.show()




# Criação do PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)

# Adicionar título
pdf.cell(0, 10, 'Relatório de Temperatura', 0, 1, 'C')

# Adicionar imagem do gráfico
pdf.image('relatorio.png', x=10, y=30, w=190)

# Salvar o PDF
pdf.output('relatorio.pdf')
