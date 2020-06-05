import tweepy
from AutenticacaoMongoDb import AutenticacaoMongoDb

db = AutenticacaoMongoDb.autenticaERetornaInstanciaDoBancoDeDados()

class CustomStreamListener(tweepy.StreamListener):
   
    def on_status(self, tweet):
        db.tweets.insert_one({         
            "id_usuario": tweet.id_str,
            "nome_usuario": tweet.user.screen_name,
            "tweet": tweet.text,
            "data_envio": tweet.created_at,
            "localizacao_usuario": tweet.user.location,
            "quantidade_seguidores": tweet.user.followers_count          
        })

        print(tweet.text)
        print("\n")

        return True

    def on_error(self, status_code):
        print("Erro com o código:", status_code)
        return True

    def on_timeout(self):
        print("Tempo esgotado!")
        return True