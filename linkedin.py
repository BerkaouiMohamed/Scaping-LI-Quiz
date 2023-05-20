from bs4 import BeautifulSoup
#you need to install BeautifulSoup 4 : pip install beautifulsoup4

with open('linkedin.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'lxml')
responses = soup.find_all('span', class_='visually-hidden')

with open('temp.txt', 'w') as output_file:

    for i, response in enumerate(responses):
        if i == 0:
            output_file.write(f'Question: {response.text}\n')
        else:
            output_file.write(f'Response {i}: {response.text}\n')
