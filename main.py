from Tweet import Tweet
from AutenticacaoMongoDb import AutenticacaoMongoDb

db = AutenticacaoMongoDb.autenticaERetornaInstanciaDoBancoDeDados()

def main():

    print('1 - Extrair Tweets')
    print('2 - Imprimir Tweets')
    print('3 - Quantidade de Tweets')
    print('4 - Gerar Arquivo txt com os tweets')
    print('5 - Copiar Coleção')
    print('6 - Extrair dados de um Perfil')
    
    print('0 - Sair')
    
    op = int(input('Informe a Opção: '))

    if(op == 1):
        #quantidade_parametros = int(input('Informe a quantidade de parâmetros de busca no Twitter:'))
        #Tweet.extrair_tweets(quantidade_parametros)
        Tweet.extrair_tweets()
    elif(op == 2):
	    Tweet.imprimir_tweets()
    elif(op == 3):
	    print(Tweet.count_tweets())
    elif(op == 4):
	    Tweet.gerar_txt_tweets()
    elif(op == 5):
	    Tweet.copiar_colecao()
    elif(op == 6):
	    Tweet.get_tweets_usuario("")
    elif(op == 0):
        exit
    else:
        print('\nOpção Incorreta\n')
        main()
		 
main()
