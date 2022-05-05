from mkweb import *
app=WebApp("index.html")
app.setDoctype("html")
app.addelement("body","test")
app.create()