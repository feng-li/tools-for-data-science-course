import requests

url = "http://www.baidu.com"

response = requests.get( url )

response.encoding = "utf-8" #设置接收编码格式

print(" r的类型" + str( type(response) ) )

print(" 状态码是:" + str( response.status_code ) )

print(" 头部信息:" + str( response.headers ) )

print( " 响应内容:" )

print( response.text )


