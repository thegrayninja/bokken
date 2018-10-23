# check ciphers on own server
# tested on Python 3.6.5 and 2.7.15rc1
import socket
import ssl


def main():
    context = ssl._create_unverified_context() #ssl.create_default_context()

    with open("cipher_list.txt", "r") as CipherFile:
        CipherList = CipherFile.readlines()

    TestCiphers(CipherList, context)


def TestCiphers(ciphers, context):
    print("working... please be patient")
    domain = '127.0.0.1'
    Results = ""

    for cipher in ciphers:
        cipher = cipher.strip()
        context.set_ciphers(cipher)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            sslSocket = context.wrap_socket(s, server_hostname=domain)

            sslSocket.connect((domain, 443))
            sslSocket.close()
            Results += "open_cipher: {}\n".format(cipher)
        except ssl.SSLError as err:
            Results += 'SSL connection failed: {}, {}\n'.format(str(err), cipher)
            continue
    SaveFile(Results)

def SaveFile(Data):
    with open("cipher_results.txt", "w") as NewCipherFile:
        NewCipherFile.write(Data)
    print("data saved to cipher_results.txt")


if __name__ == "__main__":
    main()
