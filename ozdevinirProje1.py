# Turing Makinesi ile Binary Çarpma Hesaplayıcı

class TuringMachine:

    def __init__(self, tape):

        # Bant
        self.tape = list(tape) + ['_'] * 20

        # Kafa pozisyonu
        self.head = 0

        # Başlangıç durumu
        self.state = "q0"

        # Adım sayacı
        self.step_count = 0

        # Transition table
        self.transitions = {

            # q0 -> '*' bulana kadar ilerle
            ("q0", "0"): ("q0", "0", "R"),
            ("q0", "1"): ("q0", "1", "R"),
            ("q0", "*"): ("qFindMultiplier", "*", "R"),

            # multiplier alanında ilerle
            ("qFindMultiplier", "0"): ("qFindMultiplier", "0", "R"),
            ("qFindMultiplier", "1"): ("qFindMultiplier", "1", "R"),

            # '=' bulundu
            ("qFindMultiplier", "="): ("qMultiply", "=", "L"),
        }

    # -------------------------
    # Bant görüntüleme
    # -------------------------

    def print_tape(self, read_symbol="", write_symbol="", move=""):

        print("\n=================================================")
        print(f"Step   : {self.step_count}")
        print(f"State  : {self.state}")
        print(f"Read   : {read_symbol}")
        print(f"Write  : {write_symbol}")
        print(f"Move   : {move}")

        print("\nTape:")
        print("".join(self.tape).rstrip("_"))

        pointer = " " * self.head + "^"
        print(pointer)

        print("=================================================")

    # -------------------------
    # Tek adım çalıştır
    # -------------------------

    def step(self):

        symbol = self.tape[self.head]

        key = (self.state, symbol)

        if key not in self.transitions:
            return False

        new_state, write_symbol, move = self.transitions[key]

        # Yaz
        self.tape[self.head] = write_symbol

        # Görüntüle
        self.print_tape(symbol, write_symbol, move)

        # Hareket
        if move == "R":
            self.head += 1
        elif move == "L":
            self.head -= 1

        # Durum güncelle
        self.state = new_state

        self.step_count += 1

        return True

    # -------------------------
    # Operand ayrıştırma
    # -------------------------

    def parse_operands(self):

        star_index = self.tape.index('*')
        equal_index = self.tape.index('=')

        multiplicand = "".join(self.tape[:star_index])

        multiplier = "".join(
            self.tape[star_index + 1:equal_index]
        )

        print("\n******** OPERAND AYRIŞTIRMA ********")
        print(f"Birinci Sayı  : {multiplicand}")
        print(f"İkinci Sayı   : {multiplier}")

        return multiplicand, multiplier

    # -------------------------
    # Binary toplama
    # -------------------------

    def binary_add(self, a, b):

        max_len = max(len(a), len(b))

        a = a.zfill(max_len)
        b = b.zfill(max_len)

        carry = 0
        result = ""

        for i in range(max_len - 1, -1, -1):

            total = carry

            total += int(a[i])
            total += int(b[i])

            result = str(total % 2) + result

            carry = total // 2

        if carry:
            result = "1" + result

        return result.lstrip("0") or "0"

    # -------------------------
    # Shift & Add işlemi
    # -------------------------

    def multiply(self, multiplicand, multiplier):

        print("\n******** SHIFT & ADD BAŞLADI ********")

        result = "0"

        reversed_multiplier = multiplier[::-1]

        for shift, bit in enumerate(reversed_multiplier):

            print("\n----------------------------------")
            print(f"İşlenen Bit : {bit}")
            print(f"Shift Miktarı : {shift}")

            if bit == "1":

                shifted_value = multiplicand + ("0" * shift)

                print(f"Kaydırılmış Değer : {shifted_value}")

                old_result = result

                result = self.binary_add(result, shifted_value)

                print(f"{old_result} + {shifted_value} = {result}")

            else:

                print("Bit = 0 -> toplama yapılmadı")

        return result

    # -------------------------
    # Sonucu banda yaz
    # -------------------------

    def write_result(self, result):

        self.state = "qWriteResult"

        equal_index = self.tape.index('=')

        position = equal_index + 1

        self.head = position

        for bit in result:

            current = self.tape[self.head]

            self.tape[self.head] = bit

            self.print_tape(current, bit, "R")

            self.head += 1

            self.step_count += 1

        self.state = "qAccept"

    # -------------------------
    # TM çalıştır
    # -------------------------

    def run(self):

        print("\n========== TURING MACHINE BAŞLADI ==========")

        # q0 -> '=' bulunana kadar transition çalıştır
        while self.state != "qMultiply":

            if not self.step():
                print("Geçersiz transition!")
                return

        # Operand ayrıştır
        multiplicand, multiplier = self.parse_operands()

        # Çarpma işlemi
        result = self.multiply(multiplicand, multiplier)

        # Sonucu banda yaz
        self.write_result(result)

        # Final
        print("\n========== SONUÇ ==========")

        print(f"Binary Sonuç  : {result}")

        decimal_result = int(result, 2)

        print(f"Decimal Sonuç : {decimal_result}")

        print("\nFinal Tape:")

        print("".join(self.tape).rstrip("_"))

        print("\nMakine Durumu : ACCEPT")


# =====================================================
# MAIN
# =====================================================

print("TURING MAKİNESİ İLE BINARY ÇARPMA")
print("----------------------------------")

num1 = input("Birinci binary sayı : ")
num2 = input("İkinci binary sayı  : ")

# Girdi doğrulama
if not all(c in "01" for c in num1):
    print("HATA: Birinci sayı binary değil!")
    exit()

if not all(c in "01" for c in num2):
    print("HATA: İkinci sayı binary değil!")
    exit()

# Bant oluştur
tape = num1 + "*" + num2 + "="

print("\nBaşlangıç Bandı:")
print(tape)

# TM oluştur
tm = TuringMachine(tape)

# Çalıştır
tm.run()
