clear
figlet RoniYT |lolcat

echo "\33[32;1m[1] DDOS ATTACK"
echo "\33[32;1m[2] Keluar"
echo
echo "\33[31;1mIngat !! Saya Tidak Bertanggung Jawab"

read -p "Masukan Nomor Pilihan Anda:" roni

clear
case $roni in
1)
figlet DDOS |lolcat
python2 attack.py
;;
2)
echo "\33[31;1mKeluar Berhasil"
echo "\33[31;1mJangan Lupa Subscribe RoniYT"
;;
*)
echo "Maaf Nomor Yang Anda Ketik Salah"
sh ddosroniyt.sh
;;
esac
