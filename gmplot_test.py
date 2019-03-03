from gmplot import gmplot

# place map
gmap = gmplot.GoogleMapPlotter( 34.10524, -117.29412, 12.85)

# polygon
csusb_lats, csusb_lons = zip(*[
    (34.178811, -117.326755),
    (34.178162, -117.318885),
    (34.179274, -117.313970),
    (34.184890, -117.320197),
    (34.1834, -117.3205),
    (34.178811, -117.326755),
    (32.490934, -96.95320459999999)
    ])
gmap.polygon(csusb_lats, csusb_lons, "cornflowerblue", size=40, marker = True)

# marker
my_loc =[34.11, -117.19]
gmap.marker(my_loc[0], my_loc[1], 'cornflowerblue')
gmap.marker(34.178811, -117.326755, 'cornflowerblue')
print(my_loc[0])



# Draw
gmap.draw("my_map.html")


##gmap.draw("my_map2.html")
