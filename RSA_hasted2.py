import sys
import platform,os
from urllib2 import *
from platform import system
def slowprint(s):
    for c in s :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4. / 100)

clear = ""
if "Windows" in platform.system():
	clear = "cls"
if "Linux" in platform.system():
	clear = "clear"
os.system(clear)
is_windows = sys.platform.startswith('win')

# Console Colors
if is_windows:
    # Windows deserves coloring too :D
    G = '\033[92m'  # green
    Y = '\033[93m'  # yellow
    B = '\033[94m'  # blue
    R = '\033[91m'  # red
    W = '\033[0m'   # white
    try:
        import win_unicode_console , colorama
        win_unicode_console.enable()
        colorama.init()
        #Now the unicode will work ^_^
    except:
        print("[!] Error: Coloring libraries not installed, no coloring will be used")
        G = Y = B = R = W = G = Y = B = R = W = ''


else:
    G = '\033[92m'  # green
    Y = '\033[93m'  # yellow
    B = '\033[94m'  # blue
    R = '\033[91m'  # red
    W = '\033[0m'   # white


def banner():
    print("""%s

_____       ________________                  _____      _____
\    \     /    /\          \            _____\    \   /      |_
 \    |   |    /  \    /\    \          /    / \    | /         \\
  \    \ /    /    |   \_\    |        |    |  /___/||     /\    \\
   \    |    /     |      ___/      ____\    \ |   |||    |  |    \\
   /    |    \     |      \  ____  /    /\    \|___|/|     \/      \\
  /    /|\    \   /     /\ \/    \|    |/ \    \     |\      /\     \\
 |____|/ \|____| /_____/ |\______||\____\ /____/|    | \_____\ \_____\\
 |    |   |    | |     | | |     || |   ||    | |    | |     | |     |
 |____|   |____| |_____|/ \|_____| \|___||____|/      \|_____|\|_____|
  %s%s
[ Version : 0.2 ]\033[92m
[ Author  : X-Vector ]\033[96m
[ Github  : github.com/X-Vector ]\033[93m
[ Twitter : twitter.com/@XVector11 ]\033[95m
[ Facebook: facebook.com/X.Vector1 ]\033[95m
[ GreeteZ : Karem Ali ]\033[94m

    """ % (R, W,R))
banner()


#Example
"""
N1 = 79608037716527910392060670707842954224114341083822168077002144855358998405023007345791355970838437273653492726857398313047195654933011803740498167538754807659255275632647165202835846338059572102420992692073303341392512490988413552501419357400503232190597741120726276250753866130679586474440949586692852365179
C1 = 34217065803425349356447652842993191079705593197469002356250751196039765990549766822180265723173964726087016890980051189787233837925650902081362222218365748633591895514369317316450142279676583079298758397507023942377316646300547978234729578678310028626408502085957725408232168284955403531891866121828640919987
N2 = 58002222048141232855465758799795991260844167004589249261667816662245991955274977287082142794911572989261856156040536668553365838145271642812811609687362700843661481653274617983708937827484947856793885821586285570844274545385852401777678956217807768608457322329935290042362221502367207511491516411517438589637
C2 = 48038542572368143315928949857213341349144690234757944150458420344577988496364306227393161112939226347074838727793761695978722074486902525121712796142366962172291716190060386128524977245133260307337691820789978610313893799675837391244062170879810270336080741790927340336486568319993335039457684586195656124176
N3 = 95136786745520478217269528603148282473715660891325372806774750455600642337159386952455144391867750492077191823630711097423473530235172124790951314315271310542765846789908387211336846556241994561268538528319743374290789112373774893547676601690882211706889553455962720218486395519200617695951617114702861810811
C3 = 55139001168534905791033093049281485849516290567638780139733282880064346293967470884523842813679361232423330290836063248352131025995684341143337417237119663347561882637003640064860966432102780676449991773140407055863369179692136108534952624411669691799286623699981636439331427079183234388844722074263884842748
e = 3
"""
C1 = input(">>> c1 = ")
C2 = input(">>> c2 = ")
C3 = input(">>> c3 = ")
N1 = input(">>> n1 = ")
N2 = input(">>> n2 = ")
N3 = input(">>> n3 = ")
e = input(">>> e = ")

slowprint("\n[+] Please Wait ... \033[95m\n")

try:
    def mulinv(a,b):
        b0 = b
        x0, x1 = 0, 1
        if b == 1: return 1
        while a > 1:
            q = a / b
            a, b = b, a%b
            x0, x1 = x1 - q * x0, x0
        if x1 < 0: x1 += b0
        return x1
    def powinv(x,n):
        high = 1
        while high ** n < x:
            high *= 2
        low = high/2
        while low < high:
            mid = (low + high) // 2
            if low < mid and mid**n < x:
                low = mid
            elif high > mid and mid**n > x:
                high = mid
            else:
                return mid
        return mid + 1

    def hasted(n1,n2,n3,chipher_text_1,chipher_text_2,chipher_text_3,e):
        n = [n1,n2,n3]
        a = [chipher_text_1,chipher_text_2,chipher_text_3]
        sum = 0
        prod = reduce(lambda a, b: a*b, n)
        for n_i, a_i in zip(n, a):
            p = prod / n_i
            sum += a_i * mulinv(p, n_i) * p
        return powinv(sum % p,e)

    decode = (hex(hasted(N1,N2,N3,C1,C2,C3,e))[2:]).replace('L','')
    slowprint("[+] The PlainText = ")
    print decode.decode("hex")
    slowprint("[+] Thanx For Using X-RSA Tool <3  \033[95m\n")
except:
    slowprint("[-] False Attack !! \n")
