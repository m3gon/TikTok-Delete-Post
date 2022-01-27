import requests , os
from colorama import Fore , init
init(autoreset=True)
class Main:
    def __init__(self, sessionid):
        self.sessionid = sessionid
        self.done = 0
        self.error = 0
        self.green = Fore.LIGHTGREEN_EX
        self.red = Fore.LIGHTRED_EX
        self.reset = Fore.RESET
    def get_id_your_account(self):
        try:
            self.id_account = requests.get('https://api16-core-c-alisg.tiktokv.com/aweme/v1/user/profile/self/?residence=SA&device_id=7042527263909070342&os_version=14.2&app_id=1233&iid=7054380492250679041&app_name=musical_ly&&version_code=22.8.2&channel=App%20Store&device_platform=iphone&device_type=iPhone10%2C6&app_language=en&aid=1233', headers={'Host': 'api16-core-c-alisg.tiktokv.com', 'Cookie': f'sessionid={self.sessionid}', 'User-Agent': 'TikTok 22.8.2 rv:228202 (iPhone; iOS 14.2; ar_SA@calendar=gregorian) Cronet'}).json()['user']['uid']
            print(f'[{self.green}+{self.reset}] Successfully Get Id Your Account : {self.id_account}')
        except:
            print(f'[{self.red}+{self.reset}] Error To Get Id Your Account Or Sessionid Is Error\n[{self.red}+{self.reset}] Press Enter To Exit')
            input()
            exit(0)
    def get_all_id_post(self, cursor):
        try:
            self.req_get_all_id_post = requests.get(f'https://api2-16-h2.musical.ly/aweme/v1/aweme/post/?version_code=7.7.0&language=ar&app_name=musical_ly&app_version=7.7.0&carrier_region=SA&channel=App%20Store&device_id=7042527263909070342&sys_region=SA&aid=1233&os_version=14.2&app_language=en&device_platform=iphone&device_type=iPhone10,6&iid=7057913854278108934&count=21&max_cursor={cursor}&min_cursor={cursor}&user_id={self.id_account}', headers={'Host': 'api2-16-h2.musical.ly', 'User-Agent': 'Musically/7.7.0 (iPhone; iOS 14.2; Scale/3.00)', 'Cookie': f'sessionid={self.sessionid}'})
            try:
                for i in range(len(self.req_get_all_id_post.json()['aweme_list'][0])):
                    try:
                        self.id_post = self.req_get_all_id_post.json()["aweme_list"][i]["aweme_id"]
                        self.cursor = self.req_get_all_id_post.json()['max_cursor']
                        self.req_delete_post = self.delete_posts('https://api2-t2.musical.ly/aweme/v1/aweme/delete/?version_code=7.7.0&language=ar&app_name=musical_ly&carrier_region=SA&channel=App%20Store&device_id=7042527263909070342&sys_region=SA&aid=1233&os_version=14.2&app_language=en&device_platform=iphone&device_type=iPhone10,6&iid=7057913854278108934', {'Host': 'api2-t2.musical.ly', 'Cookie': f'sessionid={self.sessionid}', 'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'Musically/7.7.0 (iPhone; iOS 14.2; Scale/3.00)'}, f'aweme_id={self.id_post}')
                        if '"status_code":0' in self.req_delete_post:
                            self.done +=1
                            print(f'\r[{self.green}+{self.reset}] Successfully Deleted Post > {self.done} | Error > {self.error}', end='')
                        else:
                            self.error +=1
                            print(f'\r[{self.green}+{self.reset}] Successfully Deleted Post > {self.done} | Error > {self.error}', end='')
                            self.delete_posts('https://api2-t2.musical.ly/aweme/v1/aweme/delete/?version_code=7.7.0&language=ar&app_name=musical_ly&carrier_region=SA&channel=App%20Store&device_id=7042527263909070342&sys_region=SA&aid=1233&os_version=14.2&app_language=en&device_platform=iphone&device_type=iPhone10,6&iid=7057913854278108934', {'Host': 'api2-t2.musical.ly', 'Cookie': f'sessionid={self.sessionid}', 'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'Musically/7.7.0 (iPhone; iOS 14.2; Scale/3.00)'}, f'aweme_id={self.id_post}')
                    except:
                        if '"status_msg":"No more videos"' or '"aweme_list":null' in self.req_get_all_id_post.text:
                            print(f'\n[{self.green}+{self.reset}] Successfully Deleted All Posts\n[{self.green}+{self.reset}] Press Enter To Exit')
                            input()
                            exit(0)
                self.get_id_your_account(self.cursor)
            except Exception as error:
                print(error)
                pass
        except Exception as errorr:
            print(errorr)
            pass
    def delete_posts(self, url, headers, data):
        return requests.post(url, headers=headers, data=data).text
if __name__ == '__main__':
    os.system("cls")
    print(f'{Fore.LIGHTYELLOW_EX}{requests.get("http://artii.herokuapp.com/make?text=Delete Post").text}')
    print(f'[{Fore.LIGHTGREEN_EX}+{Fore.RESET}] Sessionid : ', end='')
    sessionid = input()
    M = Main(sessionid)
    M.get_id_your_account()
    M.get_all_id_post(0)
