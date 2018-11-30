import folium
locations = [
    [38.366667 , 20.716667] ,
    [38.366667 , 20.716667 , 'Ithaca, home of Odysseus'],
    [33.8, 10.925 , 'Land of the Lotus Eaters (modern-day Djerba)'],
    [37.755, 14.995 , 'Land of the Laestrygonians and the  Cyclops'],
    [39.9575, 26.238889 , 'Troy'],
    [38.245833, 15.6325 , 'Scylla and the Charybdis'],
    [40.845, 14.258333, 'The Sirens'],
    [41.045278, 29.034444, 'The Cimmerians']
    ]

def map_it(locations):
    tip = 'Click on me'
    m = folium.Map(location = locations[0])
    for loc in locations[1:]:
        folium.Marker([loc[0], loc[1]], popup=loc[2], tooltip=tip).add_to(m)
    return m

m = map_it(locations)
m.save('odyssey')
