"""Main module."""

import string
import random
import ipyleaflet

class Map(ipyleaflet.Map):

    def __init__(self, center=[20, 0], zoom=2, **kwargs) -> None:

        if "scroll_wheel_zoom" not in kwargs:
            kwargs['scroll_wheel_zoom'] = True
  
        super().__init__(center=center, zoom=zoom, **kwargs)
        
        if "layer_control" not in kwargs:
            kwargs["layer_control"] = True

        if kwargs["layer_control"]:
            self.add_layer_control()

        if "fullscreen_control" not in kwargs:
            kwargs["fullscreen_control"] = True

        if kwargs["fullscreen_control"]:
            self.add_fullscreen_control() 

        if "draw_control" not in kwargs:
            kwargs["draw_control"] = True

        if kwargs["draw_control"]:
            self.add_draw_control()

        if "height" not in kwargs:
            self.layout.height = "600px"
        else:
            self.layout.height = kwargs["height"]  




    def add_fullscreen_control(self, position="topleft"):
        """Add afullscreen control to the map.

        Args:
            position (str, optional): kwargs: keyword agrument for the position. Defaults to "topleft".
        """
        fullscreen_control = ipyleaflet.FullScreenControl(position=position)
        self.add_control(fullscreen_control)


    def add_search_control(self, position="topleft", **kwargs):
        """Add a search control to the map.

        Args:
            kwargs: keyword argument to pass to the search control
        """
        if "url" not in kwargs:
            kwargs["url"] = 'https://nominatim.openstreetmap.org/search?format=json&q={s}'


        search_control = ipyleaflet.SearchControl(position=position, **kwargs)
        self.add_control(search_control)


    def add_draw_control(self, **kwargs):
        """Add a draw control to the  map.

        Args:
            kwargs: keyword arguments to pass the draw control.
        """        
        draw_control = ipyleaflet.DrawControl(**kwargs)

        draw_control.polyline =  {
            "shapeOptions": {
                "color": "#6bc2e5",
                "weight": 8,
                "opacity": 1.0
            }
        }
        draw_control.polygon = {
            "shapeOptions": {
                "fillColor": "#6be5c3",
                "color": "#6be5c3",
                "fillOpacity": 1.0
            },
            "drawError": {
                "color": "#dd253b",
                "message": "Oups!"
            },
            "allowIntersection": False
        }
        draw_control.circle = {
            "shapeOptions": {
                "fillColor": "#efed69",
                "color": "#efed69",
                "fillOpacity": 1.0
            }
        }
        draw_control.rectangle = {
            "shapeOptions": {
                "fillColor": "#fca45d",
                "color": "#fca45d",
                "fillOpacity": 1.0
            }
        }

        self.add_control(draw_control)    


    def add_layer_control(self, position="topright"):
        """Add a layer control to the map.

        Args:
        kwargs: Keyword agruments to pass to the layers control
        """
        layer_control = ipyleaflet.LayersControl(position=position)
        self.add_control(layer_control)

        
    def add_tile_layer(self, url, name, attribution="",**kwargs):
        """Add a tile layer to the map.

        Args:
            url (_type_): The url of the tile layer
            name (_type_): The name of the tile layer
            attribution (str, optional): The attribution of the layer. Defaults to "".
        """

        tile_layer = ipyleaflet.TileLayer(
            url=url,
            name=name,
            attribution=attribution,
            **kwargs
        )
        self.add_layer(tile_layer)

    def add_basemap(self, basemap, **kwargs):

        import xyzservices.providers as xyz

        if basemap.lower() == "roadmap":
            url = "http://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z} "
            self.add_tile_layer(url, name= basemap, **kwargs)
        elif basemap.lower() == "hybrid":
            url = "http://mt0.google.com/vt/lyrs=y&hl=en&x={x}&y={y}&z={z}"
            self.add_tile_layer(url, name=basemap, **kwargs)
        elif basemap.lower() == "satellite":
            url = "http://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}"
            self.add_tile_layer(url, name=basemap, **kwargs)
        else:
            try:
                basemap = eval(f"xyz.{basemap}")
                url=basemap.build_url()
                attribution = basemap.attribution
                self.add_tile_layer(url, name=basemap.name, attribution=attribution, **kwargs)
            except:
                raise ValueError(f"Basemap '{Basemap}' not found")       


    def add_geojson(self, data, name="GeoJSON", style=None, **kwargs):

        if isinstance(data, str):
            import json
            with open (data, "r") as f:
                data = json.load(f)

        if style is None:
            
            style = {
                "stroke": True,
                "color": "#000000",
                "weight": 2,
                "opacity": 1,
                "fill": True,
                "fillColor": "#0000ff",
                "fillOpacity": 0.4,
            }        

        geojson = ipyleaflet.GeoJSON(data=data, name=name, style=style, **kwargs)
        self.add_layer(geojson)

    def add_shp(self, data, name="Shapefile", style=None, **kwargs):

        import geopandas as gpd
        gdf = gpd.read_file(data)
        geojson = gdf.__geo_interface__
        self.add_geojson(geojson, name=name, style=style, **kwargs)


        
 
    














def generate_random_string(length=10, upper=False, digits=False, punctuation=False ):
    """Generate a random string of given length

    Args:
        length (int, optional): The length of the string to generate. Defaults to 10.
        upper (bool, optional): Whether to include uppercase letters. Defaults to False.
        digits (bool, optional): Whether to include lowercase letters. Defaults to False.
        punctuation (bool, optional): Whether to include pounctuation. Defaults to False.

    Returns:
        _type_: The generated string
    """    
    letters = string.ascii_lowercase
    if upper:
        letters += string.ascii_uppercase
    if digits:
        letters += string.digits
    if punctuation:
        letters += string.punctuation 
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str 


def generate_lucky_number(length=1):
    """Generate a random number of given length

    Args:
        length (int, optional): The length of the number to generate. Defaults to 1.

    Returns:
        _type_: the generated numbers
    """    
    result_str = '' .join(random.choice(string.digits) for i in range(length))
    return int(result_str)
