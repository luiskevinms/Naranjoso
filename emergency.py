from persistence.db import get_connection

from security.crypto import decrypt
from entities.user import User

connection = get_connection()
cursor = connection.cursor(dictionary=True) #el dictionary hace que retorne un tipo dict
        
query = "SELECT id, name, curp, account, password FROM users WHERE id = %s"
        
cursor.execute(query, (3,))
row = cursor.fetchone()

alexis =         User(id=row["id"], 
                 name=row['name'], 
                 curp=decrypt(row['curp']), 
                 account=row['account'], 
                 password=decrypt(row['password']))

print(alexis.password)