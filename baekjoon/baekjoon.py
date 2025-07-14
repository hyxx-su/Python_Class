# n = 0
# m = 0

# for i in range(1, 10):
#     a = int(input())
#     if a > n:
#         n = a
#         m = i

# print(n, m, sep="\n")

# print('\\    /\\')
# print(' )  ( \')')
# print('(  /  )')
# print(' \\(__)|')

# print('|\\_/|')
# print('|q p|   /}')
# print('( 0 )\"\"\"\\')
# print('|\"^\"`    |')
# print('||_/=\\\\__|')

# m = int(input())
# nlist = []

# for i in range(m):
#     h, w, n = map(int, input().split())
#     for ii in range(1, w+1):
#         for iii in range(1, h+1):
#             n -= 1
#             if n == 0:
#                 if ii < 10:
#                     nlist.append(f'{iii}0{ii}')
#                 else:
#                     nlist.append(f'{iii}{ii}')

# print(*nlist, sep="\n")

# n = int(input())
# nlist = list(int(input().split()))

# print(nlist)
# max = max(nlist)
# min = min(nlist)

# print(min, max)

# n = int(input())
# nlist = list(map(int, input().split()))

# max = -1000000
# min = 1000000

# for i in range(n):
#     if nlist[i] > max:
#         max = nlist[i]

#     if min > nlist[i]:
#         min = nlist[i]

# print(min, max)

# import random

# a = random.randint(0,1)

# if a == 1:
#     print("Yonsei")
# else:
#     print("Korea")

# n = list(input().split())

# print(len(n))

# a = int(input())
# b = int(input())
# c = int(input())

# n = a*b*c

# m = list(str(n))
# cnt = 0

# for i in range(10):
#     cnt = 0
#     for ii in m:
#         if i == int(ii):
#             cnt += 1
#     print(cnt)

# n = int(input())
# nlist = []
# rlist = []

# for i in range(n):
#     r, s = input().split()
#     s = list(s)
#     rlist.append(r)
#     nlist.append(s)

# for i in range(n):
#     for ii in nlist[i]:
#         print(ii*int(rlist[i]), end="")
#     print()

# n = list(map(int, input().split()))
# a = list(range(1,9))
# b = list(range(8,0,-1))

# if n == a:
#     print("ascending")
# elif n == b:
#     print("descending")
# else:
#     print("mixed")

# nlist = []
# m = 10
# cnt = 0

# for i in range(10):
#     n = int(input())
#     n = n % 42
#     if n in nlist:
#         cnt += 1
#     else:
#         nlist.append(n)

# print(m-cnt)

# n = int(input())
# mlist = []
# sumlist = []
# sum = 0
# cnt = 0

# for i in range(n):
#     m = input()
#     mlist.append(m)

# for i in range(len(mlist)):
#     sum = 0
#     cnt = 0
#     for ii in mlist[i]:
#         if ii == "O":
#             cnt += 1
#         else:
#             cnt = 0
#         sum += cnt
#     sumlist.append(sum)

# print(*sumlist, sep="\n")

# n = input()
# abclist = "abcdefghijklmnopqrstuvwxyz"

# for i in abclist:
#     if i in n:
#         print(n.index(i), end=" ")
#     else:
#         print(-1, end=" ")

# n = int(input())
# nlist = list(map(int, input().split()))
# sum = sum(nlist)
# max = max(nlist)
# print((sum/max*100)/n)

# a, b, c = map(int, input().split())

# n = 0

# if a == b and a == c:
#     n = 10000+a*1000
# elif a == b or c == a:
#     n = 1000+a*100
# elif b == c:
#     n = 1000+b*100
# else:
#     if a > b:
#         if a > c:
#             n = a*100
#         else:
#             n = c*100
#     elif b > c:
#         n = b*100
#     else:
#         n = c*100

# print(n)

# n = int(input())
# mlist = []

# for i in range(n):
#     m = input()
#     mlist.append(f'{m[0]}{m[-1]}')

# print(*mlist, sep="\n")

# n = int(input())
# cnt = 1

# for i in range(n, 0, -1):
#     cnt *= i

# print(cnt)

# print("�")

# n = list(map(int, input().split()))
# n.sort()
# print(*n, end=" ")

# nlist = []

# while True:
#     try:
#         n = float(input())
#         if n > 0:
#             nlist.append(f'Objects weighing {n:.2f} on Earth will weigh {n*0.167:.2f} on the moon.')
#         else:
#             break
#     except:
#         break

# print(*nlist, sep="\n")

# n = int(input())
# m = int(input())

