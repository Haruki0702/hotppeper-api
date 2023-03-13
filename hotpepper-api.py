import requests
URL="http://webservice.recruit.co.jp/hotpepper/gourmet/v1/"
API_key="807b6e7aaa8ab7dc"
restaurantaddres=input("駅を入力してください")
body={
    "key":API_key,
    "address":restaurantaddres,
    "order":4,
    "format":"json",
    "count":10
}

response=requests.get(URL,body)

datum=response.json()
stores=datum["results"]["shop"]
for store_name in stores:
    name=store_name["name"]
    price=store_name["budget"]["name"]
    is_smoking=store_name["non_smoking"]
    print(name)
    print(price)
    print(is_smoking)