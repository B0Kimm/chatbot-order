import json
import requests
import time


class YogiyoCrawler:

    def __init__(self):
        pass

    def get_json(self, url):

        payload = {}
        headers = {
          'x-apikey': 'iphoneap',
          'x-apisecret': 'fe5183cc3dea12bd0ce299cf110a75a2'
        }

        try:
            response = requests.request("GET", url, headers=headers, data = payload)
        except:
            print("ZZzzzz...")
            time.sleep(5)  # 너무 많은 request로 에러가 발생할 수 있으므로 잠시 쉰다
            return ['']  # 에러 발생 후 리스트를 리턴하여 해당번호는 패스하게 만듬
        try:
            json_data = response.json()
        except:
            print('유효하지 않은 json형식')
            return []
        # print(json_data)
        return json_data

    def get_json_store(self, start, end):
        json_list = []
        for index in range(start, end):
            index = str(index).zfill(6)
            url = f"https://www.yogiyo.co.kr/api/v1/restaurants/{index}"
            ajson = self.get_json(url)
            if isinstance(ajson, dict):
                json_list.append(ajson)
            print(f'{index}번 크롤링 중')
        
        file_path = f"./data/json/yogiyo_store({start}~{end}).json"
        with open(file_path, 'w', encoding='UTF-8-sig') as file:
            json.dump(json_list, file, indent=4, ensure_ascii=False)
        print(f'yogiyo_store({start}~{end}).json 저장완료')

    def load_json(self, file_path):

        # file_path = "./sample.json"
        with open(file_path, "r", encoding="UTF-8-SIG") as json_file:
            json_data = json.load(json_file)
            # print(json_data)

        return json_data

    def get_store_id_by_city(self, json_data, city):
        id_list = []
        for item in json_data:
            if city == item['city']:
                 id_list.append(item['id'])
        return id_list

    # 메뉴정보 json 크롤링
    def menu_crawling(self):
        pass


if __name__ == '__main__':
    yogiyo = YogiyoCrawler()
    # start = 361000
    # end = 362000
    # for i in range(9):
    #     yogiyo.get_json_store(start, end)
    #     start += 1000
    #     end += 1000
    # yogiyo.get_json_store(360000, 361000)


    # ---------------------------
    # 서울의 매장 id만 취합

    start = 0
    end = 1000
    total_list = []
    for i in range(498):
        file_path = f'./data/json/yogiyo_store({start}~{end}).json'
        json_data = yogiyo.load_json(file_path)
        id_list = yogiyo.get_store_id_by_city(json_data, '서울')
        # print(id_list)
        total_list += id_list
        start += 1000
        end += 1000

    print(len(total_list))
    file_path = "./yogiyo_store_id_list(seoul).json"
    with open(file_path, 'w', encoding='UTF-8-sig') as file:
        json.dump(total_list, file, indent=4, ensure_ascii=False)















