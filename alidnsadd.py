#!/usr/bin/env python
#coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
#client = AcsClient('<accessKeyId>', '<accessSecret>', 'default')
client = AcsClient('accessKeyId', 'accessSecret', 'default')

request = CommonRequest()
request.set_accept_format('json')
request.set_domain('alidns.aliyuncs.com')
request.set_method('POST')
request.set_protocol_type('https') # https | http
request.set_version('2015-01-09')
request.set_action_name('AddDomainRecord')

request.add_query_param('DomainName', 'lhh.fun')
request.add_query_param('RR', 'ipv6')
request.add_query_param('Type', 'AAAA')
request.add_query_param('Value', '2408:8270:450:4a88:ac19:4cd8:936a:dbe')

response = client.do_action(request)
print(response)
# python3:  print(str(response, encoding = 'utf-8'))
