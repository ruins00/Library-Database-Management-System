import mysql.connector

config = {
  'user': 'root',
  'password': 'rasengan',
  'host': 'Enter-Your-Password-Here',
  'database': 'library',
}

conn = mysql.connector.connect(**config)
cursor = conn.cursor(buffered=True)
filename = input("Enter File Name : ")
table = input("Enter table name :")
#com1 = '''select column_name from information_schema.columns
#            where table_schema = "{}" and table_name = "{}" '''.format(config['database'],table)
#cursor.execute(com1)
#ares = cursor.fetchall()
myfile = open(filename)
content = myfile.readlines()







if table == 'publisher':
    for i in range(len(content)):
        if content[i]=='\n':
            content[i]='Not Specified\n'
    com = '''insert ignore into {} (Name) values ("{}") '''
    for i in content :
        cursor.execute(com.format(table,i[:-1].upper(),))
        #print(com.format(table,i.upper(),))
        conn.commit()
elif table == 'author':
    j=0
    lst = ['{0:05}'.format(num) for num in range(1,len(content)+1)]
    com1 = '''select authorid from author where name = "{}"'''
    com = '''insert ignore into {} (authorid,name) values("{}","{}")'''
    for i in content :
        cursor.execute(com1.format(i[:-1].upper(),))
        a=cursor.fetchone()
        print(a)
        if a==None:
            cursor.execute(com.format(table,'A'+lst[j],i[:-1].upper(),))
        #print(com.format(table,'A'+lst[j],i,))
            j+=1
            conn.commit()
elif table == 'book':
    lst = ['{0:05}'.format(num) for num in range(1,len(content)+1)]
    #print(len(content))
    #print(type(content))
    #for i in content:
    #    print(i.split(','))
    com1 = '''select authorid from author where name = "{}"'''
    com = '''insert ignore into {} values("{}","{}","{}","{}","{}")'''
    com2 = "insert ignore into {} values('{}',5,0)"
    j=0
    for i in content:
        l=i.split(',')
        #print(l)
        if len(l[0])>30:
            l[0]=l[0][:30]
        cursor.execute(com1.format(l[0]))
        a=cursor.fetchone()
        print(com.format(table.upper(),'B'+lst[j],l[1].upper(),'JS01',l[2][:-1].upper(),a[0],))
        cursor.execute(com.format(table.upper(),'B'+lst[j],l[1].upper(),'JS01',l[2][:-1].upper(),a[0],))
        conn.commit()
        cursor.execute(com2.format('book_copies','B'+lst[j],))
        conn.commit()
        j+=1
        print(j)
        print('--'*50)
        








    
