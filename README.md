Turing Machine Binary Multiplication
 Proje Hakkında

Bu proje, tek bantlı Turing Makinesi mantığını kullanarak iki binary sayının çarpımını gerçekleştiren bir Python simülatörüdür. Kullanıcıdan alınan iki binary sayı, bant üzerinde işlenerek shift & add (kaydır ve topla) yöntemi ile çarpılır.

 Özellikler
Tek bantlı Turing Makinesi simülasyonu
State (durum) tabanlı işlem modeli
Operand ayrıştırma (* ve = kullanımı)
Shift & Add binary çarpma algoritması
Adım adım çalışma çıktısı (state, head, tape)
Binary ve decimal sonuç gösterimi
 Girdi Formatı

Kullanıcıdan iki binary sayı alınır:

11
10

Bant formatı:

11*10=
 Çalışma Mantığı
* karakteri ile operandlar ayrılır
Sol taraf multiplicand, sağ taraf multiplier olarak alınır
Multiplier bitleri sağdan sola okunur
Bit = 1 ise multiplicand sola kaydırılarak toplama yapılır
Bit = 0 ise işlem yapılmaz
Sonuç = karakterinden sonra banda yazılır
 Turing Makinesi Bileşenleri
Bant (Tape)
Kafa (Head)
Durumlar (States)
q0
qFindMultiplier
qMultiply
qWriteResult
qAccept
Geçiş tablosu (Transition Function)
 Çıktı Örneği

Girdi:

11
10

Çıktı:

Binary: 110
Decimal: 6

▶️ Çalıştırma
python ozdevinirProje1.py


📌 Not

Bu proje eğitim amaçlı geliştirilmiştir ve Turing Makinesi mantığını simüle etmeyi hedefler.
