from time import sleep

import pytest
import yaml
from selenium import webdriver

from pycode.login.Base import Base


# 课后作业：使用序列化的方法用cookie登录企业微信
class TestLogin(Base):
    # 复用浏览器,获取cookie,将cookie存入yaml文件中
    def test_getCookies(self):
        opt = webdriver.ChromeOptions()
        # 开启chrome浏览器debug调试模式
        opt.debugger_address = "127.0.0.1:9222"
        print(opt)
        driver = webdriver.Chrome(options=opt)
        driver.find_element_by_id("menu_contacts").click()
        cookies=driver.get_cookies()
        #将cookie序列化,存入.yaml文件中
        with open("data.yaml",mode="w",encoding="utf-8") as f:
            yaml.dump(cookies,f)

    @pytest.mark.skip
    def test_cookie_login(self):

        self.driver.get("https://work.weixin.qq.com/")
        cookies=[{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a1001846'}, {'domain': '.work.weixin.qq.com', 'expiry': 1650379076, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1618582806,1618588535,1618842977,1618843077'}, {'domain': '.qq.com', 'expiry': 1891751798, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': False, 'value': '0_5df5d4763cc9e'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': '4QBR-yGN1lxyl8lx_A81CYcZgxg3ckX2oysuKXgjcv_ogDKwXq8qB0F3TdlxRWJ7iUSQvP9Jl3XG0cYBedXdFDLILRsz9pj0QPjhr6aznB-uvoq5pCWIJMNiX-6HqchK8nQP2YViqYyleourQ_cPb0oX-qZnp_NYIlEgW4pcLm2qu8oAgth3JKWqFzN6ktvBkBkBXDVGlwTKsipaYYwZkwQt34LHlvDMjW1KiY28WKtlk24lEmMLcKz29OWAZHwWcXciViEBzPkiidelhoEelw'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': '3fCiw3lcAZku5SURMNCIUuGHJ0Qh6Z7ZSsoiHj-OtFVBawgE7h7oP-Fm_xfqBaYx'}, {'domain': '.qq.com', 'expiry': 1618930078, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.546155446.1618842977'}, {'domain': 'work.weixin.qq.com', 'expiry': 1618874511, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '4q0qa1t'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688849998647130'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688849998647130'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '2146080768'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '1525675440'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325119455437'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1618843077'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '21005188393336593'}, {'domain': '.work.weixin.qq.com', 'expiry': 1621436182, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.qq.com', 'expiry': 1681915678, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1796231888.1618582624'}, {'domain': '.qq.com', 'expiry': 1904264768, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/', 'secure': False, 'value': '4a030757b4843762'}, {'domain': '.work.weixin.qq.com', 'expiry': 1650118502, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1906646401, 'httpOnly': False, 'name': 'XWINDEXGREY', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': 'c20c02e80c85f8ad90a5103c749bf97cfef62d4d1f5d7cd9db2fe93f8ac09d3d'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 2147483641, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'vZQslmXoYG'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False, 'value': ''}]
        for cookie in cookies:
            #将获取的cookie存放webdriver的cookie中
            self.driver.add_cookie(cookie)

        self.driver.find_element_by_link_text("企业登录").click()
        sleep(2)

#进入登录界面,加载cookie到webdrive中,直接进行免登录操作
    def test_cookie_login2(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        with open("data.yaml",encoding="utf-8")as f:
            yaml_data=yaml.safe_load(f)

        for cookie in yaml_data:
            self.driver.add_cookie(cookie)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(2)
