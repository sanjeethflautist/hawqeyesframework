import requests
from common_lib.global_data import GlobalData
import logging


def restcall(url,data,method ='GET',headers =GlobalData.COMMON_HEADER):
    response = False
    logging.info("API Call with following parameters:")
    logging.info(url)
    logging.info(data)
    logging.info(method)
    logging.info(headers)
    logging.info("----------------------------------------------------------")
    #try:
    if method.upper() == 'GET':
        response = requests.get(url,data,verify=False)
    elif method.upper() == 'POST':
        response = requests.post(url, data, headers,verify=False)
    elif method.upper() == 'PUT':
        response = requests.put(url, data, headers,verify=False)
    elif method.upper() == 'PATCH':
        response = requests.patch(url, data,verify=False)
    elif method.upper() == 'DELETE':
        response = requests.delete(url,verify=False)
    else:
        logging.error(str(method)+ " is not supported please try with either GET, POST, PUT, PATCH or DELETE methods")
    #except Exception as e:
    #    logging.exception(str(e))
    logging.info(response)
    logging.info(response.content)
    file = open('collectedRes.txt','a')
    file.write(str(response.content)+"\n\n\n\n\n\n")
    return response
