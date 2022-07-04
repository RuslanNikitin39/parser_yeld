import time
from datetime import datetime
import random
from tkinter.filedialog import askdirectory, asksaveasfilename, asksaveasfile
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup as bs
import csv
import os


# WORK_URL = 'https://www.yelp.com/search?find_desc=Hair+Salons&find_loc=New+York%2C+NY%2C+United+States'
# BASE_URL = 'https://www.yelp.com'


# def save(rows, path):
#     with open(path, 'w', encoding='utf-8', newline='\n') as csvfile:
#         csv.register_dialect('myDialect', delimiter=';', quoting=csv.QUOTE_NONE)
#         writer = csv.writer(csvfile, dialect='myDialect')
#         writer.writerow(('name', 'web_site', 'owner_name', 'owner_status'))
#
#         for row in rows:
#             writer.writerow((row['name'], row['web_site'], row['owner_name'], row['owner_status']))


def get_hiders():
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'bse=7f7a1f2189734000868a0ff495b023d6; recentlocations=; hl=en_US; '
                  'wdi=1|BA6694EC20BCDE21|0x1.8ad7260abc4b1p+30|a3f440255d5eab25; _gcl_au=1.1.55123320.1656080774; '
                  '_fbp=fb.1.1656080774601.1936740182; _tt_enable_cookie=1; '
                  '_ttp=2ed27381-4805-4a77-84e8-17c9a52271ae; _ga=GA1.2.BA6694EC20BCDE21; qntcst=D; '
                  '__adroll_fpc=28d2b3940779e0b43cc71cad24bdd734-1656080778626; __qca=P0-563054302-1656080942112; '
                  '_gid=GA1.2.2060074903.1656420817; '
                  'adc=g0Ppqadfsr_Dd7HltvsMfA%3A1NXASnXS0nEE0fRrJ3kzYg%3A1656420821; g_state={"i_p":1657026893438,'
                  '"i_l":3}; location=%7B%22provenance%22%3A+%22YELP_GEOCODING_ENGINE%22%2C+%22max_latitude%22%3A+40'
                  '.8523%2C+%22display%22%3A+%22New+York%2C+NY%22%2C+%22location_type%22%3A+%22locality%22%2C'
                  '+%22country%22%3A+%22US%22%2C+%22max_longitude%22%3A+-73.7938%2C+%22unformatted%22%3A+%22New+York'
                  '%2C+NY%2C+United+States%22%2C+%22city%22%3A+%22New+York%22%2C+%22place_id%22%3A+%221208%22%2C'
                  '+%22min_latitude%22%3A+40.5597%2C+%22zip%22%3A+%22%22%2C+%22min_longitude%22%3A+-74.1948%2C'
                  '+%22address1%22%3A+%22%22%2C+%22longitude%22%3A+-74.0072%2C+%22accuracy%22%3A+4%2C+%22address2%22'
                  '%3A+%22%22%2C+%22parent_id%22%3A+975%2C+%22state%22%3A+%22NY%22%2C+%22latitude%22%3A+40.713%2C'
                  '+%22address3%22%3A+%22%22%2C+%22borough%22%3A+%22%22%2C+%22county%22%3A+null%2C+%22isGoogleHood%22'
                  '%3A+false%2C+%22language%22%3A+null%2C+%22neighborhood%22%3A+%22%22%2C+%22polygons%22%3A+null%2C'
                  '+%22usingDefaultZip%22%3A+false%2C+%22confident%22%3A+null%7D; '
                  'xcj=1|j_q5LbEP87KXBEPWn8qY9uSt4tiBsR6fjHWMiJcdNpo; _uetsid=51dd4990f6e111ecb7a14b33982b038d; '
                  '_uetvid=9a6804f0f3c911eca54f97975605a13f; _clck=f6zd6p|1|f2q|0; _gat_www=1; _gat_global=1; '
                  '_clsk=1gx3nr2|1656484784423|1|0|i.clarity.ms/collect; '
                  'OptanonConsent=isGpcEnabled=0&datestamp=Wed+Jun+29+2022+08%3A39%3A45+GMT%2B0200+('
                  '%D0%92%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B0%D1%8F+%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0%2C+%D1'
                  '%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F'
                  ')&version=6.34.0&isIABGlobal=false&hosts=&consentId=a74444f9-6bd6-4278-ac84-d8eb9a78f8cf'
                  '&interactionCount=1&landingPath=NotLandingPage&groups=BG40%3A1%2CC0003%3A1%2CC0002%3A1%2CC0001%3A1'
                  '%2CC0004%3A1&AwaitingReconsent=false; '
                  '__ar_v4=LVCLLLVUZFCSRK365YBIPN%3A20220624%3A4%7CBHPKS4B4ONEJJMGH4QCJZR%3A20220624%3A21'
                  '%7CQB5JPFIKRZDSBOZSULG4YB%3A20220624%3A21%7C7YX6SJQ4RZAMPB6LZ7CHFF%3A20220624%3A14'
                  '%7CARGNOGM3TZHSNIBHZFGOBV%3A20220624%3A3',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/102.0.0.0 Safari/537.36 '
    }
    return headers


def run_request(current_url):
    response = requests.get(current_url)
    return response