# if n <= m+60:
#     print(n*1500)
# else:
#     print((60+m)*1500+(n-m-60)*3000)

# t = int(input())
# tlist = []

# for i in range(t):
#     v, e = map(int, input().split())
#     tlist.append(e-v+2)

# print(*tlist, sep="\n")

# n, m= map(int, input().split())

# a = n-m

# if a < 0:
#     a *= -1

# print(a)

# n = int(input())
# cnt = 1

# for i in range(n, 0, -1):
#     cnt *= i

# print(cnt)

# import sys

# input = sys.stdin.readline()

# n = int(input)
# nlist = []

# for i in range(n):
#     a, b = map(int, sys.stdin.readline().split())
#     nlist.append(a+b)

# print(*nlist, sep="\n")

# n = int(input())
# m = list(map(int, input().split()))
# o = int(input())

# cnt = 0

# for i in m:
#     if i == o:
#         cnt += 1

# print(cnt)

# n = int(input())
# m = int(input())
# cnt = 0

# ablist = []

# for i in range(m):
#     a, b = map(int, input().split())
#     ablist.append(a*b)

# for i in ablist:
#     cnt += i

# if cnt == n:
#     print("Yes")
# else:
#     print("No")

# n = int(input())
# m = n // 4
# print("long "*m+"int")


# n = int(input())
# nlist = list(map(int, input().split()))
# mlist = []

# nlist.sort()

# for i in range(1, n+1):
#     cnt = 0
#     for ii in range(i):
#         cnt += nlist[ii]
#     mlist.append(cnt)
    
# print(sum(mlist))

# import sys

# n = int(sys.stdin.readline().strip())
# nlist = list(map(int, sys.stdin.readline().strip().split()))

# m = int(sys.stdin.readline().strip())
# mlist = list(map(int, sys.stdin.readline().strip().split()))

# cntlist = []

# def listcount():
#     for i in range(m):
#         cntlist.append(nlist.count(mlist[i]))
#     print(*cntlist)

# listcount()

# import sys

# n = sys.stdin.readline().strip()
# nlist = list(map(int, sys.stdin.readline().split()))

# m = sys.stdin.readline().strip()
# mlist = list(map(int, sys.stdin.readline().split()))

# cnt = {}

# for i in nlist:
#     if i in cnt:
#         cnt[i] += 1
#     else:
#         cnt[i] = 1

# for i in mlist:
#     if i in cnt:
#         print(cnt[i], end=' ')
#     else:
#         print(0, end=' ')

# print("     /~\\")
# print("    ( oo|")
# print("    _\\=/_")
# print("   /  _  \\")
# print("  //|/.\\|\\\\")
# print(" ||  \\ /  ||")
# print("============")
# print("|          |")
# print("|          |")
# print("|          |")

# nlist = []
# cntlist = []
# aeiou = "aeiou"

# while True:
#     try:
#         n = input().lower()
#         if n == "#":
#             break
#         else:
#             nlist.append(n)
#     except:
#         break

# for i in range(len(nlist)):
#     cnt = 0
#     for ii in nlist[i]:
#         if ii in aeiou:
#             cnt += 1
#     cntlist.append(cnt)
    
# print(*cntlist, sep="\n")

# print("  ___  ___  ___")
# print("  | |__| |__| |")
# print("  |           |")
# print("   \\_________/")
# print("    \\_______/")
# print("     |     |")
# print("     |     |")
# print("     |     |")
# print("     |     |")
# print("     |_____|")
# print("  __/       \\__")
# print(" /             \\")
# print("/_______________\\")

# n = input()
# cnt = 0

# for i in n:
#     cnt += 1
    
# print(cnt)

# n = list(input())
# nlist = []

# for i in n:
#     if i.isupper():
#         nlist.append(i.lower())
#     else:
#         nlist.append(i.upper())

# print(*nlist, sep="")

# print("       _.-;;-._")
# print("'-..-'|   ||   |")
# print("'-..-'|_.-;;-._|")
# print("'-..-'|   ||   |")
# print("'-..-'|_.-''-._|")

# nlist = []

# while True:
#     try:
#         n, m = map(int, input().split())
#         if n == 0 and m == 0:
#             break
#         else:
#             nlist.append(n+m)
#     except:
#         break

# print(*nlist, sep="\n")

# print(2018-1946)

# a = int(input())
# b = int(input())
# c = int(input())

# abclist = []

# abclist.append(a)
# abclist.append(b)
# abclist.append(c)

# abclist.remove(min(abclist))
# abclist.remove(max(abclist))

