import requests
import json
import math
def get_page_nums(cityname,jobname):
    """
    获取符合要求的工作页数
    :param cityname: 城市名
    :param jobname: 工作名
    :return: 总数
   """
    url="https://fe-api.zhaopin.com/c/i/sou?pageSize=60&cityId={}&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw={}&kt=3".format(cityname,jobname)
    rec=requests.get(url)
    if rec.status_code==200:
        j=json.loads(rec.text)
        count_num=j.get("data")["numFound"]
    page_nums=math.ceil(count_num/90)
    return page_nums
def get_urls(start,cityname,jobname):

    """
    获取每页工作详情url及部分职位信息
    
