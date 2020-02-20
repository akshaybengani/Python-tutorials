import http.client

conn = http.client.HTTPSConnection("movie-database-imdb-alternative.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
    'x-rapidapi-key': "76548df5a4msh7fb56fc2794b204p1d3423jsn99afe8e6de92"
    }

#conn.request("GET", "/?i=tt0120738&r=json", headers=headers)
conn.request("GET", "/?page=1&r=json&s=Lost%20in%20space", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
#


#  
# OkHttpClient client = new OkHttpClient();

# Request request = new Request.Builder()
# 	.url("https://movie-database-imdb-alternative.p.rapidapi.com/?page=1&r=json&s=Netflix")
# 	.get()
# 	.addHeader("x-rapidapi-host", "movie-database-imdb-alternative.p.rapidapi.com")
# 	.addHeader("x-rapidapi-key", "97afa4fe4cmshf820e5ee680627dp14749ejsne28f58363423")
# 	.build();

# Response response = client.newCall(request).execute();