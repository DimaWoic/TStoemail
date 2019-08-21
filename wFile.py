import time
import sendMail
import connectmysql

while True:

    time.sleep(60)
    print('Открываем Tmp1 для записи')
    rTmp1 = open('tmp1.txt', 'w')
    print('ОК')
    print('записываем в файл')
    rTmp1.write(str(connectmysql.idTsindex))
    rTmp1.close()
    print('открываем для чтение временные файлы')
    rTmp1 = open('tmp1.txt', 'r')
    rTmp2 = open('tmp2.txt', 'r')
    print('Ok')
    # print(rTmp.read())
    if (rTmp1.read() == rTmp2.read()):
        print('Запрос')
        rTmp1.close()
        rTmp2.close()
    elif (rTmp1.read() != rTmp2.read()):
        rTmp1.close()
        rTmp2.close()
        rTmp2 = open('tmp.txt', 'w')
        rTmp2.write(str(connectmysql.idTsindex))
        rTmp2.close()
        print(connectmysql.msgtoemail)
        sendMail.send_mail("wdv85@mail.ru", connectmysql.msgtoemail)

    
    
    
    
    

#f = open('tmp.txt', 'w')
#f.write(str(connectmysql.idTsindex))
#f.close()

