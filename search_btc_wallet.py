
import requests
from datetime import datetime, timedelta
import colorama as color
import termcolor as colors
color.init()


def jeden_adres():
    value = None
    while value != "XoXo":
        szukany = input("Wpisz adres BTC : ")
        try:
            url = 'XXXXXXXXX' + szukany + 'XXXXXXXXXX'
            response = requests.get(url)
            data = response.json()
            nazwa_g = data['label']
            print("\n  Adres należy do giełdy [", nazwa_g, "]")
        except:
            stats = data['found']
            print("Czy znaleziono portfel? [", stats, "]")
            print("Brak informacji o przeznaczeniu.")

def stan_konta(nowy_adres_btc):
    """Funkcja na sprawdzanie nowego adresu"""
    url_new = "XXXXXXXXXX" + nowy_adres_btc
    response_new = requests.get(url_new)
    info_new = response_new.json()
    data_new = info_new['data']
    adress_new = data_new['address']
    balance_new = data_new['balance']
    total_txs = data_new['total_txs']
    print(colors.colored("\n################### ADRES #####################", "red", 'on_yellow'))
    print("  ", adress_new)
    print("   Stan konta:", balance_new, "BTC")
    print("   Liczba transakcji:", total_txs)
    if float(balance_new) > stop_saldo:
        try:
            szukany = adress_new
            url = 'XXXXXXXXX' + szukany + 'XXXXXXXXX'
            response = requests.get(url)
            data = response.json()
            nazwa_g = data['label']
            print("\n  Adres należy do giełdy [", nazwa_g, "]")
        except:
            pass
        print(colors.colored("   Portfel posiada wysokie saldo!!", "red"))
        print(colors.colored("   Sprawdź na // https://bitinfocharts.com/pl/bitcoin/", "red"))
        input(' Continue..')
    if int(total_txs) > stop_trans:
        try:
            szukany = adress_new
            url = 'XXXXXXXXX' + szukany + 'XXXXXXXXX'
            response = requests.get(url)
            data = response.json()
            nazwa_g = data['label']
            print("\n  Adres należy do giełdy [", nazwa_g, "]")
        except:
            pass
        print(colors.colored("   Duża liczba transakcji!!", "red"))
        print(colors.colored("   Sprawdź na // https://bitinfocharts.com/pl/bitcoin/", "red"))
        input(' Continue..')
    print(colors.colored("  ########## OSTATNIA TRANSAKCJA ##############", "red", 'on_white', attrs=['bold']))
    url_2 = "XXXXXXXXX" + nowy_adres_btc

    response_2 = requests.get(url_2)

    info_2 = response_2.json()
    data_2 = info_2['data']
    txs = data_2['txs']
    txid_all = txs[:]
    liczba_t = 0

    for i in txid_all: # ustalenie ostatniej transakcji
        if i:
            liczba_t+=1
        else:
            liczba_t = 0
    if liczba_t == 0:
        print(" Brak transkacji")
    try:
        txid = txs[liczba_t-1]
    except IndexError:
        print(" Brak wydanych środków..")
        print(" Saldo portfela [", adress_new, "]", "Wynosi [", balance_new, "]")
        input(" Kliknij by wyjść")
        quit()
    hasz_transakcji = txid['txid']
    wartosc_transakcji = txid['value']
    czas_transkacji = txid['time']
    czas_transakcji = int(czas_transkacji)
    czas_conv = datetime.utcfromtimestamp(czas_transakcji + 7200).strftime('%Y-%m-%d %H:%M:%S')


    print("   Data >>>>>>>>>>>>>>>>>>>>>>>>  ", czas_conv)
    print("   Wartość transakcji >>>>>>>>>>  ", wartosc_transakcji, "BTC")

    if hasz_transakcji:
        url_3 = 'XXXXXXXXX' + hasz_transakcji
        response_3 = requests.get(url_3)

        info_3 = response_3.json()
        data_3 = info_3['data']
        out_all = data_3['outputs']

        all_adress = out_all[:]
        l_wyplat = 0
        for i in all_adress:
            if i:
                l_wyplat+=1 
        print("   Ilość wypłat  >>>>>>>>>>>>>>>  ", l_wyplat)

        kick = 0
        kwota_wypl = []
        for i in all_adress:
            value = i['value']
            kwota_wypl.append(value)
            
        l_list = len(kwota_wypl)
        if l_list == 0:
            print("Brak wypłat..")
        elif l_list == 2:
            if kwota_wypl[0] > kwota_wypl[1]:
                wieksze_saldo = out_all[0]
                out_adress = wieksze_saldo['address']
                print("   Na adres >>>>>>>>>>>>>>>>>>>>  ", out_adress)
                if out_adress == "1NDyJtNTjmwk5xPNhjgAMu4HDHigtobu1s":
                    print(colors.colored("\n  1NDyJtNTjmwk5xPNhjgAMu4HDHigtobu1s - Adres giełdy Binance!", "red"))
            elif kwota_wypl[1] > kwota_wypl[0]:
                wieksze_saldo = out_all[1]
                out_adress = wieksze_saldo['address']
                print("   Na adres >>>>>>>>>>>>>>>>>>>>  ", out_adress)
                if out_adress == "1NDyJtNTjmwk5xPNhjgAMu4HDHigtobu1s":
                    print(colors.colored("\n  1NDyJtNTjmwk5xPNhjgAMu4HDHigtobu1s - Adres giełdy Binance!", "red"))
            else:
                print("Brak transkacji..")
            if out_adress:
                stan_konta(out_adress)
        elif l_list == 1:
            wieksze_saldo = out_all[0]
            out_adress = wieksze_saldo['address']
            print("   Na adres >>>>>>>>>>>>>>>>>>>>  ", out_adress)
            if out_adress == "1NDyJtNTjmwk5xPNhjgAMu4HDHigtobu1s":
                print(colors.colored("\n  1NDyJtNTjmwk5xPNhjgAMu4HDHigtobu1s - Adres giełdy Binance!", "red"))
            if out_adress:
                stan_konta(out_adress)
        elif l_list >= 3:
            try:
                szukany = adress_new
                url = 'XXXXXXXXX' + szukany + 'XXXXXXXXX'
                response = requests.get(url)
                data = response.json()
                nazwa_g = data['label']
                print("\n  Adres należy do giełdy [", nazwa_g, "]")
            except:
                pass
            print("\n  Duża liczba wypłat w jednej transakcji..")
            print("  Sprawdź adres [", adress_new, "] być może to giełda.")
            print("  Jeśli nie to:")
            print("  - wybierz adres portfela z największą ilością BTC, wpisz/wklej i kontynuuj..")
            spec_adres = str(input("\n  Podaj adres BTC: "))
            if spec_adres:
                stan_konta(spec_adres)
        else:
            print("  Jakiś błąd ;-)")

