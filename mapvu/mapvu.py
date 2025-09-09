"""Main module."""

import string
import random
import ipyleaflet

class Map(ipyleaflet.Map):

    def __init__(self, center, zoom, **kwargs):
        if "scroll_wheel_zoom" not in kwargs:
            kwargs['scroll_wheel_zoom'] = True

        print(kwargs)   
        super().__init__(center=center, zoom=zoom, **kwargs)

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
