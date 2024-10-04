class Hospital:
    patients = [1 for i in range(200)]
    status = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}
    flag = True

    @classmethod  # Команда "узнать статус пациента"
    def get_status(cls, id_):
        if isinstance(id_, int) and id_ > 0:
            if id_ <= len(cls.patients):
                print(cls.status[cls.patients[id_ - 1]])
            else:
                print("Данного ID не существует")
        else:
            print("Введено не допустимое значение")

    @classmethod  # Команда "повысить статус пациента"
    def status_up(cls, id_):
        if isinstance(cls.patients[id_ - 1], int):
            cls.patients[id_ - 1] += 1
            if cls.patients[id_ - 1] > 3:
                print('Не желает ли вы выписать пациента?')
                resp = input()
                if resp.lower() == 'да':
                    cls.patients[id_ - 1] = f'Пациент {id_} уже выписан'
                    print('Пациент выписан из больницы')
                else:
                    cls.patients[id_ - 1] -= 1
            else:
                print(f"Новый статус пациента: {cls.status[cls.patients[id_ - 1]]}")
        else:
            print(cls.patients[id_ - 1])

    @classmethod  # Команда "понизить статус пациента"
    def status_down(cls, id_):
        cls.patients[id_ - 1] -= 1
        if cls.patients[id_ - 1] == -1:
            print('Нельзя понизить статус пациента ниже 0')
            cls.patients[id_ - 1] += 1
        else:
            print(f"Новый статус пациента: {cls.status[cls.patients[id_ - 1]]}")

    @classmethod
    def discharge(cls, id_):
        del cls.patients[id_ - 1]

    @classmethod
    def calculate_statistics(cls):
        print(f"""
        \rПациентов со статусом {cls.status[0]}: {len(list(filter(lambda x: x == 0, cls.patients)))} чел.
        \rПациентов со статусом {cls.status[1]}: {len(list(filter(lambda x: x == 1, cls.patients)))} чел.
        \rПациентов со статусом {cls.status[2]}: {len(list(filter(lambda x: x == 2, cls.patients)))} чел.
        \rПациентов со статусом {cls.status[3]}: {len(list(filter(lambda x: x == 3, cls.patients)))} чел.""")

    @classmethod
    def comandos(cls):
        print("Введите команду: ")
        s = input()
        if s[:10] == 'get status':
            cls.get_status(int(s[10:]))
        elif s[:9] == 'status up':
            cls.status_up(int(s[9:]))
        elif s[:11] == 'status down':
            cls.status_down(int(s[11:]))
        elif s[:10] == 'discharge':
            cls.discharge(int(s[10:]))
        elif s == 'calculate statistics':
            cls.calculate_statistics()
        elif s == "stop":
            cls.flag = False



while Hospital.flag:
    Hospital.comandos()
