def should_I_put_shorts_on(temp):
    if temp > 20:
        return "It's a day for shorts"
    return "Nah, it's too cold for that"

print(should_I_put_shorts_on(20))

temperatures = [1, 21, 30, 100, 10]
shorts_weather = [21]

for i in temperatures:
    if shorts_weather < temperatures:
        print("Wear shorts")
    else:
        print("Wear trousers")

#there are problems with this.
# I'd like a readout of each element in temperatures read against trousers
#
# #self note:
# # become rock solid on for [] start
# # rehash lists and tuples.
