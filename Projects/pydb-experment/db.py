from sqlite3 import connect as sqc

def create_sqlite_tb(db_name: str, tb_name: str, args: dict, delete: bool):
    row = ""
    for i in args:
        row += f"{i['key'].lower()} {i['type'].upper()}"
    db = sqc(f"{db_name}.db")
    db.cursor()
    if delete:
        db.execute(f"DROP TABLE IF EXISTS {tb_name.lower()}")
        print(f'Dropped Table {tb_name} on {db_name}')
    try:
        db.execute(f'CREATE TABLE {tb_name.lower()}({row});')
        db.close()
        return f'Created Table {tb_name} on {db_name}'
    except Exception as e:
        db.close()
        return f'ERROR CREATING DATABASE: {e}'
    
'''
args = [
    {
        'key': 'sid',
        'type': 'NUMBER(8) PRIMARY KEY,'
    },
    {
        'key': 'name',
        'type': 'VARCHAR(255)'
    }
]
print(create_sqlite_tb('db1', 'stu', args, False))
'''