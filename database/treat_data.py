def treat_column(column_value):
    if column_value.strip() in {None, '', ".", "*", "NA"}:
        return "N/A"
    return column_value


def treat_data(table, field, value):
    return treat_column(value)
