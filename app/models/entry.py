class Entry:
  def __init__(self, json_data=[]):
    self.columns = self.get_columns(json_data)

  def get_columns(self, json_data):
    columns = []
    for entry in json_data:
      for key in entry.keys():
        if key not in columns:
          columns.append(key)
    return columns