from corepython.DBInterface import DBInterface


class Oracle(DBInterface):
 def connect(self):
  print('Connecting to Oracle Database...')
 def disconnect(self):
  print('Disconnecting to Oracle Database...')

dbname = input('Enter Database Name:')
classname = globals()[dbname]
x = classname()
x.connect()
x.disconnect()