# db2.py
import sqlite3
#메모리상에 DB를 생성
#물리적인 파일로 변경
con = sqlite3.connect(r"c:\work\sample.db")
#커서객체를 리턴
cur = con.cursor()

#검색
cur.execute("select * from PhoneBook")
print(cur.fetchall())  

