import funcoes

def main():

    print('1 - Extrair Tweets')
    print('2 - Imprimir Tweets')
    print('0 - Sair')
    
    op = int(input('Informe a Opção: '))

    if(op == 1):
        quantidade_parametros = int(input('Informe a quantidade de parâmetros de busca:'))
        funcoes.extrair_tweets(quantidade_parametros)     
    elif(op == 2):
	    funcoes.imprimir_tweets()       
    elif(op == 0):
        exit
    else:
        print('\nOpção Incorreta\n')
        main()
		 
main()
