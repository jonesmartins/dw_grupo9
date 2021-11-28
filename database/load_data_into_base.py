import sqlite3
from dictionaries.load_data_dict import dictionary_column_mapping
from database.treat_data import treat_data
from dictionaries.paths_dict import *


# The Function 'get_mapped_line' extracts values from csv line and return these values mapped to the following format
# {
#     <SQlTablename1> : {
#         "fields": [<sql_field1>, <sql_field2>, ...]
#         "values": [<sql_field1_corresponding_value>, <sql_field2_corresponding_value>, ...]
#     },
#     <SQlTablename2> : {
#         "fields": [<sql_field3>, <sql_field4>, ...]
#         "values": [<sql_field3_corresponding_value>, <sql_field4_corresponding_value>, ...]
#     }
#     ...
# }
def get_mapped_line(line, dictionary, first_line):
    mapped_line = {}
    for index in range(len(first_line)):
        if first_line[index] in dictionary:
            (table, field) = dictionary[first_line[index]]
            if table not in mapped_line:
                mapped_line[table] = {"fields": [], "values": []}
            treated_data = treat_data(table, field, line[index])
            # If has field with no valid information, ignore line.
            if treated_data == "N/A":
                return None
            mapped_line[table]["fields"].append(field)
            mapped_line[table]["values"].append(treated_data)
    return mapped_line


# Memoizing inserted dimensions values to not make a Select query.
memoized_dimensions_ids = {}


def load_line(sql_connection, first_line, line):
    mapped_line = get_mapped_line(line, dictionary_column_mapping, first_line)
    if mapped_line is None:
        return False
    participacao_values = {
        "fields": [],
        "values": []
    }
    for (table, value) in mapped_line.items():
        fields_string = '`,`'.join(value['fields'])
        values_insertions = ','.join(['?' for _ in value["values"]])
        string_values = '.'.join(value['values'])
        if f"{table}-{string_values}" not in memoized_dimensions_ids:
            query = f"insert into `{table}` (`{fields_string}`) values ({values_insertions})"
            sql_connection.execute(query, value["values"])
            memoized_dimensions_ids[f"{table}-{string_values}"] = sql_connection.lastrowid
        participacao_values["fields"].append(f"{table}_id")
        participacao_values["values"].append(memoized_dimensions_ids[f"{table}-{string_values}"])
    fields_string = '`,`'.join(participacao_values['fields'])
    values_insertions = ','.join(['?' for _ in participacao_values["values"]])
    participacao_values2 = participacao_values["values"] + [line[3]]
    query = f"insert into `registro` (`{fields_string}`,`data`) values ({values_insertions},?)"
    sql_connection.execute(query, participacao_values2)
    return True


def load_data(connection, filepath):
    data_table = open(filepath, 'r')
    first = True
    first_line = None
    count = 0
    for line in data_table:
        splitted_line = line.strip().split(',')
        if first:
            first_line = splitted_line
            first = False
        elif load_line(connection, first_line, splitted_line):
            count += 1
            b = f"Loading line {count}"
            print("\r", b, end="")
    print('\n')
    print('Total lines: ', count)
