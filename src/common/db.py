import pymysql

# Open database connection
conn = pymysql.connect(host='172.26.233.89', user='python', password='1q2w3e4r5t',
                       db='test', charset='utf8')


# prepare a cursor object using cursor() method
cursor = conn.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print("Database version : %s " % data)

# disconnect from server
conn.close()

