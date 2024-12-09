from typing import Dict, Any

from tinydb import TinyDB

db = TinyDB('db.json')

templates_table = db.table('templates')


def add_data_to_db(data: dict):
    templates_table.insert({'data': data})

def remove_from_db():
    templates_table.truncate()


def get_requests_from_db() -> Dict[str, Any]:
    all_records = templates_table.all()
    result = {str(record.doc_id): record['data'] for record in all_records if 'data' in record}
    last_key = list(result.keys())[-1]
    data_last_key = result[last_key]
    return data_last_key