import requests
import re
import time
from bs4 import BeautifulSoup


def getStudentBooks(id, code):
    # while True:
    # try:
    url = "http://scistudent.eps.zu.edu.eg/(X(1)S(ocgyf1qhaxaijvus5aa0fsg4))/Views/StudentViews/StudentLogin"
    html = requests.post(url).text
    soup = BeautifulSoup(html, 'html.parser')
    viewstate_input = soup.find('input', {'name': '__VIEWSTATE'})
    viewstate_value = viewstate_input['value']
    viewstate_generator_input = soup.find('input',
                                          {'name': '__VIEWSTATEGENERATOR'})
    event_validation_input = soup.find(
        'input', {'name': '__EVENTVALIDATION'})
    viewstate_generator_value = viewstate_generator_input['value']
    event_validation_value = event_validation_input['value']

    headers = {
        'Host': 'scistudent.eps.zu.edu.eg',
        'Content-Length': '506',
        'Cache-Control': 'no-cache',
        'X-Requested-With': 'XMLHttpRequest',
        'X-MicrosoftAjax': 'Delta=true',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': '*/*',
        'Origin': 'http://scistudent.eps.zu.edu.eg',
        'Referer': url,
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'close',
    }

    data = {
        'ctl00': 'upnlLogin|LinkButton2',
        '__EVENTTARGET': 'LinkButton2',
        '__EVENTARGUMENT': '',
        '__VIEWSTATE': f'{viewstate_value}',
        '__VIEWSTATEGENERATOR': f'{viewstate_generator_value}',
        '__EVENTVALIDATION': f'{event_validation_value}',
        'loginCode': f'{code}',
        'loginPassword': f'{id}',
        '__ASYNCPOST': 'true',
    }

    response = requests.post(url, headers=headers, data=data)
    headers2 = {
        'Host': 'scistudent.eps.zu.edu.eg',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Referer': 'http://scistudent.eps.zu.edu.eg/(X(1)S(ocgyf1qhaxaijvus5aa0fsg4))/Views/StudentViews/Landing',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cookie': f"{ response.headers['Set-Cookie'] }",
        'Connection': 'close',
    }
    response2 = requests.get(
        "http://scistudent.eps.zu.edu.eg/(X(1)S(ocgyf1qhaxaijvus5aa0fsg4))/Views/StudentViews/ESubjectsExams", headers=headers2)

    soup = BeautifulSoup(response2.text, 'html.parser')
    viewstate_input_Book = soup.find('input', {'name': '__VIEWSTATE'})
    viewstate_value_Book = viewstate_input_Book['value']
    event_validation_input_Book = soup.find(
        'input', {'name': '__EVENTVALIDATION'})
    event_validation_value_Book = event_validation_input_Book['value']

    checkbox_elements = soup.find_all(
        'input', {'id': lambda x: x and x.startswith('ContentPlaceHolder1_gridview_chk_')})

    # Initialize a list to hold book names
    book_names = []
    for element in checkbox_elements:
        # Navigate to the parent <tr> element
        parent_tr = element.find_parent('tr')
        if parent_tr:
            # Assuming the book name is always in the 5th <td>
            book_name_td = parent_tr.find_all(
                'td')[4]  # This gets the 5th <td>
            book_name = book_name_td.text.strip()
            book_names.append(book_name)

    checkbox_names = [element['name'] for element in checkbox_elements]
    BooksCodes = [name.replace('$chk', '$lbtnUpdate')
                  for name in checkbox_names]
    BookUrl = "http://scistudent.eps.zu.edu.eg/(X(1)S(ocgyf1qhaxaijvus5aa0fsg4))/Views/StudentViews/ESubjectsExams"
    BooKHeaders = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Length": "5777",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": f"{ response.headers['Set-Cookie'] }",
        "Host": "scistudent.eps.zu.edu.eg",
        "Origin": "http://scistudent.eps.zu.edu.eg",
        "Referer": "http://scistudent.eps.zu.edu.eg/(X(1)S(ocgyf1qhaxaijvus5aa0fsg4))/Views/StudentViews/ESubjectsExams",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
        "X-Microsoftajax": "Delta=true",
        "X-Requested-With": "XMLHttpRequest",
    }

    # Updated to loop through each book code
    book_links = []
    for book_code in BooksCodes:
        payload = {
            "__EVENTTARGET": book_code,  # Code For Each Book
            "__VIEWSTATE": viewstate_value_Book,
            "__EVENTVALIDATION": event_validation_value_Book,
        }

        # Send the POST request for each book
        ViewBook = requests.request(
            "POST", BookUrl, headers=BooKHeaders, data=payload)
        soup = BeautifulSoup(ViewBook.text, 'html.parser')
        match1 = re.search(r'__VIEWSTATE\|(.+?)\|', ViewBook.text)
        if match1:
            viewstate = match1.group(1)
        match2 = re.search(
            r'__EVENTVALIDATION\|(.+?)\|', ViewBook.text)
        if match2:
            eventvalidation = match2.group(1)
        payload2 = {
            "__EVENTTARGET": "ctl00$ContentPlaceHolder1$gvSubjectMaterials$ctl02$lbtnUpdateFila",
            "__VIEWSTATE": f"{viewstate}",
            "__EVENTVALIDATION": f"{eventvalidation}",
        }

        Book = requests.request(
            "POST", BookUrl, headers=BooKHeaders, data=payload2)
        soup = BeautifulSoup(Book.text, 'html.parser')

        object_tag = soup.find('object')
        if object_tag:
            url = object_tag['data']
            book_links.append("http://scistudent.eps.zu.edu.eg" + url)
        else:
            print("Object tag with 'data' attribute not found.")

    print(book_links)
    print(book_names)
    finalList = [[x, y] for x, y in zip(book_names, book_links)]
    return finalList
    # except Exception as e:
    #     print(e)
    #     time.sleep(5)

    # [   ['الشبكات العصبية', '-43569.pdf'],
    #     ['المترجمات', '-43570.pdf'],
    #     ['الشبكات اللاسلكية', '-43572.pdf'],
    #     ['ادارة الشبكات', '-43574.pdf'],
    #     ['قواعد بيانات متقدمة', '-43575.pdf'],
    #     ['ذكاء اصطناعي متقدم', '-43577.pdf']
    # ]
