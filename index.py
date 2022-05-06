from mkweb import *
app=WebApp("index.html")
app.settitle("mkweb test")
app.setDoctype("html")
app.addelement("body","This is a test website made with mkweb. It is currently not usable, however, it will soon be usable. Thank you.")
app.addelement("p","this is a class test",["red-text"])
app.addelement("style","""
body{
    background-color: lightblue;
}
.red-text{
    color: red
}
""")
app.create()
