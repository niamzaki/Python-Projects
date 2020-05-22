from random import randint
jawaban_benar=randint(1,101)
print("Ini adalah game tebak angka antara 1-100, baik 1 digit ataupun 2 digit, \naturannya sederhana, anda hanya perlu menebak angka yang benar tanpa batasan percobaan")
kumpulan_jawaban=[0]
while True:
    jawaban=int(input('jawabannya antara 1-100, jawabanmu berapa?: '))
    if jawaban < 0 or jawaban > 100:
        print('jawabanmu kelewat batas')
        continue
    if jawaban==jawaban_benar:
        print(f'mantab sob, jawabanmu {jawaban_benar} itu benar dari {len(kumpulan_jawaban)} kali percobaan')
        break
    kumpulan_jawaban.append(jawaban)
    if kumpulan_jawaban[-2]:
        if abs(jawaban_benar-jawaban)<abs(jawaban-kumpulan_jawaban[-2]):
            print('jawabanmu lebih mendekati daripada yang tadi')
        else:
            print('yah, malah menjauh')
    else:
        if abs(jawaban-jawaban_benar)<=10:
            print('woh dikit lagi')
        else:
            print('masih jauh')