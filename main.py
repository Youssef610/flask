from flask import Flask, request, jsonify
from login import loginPage
from natiga import get_natiga
from register import get_register
from regist_sup import regist_sup
import asyncio

app = Flask(__name__)

async def async_login(id, code):
    return await asyncio.to_thread(loginPage, id, code)


async def async_natiga(ID, code):
    return await asyncio.to_thread(get_natiga, ID, code)


async def async_register(ID, code):
    return await asyncio.to_thread(get_register, ID, code)

async def async_regist_sup(ID, code,indexOFSub):
    return await asyncio.to_thread(regist_sup, ID, code,indexOFSub)

@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        id = data['id']
        code = data['code']
        extracted_data = loginPage(id, code)
    except Exception as e:
        error_message = "Internal Server Error: {}".format(str(e))
        return jsonify({"error": error_message}), 500

    return jsonify(extracted_data)


@app.route('/natiga', methods=['POST'])
def natiga():
    try:
        data = request.get_json()
        ID = data['id']
        code = data['code']
        extracted_data = get_natiga(ID, code)
    except Exception as e:
        error_message = "Internal Server Error: {}".format(str(e))
        return jsonify({"error": error_message}), 500

    return extracted_data


@app.route('/register', methods=['POST'])
def register():
    try:
        print('WE IN REGISTER')
        data = request.get_json()
        ID = data['id']
        code = data['code']
        extracted_data = get_register(code=code, ID=ID)
    except Exception as e:
        error_message = "Internal Server Error: {}".format(str(e))
        return jsonify({"error": error_message}), 500
    return extracted_data
@app.route('/registSup', methods=['POST'])
def regisSup():
    try:
        print('WE IN RegistSup')
        data = request.get_json()
        ID = data['id']
        code = data['code']
        indexOFSub = data['indexOFSub']
        extracted_data = regist_sup(code=code, ID=ID,indexOFSub=indexOFSub)
    except Exception as e:
        error_message = "Internal Server Error: {}".format(str(e))
        return jsonify({"error": error_message}), 500
    return extracted_data


@app.route('/')
def home():
    return jsonify({"msg": "Server For Our SCI APP..."})




