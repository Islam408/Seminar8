import findemployee
import inp
import logg
import salary
import adder
import delitebl


def work_with_phonk():
    a = inp.show_menu()

    if a == 1:
        name = inp.last_name()
        findemployee.PersonFinder(name)
        logg.log_info(name)
    elif a == 2:
        job = inp.PostJob()
        findemployee.PersonFinder(job)
        logg.log_info(job)
    elif a == 3:
        zarplata = inp.zp()
        salary.SalWal(zarplata)
        logg.log_info(zarplata)
    elif a == 4:
        person = inp.AddPer()
        adder.impo(person)
        logg.log_info(person)
    elif a ==  5:
        choz = inp.DelPerson()
        delitebl.delit(choz)
        logg.log_info(str(choz))

