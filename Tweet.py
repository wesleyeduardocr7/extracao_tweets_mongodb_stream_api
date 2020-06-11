import tweepy
from CustomStreamListener import CustomStreamListener
from AutenticacaoApiTwitter import AutenticacaoApiTwitter
from AutenticacaoMongoDb import AutenticacaoMongoDb

db = AutenticacaoMongoDb.autenticaERetornaInstanciaDoBancoDeDados()
auth = AutenticacaoApiTwitter.autentica()


class Tweet():

    @staticmethod
    def extrair_tweets():

        parametros = ['ansiedade', 'depressão','saúde mental', 'depressao', 'saude mental']
        #contador = 1

        # while contador <= quantidade_parametros:
        # parametro = input("Informe o " + str(contador) + "º parâmetro: ")
        # parametros.append(parametro)
        # contador += 1

        print("\nExtraindo tweets...")

        streaming_api = tweepy.streaming.Stream(auth, CustomStreamListener())
        streaming_api.filter(follow=None, track=parametros, languages=["pt"])

        print("\nExtração concluída com sucesso!")

    @staticmethod
    def imprimir_tweets():

        for tweet in db.extracao08_tweet_maior_140_caracteres.find():
            print('\n')
            print('Tweet: ' + str(tweet['tweet']))

    @staticmethod
    def count_tweets():
        return db.extracao08_tweet_maior_140_caracteres.count_documents({})

    @staticmethod
    def gerar_txt_tweets():

        print("Gerando Arquivo txt com os tweets...\n")

        count = 1

        arquivo = open('extracao08_tweet_maior_140_caracteres.txt','w', encoding='utf-8')

        for tweet in db.extracao08_tweet_maior_140_caracteres.find():
            arquivo.write('\n')
            arquivo.write('-----------------------------------------------------------------------------------------------------------------------------------------')
            arquivo.write('\n')
            arquivo.write('\n')
            arquivo.write('id = ' + tweet['id_tweet'])
            arquivo.write('\n('+str(count) + ')' + ' - ' + tweet['tweet'])
            arquivo.write('\n')
            count += 1

        arquivo.close()

        print("Arquivo Gerado com Sucesso!")

    def tweet_repetido_extracao08_tweet_maior_que_140_caracteres(id_tweet):
        for tweet in db.extracao08_tweet_maior_140_caracteres.find():
            if(tweet['id_tweet'] == str(id_tweet)):
                print("repetido")
                return True
        print(" nao repetido")
        return False

    @staticmethod
    def copiar_colecao():

        count = 0

        for tweet in db.extracao07_tweet_maior_que_140_caracteres.find():

            if(not tweet_repetido_extracao08_tweet_maior_que_140_caracteres(tweet["id_tweet"])):

                print(tweet["id_tweet"] + ' inserido')

                db.extracao08_tweet_maior_140_caracteres.insert_one({
                    "parametros_busca": tweet["parametros_busca"],
                    "data": tweet["data"],
                    "tipo": tweet["tipo"],
                    "id_usuario": tweet["id_usuario"],
                    "nome_usuario": tweet["nome_usuario"],
                    "id_tweet": tweet["id_tweet"],
                    "tweet": tweet["tweet"],
                    "quantidade_caracteres": tweet["quantidade_caracteres"],
                    "data_criacao_tweet": tweet["data_criacao_tweet"],
                    "quantidade_retweets": tweet["quantidade_retweets"],
                    "localizacao_usuario": tweet["localizacao_usuario"],
                    "descricao_usuario": tweet["descricao_usuario"],
                    "quantidade_seguidores_usuario": tweet["quantidade_seguidores_usuario"],
                    "data_criacao_conta_usuario": tweet["data_criacao_conta_usuario"],
                    "tweets_usuario": tweet["tweets_usuario"]
                })

                count += 1

                print(str(count))

    @staticmethod
    def get_tweets_usuario(id_usuario):

        tweets = []
        api = tweepy.API(auth)
        retweeted = "RT"
        marcacao = "@"
        count = 1

        usuario =  api.get_user(id_usuario)

        arquivo = open('dados_usuario_pedrooneto.txt', 'w', encoding='utf-8')
        
        arquivo.write('Id do Usuário : ' + str(usuario.id_str))
        arquivo.write('\nNome Usuário : ' + str(usuario.name))
        arquivo.write('\nScreen Name : ' + str(usuario.screen_name))
        arquivo.write('\nLocalização : ' + str(usuario.location))
        arquivo.write('\nDescrição : ' + str(usuario.description))
        arquivo.write('\nQuantidade de Seguidores : ' + str(usuario.followers_count))
        arquivo.write('\nQuantidade de Pessoas Seguidas : ' + str(usuario.friends_count))
        arquivo.write('\nQuantidade de Tweets Postados : ' + str(usuario.statuses_count))
        arquivo.write('\nData da Criação da Conta : ' + str(usuario.created_at))
        
        arquivo.write('\n\nLISTA DAS ÚLTIMAS POSTAGENS\n\n')
                
        for status in tweepy.Cursor(api.user_timeline, id=str(id_usuario)).items(500):            
            if(retweeted and marcacao not in status.text):
                arquivo.write('-----------------------------------------------------------------------------------------------------------------------------------------')
                arquivo.write('\n')
                arquivo.write('('+str(count) + ')' + ' - ' + str(status.text)) 
                arquivo.write('\n')
                count+=1
        
        print("\nArquivo Gerado com Sucesso!\n")



def tweet_repetido_extracao08_tweet_maior_que_140_caracteres(id_tweet):
    for tweet in db.extracao08_tweet_maior_140_caracteres.find():
        if(tweet['id_tweet'] == str(id_tweet)):
            return True
    return False

