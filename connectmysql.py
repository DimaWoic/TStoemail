#  -*- coding: cp1251 -*-

import pymysql.cursors

# Подключиться к базе данных.
connection = pymysql.connect(host='127.0.0.1',
                             user='Configure',
                             #password='128',
                             db='saratov',
                             charset='latin1',
                             cursorclass=pymysql.cursors.DictCursor)

print("Подключились к БД saratov")

try:

    with connection.cursor() as cursor:

        #cursor.execute("SET NAMES cp1251")
        #cursor.execute("SET CHARACTER SET utf8")
        #cursor.execute("SET character_set_client = utf8")
        #cursor.execute("SET character_set_connection = utf8")
        #cursor.execute("SET character_set_results = utf8")


        #SQl запрос для IdTs
        idTs = "SELECT IdTs  FROM listts"
        cursor.execute(idTs)
        rowIdts = cursor.fetchall()
        list.reverse(rowIdts)
        idTsindex = rowIdts[0].get('IdTs')
        #print(idTsindex)


        # SQL
        pst = "SELECT IdStation  FROM listts"

        # Выполнить команду запроса (Execute Query).
        cursor.execute(pst)

        row = cursor.fetchall()
        list.reverse(row)
        IdS=row[0].get('IdStation')


        # SQL
        forwprefix = "SELECT ForwPrefix  FROM listts"

        # Выполнить команду запроса (Execute Query).
        cursor.execute(forwprefix)

        row1 = cursor.fetchall()
        list.reverse(row1)
        ForP = row1[0].get('ForwPrefix')


        note = "SELECT Note  FROM listts"

        # Выполнить команду запроса (Execute Query).
        cursor.execute(note)

        row2 = cursor.fetchall()
        list.reverse(row2)
        Note = row2[0].get('Note')



        #if idTsindex==idTssawap:
         #   print("Соединение прервано изменений в базе нет")
        #else:
        msgtoemail = ("На тяговой подстанции №", row[0].get('IdStation'), row1[0].get('ForwPrefix'), row2[0].get('Note'))

        #for i in row:
        #    print (i)
        #print(row)

finally:

    # Закрыть соединение (Close connection).
    connection.close()


#msgtoemail=row2[0].get('Note')
msgtoemail = 'На тяговой подстанции №' + str(IdS)+' '+ str(ForP)+ ' '+ str(Note)


print(msgtoemail)

#msgtoemail
#sendSms.send_mail("wdv85@mail.ru", msgtoemail)
#sendSms.send_mail("maksim.filin@inbox.ru", msgtoemail)