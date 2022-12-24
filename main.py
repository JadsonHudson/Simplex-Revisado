from time import sleep
from Simplex import Simplex
import os
menu_options = {
    1: 'Inserir o dados',
    2: 'Resolver',
    3: 'Apresentar',
    0: 'Exit',
}

def main():
  opt = 1
  
  simplex = None
  while opt != 0 :
    os.system('clear') or None
    
    print_menu()
    
    opt = int(input("\n"))
    
    os.system('clear') or None
    match opt:
      case 1:
        qtdVariaveis = int(input("Quantas variavéis possue o problema: "))
        qtdRestricoes = int(input("Quantas restrições possue o problema: "))
        simplex = Simplex(qtdVariaveis, qtdRestricoes)
        simplex.initialize_tableau() 
      case 2:
        if simplex is None:
          print("Não existe matriz para resolver! Por favor, insira.")
          continue
        simplex.initialize_matrix()
        simplex.solve()
        sleep(5)
      case 3:
        if simplex is None:
          print("Não existe matriz para apresentar! Por favor, insira.")
          continue
        simplex.presentation()
        sleep(2)
      case 0:
        print("Finalizando o programa... ")
        return
      case _:
        print(f'Erro! Opção inválida, tente novamente...')
        sleep(3)
      
def print_menu():
  global menu_options
  print("-"*10,"SIMPLEX REVISADO", "-"*11)
  for key in menu_options.keys():
      print('|', key, '-', f'{menu_options[key]:<32}|')
  print("-"*39)

main()