current_temp = 17
AC_stat = "OFF"
total = 0
desired_temp_list = [29, 18, 16, 27]


def increase_temp(des_tem, ini_temp):
    global total
    total += (des_tem-ini_temp)*2


def decrease_temp(des_tem, initi_temp):
    global total
    ini_temp = initi_temp
    # print(total)
    while des_tem != initi_temp:
        if 30 >= ini_temp > 25:
            if 25 > des_tem:
                total += (ini_temp - 25)*2
                ini_temp = 25
                print(f"30 to 25 lesssss")
                print(f"current Total ==> {total}")

            if 25 < des_tem:
                total += (ini_temp - des_tem)*2
                ini_temp = des_tem
                print(f" 30 to 25 middle")
                print(f"Current Total ==> {total}")
                break

        if 25 >= ini_temp > 20:

            if 20 > des_tem:
                total += (ini_temp - 20) * 3
                ini_temp = 20
                print(f"25 to 20 lesssss")
                print(f"Current Total ==> {total}")
            if 20 < des_tem:
                total += (ini_temp - des_tem) * 3
                ini_temp = des_tem
                print("25 to 28 middle")
                print(f"Current Total ==> {total}")
                break

        if 20 >= ini_temp > 16:
            total += (ini_temp - des_tem) * 4
            ini_temp = des_tem
            print("20 to 16 middle")
            print(f"Current Total ==> {total}")
            break


def AC(des_tem, initi_temp):
    global AC_stat
    global total
    if des_tem > initi_temp and (AC_stat == "ON"):
        AC_stat = "OFF"
        print("AC turned OFF")

    if des_tem < initi_temp and (AC_stat == "OFF"):
        total += 2
        print("AC turned ON")
        AC_stat = "ON"


for desired_temp in desired_temp_list:
    print("start")
    print(current_temp, desired_temp)

    if desired_temp > current_temp:
        AC(desired_temp, current_temp)
        print(f"AC stat=> {AC_stat}")
        increase_temp(desired_temp, current_temp)
        print(
            f"Temperature is increased from {current_temp} ==> {desired_temp}")
        current_temp = desired_temp
        print(f"Current Total ==> {total}, Current temp ==> {current_temp}")

    elif desired_temp < current_temp:
        AC(desired_temp, current_temp)
        print(f"AC stat-> {AC_stat}")
        decrease_temp(desired_temp, current_temp)
        print(
            f"Temperature is decreased from {current_temp} ==> {desired_temp}")
        current_temp = desired_temp
        print(f"Current Total ==> {total}, Current temp ==> {current_temp}")

    elif desired_temp == current_temp:
        print(f"No change as desired temp == current temp ie. {current_temp}")
        print(f"Current Total ==> {total}")
        pass
