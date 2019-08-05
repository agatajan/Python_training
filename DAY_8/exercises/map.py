import folium
from folium.plugins import MarkerCluster

coordinates = [54.34632, 18.649246]

bikes_map = folium.Map(location=coordinates)
#bikes_cluster = MarkerCluster()

bike_icon = folium.Icon(icon='bicycle', prefix='fa', color="green")
bike_info = 'Stary romet'

bike_marker = folium.Marker(location=coordinates, popup=bike_info, icon=bike_icon)
#bikes_cluster.add_child(bike_marker)

bikes_map.add_child(bike_marker)
bikes_map.save('bikes_map.html')