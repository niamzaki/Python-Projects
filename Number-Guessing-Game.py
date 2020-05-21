from random import randint as ri
hasil=ri(1,101)
penyimpanan=[0]
while True:
    try:
        jawaban=int(input('masukkan angka tebakanmu '))
    except:
        print('itu bukan angka, masukkan angka')
        continue
    else:
        if jawaban < 1 or jawaban > 100:
            print('jawabanmu kelewat batas')
            continue
        if jawaban ==hasil:
            print(f'waw, jawabanmu {jawaban} dari percobaan ke-{len(penyimpanan)} bener sob')
            break
        penyimpanan.append(jawaban)
        if penyimpanan[-2]:
            if abs(jawaban-hasil)<abs(hasil-penyimpanan[-2]):
                print('ish,dikit lagi')
            else:
                print('yah, jauh sob')
        else:
            if abs(jawaban-hasil)<=10:
                print('dikit lagi')
            else:
                print('masih jauh')