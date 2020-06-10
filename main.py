from Tweet import Tweet
from AutenticacaoMongoDb import AutenticacaoMongoDb

db = AutenticacaoMongoDb.autenticaERetornaInstanciaDoBancoDeDados()

def main():

    print('1 - Extrair Tweets')
    print('2 - Imprimir Tweets')
    print('3 - Quantidade de Tweets')
    print('4 - Gerar Arquivo txt com os tweers')
    
    print('0 - Sair')
    
    op = int(input('Informe a Opção: '))

    if(op == 1):
        quantidade_parametros = int(input('Informe a quantidade de parâmetros de busca no Twitter:'))
        Tweet.extrair_tweets(quantidade_parametros)
    elif(op == 2):
	    Tweet.imprimir_tweets()
    elif(op == 3):
	    print(Tweet.count_tweets())
    elif(op == 4):
	    Tweet.gerar_txt_tweets() 
    elif(op == 0):
        exit
    else:
        print('\nOpção Incorreta\n')
        main()
		 
main()
