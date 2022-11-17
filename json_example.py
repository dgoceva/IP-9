import json
from plotly.graph_objects import Layout
from plotly import offline

FNAME = '1.0_day (1).json'
FNAME_OUT = '1.0_day.json'
FNAME_HTML = '1.0_day.html'

with open(FNAME, encoding='utf-8') as f:
    all_data = json.load(f)

# with open(FNAME_OUT, 'w') as f:
#     json.dump(all_data, f, indent=2)

# print(all_data['metadata']['title'])
# print(all_data['features'][0]['properties']['mag'])
# print(all_data['features'][0]['properties']['title'])
# print(all_data['features'][0]['geometry']['coordinates'][0])
# print(all_data['features'][0]['geometry']['coordinates'][1])

mags, lons, lats, texts = [], [], [], []
for line in all_data['features']:
    mags.append(line['properties']['mag'])
    texts.append(line['properties']['title'])
    lons.append(line['geometry']['coordinates'][0])
    lats.append(line['geometry']['coordinates'][1])

# print(mags[:5])
# print(lons[:5])
# print(lats[:5])
# print(texts[:5])

layout = Layout(title=all_data['metadata']['title'])
data = [{
    'type': 'scattergeo',
    'text': texts,
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [5*mag for mag in mags],
        'color':mags,
        'colorscale':'Viridis',
        'reversescale': True,
        'colorbar':{'title': 'Magnitude'},
    }
}]
fig = {
    'data': data,
    'layout': layout,
}
offline.plot(fig, filename=FNAME_HTML)
