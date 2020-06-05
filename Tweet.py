import tweepy
from CustomStreamListener import CustomStreamListener
from AutenticacaoApiTwitter import AutenticacaoApiTwitter
from AutenticacaoMongoDb import AutenticacaoMongoDb

db = AutenticacaoMongoDb.autenticaERetornaInstanciaDoBancoDeDados()

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

        streaming_api = tweepy.streaming.Stream(AutenticacaoApiTwitter.autentica(), CustomStreamListener())
        streaming_api.filter(follow=None, track=parametros, languages=["pt"])

        print("\nExtração concluída com sucesso!")

    @staticmethod 
    def imprimir_tweets():

        for tweet in db.tweets_extraidos.find():
            print('\n')
            print('Tweet: ' + str(tweet['tweet']))

    @staticmethod
    def count_tweets():
        return db.tweets_extraidos.count_documents({})        