# print(*abclist)

# n = int(input())
# cnt = 0
# cnt2 = 0

# for i in range(1, n+1):
#     cnt += i
#     cnt2 += i**3

# print(cnt)
# print(cnt**2)
# print(cnt2)

# import random

# print(random.randrange(10000))

# print(".  .   .")
# print("|  | _ | _. _ ._ _  _")
# print("|/\\|(/.|(_.(_)[ | )(/.")

# print("                                                           :8DDDDDDDDDDDDDD$.                                           ")
# print("                                                      DDDNNN8~~~~~~~~~~=~7DNNDNDDDNNI                                   ")
# print("                                                  ?NNDD=~=~~~~~~~~~~~~~~~~~=~~==~=INNDNN7                               ")
# print("                                               +NDDI~~~~~~~~~~~~~~~~~~~~~~~=~~========~ODND+                            ")
# print("                                            :NND~~~~~~~~~~~~~~~~~~~~~~~~~~~=~~============7NDN                          ")
# print("                                          $DD$~~~~~~~~~~~~~~~~~~~~~~~~~~~~~=~~==============~DNN                        ")
# print("                                        $DD=~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~=~~=================NND                      ")
# print("                                       ND7~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~=~~===================DD7                    ")
# print("                                     ~DD=~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~=======================8DN.                  ")
# print("                                    8DO~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~=========================DD                  ")
# print("                                   8N~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~=~~=======================DN                 ")
# print("                                  NN::::::::~~~~~~~~~~~=~~~~~~~~~~~~~~~~~~~=~~========================DDO               ")
# print("                                 $D$:::::::::::::::~~~~DD~~~~~~~~~~~~~~~~~~=~~=========================DN.              ")
# print("                                 D8:::::::::::::::::::DN=::~~~~~~~~~~~~~~~~=~~======================~~:~DN              ")
# print("                                DN:::::::::::::::::::ONO::::::::::::::::::::~~~~~~~~~~~~:::::::::::::::::DN             ")
# print("                               DN::::::::::::::::::::NN.:::::::::::::::::::::::::::DN::::::::::::::::::::$DO            ")
# print("                               DD:::::::::::::::::::DNI:::::::::::::::::::::::::::::D=::::::::::::::::::::NN            ")
# print("                              NN~~~~:::::$N?:::::::.NN::::::::::::::::::::::::::::::ND.:::::::::::::::::::+N8           ")
# print("                              N7~~~~~~~~OD7::::::::~DD::::::::::::::::::::::::::::::~D$::::::::::::::::::::DN           ")
# print("                             NN~~~~~~~~IDZ~~~~~::::DN~:::::::::::::::::::::::::::::::DN::::::::::::::::::::=N~          ")
# print("                             DD~~~~~~~~NN~~~~~~~~~=NN::::::::::::::::::::::::::::::::DN:::::::::::::::~~====NN          ")
# print("                            8D~~~~~~~~ND~~~~~~~~~~~ND~~~~~~~~:::::::::::::::::::::::::N7:::~~===============NN          ")
# print("                            DD~~~~~~~ON+~~~~~~~~~~~ND~~~~~~~~~~~~~~~~~~~=+NZ==========NN====================~ND         ")
# print("               :DD7   DNDD. N8~~~~~~~NN~~~~~~~~~~DDND~~~~~~~~~~~~~~~~~~~~ND~~=========DD=====================ND         ")
# print("               N~:DDNNN .8NDN~~~~~~~$D=~~~~~~~~+ND.DD~~~~~~~~~~~~~~~~~~~=DD~~=========~D+====================DN         ")
# print("              :D     .  ..~ND~~~~~~~NN~~~~~~~+NN$..ND~~~~~~~~~~~~~~~~~~~7N=~~=========~ND=======~============ON         ")
# print("              NN       ...:N?~~~~~~~N=~~~~~NNNI.. .7D+~~~~~~~~~~~~~~~~~=8NN~~==========NN=======N============$N         ")
# print("         N  ODN       ....DN~~~~~~~DD=8NNND$..     .DD~~~=~~~~~~~~~~~~~=NNDD=~=========8D~======NN===========~N$        ")
# print("    N? =NN  ND      .....NND~~~~~~~DDNN:...        .ND=~DNN~~~~~~~~~~~~=DN.DN~=========?N+======NN============ND        ")
# print("   $D? DN    DZ    ....ND8NN~~~~~~$D                .DD~NNDD~~~~~~~~~~~~D8..DN=========~DN======NN============DN        ")
# print("   DN ~N~   NN    ..:~NN..NZ~~~~~~DN                  NNN8.ND~~~~NDN?~~~DZ...7DD=======~NN======NN============DN        ")
# print("   ND DD    :DN.  ..ND$  .N?~~~~~=NNN                   . ..DDD$~N8OND8=N+   ..DDDZ~====NN======+D+===========ND        ")
# print("   NO         DD  ZDN    8NO~~~~~~NNN..DDDNN7               ...NND...:DDD:     .:.NDND=~DD======~DO===========DN        ")
# print("              DNDDN:.    DN~~~~~~=NNNN.ODNNNNDDNNO              ...     .         ...DNNNN=======ND===========DD        ")
# print("       INDN7    DD.     .DD~~~~~=IDND:.:~.....?DNDNN.                        ...... ....$D=======ND===========ND        ")
# print("       NN        ND.    8N=~~~~$ND::.:=~:.~=......=ND~                 .NNNNNNNNNNNNNNN.~N+======NN===========DN        ")
# print("       $DD        DN:   DD~~~~7NO...~==.:~~:.....                      NNNND? ..::..7NZ.:N?======8D~==========ZN        ")
# print("       DN?     ~D: DND.?D~~~~~DD....~:.~=~.......                            ....~=:.:~..ND======~N$==========~DO       ")
# print("       ND    ..DD.  .DNDN=~~~~DI.......:.........                           ....=~..~~~..DN======~DD===========NN       ")
# print("       DDD  :.:DD.  . DDI~~~~~ND................        .DNNNNNNNNNN7      ....=~:.:~~...NN=======ND===========?D~      ")
# print("       8D. ...OD..    DD~~~~~~+ND ............          NN:~::::~~~8N      ........~~...:ND=======DN============NN      ")
# print("       DDI:...ND     .D7~~~~~~~7NN ..........           ID8::::::::8D      .............:DN=======ON============NN      ")
# print("        ~NNND.N=.   .NN~~~~~~~~~NDN8                       ~::::::~N8       .............DN========D=============NI     ")
# print("               DDNNN.ND~~~~~~~~DD =DND                                       ............DN========N+~===========NN     ")
# print("                   ~:N=~~~~~~~~DD   .DDDD                                       ........ NN========DD============8D     ")
# print("                    8N~~~~~~~~~ND    . .7NDDD? .                                      .8DDN========NN=============D:    ")
# print("                    DD~~~~~~~~~DND:         IDNNND$.                           .+DNNNNDNIDN========DD=============DD    ")
# print("                    ND~~~~~~~~ZN 7DD .. .:DDNDDNNDNNNNDDNDND8$?===+$8DDNNNDDDDDN8I~DN====8N========NN=============NN    ")
# print("                    DD~~~~~~~~8N   DD.  .NN~~~~.~~=DNDNO.:7ODDDDNNDD8DDDND=~~~ =~~~ON====8N========DN=============DN    ")
# print("                    ND~~~~~~~~DN    ZDD  DN~~~ ~~~~~=.7DDD+.......8NNN==~~~~~ ~~~~~ONN$==DN========8N=============ON    ")
# print("                    ND~8N~=~~~ZN      DDODN=~.~~~~~=.~~~~INDNNNNDNN~~~~~~~~:~~~~~~~DN~ND=DN========DD=========~ND=8N    ")
# print("                    IN=NDDI~~~~D8       DNN::~~~~~.~~~~~=.~~ND~~ND~~~~~~~~.~~~~~~~~NN  NDNN====ND==ND~D?======DNN=ND    ")
# print("                     DNNI8ND=~~DN:       ZN=~~~~~ ~~~~~.~~~~DD~=DD~~~~~~~ ~~~~~~~=.ND. . ND===DNDD=NDDNN=====8NZDDDN    ")
# print("                      NND  IDNDNNN+       D+~~~:~~~~~~ ~~~~~DDNNN+~~~~~~~~~~~~~~:=?N7   .ND=~ND  DNNN~ID====ND7 NNN     ")
# print("                       ID                 ND~~ ~~~~~:.~~~7DDN7IDNN==~~ ~~~~~~~~ ~~DN   .:N?DDDDD NND  8N~=DDD  ZNN      ")
# print("                                          NN~:~~~~~ =7DDDD+8N  :N8DDZ.~~~~~~~~.~~~DD.   NDD+ . DN=     OND+             ")
# print("                                          DND~~~=8DNDDZ=~~ ND   NN~INND~~~~~.~~~~ND .    .    ..IDD                     ")
# print("                                         DDNNNDNNN+~~~~~~.7N.    ND~~~NDDI~ ~~~~=NNN             .DDI                   ")
# print("                                        DN=~~~~.=~~~~~~ ~~DN     +N+~~~~+DNDD~~~NNNND.            ..ND                  ")
# print("                                         DDI~~ ~~~~~~~ ~~~ND..  ..ND~~~~:~~~DNDNNNN+            ..7O8ND+                ")
# print("                                          .DND=~~~~=::~~=NN.   . . 8D~~.~~~~~~=DN$ODNDNDNNNDNNNNND8+~..                 ")
# print("                                             8DNNI=.~~~~=NDDNNNNDDNDNN.~~~~~IDDNDND7:.                                  ")
# print("                                                ?DNNDD?~DD          ~NN~~=NDD$                                          ")
# print("                                                     :DDD.            NNNN=                                             ")

