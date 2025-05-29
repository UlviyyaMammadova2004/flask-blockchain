from pymongo import MongoClient

# MongoDB Atlas bağlantı URI (şifreni <db_password> kısmına yazmalısın)
client = MongoClient("mongodb+srv://MammadovaMammadova:<db_password>@clusteblockchain.y2cgmgr0.mongodb.net/")

# Veritabanı ve koleksiyon adı
db = client["blockchain_db"]
collection = db["blocks"]

# Blok kaydetme fonksiyonu
def save_block_to_db(block):
    collection.insert_one({
        "index": block.index,
        "data": block.data,
        "hash": block.hash,
        "previous_hash": block.previous_hash
    })
