class Account:
    accounts = []  # Tüm hesaplar burada saklanır

    def __init__(self, account_number, owner, balance=0.0):
        self.__account_number = account_number  # Hesap numarası
        self.__owner = owner  # Hesap sahibinin adı
        self.__balance = balance  # Başlangıç bakiyesi
        Account.accounts.append(self)  # Yeni hesabı listeye ekle

    def deposit(self, amount):
        """Para yatırma işlemi"""
        if amount > 0:
            self.__balance += amount  # Yatırılan miktarı bakiyeye ekle
            Bank.track_transaction(f"{self.__owner} hesabına {amount} TL yatırıldı.")
            print(f"{amount} TL yatırıldı. Yeni bakiye: {self.__balance} TL")
        else:
            print("Yatırılan miktar sıfırdan büyük olmalıdır.")

    def withdraw(self, amount):
        """Para çekme işlemi"""
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount  # Çekilen miktarı bakiyeden düş
                Bank.track_transaction(f"{self.__owner} hesabından {amount} TL çekildi.")
                print(f"{amount} TL çekildi. Yeni bakiye: {self.__balance} TL")
            else:
                print("Yetersiz bakiye.")
        else:
            print("Çekilen miktar sıfırdan büyük olmalıdır.")

    def view_balance(self):
        """Bakiyeyi görüntüle"""
        print(f"Hesap Sahibi: {self.__owner}, Hesap Numarası: {self.__account_number}, Bakiyeniz: {self.__balance} TL")

class Bank:
    transaction_history = []  # İşlem geçmişi

    @staticmethod
    def display_bank_info():
        """Banka bilgilerini göster"""
        print("Banka Bilgileri:")
        print("Banka adı: Modern Banka")
        print("Müşteri memnuniyeti önceliğimizdir.")
    
    @staticmethod
    def track_transaction(description):
        """İşlem geçmişini kaydet"""
        Bank.transaction_history.append(description)

    @staticmethod
    def display_transaction_history():
        """İşlem geçmişini göster"""
        print("İşlem Geçmişi:")
        for transaction in Bank.transaction_history:
            print(transaction)

def main():
    while True:
        print("\n--- Banka Hesap Yönetim Sistemi ---")
        print("1. Hesap Oluştur")
        print("2. Para Yatır")
        print("3. Para Çek")
        print("4. Bakiye Görüntüle")
        print("5. Banka Bilgileri Göster")
        print("6. İşlem Geçmişini Göster")
        print("0. Çıkış")
        choice = input("Seçiminizi yapın: ")

        if choice == '0':
            break
        elif choice == '1':
            account_number = input("Hesap numarasını girin: ")
            owner = input("Hesap sahibinin adını girin: ")
            new_account = Account(account_number, owner)
            print(f"{owner} için hesap oluşturuldu.")
        elif choice == '2':
            account_number = input("Para yatırılacak hesap numarasını girin: ")
            amount = float(input("Yatırılacak miktarı girin: "))
            for account in Account.accounts:
                if account._Account__account_number == account_number:
                    account.deposit(amount)
                    break
            else:
                print("Hesap bulunamadı.")
        elif choice == '3':
            account_number = input("Para çekilecek hesap numarasını girin: ")
            amount = float(input("Çekilecek miktarı girin: "))
            for account in Account.accounts:
                if account._Account__account_number == account_number:
                    account.withdraw(amount)
                    break
            else:
                print("Hesap bulunamadı.")
        elif choice == '4':
            account_number = input("Bakiyesi görüntülenecek hesap numarasını girin: ")
            for account in Account.accounts:
                if account._Account__account_number == account_number:
                    account.view_balance()
                    break
            else:
                print("Hesap bulunamadı.")
        elif choice == '5':
            Bank.display_bank_info()
        elif choice == '6':
            Bank.display_transaction_history()
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
