import json

with open("data.json", "r", encoding='utf-8') as data:

    movies = json.load(data)

    print(type(movies))

    final = list()
    for idx, movie in enumerate(movies):
        new = dict()
        new["model"] = "movies.movie"
        new["pk"] = idx+1
        new["fields"] = movie
        final.append(new)

    with open('movies.json', 'w') as fp:
        json.dump(final, fp)