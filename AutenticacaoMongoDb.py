from pymongo import MongoClient

class AutenticacaoMongoDb():
    
    @staticmethod    
    def autenticaERetornaInstanciaDoBancoDeDados():         
        client = MongoClient("")
        db = client.get_database('')    
        return db
           
    
        

