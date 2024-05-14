import requests
from bs4 import BeautifulSoup
import json
from flask import jsonify
import re


def delete_sup(code, ID, indexOFSub):
    while True:
        try:
            res = requests.post(
                'https://studentactivities.zu.edu.eg/Students/Registration/ed_login.aspx'
            )
            html = res.text
            soup = BeautifulSoup(html, 'html.parser')
            viewstate_input = soup.find('input', {'name': '__VIEWSTATE'})
            viewstate_value = viewstate_input['value']
            viewstate_generator_input = soup.find('input',
                                                  {'name': '__VIEWSTATEGENERATOR'})
            event_validation_input = soup.find(
                'input', {'name': '__EVENTVALIDATION'})
            viewstate_generator_value = viewstate_generator_input['value']
            event_validation_value = event_validation_input['value']
            cookies = res.cookies
            cookie_strings = []
            for cookie in cookies:
                cookie_strings.append(f"{cookie.name}={cookie.value}")
            url = "https://studentactivities.zu.edu.eg/Students/Registration/ed_login.aspx"

            headers = {
                "cookie": f"{cookie_strings[0]}",
                "content-length": "1022",
                "sec-ch-ua": '"Chromium";v="121", "Not A(Brand";v="99"',
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "cache-control": "no-cache",
                "x-microsoftajax": "Delta=true",
                "sec-ch-ua-mobile": "?0",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Safari/537.36",
                "sec-ch-ua-platform": '"Windows"',
                "accept": "*/*",
                "origin": "https://studentactivities.zu.edu.eg",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://studentactivities.zu.edu.eg/Students/Registration/ed_login.aspx",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "priority": "u=1, i"
            }
            # Form data
            data = {
                "ctl00$ScriptManager1": "ctl00$cntphmaster$panal1|ctl00$cntphmaster$btn_Login",
                "ctl00$cntphmaster$txt_StudCode": f"{code}",
                "ctl00$cntphmaster$txt_Nationalnum": f"{ID}",
                "__LASTFOCUS": "",
                "__EVENTTARGET": "",
                "__EVENTARGUMENT": "",
                "__VIEWSTATE": f"{viewstate_value}",
                "__VIEWSTATEGENERATOR": f"{viewstate_generator_value}",
                "__EVENTVALIDATION": f"{event_validation_value}",
                "__ASYNCPOST": "true",
                "ctl00$cntphmaster$btn_Login": "تسجيل دخول",
            }

            response = requests.post(url, headers=headers, data=data)

            url1 = "https://studentactivities.zu.edu.eg/Students/Registration/ED/OR_MAIN_PAGE.aspx"
            headers1 = {
                "cookie": f"{cookie_strings[0]}",
                "content-length": "1608",
                "sec-ch-ua": '"Chromium";v="121", "Not A(Brand";v="99"',
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "cache-control": "no-cache",
                "x-microsoftajax": "Delta=true",
                "sec-ch-ua-mobile": "?0",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Safari/537.36",
                "sec-ch-ua-platform": '"Windows"',
                "accept": "*/*",
                "origin": "https://studentactivities.zu.edu.eg",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://studentactivities.zu.edu.eg/Students/Registration/ED/OR_MAIN_PAGE.aspx",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "priority": "u=1, i"
            }

            data1 = {
                "ctl00$ScriptManager1": "ctl00$paneltbl|ctl00$lbRecordStudentPrimarySubjectsCredit",
                "__EVENTTARGET": "ctl00$lbRecordStudentPrimarySubjectsCredit",
                "__EVENTARGUMENT": "",
                "__VIEWSTATE": f"{viewstate_value}",
                "__VIEWSTATEGENERATOR": f"{viewstate_generator_value}",
                "__EVENTVALIDATION": f"{event_validation_value}",
                "__ASYNCPOST": "true",
            }

            response1 = requests.post(url1, headers=headers1, data=data1)

            url2 = "https://studentactivities.zu.edu.eg/Students/Registration/ED/OR_RecordStudentPrimarySubjectsCredit.aspx"
            headers2 = {

                "cookie": f"{cookie_strings[0]}",
                "sec-ch-ua": '"Chromium";v="121", "Not A(Brand";v="99"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"Windows"',
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Safari/537.36",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "navigate",
                "sec-fetch-user": "?1",
                "sec-fetch-dest": "document",
                "referer": "https://studentactivities.zu.edu.eg/Students/Registration/ED/OR_MAIN_PAGE.aspx",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "priority": "u=0, i"
            }
            response2 = requests.get(url2, headers=headers2)
            html2 = response2.text
            soup = BeautifulSoup(html2, 'html.parser')
            desired_values = [
                "ctl00$cntphmaster$txtEdPhaseNodeIdHidden",
                "ctl00$cntphmaster$txtAsNodeHidden",
                "ctl00$cntphmaster$Txtstudid",
                "ctl00$cntphmaster$txtAsNodeIDHidden",
                "ctl00$cntphmaster$HidEdStudScholasticId"
            ]

            extracted_values = {}

            for value_id in desired_values:
                element = soup.find("input", {"name": value_id})
                if element:
                    extracted_values[value_id] = element.get('value')
            viewstate_input = soup.find('input', {'name': '__VIEWSTATE'})
            viewstate_value2 = viewstate_input['value']
            event_validation_input = soup.find(
                'input', {'name': '__EVENTVALIDATION'})
            event_validation_value2 = event_validation_input['value']

            url3 = "https://studentactivities.zu.edu.eg/Students/Registration/ED/OR_RecordStudentPrimarySubjectsCredit.aspx"
            payload3 = {'ctl00$ScriptManager1': 'ctl00$cntphmaster$panal1|ctl00$cntphmaster$GridDataCount_DropDownList',
                        '__EVENTTARGET': 'ctl00$cntphmaster$GridDataCount_DropDownList',
                        '__EVENTARGUMENT': '',
                        '__LASTFOCUS': '',
                        '__VIEWSTATE': f'{viewstate_value2}',
                        '__VIEWSTATEGENERATOR': '798032E8',
                        '__SCROLLPOSITIONX': '0',
                        '__SCROLLPOSITIONY': '0',
                        '__VIEWSTATEENCRYPTED': '',
                        '__EVENTVALIDATION': f'{event_validation_value2}',
                        'ctl00$cntphmaster$txtEdAcadYearYearIdHidden': '54',
                        'ctl00$cntphmaster$txtEdPhaseNodeIdHidden': extracted_values['ctl00$cntphmaster$txtEdPhaseNodeIdHidden'],
                        'ctl00$cntphmaster$txtAsNodeHidden': extracted_values['ctl00$cntphmaster$txtAsNodeHidden'],
                        'ctl00$cntphmaster$Txtstudid': extracted_values['ctl00$cntphmaster$Txtstudid'],
                        'ctl00$cntphmaster$GridDataCount_DropDownList': '300',
                        'ctl00$cntphmaster$txtEdStudScholasticHidden': '',
                        'rbHiddenHasGroup': '',
                        'rbHiddenHasGroup': '',
                        'rbHiddenHasGroup': '',
                        'rbHiddenHasGroup': '',
                        'rbHiddenHasGroup': '',
                        'rbHiddenHasGroup': '',
                        'rbHiddenHasGroup': '',
                        'rbHiddenHasGroup': '',
                        'rbHiddenHasGroup': '',
                        'rbHiddenHasGroup': '',
                        'ctl00$cntphmaster$txtAsNodeIDHidden':  extracted_values['ctl00$cntphmaster$txtAsNodeIDHidden'],
                        'ctl00$cntphmaster$txtEDSUBJECTID': '',
                        'ctl00$cntphmaster$txtFacultyTransfereFrom': '',
                        'ctl00$cntphmaster$txtCurrentFacultyTransfereTo': '',
                        'ctl00$cntphmaster$txtEdPhaseNodeID': '',
                        'ctl00$cntphmaster$txtAsNodeID': '',
                        'ctl00$cntphmaster$txtedStudDiversionToAppId': '',
                        'ctl00$cntphmaster$txtEdAcadYearID': '',
                        'ctl00$cntphmaster$txtEdSubjectIDs': '',
                        'ctl00$cntphmaster$grdEdStudSubjectPhase$ctl02$ctl00': 'on',
                        'ctl00$cntphmaster$grdEdStudSubjectPhase$ctl03$ctl00': 'on',
                        'ctl00$cntphmaster$grdEdStudSubjectPhase$ctl04$ctl00': 'on',
                        'ctl00$cntphmaster$grdEdStudSubjectPhase$ctl05$ctl00': 'on',
                        'ctl00$cntphmaster$grdEdStudSubjectPhase$ctl06$ctl00': 'on',
                        'ctl00$cntphmaster$grdEdStudSubjectPhase$ctl08$ctl00': 'on',
                        'ctl00$cntphmaster$HidEdStudScholasticId': extracted_values['ctl00$cntphmaster$HidEdStudScholasticId'],
                        '__ASYNCPOST': 'true', }
            headers3 = {
                'cookie': f'{cookie_strings[0]}',
                'content-length': '7870',
                'sec-ch-ua': '"Chromium";v="121", "Not A(Brand";v="99"',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'cache-control': 'no-cache',
                'x-microsoftajax': 'Delta=true',
                'sec-ch-ua-mobile': '?0',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Safari/537.36',
                'sec-ch-ua-platform': '"Windows"',
                'accept': '*/*',
                'origin': 'https://studentactivities.zu.edu.eg',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://studentactivities.zu.edu.eg/Students/Registration/ED/OR_RecordStudentPrimarySubjectsCredit.aspx',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'priority': 'u=1, i'
            }
            response3 = requests.request(
                "POST", url3, headers=headers3, data=payload3)
            if "error" not in response3.text:
                selectSupTable = response3.text
                pattern = r"__EVENTVALIDATION\|([^\|]+)"
                matches = re.findall(pattern, selectSupTable)
                for match in matches:
                    event_validation_value5 = match

                pattern = r"__VIEWSTATE\|([^\|]+)"
                matches = re.findall(pattern, selectSupTable)
                for match in matches:
                    viewstate_value5 = match

                url = "https://studentactivities.zu.edu.eg/Students/Registration/ED/OR_RecordStudentPrimarySubjectsCredit.aspx"

                payload = {
                    'ctl00$ScriptManager1': 'ctl00$cntphmaster$panal1|ctl00$cntphmaster$grdEdStudSubjectPhase$ctl07$btnDelete',
                    'ctl00$cntphmaster$txtEdAcadYearYearIdHidden': '54',
                    'ctl00$cntphmaster$txtEdPhaseNodeIdHidden': extracted_values['ctl00$cntphmaster$txtEdPhaseNodeIdHidden'],
                    'ctl00$cntphmaster$txtAsNodeHidden': extracted_values['ctl00$cntphmaster$txtAsNodeHidden'],
                    'ctl00$cntphmaster$Txtstudid': extracted_values['ctl00$cntphmaster$Txtstudid'],
                    'ctl00$cntphmaster$GridDataCount_DropDownList': '300',
                    'ctl00$cntphmaster$txtEdStudScholasticHidden': '',
                    'rbHiddenHasGroup': '',
                    'rbHiddenHasGroup': '',
                    'rbHiddenHasGroup': '',
                    'rbHiddenHasGroup': '',
                    'rbHiddenHasGroup': '',
                    'rbHiddenHasGroup': '',
                    'rbHiddenHasGroup': '',
                    'rbHiddenHasGroup': '',
                    'rbHiddenHasGroup': '',
                    'rbHiddenHasGroup': '',
                    'rbHiddenHasGroup': '',
                    'rbHiddenHasGroup': '',
                    'rbHiddenHasGroup': '',
                    'rbHiddenHasGroup': '',
                    'rbHiddenHasGroup': '',
                    'rbHiddenHasGroup': '',
                    'rbHiddenHasGroup': '',
                    'rbHiddenHasGroup': '',
                    'rbHiddenHasGroup': '',
                    'rbHiddenHasGroup': '',
                    'rbHiddenHasGroup': '',
                    'rbHiddenHasGroup': '',
                    'rbHiddenHasGroup': '',
                    'rbHiddenHasGroup': '',
                    'rbHiddenHasGroup': '',
                    'rbHiddenHasGroup': '',
                    'rbHiddenHasGroup': '',
                    'rbHiddenHasGroup': '',
                    'ctl00$cntphmaster$txtAsNodeIDHidden': extracted_values['ctl00$cntphmaster$txtAsNodeIDHidden'],
                    'ctl00$cntphmaster$txtEDSUBJECTID': '',
                    'ctl00$cntphmaster$txtFacultyTransfereFrom': '',
                    'ctl00$cntphmaster$txtCurrentFacultyTransfereTo': '',
                    'ctl00$cntphmaster$txtEdPhaseNodeID': '',
                    'ctl00$cntphmaster$txtAsNodeID': '',
                    'ctl00$cntphmaster$txtedStudDiversionToAppId': '',
                    'ctl00$cntphmaster$txtEdAcadYearID': '',
                    'ctl00$cntphmaster$txtEdSubjectIDs': '',
                    'ctl00$cntphmaster$grdEdStudSubjectPhase$ctl02$ctl00': 'on',
                    'ctl00$cntphmaster$grdEdStudSubjectPhase$ctl03$ctl00': 'on',
                    'ctl00$cntphmaster$grdEdStudSubjectPhase$ctl04$ctl00': 'on',
                    'ctl00$cntphmaster$grdEdStudSubjectPhase$ctl05$ctl00': 'on',
                    'ctl00$cntphmaster$grdEdStudSubjectPhase$ctl07$ctl00': 'on',
                    'ctl00$cntphmaster$HidEdStudScholasticId': extracted_values['ctl00$cntphmaster$HidEdStudScholasticId'],
                    '__EVENTTARGET': '',
                    '__EVENTARGUMENT': '',
                    '__LASTFOCUS': '',
                    '__VIEWSTATE': f'{viewstate_value5}',
                    '__VIEWSTATEGENERATOR': '798032E8',
                    '__SCROLLPOSITIONX': '0',
                    '__SCROLLPOSITIONY': '0',
                    '__EVENTVALIDATION': f'{event_validation_value5}',
                    '__VIEWSTATEENCRYPTED': '',
                    '__ASYNCPOST': 'true',
                    f'ctl00$cntphmaster$grdEdStudSubjectPhase$ctl0{indexOFSub}$btnDelete.x': '10',
                    f'ctl00$cntphmaster$grdEdStudSubjectPhase$ctl0{indexOFSub}$btnDelete.y': '14',
                }
                headers = {
                    "Accept": "*/*",
                    "Accept-Encoding": "gzip, deflate, br, zstd",
                    "Accept-Language": "en,ar;q=0.9,en-US;q=0.8",
                    "Cache-Control": "no-cache",
                    "Content-Length": "17051",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "Cookie": "ASP.NET_SessionId=4r004yfwvsgbt355tbdgf545",
                    "Origin": "https://studentactivities.zu.edu.eg",
                    "Referer": "https://studentactivities.zu.edu.eg/Students/Registration/ED/OR_RecordStudentPrimarySubjectsCredit.aspx",
                    "Sec-Ch-Ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
                    "Sec-Ch-Ua-Mobile": "?0",
                    "Sec-Ch-Ua-Platform": '"Windows"',
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-origin",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
                    "X-Microsoftajax": "Delta=true"
                }
                x = requests.post(url, headers=headers, data=payload)
                soup = BeautifulSoup(x.text, 'html.parser')

                # Extract the text value from the span element
                span_element = soup.find(
                    'span', id='ctl00_cntphmaster_ConfirmUserControl_lblmessage')
                if span_element:
                    extracted_value = span_element.text
                    return jsonify({"msg": "تم حذف المقرر"})
                else:
                    print("Span element not found.")

            else:
                continue

        except Exception as e:
            continue
