'''
Exercise 4.5
Print the values of name, post_code and street_number from the dictionary
Extension: Print the values of longitude and latitude from the inner dictionary
'''
place = {
'name': 'The Anchor',
'post_code': 'E14 6HY',
'street_number': '54',
'location': {
'longitude': 127,
'latitude': 63,
}
}

print(place['name'])
print(place['post_code'])
print(place['street_number'])

location = place['location']
print(location['longitude'])
print(location['latitude'])
 