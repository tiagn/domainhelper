#!/usr/bin/env python
# -*- coding: utf8 -*-
from domainhelper import verify_domain, get_multi_domain, get_top_domain, get_domain_suffix


def test_domainhelper():
    assert verify_domain('baidu.com') == True
    assert verify_domain('www.baIdu.com') == True
    assert verify_domain('wwww.wWw.baidu.Com') == True
    assert verify_domain('中国.cOm') == True
    assert verify_domain('www.Wc中国.com') == True
    assert verify_domain('广东.中C国。com') == True
    assert verify_domain('baidCu.中国') == True
    assert verify_domain('中国EW.中国') == True
    assert verify_domain('广东.中国。中国') == True
    assert verify_domain('asdfEw.不存在') == False
    assert verify_domain('ba_iduE.com') == False
    assert verify_domain('w_ww.baEidu.com') == True
    assert verify_domain('ww_ww.w_ww.baidu.com') == True
    assert verify_domain('中_国.com') == False
    assert verify_domain('ww_Ew.中国.com') == True
    assert verify_domain('广_东.中国。com') == True
    assert verify_domain('bai_du.中国') == False
    assert verify_domain('中_国E.中国') == False
    assert verify_domain('广__东.中E国。中国') == True
    assert verify_domain('asdf.不存在') == False
    assert get_multi_domain('a.b.c.www.baidu.com.cn') == ['baidu.com.cn', 'www.baidu.com.cn', 'c.www.baidu.com.cn',
                                                          'b.c.www.baidu.com.cn', 'a.b.c.www.baidu.com.cn']
    assert get_top_domain('a.b.c.www.baidu.com.cn') == 'baidu.com.cn'
    assert get_domain_suffix('a.b.c.www.baidu.com.cn') == '.com.cn'


if __name__ == '__main__':
    test_domainhelper()
