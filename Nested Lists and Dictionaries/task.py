#regular dictionary
capitals = {
    "France" : "Paris",
    "Germany" : "Berlin",
}

#List inside dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

#Challenge to print Lille from above
print(travel_log["France"][1])

#Challnge to print letter D from below nested list
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

#Challenge -- print Stuttgart from below nested lists/dictionaries
travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}
print(travel_log["Germany"]["cities_visited"][2])
