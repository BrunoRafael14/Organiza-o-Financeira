import os 
import csv

class Categorias:
    def __init__(self, nome):
        self.nome_categoria = nome




class Faturamento:
    def __init__(self, nome, valor, data, categoria):
        self.nome = nome
        self.valor = valor
        self.categoria = categoria
        self.data = data

    def cadastrar_movimentacao(self):

        if self.valor >= 0:
            arquivo_vazio = os.path.getsize("informacoes/dados/receitas.csv") == 0

            if arquivo_vazio:
                with open("informacoes/dados/receitas.csv", "a", encoding="utf-8", newline="") as file:
                    gravador = csv.writer(file)   
                    gravador.writerow(("Nome", "Valor", "Data", "categoria"))

            with open('informacoes/dados/receitas.csv', 'a') as file:
                gravador = csv.writer(file)

                gravador.writerow((self.nome, self.valor, self.data, self.categoria))