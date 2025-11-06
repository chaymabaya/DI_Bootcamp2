brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}
brand["number_stores"] = 2
print(brand["number_stores"])
print (f"zara propose des vetement pour {brand["type_of_clothes"] })")
brand.update({"country_creation" : "spain"})
print(brand['country_creation'])
if "international_competitors" in brand:
    brand ["international_competitors"].append("Desigual ")
brand.pop("creation_date")
print( "creation_date" in brand)
print(brand["international_competitors"][-1])
print (brand["major_color"]["US"])
print(len(brand.keys()))
print(brand.keys())