from time import sleep
import numpy as np
class Simplex:
  def __init__(self, amount_variables : int, amount_restrictions : int):
    self.amount_variables = amount_variables + 1
    self.amount_restrictions = amount_restrictions + 1
    self.amount_decision_variables = self.amount_variables - self.amount_restrictions
    self.tableau = np.zeros((self.amount_restrictions, self.amount_variables), dtype=float)
    self.objetive_function = None
    self.list_indices_in_base = None

# Inserção dos dados do tableau
  def initialize_tableau(self):
    for line in range(self.amount_restrictions):
      for column in range(self.amount_variables):
        if line == (self.amount_restrictions - 1) and column < (self.amount_variables - 1):
          self.tableau[line][column] = float(input(f'Valor do coeficiente {column + 1} da função-objetivo: '))
          continue
        elif line < (self.amount_restrictions - 1) and column == (self.amount_variables - 1):
          self.tableau[line][column] = float(input(f'Valor da restrição {line + 1}: '))
          continue
        elif line == (self.amount_restrictions - 1) and column == (self.amount_variables - 1):
          self.tableau[line][column] = float(input(f'Valor da função-objetivo: '))
          self.objetive_function = self.tableau[line][column]
          continue
        self.tableau[line][column] = float(input(f'Valor na posição M[{line+1}][{column+1}]: '))
  
# Encontrar a coluna que entrará na base do Tableau
  def entry_column(self) -> int:
    pass

# Encontrar a linha que sairá da base do Tableau
  def output_line(self) -> int:
    pass

# Atualizar as matrizes
  def matrix_update(self):
    pass

# Inserir os novos valores da matriz
  def recalculate_matrices(self):
    pass
  
# Atualizar o tableau
  # def uptade_tableau(self):
  #   pass

# Inicializar as matrix (matrix_R, matrix_B, matrix_b, matrix_cr, matrix_cb, objetive function, list_indices_in_base)
  def initialize_matrix(self):
    self.matrix_R = self.tableau[0:self.amount_restrictions-1, 0:self.amount_decision_variables].copy()
    self.matrix_B = self.tableau[0:self.amount_restrictions-1,
                                 self.amount_decision_variables:self.amount_variables-1].copy()
    self.matrix_b =self.tableau[0:self.amount_restrictions-1, self.amount_variables-1].copy()
    self.matrix_cr =self.tableau[self.amount_restrictions-1, 0:self.amount_decision_variables].copy()
    self.matrix_cb = self.tableau[self.amount_restrictions-1, self.amount_decision_variables:self.amount_variables-1].copy()
    self.objetive_function = self.tableau[self.amount_restrictions-1, 0:self.amount_variables-1].copy()
    self.index_of_base_variables = [value for value in range(self.amount_decision_variables,self.amount_variables-1)]
    # print(f"\nVariáveis básicas\n-----------\n{self.index_of_base_variables}\n-----------\n\n")
# Função que retorna o valor da função objetivo
  def objective_function_value(self) -> float:
    total = 0
    i = 0
    for value in self.matrix_b:
      index = self.index_of_base_variables[i]
      total += self.objetive_function[index] * value
      i += 1
    return total
# Resolver o simplex(método principal) - Testar a solução.
  def solve(self):
    # print("\n\n--------------------------------------------------------\n\n")
    if min(self.matrix_cr) < 0:
      # Encontrando a coluna que entra e a linha que sai
      maisNegativo = min(self.matrix_cr)
      colunaEntra = int(np.where(self.matrix_cr == maisNegativo)[0])
      razoes = [(self.tableau[i][self.amount_variables-1]/self.tableau[i][colunaEntra]) for i in range(self.amount_restrictions-1)]
      linhaSai = razoes.index(min(razoes))
      
      # Atualizando os valores das matrizes para realizar as multiplicações.
      self.index_of_base_variables[linhaSai] = colunaEntra
      temp = self.matrix_cr[colunaEntra]
      self.matrix_cr[colunaEntra] = self.matrix_cb[self.amount_decision_variables+linhaSai-2]
      temp_matrix_cb = self.matrix_cb.copy()
      temp_matrix_cb[self.amount_decision_variables+linhaSai-2] = temp
      temp_matrix_R = self.matrix_R.copy()
      temp_matrix_B = self.matrix_B.copy()
      self.matrix_R[:,colunaEntra], temp_matrix_B[:, linhaSai] = temp_matrix_B[:, linhaSai], temp_matrix_R[:, colunaEntra]
      
      # novos valores de R, cr e B
      new_cr = self.matrix_cr - np.dot(temp_matrix_cb, np.dot(np.linalg.inv(temp_matrix_B),self.matrix_R))
      new_R = np.dot(np.linalg.inv(temp_matrix_B), self.matrix_R)
      new_b = np.dot(np.linalg.inv(temp_matrix_B), self.matrix_b)
      # np.dot(temp_matrix_cb, np.dot(np.linalg.inv(temp_matrix_B), self.matrix_b))
      
      self.matrix_R[:] = new_R[:]
      self.matrix_cr[:] = new_cr[:]
      self.matrix_b[:] = new_b[:]
      # print(f"\nValor das variáveis básicas\n-----------\n{self.matrix_b}\n-----------\n\n")
      # print("----------------------------TABLEAU----------------------------")
      # print(self.tableau)
      # print("---------------------------------------------------------------")
      self.solve()
    elif min(self.matrix_cr) > 0:
      value = self.objective_function_value()
      print(f"\n\nResultado: {value} com as variáveis {[value + 1 for value in self.index_of_base_variables]} na base\n\n\n")
      sleep(10)
    pass
  
# Apresentação das informações do tableau
  def presentation(self):
    print(self.tableau)
    print("\n-----------MATRIZ R-----------")
    print(self.matrix_R)
    print("\n-----------MATRIZ B-----------")
    print(self.matrix_B)
    print("\n-----------MATRIZ cr-----------")
    print(self.matrix_cr)
    print("\n-----------MATRIZ cb-----------")
    print(self.matrix_cb)
    print("\n-----------MATRIZ b-----------")
    print(self.matrix_b)
    pass