import pymongo

# URL de conexão com o MongoDB
url = "mongodb://localhost:27017/"

# Nome do banco de dados e da coleção
db_name = "test"
collection_name = "item"

# Conectando ao MongoDB
client = pymongo.MongoClient(url)

# Selecionando o banco de dados e a coleção
db = client[db_name]
collection = db[collection_name]

# Consultando os dados
query = {"price":30}
dados = collection.find(query)

# Imprimindo os dados
for dado in dados:
    print(dado)