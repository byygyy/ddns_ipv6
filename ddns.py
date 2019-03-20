#!/usr/bin/env python
#coding=utf-8
import os
import time
import urllib2
import re
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest

def ddns_ipv6():
    ipv6_address_last = None
    while(True):
        ipv6_address_current = get_Local_ipv6_address()
        if ipv6_address_last <> ipv6_address_current:
            print 'domain name is not the same, changing ....'
            alidns_update(ipv6_address_current)
	    ipv6_address_last = ipv6_address_current
        else:
            print 'domain name is the same, wait next time check after 3600 s'
        time.sleep(3600)

def alidns_update(ipv6_address=None):
    client = AcsClient('LTAITiGjmlacminr', 'nAMZ7YLVIBwbQWiwIo5D94aBU8mf1p', 'default')
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('alidns.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https') # https | http
    request.set_version('2015-01-09')
    request.set_action_name('UpdateDomainRecord')

    request.add_query_param('RecordId', '17316324837254144')
    request.add_query_param('RR', 'ipv6')
    request.add_query_param('Type', 'AAAA')
    request.add_query_param('Value', ipv6_address)

    response = client.do_action(request)
    print(response)

def get_Local_ipv6_address():
    """
        Get local ipv6
    """
    pageURL='http://ipv6.sjtu.edu.cn/'
    content=urllib2.urlopen(pageURL).read()

    ipv6_pattern='(([a-f0-9]{1,4}:){7}[a-f0-9]{1,4})'

    m = re.search(ipv6_pattern, content)

    if m is not None:
        return str(m.group())
    else:
        return None

if __name__ == "__main__":
    ddns_ipv6()