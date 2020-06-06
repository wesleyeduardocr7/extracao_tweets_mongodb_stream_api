import tweepy
from AutenticacaoMongoDb import AutenticacaoMongoDb

db = AutenticacaoMongoDb.autenticaERetornaInstanciaDoBancoDeDados()

class CustomStreamListener(tweepy.StreamListener):
   
    def on_status(self, tweet):

        db.tweets_extraidos.insert_one({
            "tweet": tweet.text                  
        })

        print(tweet.text)
        print("\n")     

        return True

    def on_error(self, status_code):
        print("Erro com o código:", status_code)
        return True