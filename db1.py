# db1.py
import sqlite3
#메모리상에 DB를 생성
#물리적인 파일로 변경
con = sqlite3.connect("test.db")
#커서객체를 리턴
cur = con.cursor()
#테이블 생성(테이블 스키마 - 구조)
cur.execute("create table if not exists PhoneBook(Name text, PhoneNum text)")
#입력
cur.execute("insert into PhoneBook values('derick', '010-222');")
#입력파라메터로 받기
name = "전우치"
phoneNumber = "010-123-1234"
cur.execute("insert into PhoneBook values(?, ?);", (name, phoneNumber))
#여러번 SQL 구문 실행
datalist = (("박문수", "010-222"), ("이순신", "010-333"))
cur.executemany("insert into PhoneBook values(?, ?);", datalist)

#검색
cur.execute("select * from PhoneBook")
print(cur.fetchall())   

