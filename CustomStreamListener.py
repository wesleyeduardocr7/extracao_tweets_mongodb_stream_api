import tweepy
from AutenticacaoMongoDb import AutenticacaoMongoDb
from AutenticacaoApiTwitter import AutenticacaoApiTwitter

db = AutenticacaoMongoDb.autenticaERetornaInstanciaDoBancoDeDados()
auth = AutenticacaoApiTwitter.autentica()

class CustomStreamListener(tweepy.StreamListener):

    def on_status(self, status):

        if not hasattr(status, "retweeted_status"):

            try:                

                print(status.extended_tweet["full_text"])

                print("id_tweet > 140ch:" + status.id_str)

                print("Tamanho = " + str(len(status.extended_tweet["full_text"]))) 

                print("\n")

                if(not tweet_repetido_extracao08_tweet_maior_que_140_caracteres(status.id_str)):

                    tweet_maior_140ch = True

                    insere_mongodb(status,tweet_maior_140ch)  

            except AttributeError:                

                print(status.text)  

                print("id_tweet <= 140ch:" + status.id_str)

                print("Tamanho = " + str(len(status.text))) 

                print("\n")             

                if(not tweet_repetido_extracao08_tweet_menor_igual_140_caracteres(status.id_str)):

                    tweet_menor_140ch = False    

                    insere_mongodb(status,tweet_menor_140ch)


    def on_error(self, status_code):
        print("Erro com o código:", status_code)
        return True


def tweet_repetido_extracao08_tweet_maior_que_140_caracteres(id_tweet):
    for tweet in db.extracao08_tweet_maior_que_140_caracteres.find():
        if(tweet['id_tweet'] == str(id_tweet)):
            return True
    return False


def tweet_repetido_extracao08_tweet_menor_igual_140_caracteres(id_tweet):
    for tweet in db.extracao08_tweet_menor_igual_140_caracteres.find():
        if(tweet['id_tweet'] == str(id_tweet)):
            print("repetido\n")
            return True
    return False


def get_tweets_usuario(nome_usuario):

    tweets = []
    api = tweepy.API(auth)
    retweeted = "RT"
    marcacao = "@"

    for status in tweepy.Cursor(api.user_timeline, id=str(nome_usuario)).items(100):
        if(retweeted and marcacao not in status.text):
            tweets.append(status.text)

    return tweets


def insere_mongodb(status, tweet_maior_140ch):
    if(tweet_maior_140ch):
        db.extracao08_tweet_maior_140_caracteres.insert_one({
            "parametros_busca": "ansiedade,depressão,saúde mental,depressão,saude mental",
            "data": "10-06-2020-08-00-am",
            "tipo": "tweets maiores que 140 caracteres",
            "id_usuario": status.user.id_str,
            "nome_usuario": status.user.screen_name,
            "id_tweet": status.id_str,
            "tweet": status.extended_tweet["full_text"],
            "quantidade_caracteres": str(len(status.extended_tweet["full_text"])),
            "data_criacao_tweet": status.created_at,
            "quantidade_retweets": status.retweet_count,
            "localizacao_usuario": status.user.location,
            "descricao_usuario": status.user.description,
            "quantidade_seguidores_usuario": status.user.followers_count,
            "data_criacao_conta_usuario": status.user.created_at,
            "tweets_usuario":  get_tweets_usuario(status.user.screen_name)
        })
    else:
        db.extracao08_tweet_menor_igual_140_caracteres.insert_one({
            "parametros_busca": "ansiedade,depressão,saúde mental,depressão,saude mental",
            "data": "10-06-2020-08-00-am",
            "tipo": "tweets menores que 140 caracteres",
            "id_usuario": status.user.id_str,
            "nome_usuario": status.user.screen_name,
            "id_tweet": status.id_str,
            "tweet": status.text,
            "quantidade_caracteres": str(len(status.text)),
            "data_criacao_tweet": status.created_at,
            "quantidade_retweets": status.retweet_count,
            "localizacao_usuario": status.user.location,
            "descricao_usuario": status.user.description,
            "quantidade_seguidores_usuario": status.user.followers_count,
            "data_criacao_conta_usuario": status.user.created_at,
            "tweets_usuario":  get_tweets_usuario(status.user.screen_name)
        })
