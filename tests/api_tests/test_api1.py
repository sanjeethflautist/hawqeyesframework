import requests
from common_lib.global_data import GlobalData
from common_lib.assertions import assert_valid_schema
import common_lib.api as api
import json


def test_GET_LIST_USERS():
    data = {'page':2}
    response = api.restcall(GlobalData.REQRES_API_USERS,data=data,method = 'GET')
    assert response.status_code == 200
    json_data = json.loads(response.content)
    assert_valid_schema (json_data,"user_scheema.json")
    print(json_data)

def test_GET_SINGLE_USER():
    response = api.restcall(GlobalData.REQRES_API_USERS+"/2",data={},method = 'GET')
    assert response.status_code == 200

def test_GET_SINGLE_USER_NOT_FOUND():
    response = api.restcall(GlobalData.REQRES_API_USERS+"/23",data={},method = 'GET')
    assert response.status_code == 404

def test_GET_LIST_RESOURCE():
    response = api.restcall(GlobalData.REQRES_API_UNKNOWN+"/2",data={},method = 'GET')
    assert response.status_code == 200

def test_GET_SINGLE_RESOURCE():
    response = api.restcall(GlobalData.REQRES_API_UNKNOWN,data={},method = 'GET')
    assert response.status_code == 200

def test_GET_SINGLE_RESOURCE_NOTFOUND():
    response = api.restcall(GlobalData.REQRES_API_USERS+"/23",data={},method = 'GET')
    assert response.status_code == 404

def test_POST_CREATE():
    data = {"name": "morpheus","job": "leader"}
    response = api.restcall(GlobalData.REQRES_API_USERS,data=data,method = 'POST')
    assert response.status_code == 201

def test_PUT_UPDATE():
    data = {"name": "morpheus", "job": "zion resident"}
    response = api.restcall(GlobalData.REQRES_API_USERS+"/2",data=data,method = 'PUT')
    assert response.status_code == 200

def test_PATCH_UPDATE():
    data = {"name": "morpheus", "job": "zion resident"}
    response = api.restcall(GlobalData.REQRES_API_USERS+"/2",data=data,method = 'PATCH')
    assert response.status_code == 200

def test_DELETE():
    response = api.restcall(GlobalData.REQRES_API_USERS+"/2",data={},method = 'DELETE')
    assert response.status_code == 204

def test_POST_REGISTER_SUCCESSFUL():
    data = { "email": "eve.holt@reqres.in",  "password": "pistol"}
    response = api.restcall(GlobalData.REQRES_API_REGISTER,data=data,method = 'POST')
    assert response.status_code == 200

def test_POST_REGISTER_UNSUCCESSFUL():
    data = { "email": "sydney@fife"}
    response = api.restcall(GlobalData.REQRES_API_REGISTER,data=data,method = 'POST')
    assert response.status_code == 400

def test_POST_LOGIN_SUCCESSFUL():
    data = { "email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = api.restcall(GlobalData.REQRES_API_LOGIN,data=data,method = 'POST')
    assert response.status_code == 200

def test_POST_LOGIN_UNSUCCESSFUL():
    data = { "email": "peter@klaven"}
    response = api.restcall(GlobalData.REQRES_API_LOGIN,data=data,method = 'POST')
    assert response.status_code == 400

def test_GET_DELAYED_RESPONSE():
    data = {'delay': 3}
    response = api.restcall(GlobalData.REQRES_API_USERS,data=data,method = 'GET')
    assert response.status_code == 200