answear = None
while answear != 2:
    print(colors.colored('\n\n                            Menu startowe', 'blue', attrs=['bold']))
    print(colors.colored('                         ==================', 'blue', attrs=['dark']))
    print(" ")
    print(colors.colored("                          1. Sprawdź adres BTC (max 1 zapytanie na 1 sekundę)", 'yellow'))
    print(colors.colored("                          2. Sprawdź ostatnie wypłaty (tylko największe)", 'green'))
    print("                          3. Info")
    print(colors.colored("             |", 'green'))
    print(colors.colored("             V", 'green'))
    answear = input(" Wybieram.. :")
    if answear == "2":
        break
    elif answear == "3":
        print("""
          W przypadku pytań lub błędów:""")
        print(colors.colored("          polic@majster.hub.pl\n", 'cyan'))
        print("Program może mieć wady ale spokojnie.. nie wysadzi komputera.")
        print("Dane blockchain pobierane są z zewnętrznych serwerów.")
    elif answear == "1":
        jeden_adres()

adres_btc = str(input("\n  Wpisz adres BTC: "))
stop_saldo = int(input("  Poinformuj gdy saldo wynosi minimum (wpisz liczbę BTC): "))
stop_trans = int(input("  Poinformuj gdy ilośc transakcji wynosi minimum (wpisz liczbę): "))

#Sprawdzenie odpowiedzi serwera
url = "XXXXXXXXX" + adres_btc

response = requests.get(url)
status = response.status_code

