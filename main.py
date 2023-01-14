import requests, json, socket
from multiprocessing.dummy import Pool

class Domain:
    def __init__(self, domain):
        self.domain = domain

    def subdomains(self):
        try:
            r = requests.get("https://sonar.omnisint.io/subdomains/{}".format(self.domain))
            result = json.loads(r.text)
            print("        [{}] > [{} Domain]".format(self.domain, len(result)))
            for a in result:
                open('results/subdomains.txt', 'a').write('http://' + a + "\n")
        except:
            pass
    
    def reverse(self):
        try:
            ips = socket.gethostbyname(self.domain)
            r = requests.get("https://premiumbins.tk/reverse/?ip={}".format(ips))
            result = json.loads(r.text)
            print("        [{}] > [{} Domain]".format(self.domain, len(result)))
            for a in result:
                open('results/reverse.txt', 'a').write('http://' + a + "\n")
        except:
            pass
    
    def All(self):
        try:
            ips = socket.gethostbyname(self.domain)
            r = requests.get("https://sonar.omnisint.io/all/{}".format(ips))
            result = json.loads(r.text)
            print("        [{}] > [{} Domain]".format(self.domain, len(result)))
            for a in result:
                open('results/all.txt', 'a').write('http://' + a + "\n")
        except:
            pass
        
    def process(self):
        if selection == "1":
            website.subdomains()
        elif selection == "2":
            website.reverse()
        elif selection == "3":
            website.All()
        else:
            print("        [!] Wrong input please try again...")

def asuna(list):    
    global website
    website = Domain(list)
    website.process()

def main():
    print("""
        Reverse IP
        Author : angga1337

        [1] Subdomain
        [2] Reverse IP
        [3] All (Subdomain, tlds, reverse)
    """)

    global selection
    try:
        selection = input("        root@angga1337~# ")
        urList = open(input("        root@weblist~# "), "r").read().replace("https://", "").replace("http://", "").replace("/", "").split("\n")
        thread = int(input("        root@threads~# "))
        print("\n")
        pool = Pool(thread)
        pool.map(asuna, urList)
        pool.close()
        pool.join
    except:
        print("        [!] Something wrong please try again...")

if __name__ == '__main__':
    main()