def get_website(date_soup, b_url):
    ws = date_soup.find_all('a', class_='css-1um3nx', rel='noopener')
    website = 'None'
    if ws:
        link = ws[0].attrs['href'].replace('/biz_redir?url=http%3A%2F%2F', 'http://www.').replace('/biz_redir?url=https%3A%2F%2F', 'https://www.')
        link_list = link.split('&')[0].split('.')
        if link_list[1] == 'www':
            link_list.pop(1)
        n = 0
        for el in link_list:
            if '%' in el:
                i = 0
                new_el = ''
                while not el[i] == '%':
                    new_el = new_el + el[i]
                    i += 1
                link_list[n] = new_el
            n += 1
        return f'{".".join(link_list)}'
    return website


def get_links(current_url, path, page):
    url = urlparse(work_url)
    base_url = f'{url.scheme}://{url.netloc}'
    params = {'start': page}
    pages = 10 + page
    d_list = []

    headers = get_hiders()

    with open(path, 'w', encoding='utf-8', newline='\n') as csvfile:
        csv.register_dialect('myDialect', delimiter=';', quoting=csv.QUOTE_NONE)
        writer = csv.writer(csvfile, dialect='myDialect')
        writer.writerow(('name', 'web_site', 'owner_name', 'owner_status', 'e-mail'))

        while params['start'] <= pages:
            print(f'Обрабатываю {int((params["start"] + 10) / 10)} страницу... ')
            if int(params["start"]) == 0:
                response = requests.get(current_url, headers=headers)
            else:
                response = requests.get(current_url, headers=headers, params=params)
            if not response.status_code == 200:
                print(f'Ошибка: {response.status_code}')
                break
            text = response.text
            soup = bs(text, "html.parser")

            cards = soup.find_all('a', class_='css-1m051bw')
            pag_nav = soup.find('div', attrs={'aria-label': 'Pagination navigation'})

            time_counter = 0
            for card in cards:

                if time_counter == 3:
                    time_counter = 0
                    time.sleep(random.randint(20, 30))

                link_card = card.attrs['href']
                if '/biz/' in link_card:
                    data_dict = {}
                    name_card = card.attrs['name']
                    data_dict['name'] = name_card
                    response = run_request(base_url + link_card)
                    if not response.status_code == 200:
                        print(f'Ошибка: {response.status_code}')
                        continue
                    c_text = response.text
                    c_soup = bs(c_text, "html.parser")

                    data_dict['web_site'] = get_website(c_soup, base_url)

                    business_info = c_soup.find_all('section', attrs={'aria-label': 'About the Business'})
                    if business_info:
                        owner_name = business_info[0].find('p', class_='css-ux5mu6', attrs={'data-font-weight': 'bold'})
                        if owner_name:
                            data_dict['owner_name'] = owner_name.text
                        else:
                            data_dict['owner_name'] = 'None'

                        owner_status = business_info[0].find('p', class_='css-chan6m', attrs={'aria-hidden': 'true'})
                        if owner_status:
                            data_dict['owner_status'] = owner_status.text
                        else:
                            data_dict['owner_status'] = 'None'
                    else:
                        data_dict['owner_name'] = 'None'
                        data_dict['owner_status'] = 'None'
                    # если в основной части нет данных о владельце, поищем в комментах
                    if data_dict['owner_status'] == 'None' or not data_dict['owner_status'] == 'Business Owner':
                        ask_com = c_soup.find_all('section', attrs={'aria-label': 'Ask the Community'})
                        if ask_com:
                            owner_name = ask_com[0].find('span', class_='css-1fnccdf',
                                                         attrs={'data-font-weight': 'semibold'})
                            if owner_name:
                                list_own = owner_name.text.split(',')
                                if len(list_own) > 1:
                                    data_dict['owner_name'] = list_own[0]
                                    data_dict['owner_status'] = list_own[1].strip()

                    create_email(data_dict)

                    d_list.append(data_dict)
                    print(f'\t{data_dict}')
                    writer.writerow(
                        (data_dict['name'],
                         data_dict['web_site'],
                         data_dict['owner_name'],
                         data_dict['owner_status'],
                         data_dict['e-mail']
                         ))
                    time_counter += 1
                    time.sleep(random.randint(10, 20))

            last_page_num = int(pag_nav.find_all('div', class_='undefined display--inline-block__09f24__fEDiJ '
                                                               'border-color--default__09f24__NPAKY')[-2].text) * 10
            pages = last_page_num if pages < last_page_num else pages
            params['start'] += 10
            time.sleep(random.randint(10, 20))


def create_email(c_dict):
    c_dict['e-mail'] = 'None'
    if not c_dict['owner_name'] == 'None' and not c_dict['web_site'] == 'None':
        list_for_adress = c_dict['web_site'].split('.')
        c_dict['e-mail'] = f"{c_dict['owner_name'].replace(' ', '').replace('.', '')}@{list_for_adress[-2]}.{list_for_adress[-1]}".lower()


if __name__ == '__main__':
    work_url = input('Введите адрес: ')
    # work_url = WORK_URL

    start_page = input('Введите начальную страницу: ')

    if start_page == '':
        start_page = 0
    else:
        start_page = (int(start_page) - 1) * 10

    file_name = datetime.now().strftime("%d%m%Y-%H%M%S")+'.csv'
    print(file_name)

    # print('Выберите директорию для сохранения файла.')
    # current_path = asksaveasfilename(filetypes=[("csv", ".csv")], initialfile='*.csv')

    if file_name:
        # current_path:
        get_links(work_url, file_name, start_page)
        print(f'Данные сохранены в {file_name}')
