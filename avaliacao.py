from datetime import datetime

mes = f"{datetime.now().month:02d}"


print("=== Avaliação Inicial ===")
num = input("Número do atendimento: ")
objetivo = input("Objetivo: ")
peso_altura = input("Peso e altura: ")
lesao = input("Lesão ou restrição: ")
nivel = input("Nível: ")
local_tempo_freq = input("Local, tempo e frequência: ")
obs = input("Observação: ")
dia = input("Dia: ")
mes = input("Mês: ")

texto = (
    f"\n\n{num}° Atendimento / Objetivo: {objetivo} / Peso e Altura: {peso_altura} "
    f"/ Lesão ou Restrição: {lesao} / Nível: {nivel} / Local, Tempo e Frequência: {local_tempo_freq} "
    f"/ Observação: {obs} / Att Vinícius Ghilardi em {dia}/{mes}/2025."
)

print(texto)