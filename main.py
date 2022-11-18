import json
import pypostalwin


def get_json_address(address: "string") -> "string":
    try:
        parser = pypostalwin.AddressParser()
        parsed_address = parser.runParser(address)
    except Exception:
        return {'street': "", 'housenumber': ""}

    street = ""
    housenumber = ""
    for info in parsed_address:
        if info.keys().__contains__('road'):
            street_lowercase = info['road']
            index_original_street = address.lower().find(street_lowercase)
            street = address[index_original_street: index_original_street + len(street_lowercase)]
        elif info.keys().__contains__('house_number'):
            housenumber_lowercase = info['house_number']
            index_original_housenumber = address.lower().find(housenumber_lowercase)
            housenumber = address[index_original_housenumber: index_original_housenumber + len(housenumber_lowercase)]

    return json.dumps({'street': street, 'housenumber': housenumber})

print(get_json_address("Auf der Vogelwiese 23 b"))