# n = int(input())
# nlist = []

# for i in range(n):
#     m = int(input())
#     nlist.append(m)

# for i in range(n-1):
#     m = nlist[i]
#     if m == 1:
#         print("#")
#     else:
#         o = m-2
#         print("#"*m)
#         for i in range(o):
#             print("#"+"J"*o+"#")
#         print("#"*m)
#     print()

# m = nlist[-1]

# if m == 1:
#     print("#")
# else:
#     o = m-2
#     print("#"*m)
#     for i in range(o):
#         print("#"+"J"*o+"#")
#     print("#"*m)

# n = int(input(), 16)

# print(n)

# n = int(input())
# nlist = []

# for i in range(1, n+1):
#     m = input()
#     nlist.append(f'{i}. {m}')

# print(*nlist, sep="\n")

# n, m = map(int, input().split())

# nlist = [0 for i in range(n)]

# for i in range(m):
#     i, j, k = map(int, input().split())
#     l = j-i
#     for ii in range(l+1):
#         nlist[i-1+ii] = k

# print(*nlist)

# n, m = map(int, input().split())

# if m == 1 or n > 16 or n <= 11:
#     print(280)
# else:
#     print(320)

# n = int(input())
# m = input()

# print(n * int(m[2]))
# print(n * int(m[1]))
# print(n * int(m[0]))
# print(n * int(m))

