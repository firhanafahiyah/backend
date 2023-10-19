negara = ("korea selatan", "tiongkok", "mongolia", "prancis")
print(negara)

# convert variabel tuple menjadi list
country = list(negara)

# menambahkan,menghapus & menghapus data
country[0] = "korea utara"
country.append("taiwan")
country.remove("prancis")
negara = tuple(country)

# convert variabel list menjadi tuple
negara = tuple(country)


print(type(negara))