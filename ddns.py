#!/usr/bin/env python
#coding=utf-8
import os
import time
import urllib2
import re
import commands
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest

def ddns_ipv6():
    ipv6_address_last = None
    while(True):
        #get ipv6 address from windows
        #ipv6_address_current = get_Local_ipv6_address()
        #get ipv6 address from linux server
        ipv6_address_current = get_Local_linux_ipv6_address()
        if ipv6_address_last <> ipv6_address_current:
            print 'domain name is not the same, changing ....'
            alidns_update(ipv6_address_current,'17335666358574080','ipv6','AAAA') #ipv6.lhh.fun
            alidns_update(ipv6_address_current,'17340956348144640','blog','AAAA') #blog.lhh.fun
	    alidns_update(ipv6_address_current,'17346273820107776','@','AAAA') #robin.org.cn
            alidns_update(ipv6_address_current,'17346274190450688','www','AAAA') #www.robin.org.cn
            alidns_update(ipv6_address_current,'17346444077979648','up','AAAA') #up.robin.org.cn 
            ipv6_address_last = ipv6_address_current
            print 'domain name have been changed, wait next time check after 600 s'
        else:
            print 'domain name is the same, wait next time check after 600 s'
        time.sleep(600)

def alidns_update(ipv6_address=None,RecordId=None,RR=None,Type=None):
    client = AcsClient('LTAITiGjmlacminr', 'nAMZ7YLVIBwbQWiwIo5D94aBU8mf1p', 'default')
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('alidns.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https') # https | http
    request.set_version('2015-01-09')
    request.set_action_name('UpdateDomainRecord')

    request.add_query_param('RecordId', RecordId)
    request.add_query_param('RR', RR)
    request.add_query_param('Type', Type)
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

def get_Local_linux_ipv6_address():
    (status, output) = commands.getstatusoutput("ifconfig|grep inet6|grep global|grep 'prefixlen 64'|awk '{print $2}'|sed -n '1p'")
    return str(output)

if __name__ == "__main__":
    ddns_ipv6()
