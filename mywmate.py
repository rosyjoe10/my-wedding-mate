import mysql.connector
con=mysql.connector.connect(host='localhost', username='root', password=’’,database='myweddingmate')
cur=con.cursor()
print('*******************************************MY WEDDING MATE*****************************************')
print()
print('1.REGISTER')
print('2.LOGIN')
n=int(input('ENTER YOUR CHOICE:'))
if n==1:
    name=input('ENTER YOUR USERNAME:')
    passwd=input('ENTER YOUR PASSWORD:')
    print()
    query="insert into userid values ('{0}','{1}')".format(name,passwd)
    cur.execute(query)
    con.commit()
    print('USER CREATED SUCCESSFULLY')
elif n==2:
    name=input('ENTER YOUR USERNAME:')
    print()
    passwd=input('ENTER YOUR PASSWORD:')
    query="select * from userid where password=('{0}') and username=('{1}')".format(passwd,name)
    cur.execute(query)
    if cur.fetchone() is None:
        print()
        print('INVALID USERNAME OR PASSWORD')
    else:
        print()
        c='y'
        while c.lower()=='y':
            print('_________________________________WELCOME TO MWM MARTIMONIAL SERVICE________________________________')
            print()
            print("1.TO ENTER PERSONAL DETAILS")
            print('2.TO EDIT YOUR DETAILS')
            print('3.TO SEARCH FOR YOUR PERFECT MATCH')
            print('4.TO DELETE YOUR ACCOUNT')
            choice=int(input('ENTER YOUR CHOICE:'))
            if choice==1:
                print('3.IF YOU ARE A POTENTIAL GROOM')
                print('4.IF YOU ARE A POTENTIAL BRIDE')
                ch=int(input('ENTER YOUR CHOICE:'))
                if ch==3:
                    print("PLEASE ENTER YOUR DETAILS")
                    a=input('FULL NAME:')
                    b=input('DISTRICT:')
                    z=input('RELIGION:')
                    d=input('DATE OF BIRTH:')
                    e=input('YOUR AGE:')
                    f=input('PROFESSION:')
                    g=input('PHONE NUMBER:')
                    h=input('STAR SIGN:')
                    insert="insert into grooms values('{}','{}','{}','{}','{}','{}','{}','{}')".format(a,b,z,d,e,f,g,h)
                    cur.execute(insert)
                    con.commit()
                    print ('YOUR DETAILS HAVE BEEN ENTERED')
                    c=input('DO YOU WANT TO CONTINUE (y/n):')
                    if c =='y' :
                        continue
                    else:
                        break
                elif ch==4:
                    print("PLEASE ENTER YOUR DETAILS")
                    i=input('FULL NAME:')
                    j=input('DISTRICT:')
                    k=input('RELIGION:')
                    l=input('DATE OF BIRTH:')
                    m=input('YOUR AGE:')
                    n=input('PROFESSION:')
                    o=input('PHONE NUMBER:')
                    p=input('STAR SIGN:')
                    insert="insert into brides values( '{}','{}','{}','{}','{}','{}','{}','{}')".format(i,j,k,l, m,n,o,p)
                    cur.execute(insert)
                    con.commit()
                    print ('YOUR DETAILS HAVE BEEN ENTERED')
                    c=input('DO YOU WANT TO CONTINUE (y/n):')
                    if c =='y' :
                        continue
                    else:
                        break
            elif choice==4:
                print('1.IF YOU WERE A POTENTIAL GROOM')
                print('2.IF YOU WERE A POTENTIAL BRIDE')
                ce=int(input('ENTER YOUR CHOICE:'))
                if ce==1:
                    nme=input('ENTER YOUR FULL NAME:')
                    cde=("delete from grooms where name='{}'").format(nme)
                    cur.execute(cde)
                    con.commit()
                    print('YOUR DETAILS HAVE BEEN REMOVED')
                elif ce==2:
                    nme=input('ENTER YOUR FULL NAME:')
                    cde=('delete from brides where name="{}"').format(nme)
                    cur.execute(cde)
                    con.commit()
                    print('YOUR DETAILS HAVE BEEN REMOVED')
                else:
                    print("404 ERROR")
                    break
                uname=input('ENTER YOUR USERNAME:')
                de=('delete from userid where username="{}"').format(uname)
                cur.execute(de)
                con.commit()
                print('YOUR ACCOUNT HAS BEEN DELETED')
                break
            elif choice==2:
                print('3.IF YOU ARE A POTENTIAL GROOM')
                print('4.IF YOU ARE A POTENTIAL BRIDE')
                cho=int(input('ENTER YOUR CHOICE:'))
                if cho==3:
                    name=input('ENTER YOUR FULL NAME:')
                    col=input('ENTER WHAT YOU WANT TO EDIT:')
                    val=input('ENTER NEW VALUE:')
                    if col=='age':
                        val=int(val)
                        alt='update grooms set {}={} where name="{}"'.format(col,val,name)
                        cur.execute(alt)
                        con.commit()
                        print('YOUR DETAILS HAVE BEEN ALTERED')
                    else:
                        alt='update grooms set {}="{}" where name="{}"'.format(col,val,name)
                        cur.execute(alt)
                        con.commit()
                        print('YOUR DETAILS HAVE BEEN ALTERED')
                elif cho==4:
                    name=input('ENTER YOUR FULL NAME:')
                    col=input('ENTER WHAT YOU WANT TO EDIT:')
                    val=input('ENTER NEW VALUE:')
                    if col=='age':
                        val=int(val)
                        alt='update brides set {}={} where name="{}"'.format(col,val,name)
                        cur.execute(atl)
                        con.commit()
                        print('YOUR DETAILS HAVE BEEN ALTERED')
                    else:
                        alt='update brides set {}="{}" where name="{}"'.format(col,val,name)
                        cur.execute(alt)
                        con.commit()
                        print('YOUR DETAILS HAVE BEEN ALTERED')
                else:
                    print("404 ERROR")
                    break
            elif choice==3:
                print('5.IF YOU ARE SEARCHING FOR A PROSPECTIVE GROOM')
                print('6.IF YOU ARE SEARCHING FOR A PROSPECTIVE BRIDE')
                ch=int(input('ENTER YOUR CHOICE:'))
                
                if ch==5:
                    print('ENTER SPECIFICATIONS FOR WHAT YOU ARE LOOKING FOR:')
                    print('1-TO VIEW ALL PROSPECTIVE GROOMS')
                    print('2-TO SEARCH BY DISTRICT')
                    print('3-TO SEARCH BY RELIGION')
                    print('4-TO SEARCH BY AGE')
                    print('5-TO SEARCH BY PROFESSION')
                    print('6-TO SEARCH COMPATIBLE STAR SIGN')
                    ce=int(input('ENTER YOUR CHOICE:'))
                    if ce==1:
                        display="select * from grooms"
                        cur.execute(display)
                        myrec=cur.fetchall()
                        for i in myrec:
                            print(i)
                    elif ce==2:
                        dis=input('ENTER DISTRICT TO SEARCH BY:')
                        dis.lower()
                        display="select * from grooms where district='{}'".format(dis)
                        cur.execute(display)
                        myrec=cur.fetchall()
                        for i in myrec:
                            print(i)
                    elif ce==3:
                        dis=input('ENTER RELIGION TO SEARCH BY:')
                        dis.lower()
                        display="select * from grooms where religion='{}'".format(dis)
                        cur.execute(display)
                        myrec=cur.fetchall()
                        for i in myrec:
                            print(i)
                    elif ce==4:
                        dis=int(input('ENTER AGE TO SEARCH BY:'))
                        display="select * from grooms where age='{}'".format(dis)
                        cur.execute(display)
                        myrec=cur.fetchall()
                        for i in myrec:
                            print(i)
                    elif ce==5:
                        dis=input('ENTER PROFESSION TO SEARCH BY:')
                        dis.lower()
                        display="select * from grooms where profession='{}'".format(dis)
                        cur.execute(display)
                        myrec=cur.fetchall()
                        for i in myrec:
                            print(i)
                    elif ce==6:
                        dis=input('ENTER YOUR STAR SIGN:')
                        dis.lower()
                        if dis=="aries":
                            cur.execute("SELECT * from grooms where star_sign in ('leo','gemini','sagittarius')")
                            myrec=cur.fetchall()
                            for i in myrec:
                                print(i)
                        elif dis=="taurus":
                            cur.execute("SELECT * from grooms where star_sign in ('taurus','virgo','cancer')")
                            myrec=cur.fetchall()
                            for i in myrec:
                                print(i)
                        elif dis=="gemini":
                            cur.execute("SELECT * from grooms where star_sign in ('aquarius','libra','leo')")
                            myrec=cur.fetchall()
                            for i in myrec:
                                print(i)
                        elif dis=="cancer":
                            cur.execute("SELECT * from grooms where star_sign in ('pisces','cancer','scorpio')")
                            myrec=cur.fetchall()
                            for i in myrec:
                                print(i)
                        elif dis=="leo":
                            cur.execute("SELECT * from grooms where star_sign in ('aries','leo','sagittarius')")
                            myrec=cur.fetchall()
                            for i in myrec:
                                print(i)
                        elif dis=="virgo":
                            cur.execute("SELECT * from grooms where star_sign in ('scorpio','taurus','capricon')")
                            myrec=cur.fetchall()
                            for i in myrec:
                                print(i)
                        elif dis=="libra":
                            cur.execute("SELECT * from grooms where star_sign in ('aquarius','sagittarius','gemini')")
                            myrec=cur.fetchall()
                            for i in myrec:
                                print(i)
                        elif dis=="scorpio":
                            cur.execute("SELECT * from grooms where star_sign in ('cancer','scorpio','pisces')")
                            myrec=cur.fetchall()
                            for i in myrec:
                                print(i)
                        elif dis=="sagittarius":
                            cur.execute("SELECT * from grooms where star_sign in ('leo','sagittarius','aries'")
                            myrec=cur.fetchall()
                            for i in myrec:
                                print(i)
                        elif dis=="capricon":
                            cur.execute("SELECT * from grooms where star_sign in ('capricon','virgo','taurus')")
                            myrec=cur.fetchall()
                            for i in myrec:
                                print(i)
                        elif dis=="aquarius":
                            cur.execute("SELECT * from grooms where star_sign in ('aquarius','libra','gemini')")
                            myrec=cur.fetchall()
                            for i in myrec:
                                print(i)
                        elif dis=="pisces":
                            cur.execute("SELECT * from grooms where star_sign in ('pisces','cancer','scorpio')")
                            myrec=cur.fetchall()
                            for i in myrec:
                                print(i)
                        else:
                            print("404 ERROR")
                            break
                    else:
                        print("404 ERROR")
                        break
                    c=input('DO YOU WANT TO CONTINUE (y/n):')
                    if c =='y' :
                        continue
                    else:
                        break
                elif ch==6:
                    print('ENTER SPECIFICATIONS FOR WHAT YOU ARE LOOKING FOR:')
                    print('1-TO VIEW ALL PROSPECTIVE BRIDES')
                    print('2-TO SEARCH BY DISTRICT')
                    print('3-TO SEARCH BY RELIGION')
                    print('4-TO SEARCH BY AGE')
                    print('5-TO SEARCH BY PROFESSION')
                    print('6-TO SEARCH COMPATIBLE STAR SIGN')
                    ce=int(input('ENTER YOUR CHOICE:'))
                    if ce==1:
                        display="select * from brides"
                        cur.execute(display)
                        myrec=cur.fetchall()
                        for i in myrec:
                            print(i)
                    elif ce==2:
                        dis=input('ENTER DISTRICT TO SEARCH BY:')
                        dis.lower()
                        display="select * from brides where district='{}'".format(dis)
                        cur.execute(display)
                        myrec=cur.fetchall()
                        for i in myrec:
                            print(i)
                    elif ce==3:
                        dis=input('ENTER RELIGION TO SEARCH BY:')
                        dis.lower()
                        display="select * from brides where religion='{}'".format(dis)
                        cur.execute(display)
                        myrec=cur.fetchall()
                        for i in myrec:
                            print(i)
                    elif ce==4:
                        dis=int(input('ENTER AGE TO SEARCH BY:'))
                        display="select * from brides where age='{}'".format(dis)
                        cur.execute(display)
                        myrec=cur.fetchall()
                        for i in myrec:
                            print(i)
                    elif ce==5:
                        dis=input('ENTER PROFESSION TO SEARCH BY:')
                        dis.lower()
                        display="select * from brides where profession='{}'".format(dis)
                        cur.execute(display)
                        myrec=cur.fetchall()
                        for i in myrec:
                            print(i)
                    elif ce==6:
                        dis=input('ENTER YOUR STAR SIGN:')
                        dis.lower()
                        if dis=="aries":
                            cur.execute("SELECT * from brides where star_sign in ('leo','gemini','sagittarius')")
                            myrec=cur.fetchall()
                            for i in myrec:
                                print(i)
                        elif dis=="taurus":
                            cur.execute("SELECT * from brides where star_sign in ('taurus','virgo','cancer')")
                            myrec=cur.fetchall()
                            for i in myrec:
                                print(i)
                        elif dis=="gemini":
                            cur.execute("SELECT * from brides where star_sign in ('aquarius','libra','leo')")
                            myrec=cur.fetchall()
                            for i in myrec:
                                print(i)
                        elif dis=="cancer":
                            cur.execute("SELECT * from brides where star_sign in ('pisces','cancer','scorpio')")
                            myrec=cur.fetchall()
                            for i in myrec:
                                print(i)
                        elif dis=="leo":
                            cur.execute("SELECT * from brides where star_sign in ('aries','leo','sagittarius')")
                            myrec=cur.fetchall()
                            for i in myrec:
                                print(i)
                        elif dis=="virgo":
                            cur.execute("SELECT * from brides where star_sign in ('scorpio','taurus','capricon')")
                            myrec=cur.fetchall()
                            for i in myrec:
                                print(i)
                        elif dis=="libra":
                            cur.execute("SELECT * from brides where star_sign in ('aquarius','sagittarius','gemini')")
                            myrec=cur.fetchall()
                            for i in myrec:
                                print(i)
                        elif dis=="scorpio":
                            cur.execute("SELECT * from brides where star_sign in ('cancer','scorpio','pisces')")
                            myrec=cur.fetchall()
                            for i in myrec:
                                print(i)
                        elif dis=="sagittarius":
                            cur.execute("SELECT * from brides where star_sign in ('leo','sagittarius','aries'")
                            myrec=cur.fetchall()
                            for i in myrec:
                                print(i)
                        elif dis=="capricon":
                            cur.execute("SELECT * from brides where star_sign in ('capricon','virgo','taurus')")
                            myrec=cur.fetchall()
                            for i in myrec:
                                print(i)
                        elif dis=="aquarius":
                            cur.execute("SELECT * from brides where star_sign in ('aquarius','libra','gemini')")
                            myrec=cur.fetchall()
                            for i in myrec:
                                print(i)
                        elif dis=="pisces":
                            cur.execute("SELECT * from brides where star_sign in ('pisces','cancer','scorpio')")
                            myrec=cur.fetchall()
                            for i in myrec:
                                print(i)
                        else:
                            print("404 ERROR")
                            break
                    else:
                        print("404 ERROR")
                        break
                    c=input('DO YOU WANT TO CONTINUE (y/n):')
                    c.lower()
                    if c =='y' :
                        continue
                    else:
                        break
            
        
                else:
                    print("404 ERROR")
                    break
