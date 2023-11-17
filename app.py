from flask import Flask, jsonify, request

app = Flask(__name__)

animes = [{
        "id" : 1,
        "titulo" : "One Piece",
        "poster" : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTg8qsxd8TVLcD6T5KBIDive3PbgPGg7tJvJA&usqp=CAU", 
        "categoria" : "Pelea", 
        "rating" : 9.7, 
        "reviews" : 4568, 
        "season" : "Summer 2023", 
        "tipo" : "Shonen"}, 
     { 
        "id" : 2,
        "titulo" : "Fullmetal Alchemist",
        "poster" : "https://m.media-amazon.com/images/M/MV5BMmI5NmFlZjItOTBhOC00NGI0LWIyNDAtODJhOTJjZDEyMTYyXkEyXkFqcGdeQXVyNjAwNDUxODI@._V1_.jpg", 
        "categoria" : "Aventura", 
        "rating" : 9.9, 
        "reviews" : 3678, 
        "season" : "Winter 2016",
        "tipo" : "Shonen" 
        },
     {
        "id" : 3,
        "titulo" : "Rent A Girlfriend",
        "poster" : "https://infoliteraria.com/wp-content/uploads/2022/09/kanokari2_teaser.jpg.webp", 
        "categoria" : "Comedia Romantica", 
        "rating" : 6.8, 
        "reviews" : 1345,
        "season" : "Autumn 2022",
        "tipo" : "Harem" 
        }
     ]

@app.route("/")
def index():
    return "Hola, bienvenido Animelist!"

@app.route("/anime")
def anime_list():
    return jsonify(animes)

@app.route("/anime/<int:id>")
def create_anime(id):
    anime_found = [anime for anime in animes if anime['id'] == id]
    if (len(anime_found) > 0):
        return jsonify({"id" : anime_found[0]})
    return jsonify({"message" : "Anime not found :c"})

@app.route("/anime", methods = ['POST'])
def addAnime():
    new_anime = {

        "id" : request.json['id'],
        "titulo" : request.json['titulo'],
        "poster" : request.json['poster'], 
        "categoria" : request.json['categoria'], 
        "rating" : request.json['rating'], 
        "reviews" : request.json['reviews'],
        "season" : request.json['season'],
        "tipo" : request.json['tipo'] 
    }
    animes.append(new_anime)
    return jsonify({"message: " : "Anime Added Succesfully"})

@app.route("/anime/<int:id>", methods = ['DELETE'])
def deleteAnime(id):
    anime_found = [anime for anime in animes if anime['id'] == id]
    if (len(anime_found) > 0):
        animes.remove(anime_found[0])
        return jsonify({"message" : "Anime Deleted Succesfully"})
    return jsonify({"message" : "Anime not found :c"})

@app.route("/anime/<int:id>", methods = ['PUT'])
def updateCAnime(id):    
    anime_found = [anime for anime in animes if anime['id'] == id]
    if (len(anime_found) > 0):
        anime_found[0]['id'] = request.json['id']
        anime_found[0]['titulo'] = request.json['titulo']
        anime_found[0]['poster'] = request.json['poster']
        anime_found[0]['categoria'] = request.json['categoria']
        anime_found[0]['rating'] = request.json['rating']
        anime_found[0]['reviews'] = request.json['reviews']
        anime_found[0]['season'] = request.json['season']
        anime_found[0]['tipo'] = request.json['tipo']
        return jsonify({"message" : "Anime Updated"})
    return jsonify({"message" : "Anime not found :c"})

@app.route("/anime/<int:id>", methods = ['PATCH'])
def updatePAnime(id):

    anime_found = [anime for anime in animes if anime['id'] == id]
        
    if (len(anime_found) == 0):
        return jsonify({"message" : "Anime not found :c"})

    anime = anime_found[0]
    patch_data = request.json
    
    for field, value in patch_data.items():
        if field in anime:
            anime[field] = value

    return jsonify({"message" : "Anime Updated"})
        
if __name__ == "__main__":
    app.run(debug=True)