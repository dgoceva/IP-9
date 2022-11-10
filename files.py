import json
import csv

STRING = 'Sed tempus odio sed pharetra maximus. \
    Interdum et malesuada fames ac ante ipsum primis in faucibus. Proin rhoncus purus at nisi varius sagittis. Pellentesque suscipit consectetur scelerisque. Donec at arcu elit. Vivamus urna turpis, lacinia at commodo vitae, maximus a nulla. Pellentesque interdum sed urna nec auctor. Donec tincidunt efficitur fermentum. Mauris pretium, lectus nec pretium pellentesque, diam felis consequat turpis, nec mollis tellus libero in risus. Duis mollis dignissim lobortis. In quis velit ac nisi porttitor dignissim. Donec feugiat rhoncus augue et porttitor. Suspendisse venenatis ut magna auctor condimentum. Sed mattis eros laoreet venenatis facilisis. Praesent commodo eleifend quam quis consequat. Sed tempor enim vitae consectetur hendrerit.'
with open('lorem.txt') as f:
    print(f.read())

with open('lorem.txt') as f:
    for line in f:
        print(line.upper())

with open('lorem.txt', 'a') as f:
    f.write(STRING)

f = open('lorem.txt', 'r')
for line in f.readlines():
    print(line)
f.close()

with open('lorem.txt', 'rb') as f:
    print(f.read())

with open('euro_countries.json') as f:
    data = json.load(f)
# print(type(data), data)
for country in data:
    if country['name'].startswith('B'):
        print(country)

result = []
for country in data:
    if country['code'].startswith('B'):
        # print(country['name'])
        result.append(country)
with open('B_country.json', 'w') as f:
    json.dump(result, f)

with open('euro_countries.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'code'])
    writer.writeheader()
    writer.writerows(data)
