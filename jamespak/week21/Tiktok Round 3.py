'''
{
  "field1": "val1",
  "field1": "val2"
}
=>
{
  "field1": ["val1", "val2"]
}


{
  "parent1": {
    "field1": "val1",
  },
  "parent1": {
    "field1": "val1-2",
    "field2": "val2",
  }
}
=>
{
  "parent1": {
    "field1": ["val1", "val1-2"],
    "field2": "val2",
  }
}
'''
'''
[("field1", "val1"), ("field1", "val2")]

[("parent1", [("field1", "val1")]), ("parent1", [("field1", "val1-2"), ("field2", "val2")])]
'''

res = defaultdict(list)
def merge_json(data, res):
    
    for d in data:
        if type(d[1]) == str:
            res[d[0]].append(d[1])
        else:
            merge_json(d[1], res)
    
merge_json([("parent1", [("field1", "val1")]), ("parent1", [("field1", "val1-2"), ("field2", "val2")])], res)

"""
CTR focus
10 items

dataset
userId, clicked content's ids, positive content, negative contents, dwell time, purchase, position

clicked: laptop, keyboard
mouse*, headset, printer, chargers
"""

