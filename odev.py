from logic import *

people = ["Ali", "Ayse", "Ahmet", "Mehmet", "Metin"]
cities = ["Izmir", "Ankara", "Bursa", "Balikesir", "Istanbul"]
symbols = {person: Symbol(person) for person in people}
locations = {city: Symbol(city) for city in cities}


knowledge = And(
    # Each person lives in a different city
    And([Or(symbols[person] == locations[city] for city in cities) for person in people]),
    
    
    Or(symbols["Ali"] == locations["Izmir"], symbols["Ayse"] == locations["Izmir"]),
  
    Not(symbols["Ahmet"] == locations["Ankara"]),
 
    symbols["Metin"] == locations["Istanbul"],
 
    Or(symbols["Mehmet"] == locations["Bursa"], symbols["Ali"] == locations["Bursa"])
)

possible_cities_for_Ahmet = [city for city in cities if model_check(knowledge, symbols["Ahmet"] == locations[city])]

print(f"Ahmet could live in: {', '.join(possible_cities_for_Ahmet)}")
