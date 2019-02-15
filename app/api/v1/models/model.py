import json
parties = []


class Party:
    """class to hold party object"""

    def __init__(self):
        self.db = parties

    def save(self, name, hqaddress, logoUrl):

        party = {
            "id": len(self.db)+1,
            "name": name,
            "hqaddress": hqaddress,
            "logoUrl": logoUrl,
        }
        self.db.append(party)
        return self.db

    def get_all_parties(self):
        return self.db

    # def update(self, data):
    #     for key in data:
    #         setattr(self, key, data[key])
    #     setattr(self)
    #     return self.view()
    #
    def delete(self, name):
        party = {
            "name": name,
        }

        self.db.append(party)
        return self.db
    #

    #
    # @staticmethod
    # def get_party_by_name(cls, name):
    #     for name in parties.name:
    #         party = parties.get(name)
    #         if parties.name == name:
    #             return parties
    #     return None
