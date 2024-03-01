from domain.tranzactie_manager import *


def print_meniu_lista_comenzi():
    print('1. Sterge toate tranzactiile de un anumit tip.')
    print('2. Sorteaza lista crescator dupa suma.')
    print("3. Undo: reface ultima operație.")


def print_lst(lst):
    for i in lst:
        print('- Zi: ', i[0], '- Suma: ', i[1], '-Tip: ', i[2])


def run():
    tranzactie_manager=setup_tranzactii_manager(True)
    print_meniu_lista_comenzi()
    lst=input(print('Dati optiunile separate prin virgula (ex: 1,2,3,2): '))
    lst_comenzi=lst.split(',')
    i=0
    while i<len(lst_comenzi):
        if lst_comenzi[i]=='1':
            if lst_comenzi[i+1] == '1' or lst_comenzi[i+1] == '1':
                t=int(ord(lst_comenzi[i+1])-48)
                delete_tranzactie_from_manager_tip(tranzactie_manager, t)
            i+=1
        elif lst_comenzi[i]=='2':
            ordonare_lista(tranzactie_manager[0])
            i+=1
        elif lst_comenzi[i] == '3':
            try:
                undo(tranzactie_manager)
                i += 1
            except ValueError:
                print('Nu se poate face undo.')
                return
        else: i+=1
    print('Lista modificata este: ')
    print_lst(tranzactie_manager[0])
