from flask import Flask, jsonify, request
import csv
all_movies=[]

with open("movies.csv") as f:
    reader=csv.reader(f)
    data=list(reader)
    all_movies=data[1:]
    
like_movies=[]
not_liked_movies=[]
unwatched_movies=[]

app=Flask(__name__)
@app.route("/get-movie")
def get_movie():
    return jsonify({
        "data":all_movies[0],
        "status":"success"
    })

@app.route("/like-movie",methods=["POST"])
def like_movies():
    movie=all_movies[0]
    all_movies=all_movies[1:]
    like_movies.append(movie)
    return jsonify({
        "status":"success"
    }),201

@app.route("/unlike-movie",methods=["POST"])
def not_liked_movies():
    movie=all_movies[0]
    all_movies=all_movies[1:]
    not_liked_movies.append(movie)
    return jsonify({
        "stauts":"success"
    }),201

if __name__ =="__main__":
    app.run()
