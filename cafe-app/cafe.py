class Cafe:
    def __init__(self, name, district, map_link):
        self.name = name
        self.district = district
        self.map_link = map_link

    def to_dict(self):
        return {
            "name": self.name,
            "district": self.district,
            "map_link": self.map_link,
        }