if status == 200:
    print("\n  Status serwera")
    print(colors.colored("  Działa", "green"))
    info = response.json()
    data = info['data']
    adress = data['address']
    balance = data['balance']
    total = data['total_txs']
    print(colors.colored("\n################### ADRES #####################", "red", "on_yellow"))
    print("  ", adress)
    print("   Stan konta:", balance, "BTC")
    print("   Liczba transakcji IN:", total)
    if float(balance) > stop_saldo:
        try:
            szukany = adress
            url = 'XXXXXXXXX' + szukany + 'XXXXXXXXX'
            response = requests.get(url)
            data = response.json()
            nazwa_g = data['label']
            print("\n  Adres należy do giełdy [", nazwa_g, "]")
        except:
            pass
        print(colors.colored("   Portfel posiada wysokie saldo!!", "red"))
        print(colors.colored("   Sprawdź na // https://bitinfocharts.com/pl/bitcoin/", "red"))
        input('Continue..')
    
    if int(total) > stop_trans:
        try:
            szukany = adress
            url = 'XXXXXXXXX' + szukany + 'XXXXXXXXX'
            response = requests.get(url)
            data = response.json()
            nazwa_g = data['label']
            print("\n  Adres należy do giełdy [", nazwa_g, "]")
        except:
            pass
        print(colors.colored("   Duża liczba transakcji!!", "red"))
        print(colors.colored("   Sprawdź na // https://bitinfocharts.com/pl/bitcoin/", "red"))
        input('Continue..')

    url_2 = "XXXXXXXXX" + adres_btc

    response_2 = requests.get(url_2)

    info_2 = response_2.json()
    data_2 = info_2['data']
    txs = data_2['txs']
    txid_all = txs[:]
    liczba_t = 0
    lista_hashy = []
    for i in txid_all:
        if i:
            hashe = i['txid']
            lista_hashy.append(hashe)
            liczba_t+=1
        else:
            liczba_t = 0

    if liczba_t == 0:
        print("Brak transkacji")

    elif liczba_t > 99:
        print("Sorry ale nie mogę wykonać więcej jak", liczba_t, "zapytań")
        print("Limity API :(")

    else:
        txid = txs[liczba_t-1]
        hasz_transakcji = txid['txid']
        l_hashy = len(lista_hashy)
        print("   Liczba transakcji OUT:", l_hashy)
        if l_hashy > 2:
            del lista_hashy[l_hashy-1]
            do_sprawdzenia = lista_hashy[-2:] 
            print("  >> Hashe 2 poprzednich transakcji ",do_sprawdzenia)
        elif l_hashy == 2:
            del lista_hashy[l_hashy-1]
            do_sprawdzenia = lista_hashy[:]
            print("  >> Hash poprzedniej transakcji ", do_sprawdzenia)
        print(colors.colored("  ########## OSTATNIA TRANSAKCJA ##############", "red", 'on_white', attrs=['bold']))
        wartosc_transakcji = txid['value']
        czas_transkacji = txid['time']
        czas_transakcji = int(czas_transkacji)
        czas_conv = datetime.utcfromtimestamp(czas_transakcji + 7200).strftime('%Y-%m-%d %H:%M:%S')

        print("   Data >>>>>>>>>>>>>>>>>>>>>>>>  ", czas_conv)
        print("   Wartość transakcji >>>>>>>>>>  ", wartosc_transakcji, "BTC")

        if hasz_transakcji:
            url_3 = 'XXXXXXXXX' + hasz_transakcji
            response_3 = requests.get(url_3)

            info_3 = response_3.json()
            data_3 = info_3['data']
            out_all = data_3['outputs']

            all_adress = out_all[:]
            l_wyplat = 0
            for i in all_adress:
                if i:
                    l_wyplat+=1
            print("   Ilość wypłat  >>>>>>>>>>>>>>>  ", l_wyplat)
            kick = 0
            kwota_wypl = []
            for i in all_adress:
                value = i['value']
                kwota_wypl.append(value)
            
            l_list = len(kwota_wypl)
            if l_list == 0:
                print("Brak wypłat..")
            elif l_list == 2:
                if kwota_wypl[0] > kwota_wypl[1]:
                    wieksze_saldo = out_all[0]
                    out_adress = wieksze_saldo['address']
                    print("   Na adres >>>>>>>>>>>>>>>>>>>>  ", out_adress)
                    if out_adress == "1NDyJtNTjmwk5xPNhjgAMu4HDHigtobu1s":
                        print(colors.colored("\n  1NDyJtNTjmwk5xPNhjgAMu4HDHigtobu1s - Adres giełdy Binance!", "red"))
                elif kwota_wypl[1] > kwota_wypl[0]:
                    wieksze_saldo = out_all[1]
                    out_adress = wieksze_saldo['address']
                    print("   Na adres >>>>>>>>>>>>>>>>>>>>  ", out_adress)
                    if out_adress == "1NDyJtNTjmwk5xPNhjgAMu4HDHigtobu1s":
                        print(colors.colored("\n  1NDyJtNTjmwk5xPNhjgAMu4HDHigtobu1s - Adres giełdy Binance!", "red"))
                else:
                    print("Brak transkacji..")
                if out_adress:
                    stan_konta(out_adress)
            elif l_list == 1:
                wieksze_saldo = out_all[0]
                out_adress = wieksze_saldo['address']
                print("   Na adres >>>>>>>>>>>>>>>>>>>>  ", out_adress)
                if out_adress == "1NDyJtNTjmwk5xPNhjgAMu4HDHigtobu1s":
                    print(colors.colored("\n  1NDyJtNTjmwk5xPNhjgAMu4HDHigtobu1s - Adres giełdy Binance!", "red"))
                if out_adress:
                    stan_konta(out_adress)
            elif l_list >= 3:
                try:
                    szukany = out_adress
                    url = 'XXXXXXXXX' + szukany + 'XXXXXXXXX'
                    response = requests.get(url)
                    data = response.json()
                    nazwa_g = data['label']
                    print("\n  Adres należy do giełdy [", nazwa_g, "]")
                except:
                    pass
                print("\n  Duża liczba wypłat w jednej transakcji..")
                print("  Sprawdź adres", adress)
                print("  Wybierz adres portfela z największą ilością BTC, wpisz/wklej i kontynuuj..")
                if do_sprawdzenia:
                    print("  >> Jeśli zakończyłeś wyszukiwanie, sprawdź Hash poprzedniej transakcji \n", do_sprawdzenia)
                spec_adres = str(input("\n  Podaj adres BTC: "))
                if spec_adres:
                    stan_konta(spec_adres)
        else:
            print("  Jakiś błąd ;-)")

else:
    print("  Status serwera <", status, ">")
    print(colors.colored("  Nie działa", "red"))




#-------------------------------

input("Aha.. ;-) i koniec programu..")

