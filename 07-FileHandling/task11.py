import array as ar
film_titles = ["film1","film2","film3","film4","film5"]
with open("film.txt", "w") as f:
    for i in range(5):
        f.write(f" {film_titles[i]}\n")
 