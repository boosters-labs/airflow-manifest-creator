import sys
from urllib.parse import quote

# usage
# python3 amc.py $id $pw

id = sys.argv[1]
pw = sys.argv[2]

r = f'http://{quote(id)}:{quote(pw)}@'

print(r)
