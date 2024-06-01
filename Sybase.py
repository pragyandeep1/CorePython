from corepython.DBInterface import DBInterface
class Sybase(DBInterface):
 def connect(self):
  print('Connecting to Sybase Database...')
 def disconnect(self):
  print('Disconnecting to Sybase Database...')
dbname = input('Enter Database Name:')
classname = globals()[dbname]
x = classname()
x.connect()
x.disconnect()