from informacoes.categorias import Faturamento
import os
import csv

# print("Informe qual ação deseja realizar:")
# print("1 - Cadastrar Movimentação")
# print("2 - Cadastrar Categoria")
# print("3 - Relatório de Movimentações")
# print("4 - Sair")
# menu = input("")

teste = Faturamento("Venda de Produto", 150.00, "2023-10-01", "Vendas")
teste.cadastrar_movimentacao()

