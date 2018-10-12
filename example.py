#!/usr/bin/env python
# -*- coding: utf8 -*-
from domainhelper import get_multi_domain, get_top_domain, get_domain_suffix


def demo():
    domains = ['a.b.c.www.baidu.com.cn', 'asdfEw.不存在', 'www.qq.com', '国际化域名.org']
    for domain in domains:
        print(domain + ": " + str(get_domain_suffix(domain)))
        print(domain + ": " + str(get_top_domain(domain)))
        print(domain + ": " + str(get_multi_domain(domain)))
        print('')


if __name__ == '__main__':
    demo()
