import requests


url = "https://akabab.github.io/superhero-api/api/all.json"

response = requests.get(url)

data1 = response.json()

for row in data1:
    if row["name"] == "Hulk":
        int_hulk = row["powerstats"]["intelligence"]
    elif row["name"] == "Captain America":
        int_captain = row["powerstats"]["intelligence"]
    elif row["name"] == "Thanos":
        int_thanos = row["powerstats"]["intelligence"]        
print(f"Hulk: {int_hulk}, Captain Amerika: {int_captain}, Thanos: {int_thanos}")

if int_hulk > int_captain:
    if int_hulk > int_thanos:
        print("Самый умный Hulk")
    else:
        print("Самый умный Thanos") 
elif int_captain > int_thanos:
    print("Самый умный Captain Amerika")

else:
    print("Самый умный Thanos") 



class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def href(self,path):
        params = {"path":f"/{path}"}
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        path_to_file = data["href"]
        return path_to_file
    def upload(self,paths: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать
        with open(paths, "rb") as f:
            response = requests.post(uploader.href(paths), files = {"file":f})
            print(response.status_code)


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    
    file_list = ["moon.jpg","stone.jpg","wolf.png"]
    token = open("private/token.txt").read()
    url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
    headers = {"Authorization": "OAuth "+ token}
    uploader = YaUploader(token)
    for file in file_list:
        uploader.upload(file)
    

url1 = "https://api.stackexchange.com/2.3/questions"

params1 = {
    "sort": "activity",
    "tagged":"Python",
    "fromdate": "1688860800",
     "order": "desc",
      "site": "stackoverflow" }


response = requests.get(url1, params = params1)
data = response.json()
for row in data["items"]:
    print(row["title"])


