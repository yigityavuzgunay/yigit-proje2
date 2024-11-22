from abc import ABC, abstractmethod

class Controllable(ABC):
    def turn_on(self):
        pass

    def turn_off(self):
        pass

    def get_status(self):
        pass

# Cihazları temsil eden sınıf
class Appliance(Controllable):
    def __init__(self, name):
        self.name = name
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"{self.name} açıldı.")

    def turn_off(self):
        self.is_on = False
        print(f"{self.name} kapatıldı.")

    def get_status(self):
        status = "açık" if self.is_on else "kapalı"
        print(f"{self.name} durumu: {status}")

# Işık cihazı
class Light(Appliance):
    def __init__(self, name):
        super().__init__(name)

# Termostat cihazı
class Thermostat(Appliance):
    def __init__(self, name):
        super().__init__(name)
        self.temperature = 22  # Varsayılan sıcaklık

    def set_temperature(self, temp):
        self.temperature = temp
        print(f"{self.name} sıcaklığı {self.temperature}°C olarak ayarlandı.")

# Güvenlik Sistemi cihazı
class SecuritySystem(Appliance):
    def __init__(self, name):
        super().__init__(name)
        self.alarm_triggered = False

    def trigger_alarm(self):
        self.alarm_triggered = True
        print(f"{self.name} alarmı tetiklendi!")

    def reset_alarm(self):
        self.alarm_triggered = False
        print(f"{self.name} alarmı sıfırlandı.")

# Akıllı Ev Sistemi
class SmartHome:
    def __init__(self):
        self.appliances = []

    def add_appliance(self, appliance):
        self.appliances.append(appliance)

    def control_appliances(self):
        while True:
            print("\n--- Cihazlar ---")
            for i, appliance in enumerate(self.appliances):
                print(f"{i + 1}. {appliance.name}")

            choice = input("Kontrol etmek için cihaz numarasını seçin (çıkmak için 'q'): ")
            if choice == 'q':
                break

            try:
                appliance = self.appliances[int(choice) - 1]
            except (IndexError, ValueError):
                print("Geçersiz seçim. Lütfen tekrar deneyin.")
                continue

            action = input("Yapmak istediğiniz işlemi seçin (aç/kapat/durum/sıcaklık/alarm): ").lower()
            if action == "aç":
                appliance.turn_on()
            elif action == "kapat":
                appliance.turn_off()
            elif action == "durum":
                appliance.get_status()
            elif isinstance(appliance, Thermostat) and action == "sıcaklık":
                temp = int(input("Yeni sıcaklığı girin: "))
                appliance.set_temperature(temp)
            elif isinstance(appliance, SecuritySystem) and action == "alarm":
                alarm_action = input("Alarmı tetiklemek için 'tetik', sıfırlamak için 'sıfırla' yazın: ").lower()
                if alarm_action == "tetik":
                    appliance.trigger_alarm()
                elif alarm_action == "sıfırla":
                    appliance.reset_alarm()
            else:
                print("Bu işlem bu cihaz için geçerli değil.")

# Ana program
if __name__ == "__main__":
    smart_home = SmartHome()

    # Cihaz ekleme
    smart_home.add_appliance(Light("Salon Işığı"))
    smart_home.add_appliance(Thermostat("Salon Termostatı"))
    smart_home.add_appliance(SecuritySystem("Bina Güvenlik Sistemi"))

    # Cihazları kontrol etme
    smart_home.control_appliances()
