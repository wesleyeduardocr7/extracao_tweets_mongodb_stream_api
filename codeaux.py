 
            try:                
                """print(status.retweeted_status.extended_tweet["full_text"])
                print("(retweeted_maior_que_140_caracteres) | Tamanho =  " + str(len(status.retweeted_status.extended_tweet["full_text"])))
                db.extracao03_retweeted_maior_que_140_caracteres.insert_one({
                    "id_usuario":status.user.id_str,
                    "nome_usuario":status.user.screen_name,
                    "id_tweet":status.id_str,
                    "tweet":status.retweeted_status.extended_tweet["full_text"], 
                    "quantidade_caracteres": str(len(status.retweeted_status.extended_tweet["full_text"])), 
                    "data_criacao_tweet":status.created_at,                 
                    "quantidade_retweets":status.retweet_count,
                    "localizacao_usuario": status.user.location,
                    "descricao_usuario": status.user.description,
                    "quantidade_seguidores_usuario": status.user.followers_count,
                    "data_criacao_conta_usuario":status.user.created_at                                    
                })
                print("\n")"""
            except AttributeError:
               """ print(status.retweeted_status.text)
                print("(retweeted_menor_igual_140_caracteres) | Tamanho = " + str(len(status.retweeted_status.text)))                
                db.extracao03_retweeted_menor_igual_140_caracteres.insert_one({
                    "id_usuario":status.user.id_str,
                    "nome_usuario":status.user.screen_name,
                    "id_tweet":status.id_str,
                    "tweet":status.retweeted_status.text, 
                    "quantidade_caracteres": str(len(status.retweeted_status.text)), 
                    "data_criacao_tweet":status.created_at,                 
                    "quantidade_retweets":status.retweet_count,
                    "localizacao_usuario": status.user.location,
                    "descricao_usuario": status.user.description,
                    "quantidade_seguidores_usuario": status.user.followers_count,
                    "data_criacao_conta_usuario":status.user.created_at                                    
                })
                print("\n")"""