from pymongo import MongoClient

def get_mongodb_client():
    # Atlas에서 복사한 주소를 여기에 넣으세요 (따옴표 필수)
    uri = "mongodb+srv://admin:wjdgmldi123!@cluster0.acv6bvr.mongodb.net/?appName=Cluster0"
    client = MongoClient(uri)
    return client

def save_application(data):
    client = get_mongodb_client()
    db = client['SUR-VIBE']  # 데이터베이스 이름
    collection = db['cluster0']  # 컬렉션(테이블) 이름
    collection.insert_one(data)  # 데이터 저장!
    client.close()