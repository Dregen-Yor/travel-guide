import requests

# 爬虫程序的基本设置
url = 'https://www.example.com'  # 爬取目标 URL
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.1008.47'
}

# 爬取数据
response = requests.get(url, headers=headers)

if response.status_code == 200:
    with open('data.txt', 'w') as f:
        f.write(response.text)
else:
    print(f'Failed to get data: {response.status_code}')
