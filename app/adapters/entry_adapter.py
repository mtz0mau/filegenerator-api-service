def get_columns(json_data):
  columns = []
  for entry in json_data:
    for key in entry.keys():
      if key not in columns:
        columns.append(key)
  return columns

def get_rows(json_data):
  rows = []
  for entry in json_data:
    row = []
    for key in get_columns(json_data):
      row.append(entry.get(key, ""))
    rows.append(row)
  return rows

def data_merge(json_data):
  data = [get_columns(json_data)]
  data.extend(get_rows(json_data))
  return data