#!/home/ubuntu/.local/share/virtualenvs/build-a-blog-755dbNp1/bin/python

import ibm_db
conn_str='database=handymia;hostname=handymia.com;port=50000;protocol=tcpip;uid=db2inst1;pwd=db2inst1'
ibm_db_conn = ibm_db.connect(conn_str,'','')

# Connect using ibm_db_dbi
import ibm_db_dbi
conn = ibm_db_dbi.Connection(ibm_db_conn)
# Execute tables API
conn.tables('DB2ADMIN', '%')
#[{'TABLE_CAT': None, 'TABLE_SCHEM': 'DB2ADMIN', 'TABLE_NAME': 'MYTABLE', 'TABLE_TYPE': 'TABLE', 'REMARKS': None}]

# create table using ibm_db
#create="create table mytable(id int, name varchar(50))"
#ibm_db.exec_immediate(ibm_db_conn, create)
'''
#Insert 3 rows into the table
insert = "insert into roles values(?,?)"
params=((1,'role1'),(2,'role2'),(3,'role3'))
stmt_insert = ibm_db.prepare(ibm_db_conn, insert)
ibm_db.execute_many(stmt_insert,params)
'''
# Fetch data using ibm_db_dbi
select="select role_id, role_name from roles;"
cur = conn.cursor()
cur.execute(select)
row=cur.fetchall()
print("{} \t {}".format(row[0],row[1]))
#(1, 'Sanders')   (2, 'Pernal')   (3, 'OBrien')
#row=cur.fetchall()
print(row[1])
#[]

# Fetch data using ibm_db
stmt_select = ibm_db.exec_immediate(ibm_db_conn, select)
cols = ibm_db.fetch_tuple( stmt_select )
print("%s, %s" % (cols[0], cols[1]))
#1, Sanders
cols = ibm_db.fetch_tuple( stmt_select )
print("%s, %s" % (cols[0], cols[1]))
#2, Pernal
cols = ibm_db.fetch_tuple( stmt_select )
print("%s, %s" % (cols[0], cols[1]))
#3, OBrien
cols = ibm_db.fetch_tuple( stmt_select )
print(cols)
#False

# Close connections
cur.close()
#True
ibm_db.close(ibm_db_conn)
#True
