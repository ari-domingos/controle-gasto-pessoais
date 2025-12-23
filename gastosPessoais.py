import os

meses = ["", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
categoria = ["", "Alimentação", "Transporte", "Moradia", "Lazer", "Cartão", "Outros"]

gastos = []

def adicionarGasto():
    while True:
        try:
            os.system("cls")

            print("\n" + "-" * 31)
            print("        ADICIONAR GASTO")
            print("-" * 31)

            print("\n---- Gasto de número (ID) ----") # ID
            idGasto = int(input(" ID: ")) 

            if idGasto < 0:
                os.system("cls")

                print("\n" + "-" * 37)
                print("Erro: digite apenas valores positivos")
                print("-" * 37)
                input("  Pressione ENTER para continuar...")
                continue

            idDuplicado = False
            for gasto in gastos:
                if gasto['id'] == idGasto:
                    os.system("cls")

                    print("\n" + "-" * 48)
                    print("Erro: já existe um ID com essa compra registrada")
                    print(f"\nID: {gasto['id']}\nMês: {meses[gasto['mes']]}\nCategoria: {categoria[gasto['categoria']]}\nValor: R$ {gasto['valor']:.2f}")
                    print("-" * 48)
                    input("     Pressione ENTER para continuar...")     

                    idDuplicado = True
                    break
            if idDuplicado:
                continue       
            

            print("\n---- Valor do gasto ----") # VALOR
            valorGasto = float(input(" R$ ")) 

            if valorGasto <= 0:
                os.system("cls")

                print("\n" + "-" * 37)
                print("Erro: digite apenas valores positivos")
                print("-" * 37)
                input("  Pressione ENTER para continuar...")
                continue

            print("\n------------ Mês do gasto --------------") # MÊS
            print(" 1. Janeiro    2. Fevereiro   3. Março")
            print(" 4. Abril      5. Maio        6. Junho")
            print(" 7. Julho      8. Agosto      9. Setembro")
            print(" 10. Outubro   11. Novembro   12. Dezembro")
            opcaoMes = int(input("\nEscolha o mês: "))
            
            if opcaoMes in (1, 2, 3, 4, 5 , 6, 7, 8, 9, 10, 11, 12):
                print(f"Mês: {meses[opcaoMes]}")

            else:
                os.system("cls")

                print("\n" + "-" * 34)
                print("Erro: digite apenas números (1-12)")
                print("-" * 34)
                input("Pressione ENTER para continuar...")
                continue

            print("\n--- Categoria ---")
            print(" 1. Alimentação")
            print(" 2. Transporte")
            print(" 3. Moradia")
            print(" 4. Lazer")
            print(" 5. Cartão")
            print(" 6. Outros")
            opcaoCategoria = int(input("\nEscolha a categoria: "))

            valorAlimentacao = 0
            valorTransporte = 0
            valorMoradia = 0
            valorLazer = 0
            valorCartao = 0
            valorOutros = 0

            if opcaoCategoria == 1:
                valorAlimentacao += valorGasto
                print(f"Categoria {categoria[opcaoCategoria]}")

            elif opcaoCategoria == 2:
                valorTransporte += valorGasto
                print(f"Categoria {categoria[opcaoCategoria]}")
            
            elif opcaoCategoria == 3:
                valorMoradia += valorGasto
                print(f"Categoria {categoria[opcaoCategoria]}")

            elif opcaoCategoria == 4:
                valorLazer += valorGasto
                print(f"Categoria {categoria[opcaoCategoria]}")

            elif opcaoCategoria == 5:
                valorCartao += valorGasto
                print(f"Categoria {categoria[opcaoCategoria]}")

            elif opcaoCategoria == 6:
                valorOutros += valorGasto
                print(f"Categoria {categoria[opcaoCategoria]}")

            else:
                os.system("cls")

                print("\n" + "-" * 33)
                print("Erro: digite apenas números (1-6)")
                print("-" * 33)
                input("Pressione ENTER para continuar...")
                continue

            novoGasto = {
                'id': idGasto,
                'valor': valorGasto,
                'mes': opcaoMes,
                'categoria': opcaoCategoria,
                'gastoAlimentacao': valorAlimentacao, # !!!!!!
                'gastoTransporte': valorTransporte,
                'gastoMoradia': valorMoradia,
                'gastoLazer': valorLazer,
                'gastoCartao': valorCartao,
                'gastoOutros': valorOutros,
            }

            gastos.append(novoGasto)
            break

        except ValueError:
            os.system("cls")

            print("-" * 31)
            print("  Erro: digite apenas números")
            print("-" * 31)
            input("Pressione ENTER para continuar...")

def listarGastos():
    os.system("cls")

    print("\n" + "-" * 54)
    print("                 LISTAGEM DE GASTOS")
    print("-" * 54)

    print("\n    ID    |    Mês    |    Categoria    |    Valor    ")
    print("-" * 54)
     
    for gasto in gastos:
        print(f"   {gasto['id']}   |   {meses[gasto['mes']]}   |   {categoria[gasto['categoria']]}   |   R$ {gasto['valor']:.2f}   ") # !!!!!!

def totalGeralGastos():
    os.system("cls")

    print("\n" + "-" * 31)
    print("          TOTAL GERAL")
    print("-" * 31)

    somaTotalGeral = 0

    for gasto in gastos:
        somaTotalGeral += gasto['valor']

    print(f"\nTotal geral: R$ {somaTotalGeral:.2f}")
    print('-' * 31)

def totalGeralCategoria():
    os.system("cls")

    print("\n" + "-" * 31)
    print("      TOTAL POR CATEGORIA")
    print("-" * 31)

    somaTotalAlimentacao = 0
    somaTotalTransporte = 0 
    somaTotalMoradia = 0
    somaTotalLazer = 0
    somaTotalCartao = 0 
    somaTotalOutros = 0

    for gasto in gastos:
        somaTotalAlimentacao += gasto['gastoAlimentacao']
        somaTotalTransporte += gasto['gastoTransporte']
        somaTotalMoradia += gasto['gastoMoradia']
        somaTotalLazer += gasto['gastoLazer']
        somaTotalCartao += gasto['gastoCartao']
        somaTotalOutros += gasto['gastoOutros']

    print(f"\nAlimentação: R$ {somaTotalAlimentacao:.2f}")
    print(f"Transporte: R$ {somaTotalTransporte:.2f}")
    print(f"Moradia: R$ {somaTotalMoradia:.2f}")
    print(f"Lazer: R$ {somaTotalLazer:.2f}")
    print(f"Cartão: R$ {somaTotalCartao:.2f}")
    print(f"Outros: R$ {somaTotalOutros:.2f}")
    print("-" * 31)

def totalmes():
    os.system("cls")

    print("\n" + "-" * 31)
    print("         TOTAL POR MÊS")
    print("-" * 31)

def definirLimiteMensal():
    os.system("cls")

    print("\n" + "-" * 31)
    print("     DEFINIR LIMITE MENSAL")
    print("-" * 31)

def excluirgasto():
    os.system("cls")

    print("\n" + "-" * 31)
    print("         EXCLUIR GASTO")
    print("-" * 31)

while True:
    os.system("cls")

    print("\n" + "=" * 31)
    print("  CONTROLE DE GASTOS PESSOAIS")
    print("=" * 31)
    print("\n 1. Adicionar gasto")
    print(" 2. Listar gastos")
    print(" 3. Total geral")
    print(" 4. Total por categoria")
    print(" 5. Total por mês")
    print(" 6. Definir limite mensal")
    print(" 7. Excluir gasto")
    print(" 8. Sair")
    print("-" * 31)

    try:
        opcaoEscolhida = int(input(" Escolha uma opção: "))

        if opcaoEscolhida == 1:
            adicionarGasto()

            print("-" * 31)
            print(" Gasto adicionado com sucesso!")
            print("-" * 31)
            input("Pressione ENTER para continuar...")

        elif opcaoEscolhida == 2:
            listarGastos()

            print("-" * 54)
            input("Pressione ENTER para continuar...")

        elif opcaoEscolhida == 3:
            totalGeralGastos()
        
            input("Pressione ENTER para continuar...")

        elif opcaoEscolhida == 4:
            totalGeralCategoria()

            input("Pressione ENTER para continuar...")

        elif opcaoEscolhida == 5:
            totalmes()

            input("Pressione ENTER para continuar...")

        elif opcaoEscolhida == 6:
            definirLimiteMensal()

            input("Pressione ENTER para continuar...")

        elif opcaoEscolhida == 7:
            excluirgasto()

            input("Pressione ENTER para continuar...")

        elif opcaoEscolhida == 8:
            os.system("cls")

            print("\n" + "-" * 31)
            print("      SAINDO DO SISTEMA...")
            print("-" * 31 )
            print("")
            break

        else:
            os.system("cls")

            print("\n" + "-" * 33)
            print("Erro: digite apenas números (1-8)")
            print("-" * 33)
            input("Pressione ENTER para continuar...")
            
    except ValueError:
        os.system("cls")

        print("\n" + "-" * 31)
        print("  Erro: digite apenas números")
        print("-" * 31)
        input("Pressione ENTER para continuar...")