from emoji import emoji_count

def create_table(dict_list):
  table_list = list(dict_list[0].keys())
  for d in dict_list:
    for k in d.keys():
      table_list.append(d[k])
  colSize = max(map(len,table_list))
  text = "```mathematica\n"
  i = 0
  for entry in table_list:
    space_size = colSize + 2 - len(entry) - emoji_count(entry) + entry.count("☢")
    text += entry + (" " * space_size)
    if i == len(dict_list[0].keys()) - 1:
      text += "\n"
      i = 0
    else:
      text += "|"
      i+=1
  text += "```"
  return text
