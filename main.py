'''Essa função solicita uma entrada do usuário e garante que a entrada seja válida (1 ou 2). 
Ela continua pedindo até que o usuário forneça uma entrada correta.
resposta.isdigit() verifica se a entrada é um número.
int(resposta) == 1 or int(resposta) == 2 garante que o número seja 1 ou 2.'''
def obter_resposta():
    while True:
        resposta = input("Escolha '1' para SIM ou '2' para NÃO: ")
        if resposta.isdigit() and (int(resposta) == 1 or int(resposta) == 2):
            return int(resposta)
        else:
            print("-------------------------------")
            print("Opção inválida, Digite 1 para 'SIM' e 2 para 'NÃO'")

def main():
    tabelas = [
        [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63],
        [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31, 34, 35, 38, 39, 42, 43, 46, 47, 50, 51, 54, 55, 58, 59, 62, 63],
        [4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31, 36, 37, 38, 39, 44, 45, 46, 47, 52, 53, 54, 55, 60, 61, 62, 63],
        [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31, 40, 41, 42, 43, 44, 45, 46, 47, 56, 57, 58, 59, 60, 61, 62, 63],
        [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63],
        [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]
    ]

    pesos = [1, 2, 4, 8, 16, 32]

    while True:
        print("BEM VINDO AO PROGRAMA NumberCracker!")
        print("VOU ADIVINHAR O NÚMERO QUE VOCÊ PENSOU")
        print("PENSE EM UM NÚMERO DE 1 A 63")
        print("ASSIM QUE TIVER PRONTO, ESCOLHA '1' PARA SIM OU '2' PARA NÃO")
        print("Caso deseje encerrar, digite 'sair'")
        print("------------------------------------------------------------------")

        total = 0
        for i in range(6):
            print(f"TABELA {i + 1}")
            print("--------")
            for j in range(0, len(tabelas[i]), 4):
                print(" ".join(map(str, tabelas[i][j:j + 4])))
            print("O número que você pensou, está nesta tabela?")
            resposta = obter_resposta()
            if resposta == 1:
                total += pesos[i]
                
        '''pergunta ao usuário se deseja jogar novamente. Se a resposta não for 's', 
            o loop termina e o programa se encerra.'''
        print(f"O número que você pensou foi {total}")
        if input("Deseja jogar novamente? (s=Sim/n=Não): ").lower() != 's':
            break

'''Esse bloco garante que a função main() só será executada se o script for executado diretamente, não quando importado como módulo em outro script.'''
if __name__ == "__main__":
    main()