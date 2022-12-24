import numpy as np
from time import sleep
class Simplex:
  # Inicialização do tableau com o tamanho. obs.: considero os valores da base e função objetivo também.
  def __init__(self, qtdVariaveis: int, qtdRestricoes: int):
    self.qtdVariaveis = qtdVariaveis
    self.qtdRestricoes = qtdRestricoes
    self.qtdVariaveisDecisao = self.qtdVariaveis - self.qtdRestricoes
    self.table = np.zeros((self.qtdRestricoes+1, self.qtdVariaveis+1), dtype=float)
  
  def menorRazao(self, colunaEntra: int) -> int:
    razoes = [(self.table[i][self.qtdVariaveis]/self.table[i][colunaEntra]) for i in range(self.qtdRestricoes)]
    linhaSai = np.where(razoes == min(razoes))
    return linhaSai
  
  def alterar_matrizes(self, coluna, linha):
    self.matriz_R[0:self.qtdRestricoes, coluna] = coluna
    pass
  
  def resolver_tableau(self):
    # Busca o elemento que entrará na base
    maisNegativo = min(self.cr)
    if maisNegativo < 0:
      colunaEntra = np.where(self.cr == maisNegativo)
      linhaSai = self.menorRazao(colunaEntra)
      self.alterar_matrizes(colunaEntra, linhaSai)
    else:
      pass
    pass
  

  def montar_tableau(self):
    for i in range(self.qtdRestricoes+1):
      for j in range(self.qtdVariaveis+1):
        if i == self.qtdRestricoes and j != self.qtdVariaveis:
          self.table[i][j] = float(input(f'Valor da função-objetivo na posição M[{i}][{j}]: '))
          continue
        if i != self.qtdRestricoes and j == self.qtdVariaveis:
          self.table[i][j] = float(input(f'Valor da base na posição M[{i}][{j}]: '))
          continue
        self.table[i][j] = float(input(f'Valor na posição M[{i}][{j}]: '))
    self.matriz_R = self.table[0:self.qtdRestricoes, 0:self.qtdVariaveisDecisao]
    self.matriz_B = self.table[0:self.qtdRestricoes, self.qtdVariaveisDecisao:self.qtdVariaveis]
    self.b = self.table[0:self.qtdRestricoes, self.qtdVariaveis]
    self.cr = self.table[self.qtdRestricoes, 0:self.qtdVariaveisDecisao]
    self.cb = self.table[self.qtdRestricoes, self.qtdVariaveisDecisao:self.qtdVariaveis]
    self.resolver_tableau()
  
  def apresentar(self):
    print(self.table)
    print("\n-----------MATRIZ R-----------")
    print(self.matriz_R)
    print("\n-----------MATRIZ B-----------")
    print(self.matriz_B)
    print("\n-----------MATRIZ cr-----------")
    print(self.cr)
    print("\n-----------MATRIZ cb-----------")
    print(self.cb)
    print("\n-----------MATRIZ b-----------")
    print(self.b)
    pass