# nlist = []

# for i in range(5):
#     n = int(input())
#     nlist.append(n)

# print(sum(nlist))

# print("""SHIP NAME      CLASS          DEPLOYMENT IN SERVICE
# N2 Bomber      Heavy Fighter  Limited    21        
# J-Type 327     Light Combat   Unlimited  1         
# NX Cruiser     Medium Fighter Limited    18        
# N1 Starfighter Medium Fighter Unlimited  25        
# Royal Cruiser  Light Combat   Limited    4         """)

# n, m = map(int, input().split())

# if n == m:
#     print(1)
# else:
#     print(0)

# n, m = map(int, input().split())

# if n*100 >= m:
#     print("Yes")
# else:
#     print("No")

# n = list(map(int, input().split()))

# a = n[0] * n[1]
# b = n[2] * n[3] * n[4]

# print(a - b)

# n = input()
# m = input()

# if len(n) >= len(m):
#     print("go")
# else:
#     print("no")

# a, b, c = map(int, input().split())

# n = b // a
# m = n * 3 * c

# print(m)

# a, b, c = map(int, input().split("/"))

# if a+c < b or b == 0:
#     print("hasu")
# else:
#     print("gosu")

# n, a, b = map(int, input().split())

# a -= n
# b -= n

# if a == b:
#     print("Anything")
# elif a < b:
#     print("Bus")
# else:
#     print("Subway")

# n = int(input())

# for i in range(1, n+1):
#     print(f"Hello World, Judge {i}!")

# nlist = {
#     "NLCS": "North London Collegiate School",
#     "BHA": "Branksome Hall Asia",
#     "KIS": "Korea International School",
#     "SJA": "St. Johnsbury Academy"
# }

# n = input()

# print(nlist[n])

# n = int(input())
# nlist = []

# for i in range(n):
#     a, b, c = map(int, input().split())
#     m = a * (c - 1) + b
#     nlist.append(m)

# print(*nlist, sep="\n")

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())

# if a < 0:
#     a *= -c
#     b *= e
#     print(a+b+d)
# elif a == 0:
#     print((b-a)*e)
# else:
#     print((b-a)*e)

# a, b = map(int, input().split())
# c, d = map(int, input().split())

# n = a + d
# m = b + c

# if n > m:
#     print(m)
# else:
#     print(n)