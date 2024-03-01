import socket


def main():
    server = ('127.0.0.1', 1234)

    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        c.connect(server)
    except socket.error as e:
        print("Eroare la conectarea la server:", str(e))
        return 1

    sir = input("Introduceti un sir: ")
    caracter = input("Introduceti un caracter: ")[0]

    c.send(sir.encode())  # Convertim sirul in bytes si il trimitem
    c.send(caracter.encode())  # Convertim caracterul in bytes si il trimitem

    numar_pozitii_bytes = c.recv(4)  # Numarul de pozitii vine sub forma unui int de 4 bytes
    numar_pozitii = int.from_bytes(numar_pozitii_bytes, byteorder='big')

    pozitii_bytes = c.recv(4 * numar_pozitii)  # Pozitiile sunt un sir de int-uri de 4 bytes fiecare
    pozitii = [int.from_bytes(pozitii_bytes[i:i + 4], byteorder='big') for i in range(0, len(pozitii_bytes), 4)]

    print("Pozitiile caracterului '{}' in sir: {}".format(caracter, pozitii))

    c.close()


if __name__ == "__main__":
    main()
