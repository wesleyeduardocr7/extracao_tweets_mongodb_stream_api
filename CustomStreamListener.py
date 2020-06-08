import tweepy
from AutenticacaoMongoDb import AutenticacaoMongoDb

db = AutenticacaoMongoDb.autenticaERetornaInstanciaDoBancoDeDados()

class CustomStreamListener(tweepy.StreamListener):        

    def on_status(self, status):
       
        if not hasattr(status, "retweeted_status"):

            try:                
                print(status.extended_tweet["full_text"]) 
                print("(tweet_maior_que_140_caracteres) | Tamanho = " + str(len(status.extended_tweet["full_text"])))
                db.extracao05_tweet_maior_que_140_caracteres.insert_one({
                    "parametros_busca":"ansiedade,depressão,saúde mental,depressao,saude mental",
                    "id_usuario":status.user.id_str,
                    "nome_usuario":status.user.screen_name,
                    "id_tweet":status.id_str,
                    "tweet":status.extended_tweet["full_text"], 
                    "quantidade_caracteres": str(len(status.extended_tweet["full_text"])),
                    "data_criacao_tweet":status.created_at,                 
                    "quantidade_retweets":status.retweet_count,
                    "localizacao_usuario": status.user.location,
                    "descricao_usuario": status.user.description,
                    "quantidade_seguidores_usuario": status.user.followers_count,
                    "data_criacao_conta_usuario":status.user.created_at                                    
                })                            
                print("\n")
            except AttributeError:
                print(status.text)
                print("(tweet_menor_igual_140_caracteres) | Tamanho = " + str(len(status.text)))               
                db.extracao05_tweet_menor_igual_140_caracteres.insert_one({
                    "parametros_busca":"ansiedade,depressão,saúde mental,depressao,saude mental",
                    "id_usuario":status.user.id_str,
                    "nome_usuario":status.user.screen_name,
                    "id_tweet":status.id_str,
                    "tweet":status.text, 
                    "quantidade_caracteres": str(len(status.text)), 
                    "data_criacao_tweet":status.created_at,                 
                    "quantidade_retweets":status.retweet_count,
                    "localizacao_usuario": status.user.location,
                    "descricao_usuario": status.user.description,
                    "quantidade_seguidores_usuario": status.user.followers_count,
                    "data_criacao_conta_usuario":status.user.created_at                                    
                })
                print("\n")

    def on_error(self, status_code):
        print("Erro com o código:", status_code)
        return True