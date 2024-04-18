import sqlite3


db_name = "cats_db"


def check_credentials(login, password):
	connection = sqlite3.connect(db_name)
	connection.set_trace_callback(print)
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM credentials where login=? and password=?;", (login, password))
	user = cursor.fetchall()
	print(user)
	return user[0]


def post_credentials(credentials):
	connection = sqlite3.connect(db_name)
	connection.set_trace_callback(print)
	cursor = connection.cursor()
	cursor.execute("INSERT INTO user(name) VALUES(NULL);")
	user_id = cursor.lastrowid
	cursor.execute("INSERT INTO credentials(login, password, user_id) VALUES(?,?,?);", (credentials.login, credentials.password, user_id))
	connection.commit()


def check_login(login):
	connection = sqlite3.connect(db_name)
	connection.set_trace_callback(print)
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM credentials WHERE login=?;", (login,))
	if cursor.fetchone():
		return False
	else:
		return True
