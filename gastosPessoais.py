import os

# ======================= DADOS =======================

meses = [
    "", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

categorias = [
    "", "Alimentação", "Transporte", "Moradia", "Lazer", "Outros"
]

gastos = []

# ======================= LAYOUT =======================

def limpar():
    os.system("cls")
    
def cabecalho(titulo):
    limpar()
    print("=" * 50)
    print(titulo.center(50))
    print("=" * 50)

def pausa():
    input("\nPressione ENTER para continuar...")

# ======================= FUNÇÕES =======================

def adicionarGasto():
    while True:
        try:
            limpar()
            cabecalho("ADICIONAR GASTO")

            idGasto = int(input("ID do gasto: "))
            if idGasto <= 0:
                print("\nID inválido.")
                pausa()
                continue

            for gasto in gastos:
                if gasto['id'] == idGasto:
                    print("\nID já existente.")
                    print(
                        f"\nID: {gasto['id']}"
                        f"\nMês: {meses[gasto['mes']]}"
                        f"\nCategoria: {categorias[gasto['categoria']]}"
                        f"\nValor: R$ {gasto['valor']:.2f}"
                    )
                    pausa()
                    return

            valor = float(input("Valor (R$): "))
            if valor <= 0:
                print("\nValor inválido.")
                pausa()
                continue

            print("\nMês:")
            for m in range(1, 13):
                print(f"{m}. {meses[m]}")

            mes = int(input("\nEscolha: "))
            if mes < 1 or mes > 12:
                print("\nMês inválido.")
                pausa()
                continue

            print("\nCategoria:")
            for c in range(1, 6):
                print(f"{c}. {categorias[c]}")

            categoria = int(input("\nEscolha: "))
            if categoria < 1 or categoria > 5:
                print("\nCategoria inválida.")
                pausa()
                continue

            novoGasto = { 
                "id": idGasto,
                "valor": valor,
                "mes": mes,
                "categoria": categoria
            }

            gastos.append(novoGasto) 

            print("\nGasto cadastrado com sucesso.")
            pausa()
            return

        except ValueError:
            print("\nDigite apenas números.")
            pausa()

def listarGastos():
    limpar()
    cabecalho("LISTAGEM DE GASTOS")

    if not gastos:
        print("\nNenhum gasto registrado.")
        pausa()
        return

    print(f"{'ID':<5}{'Mês':<15}{'Categoria':<15}{'Valor':>10}")
    print("-" * 50)

    for gasto in gastos:
        print(
            f"{gasto['id']:<5}"
            f"{meses[gasto['mes']]:<15}"
            f"{categorias[gasto['categoria']]:<15}"
            f"R$ {gasto['valor']:>7.2f}"
        )

    pausa()
     
def totalGeral():
    limpar()
    cabecalho("TOTAL GERAL")

    if not gastos:
        print("\nNenhum gasto registrado.")
        pausa()
        return

    total = sum(gasto['valor'] for gasto in gastos)
    print(f"\nTotal geral: R$ {total:.2f}")

    pausa()


def totalPorCategoria():
    limpar()
    cabecalho("TOTAL POR CATEGORIA")

    if not gastos:
        print("\nNenhum gasto registrado.")
        pausa()
        return

    totais = [0] * 6

    for gasto in gastos:
        totais[gasto['categoria']] += gasto['valor']

    for c in range(1, 6):
        print(f"{categorias[c]:<15} : R$ {totais[c]:.2f}")

    pausa()

def totalPorMes():
    limpar()
    cabecalho("TOTAL POR MÊS")  

    if not gastos:
        print("\nNenhum gasto registrado.")
        pausa()
        return
    
    totais = [0] * 13

    for gasto in gastos:
        totais[gasto['mes']] += gasto['valor']

    for m in range(1, 13):
        print(f"{meses[m]:<12} : R$ {totais[m]:.2f}")

    pausa()
    
def excluirGasto():
    limpar()
    cabecalho("EXCLUIR GASTO")

    if not gastos:
        print("\nNenhum gasto registrado.")
        pausa()
        return

    print(f"{'ID':<5}{'Mês':<15}{'Categoria':<15}{'Valor':>10}")
    print("-" * 50)

    for gasto in gastos:
        print(
            f"{gasto['id']:<5}"
            f"{meses[gasto['mes']]:<15}"
            f"{categorias[gasto['categoria']]:<15}"
            f"R$ {gasto['valor']:>7.2f}"
        )

    try:
        idExcluir = int(input("\nDigite o ID: "))
        for gasto in gastos:
            if gasto['id'] == idExcluir:
                gastos.remove(gasto)
                print("\nGasto removido com sucesso.")
                pausa()
                return

        print("\nID não encontrado.")
        pausa()

    except ValueError:
        print("\nDigite apenas números.")
        pausa()
     
# ======================= MENU =======================

while True:
    limpar()
    cabecalho("CONTROLE DE GASTOS PESSOAIS")

    print("1 - Adicionar gasto")
    print("2 - Listar gastos")
    print("3 - Total geral")
    print("4 - Total por categoria")
    print("5 - Total por mês")
    print("6 - Excluir gasto")
    print("0 - Sair")

    try:
        opcao = int(input("\nEscolha: "))

        if opcao == 1:
            adicionarGasto()
        elif opcao == 2:
            listarGastos()
        elif opcao == 3:
            totalGeral()
        elif opcao == 4:
            totalPorCategoria()
        elif opcao == 5:
            totalPorMes()
        elif opcao == 6:
            excluirGasto()
        elif opcao == 0:
            limpar()
            print("=" * 50)            
            print("SAINDO DO SISTEMA...".center(50))
            print("=" * 50)            
            break
        else:
            print("\nOpção inválida.")
            pausa()

    except ValueError:
        print("\nDigite apenas números.")
        pausa()
