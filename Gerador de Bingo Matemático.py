import random
from fpdf import FPDF

# Função para gerar uma cartela de bingo
def gerar_cartela():
  numeros = []
  for i in range(2, 6):
    for j in range(1, 11):
      numeros.append(i * j)
  random.shuffle(numeros)
  return numeros[:25]

# Função para gerar o PDF com as cartelas
def gerar_pdf(cartelas):
  pdf = FPDF()
  for cartela in cartelas:
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for i in range(5):
      for j in range(5):
        pdf.cell(20, 10, str(cartela[i * 5 + j]), border=1, align="center")
  pdf.output("cartelas_bingo.pdf")

# Quantidade de cartelas
quantidade_cartelas = int(input("Digite a quantidade de cartelas desejadas: "))

# Gerar cartelas
cartelas = []
for i in range(quantidade_cartelas):
  cartelas.append(gerar_cartela())

# Gerar PDF
gerar_pdf(cartelas)

print("As cartelas foram geradas e salvas no arquivo 'cartelas_bingo.pdf'.")
