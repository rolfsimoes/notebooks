import folium
import vincent
import pandas

def createTSMap(pos, timeSeries, zoom_start = 4.0):
    #map = folium.Map(location=[pos['lat'], pos['lon']], zoom_start = 4,crs = 'EPSG4326') # Forces EPSG4326 to make MOD13A2_M_NDVI work
    map = folium.Map(location = [pos['lat'], pos['lon']], zoom_start = zoom_start)

    df = timeSeries;
    df.index = df.index.values.astype('M8[D]')
    chart = vincent.Line(df[['evi','ndvi']], width = 300, height = 150)
    chart.legend(title = '')
    chart.axis_titles(x = 'dates', y = '')

    popup = folium.Popup(max_width = 400)
    folium.Vega(chart.to_json(), height = 200, width = 450).add_to(popup)
    folium.Marker([pos['lat'], pos['lon']], popup = popup, icon = folium.Icon(color = 'green', icon = 'info-sign')).add_to(map)

    #wms = folium.features.WmsTileLayer('https://neo.sci.gsfc.nasa.gov/wms/wms',
    #                                   name='MODIS Data',
    #                                   format='image/png',
    #                                   layers='MOD13A2_M_NDVI')
    #wms.add_to(map)
    return map
