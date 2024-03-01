from domain.tranzactie_manager import *
from domain.tranzactie import *
from utils.list_operations import print_list, add_tranzactie, afisare_sum, afisare_zi_sum, afisare_tip
from ui.lista_comenzi import run


def print_lista_comenzi():
    print('1. Meniu')
    print('2. Lista de comenzi')


def print_menu():
    print("Cont bancar: ")
    print("1. Adaugă o tranzacție nouă.")
    print("2. Actualizare tranzacție.")
    print("3. Ștergere toate tranzacțiile dintr-o zi specificată.")
    print("4. Ștergere toate tranzacțiile dintr-o perioada data.")
    print("5. Ștergere toate tranzacțiile de un anumit tip.")
    print("6. Tipărește tranzacțiile cu sume mai mari decât o sumă dată.")
    print("7. Tipărește toate tranzacțiile efectuate înainte de o zi și mai mari decât o sumă.")
    print("8. Tipărește tranzacțiile de un anumit tip.")
    print("9. Calculează suma totală a tranzacțiilor de un anumit tip. (1-intrare, 2-ieșire)")
    print("10. Determină soldul contului la o dată specificată.")
    print("11. Tipărește toate tranzacțiile de un anumit tip ordonat după sumă.")
    print("12. Elimină toate tranzacțiile de un anumit tip. (1-intrare, 2-ieșire)")
    print("13. Elimină toate tranzacțiile cu suma mai mică decât o sumă dată și de un anumit tip. (1-intrare, 2-ieșire)")
    print("14. Undo: reface ultima operație.")
    print("15. Iesire din aplicatie.")


def add_tranzactie_ui(tranzactie_manager):
    try:
        zi = int(input("Ziua tranzactiei:"))
        suma=int(input("Suma tranzactiei:"))
        tip=int(input("Tipul tranzactiei (intrare - 1 sau iesire - 2):"))

        lst=create_tranzactie(zi, suma, tip)
        add_tranzactie_to_manager(tranzactie_manager, lst)
        print("Tranzactia s-a adaugat cu succes.")

    except ValueError:
        print('Introduceti numere pentru ziua, suma si tipul tranzactiei')


def start():
    tranzactie_manager=setup_tranzactii_manager(True)
    finished=False
    print_lista_comenzi()
    opt=int(input("Opțiunea dumneavoastra este:"))
    if opt==1:
        while not finished:
            print_menu()
            opt=int(input("Opțiunea dumneavoastra este:"))
            if opt==1:
                add_tranzactie_ui(tranzactie_manager)
                print('Lista curenta este: ')
                print_list(tranzactie_manager)
            elif opt==2:
                actualizare_tranzactie(tranzactie_manager)
                print('Lista actualizata este: ')
                print_list(tranzactie_manager)
            elif opt==3:
                z=int(input("Dați ziua:"))
                delete_tranzactie_from_manager_zi(tranzactie_manager, z)
                print('Lista curenta este: ')
                print_list(tranzactie_manager)
            elif opt==4:
                zi=int(input("Dați ziua de inceput:"))
                zf=int(input("Dați ziua de sfarsit:"))
                delete_tranzactie_from_manager_perioada(tranzactie_manager, zi, zf)
                print('Lista curenta este: ')
                print_list(tranzactie_manager)
            elif opt==5:
                t = int(input("Dați tipul de tranzacție (1 - intrare, 2 - ieșire) :"))
                delete_tranzactie_from_manager_tip(tranzactie_manager, t)
                print('Lista curenta este: ')
                print_list(tranzactie_manager)
            elif opt==6:
                s=int(input("Dați suma:"))
                afisare_sum(tranzactie_manager[0], s)
            elif opt==7:
                z=int(input("Dați ziua:"))
                s=int(input("Dați suma:"))
                afisare_zi_sum(tranzactie_manager[0], z, s)
            elif opt==8:
                t=int(input("Dați tipul (1 - intrare, 2 - ieșire):"))
                afisare_tip(tranzactie_manager[0], t)
            elif opt==9:
                t=int(input("Dați tipul de tranzacție (1 - intrare, 2 - ieșire):"))
                s=get_sum_tip(tranzactie_manager[0], t)
                print(s)
            elif opt==10:
                z=int(input("Dați ziua:"))
                intr=get_sum_tip_zi(tranzactie_manager[0], 1, z)
                ies=get_sum_tip_zi(tranzactie_manager[0], 2, z)
                print("Soldul contului dumneavoastră este: ")
                print(intr-ies)
            elif opt==11:
                crt_lst=ordonare_lista(tranzactie_manager[0])
                t=int(input("Dați tipul de tranzacție (1 - intrare, 2 - ieșire):"))
                afisare_tip(crt_lst, t)
            elif opt==12:
                t=int(input("Dați tipul de tranzacție (1 - intrare, 2 - ieșire):"))
                delete_tranzactie_from_manager_tip(tranzactie_manager, t)
                print('Lista curenta este: ')
                print_list(tranzactie_manager)
            elif opt==13:
                s=int(input("Dați suma:"))
                delete_tranzactie_from_manager_sum(tranzactie_manager, s)
                t=int(input("Dați tipul de tranzacție (1 - intrare, 2 - ieșire):"))
                delete_tranzactie_from_manager_tip(tranzactie_manager, t)
                print('Lista curenta este: ')
                print_list(tranzactie_manager)
            elif opt==14:
                undo(tranzactie_manager)
                print('Lista curenta este: ')
                print_list(tranzactie_manager)
            elif opt==15:
                finished=True
            else:
                print("Optiunea introdusa este invalida.")
    elif opt==2:
        run()
