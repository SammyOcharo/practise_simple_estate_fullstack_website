from rest_framework.exceptions import APIException

class PropertyNotFound(APIException):
    statsu_code = 404
    default_detail = "The requested property does not exist"
    