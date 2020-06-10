import tweepy
from CustomStreamListener import CustomStreamListener
from AutenticacaoApiTwitter import AutenticacaoApiTwitter
from AutenticacaoMongoDb import AutenticacaoMongoDb

db = AutenticacaoMongoDb.autenticaERetornaInstanciaDoBancoDeDados()
auth = AutenticacaoApiTwitter.autentica()

class Tweet():

    @staticmethod
    def extrair_tweets(quantidade_parametros):

        parametros = []
        contador = 1

        while contador <= quantidade_parametros:
            parametro = input("Informe o " + str(contador) + "º parâmetro: ")
            parametros.append(parametro)
            contador += 1

        print("\nExtraindo tweets...")

        streaming_api = tweepy.streaming.Stream(auth, CustomStreamListener())
        streaming_api.filter(follow=None, track=parametros, languages=["pt"])
        
        print("\nExtração concluída com sucesso!")

    @staticmethod
    def imprimir_tweets():

        for tweet in db.extracao08_tweet_maior_que_140_caracteres.find():
            print('\n')
            print('Tweet: ' + str(tweet['tweet']))

    @staticmethod
    def count_tweets():
        return db.extracao08_tweet_maior_que_140_caracteres.count_documents({})

    @staticmethod
    def gerar_txt_tweets():

        print("Gerando Arquivo txt com os tweets...\n")

        count = 1

        arquivo = open('test.txt', 'w', encoding='utf-8')

        for tweet in db.extracao08_tweet_maior_que_140_caracteres.find():
            arquivo.write('\n')
            arquivo.write('-----------------------------------------------------------------------------------------------------------------------------------------')
            arquivo.write('\n')
            arquivo.write('\n')
            arquivo.write('('+str(count) + ')' + ' - ' + tweet['id_tweet'])
            arquivo.write('\n')
            count += 1

        arquivo.close()

        print("Arquivo Gerado com Sucesso!")

    