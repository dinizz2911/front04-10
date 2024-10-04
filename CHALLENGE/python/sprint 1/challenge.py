import random

# Função para exibir o menu principal
def exibir_menu():
    print("\n==== MENU PRINCIPAL ====")
    print("1. Coletar Dados em Tempo Real")
    print("2. Detectar Anomalias")
    print("3. Exibir Painel de Monitoramento")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")
    return opcao

# Função para validar a entrada do usuário no menu
def validar_opcao(opcao):
    # Verifica se a opção escolhida está entre as opções válidas
    if opcao not in ['1', '2', '3', '4']:
        print("Opção inválida. Por favor, selecione uma opção do menu.")
        return False
    return True

# Função para simular a coleta de dados dos trens
def coletar_dados():
    print("\n=== Coletando Dados em Tempo Real ===")
    # Simula a coleta de dados de trens (velocidade, temperatura, vibração)
    dados = {
        'velocidade': random.uniform(40, 120),  # Velocidade em km/h
        'temperatura': random.uniform(20, 80),  # Temperatura em °C
        'vibração': random.uniform(0, 1)        # Vibração em g-força
    }
    print(f"Dados coletados: {dados}")
    return dados

# Função para simular a detecção de anomalias nos dados coletados
def detectar_anomalias(dados):
    print("\n=== Detectando Anomalias ===")
    # Verifica se algum dos valores está acima dos limites estabelecidos
    if dados['velocidade'] > 100 or dados['temperatura'] > 70 or dados['vibração'] > 0.8:
        print("Anomalia detectada!")
    else:
        print("Nenhuma anomalia detectada.")

# Função para simular a exibição de um painel de monitoramento
def exibir_painel():
    print("\n=== Exibindo Painel de Monitoramento ===")
    print("Monitoramento em tempo real...")
    # Aqui poderia haver integração com uma interface gráfica no futuro.
    # Por exemplo, gráficos em tempo real ou alertas visuais.

# Função principal que controla o fluxo do programa
def main():
    while True:
        opcao = exibir_menu()
        if validar_opcao(opcao):
            if opcao == '1':
                dados = coletar_dados()
            elif opcao == '2':
                # Verifica se os dados foram coletados antes de tentar detectar anomalias
                if 'dados' in locals():
                    detectar_anomalias(dados)
                else:
                    print("Por favor, colete os dados primeiro.")
            elif opcao == '3':
                exibir_painel()
            elif opcao == '4':
                print("Encerrando o programa...")
                break

# Ponto de entrada do programa
if __name__ == "__main__":
    main()