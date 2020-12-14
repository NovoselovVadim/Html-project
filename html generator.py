class Document:
    def __init__(self):
        self.base = """<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
<body>
</body>
</html>
"""
        base=self.base
        self = open("page.html", "w+", encoding="utf-8")
        self.write(base)
        self.close()
    def title(self,text):
        self.text=text
        index=self.base.find("</head>")
        self.base=self.base[:index]+"    <title>"+self.text+"</title>"+"""
"""+self.base[index:]
        base=self.base
        self = open("page.html", "w+", encoding="utf-8")
        self.write(base)
        self.close()
    def paragraph(self,text):
        self.text = text
        index = self.base.find("</body>")
        self.base = self.base[:index] + "    <p>" + self.text + "</p>" + """
""" + self.base[index:]
        base = self.base
        self = open("page.html", "w+", encoding="utf-8")
        self.write(base)
        self.close()
    def br(self):
        index = self.base.find("</body>")
        self.base = self.base[:index] + "    <br>"+ """
""" + self.base[index:]
        base = self.base
        self = open("page.html", "w+", encoding="utf-8")
        self.write(base)
        self.close()
    def heading(self,text,number):
        self.number = number
        self.text = text
        index = self.base.find("</body>")
        self.base = self.base[:index] + "    <h"+str(self.number)+">" + self.text + "</h"+str(self.number)+">" + """
""" + self.base[index:]
        base = self.base
        self = open("page.html", "w+", encoding="utf-8")
        self.write(base)
        self.close()
    def image(self,link,width="",height=""):
        self.link=link
        self.width=width
        self.height=height
        index = self.base.find("</body>")
        self.base = self.base[:index] + '    <img src="'+self.link+'" width="'+str(self.width)+'" height="'+str(self.height)+'" >' + """
""" + self.base[index:]
        base = self.base
        self = open("page.html", "w+", encoding="utf-8")
        self.write(base)
        self.close()
    def audio(self,link):
        self.link = link
        index = self.base.find("</body>")
        self.base = self.base[:index] + '    <audio controls="">'+"""
        """+'<source src="' + self.link +'" type="audio/mpeg">' + """
    </audio>""" + """
"""+self.base[index:]
        base = self.base
        self = open("page.html", "w+", encoding="utf-8")
        self.write(base)
        self.close()
    def video(self,link,width="",height=""):
        self.link = link
        self.width = width
        self.height = height
        index = self.base.find("</body>")
        self.base = self.base[:index] + '    <video controls="" width="'+str(self.width)+'" heigth="'+str(self.height)+'">' + """
        """ + '<source src="' + self.link + '">' + """
    </video>""" + """
""" + self.base[index:]
        base = self.base
        self = open("page.html", "w+", encoding="utf-8")
        self.write(base)
        self.close()
    def input(self,text):
        self.text = text
        index = self.base.find("</body>")
        self.base = self.base[:index] + '    <input placeholder="' + self.text + '">' + """
""" + self.base[index:]
        base = self.base
        self = open("page.html", "w+", encoding="utf-8")
        self.write(base)
        self.close()
    def textarea(self, text):
        self.text = text
        index = self.base.find("</body>")
        self.base = self.base[:index] + '    <textarea placeholder="' + self.text + '">' + '</textarea>'+"""
 """ + self.base[index:]
        base = self.base
        self = open("page.html", "w+", encoding="utf-8")
        self.write(base)
        self.close()
    def ordered_list(self,elements):
        self.elements=elements
        index = self.base.find("</body>")
        self.base = self.base[:index] + '   <ol>' +"""
""" + self.base[index:]

        for i in range(elements):
            print("Enter ", i + 1, " element of list")
            data = str(input())
            index = self.base.find("</body>")
            self.base = self.base[:index] + "       <li>" + data + "</li>" + """
""" + self.base[index:]

        index = self.base.find("</body>")
        self.base = self.base[:index] + "    </ol>" + """
""" + self.base[index:]
        base = self.base
        self = open("page.html", "w+", encoding="utf-8")
        self.write(base)
        self.close()
    def unordered_list(self,elements):
        self.elements=elements
        index = self.base.find("</body>")
        self.base = self.base[:index] + '    <ul>' +"""
""" + self.base[index:]

        for i in range(elements):
            print("Enter ", i + 1, " element of list")
            data = str(input())
            index = self.base.find("</body>")
            self.base = self.base[:index] + "       <li>" + data + "</li>" + """
""" + self.base[index:]

        index = self.base.find("</body>")
        self.base = self.base[:index] + "    </ul>" + """
""" + self.base[index:]
        base = self.base
        self = open("page.html", "w+", encoding="utf-8")
        self.write(base)
        self.close()
    def strong(self,text):
        self.text=text
        index=self.base.find("</body>")
        self.base=self.base[:index]+"    <strong>"+self.text+"</strong>"+"""
"""+self.base[index:]
        base=self.base
        self = open("page.html", "w+", encoding="utf-8")
        self.write(base)
        self.close()
    def small(self,text):
        self.text=text
        index=self.base.find("</body>")
        self.base=self.base[:index]+"    <small>"+self.text+"</small>"+"""
"""+self.base[index:]
        base=self.base
        self = open("page.html", "w+", encoding="utf-8")
        self.write(base)
        self.close()
    def emphasized(self,text):
        self.text=text
        index=self.base.find("</body>")
        self.base=self.base[:index]+"    <em>"+self.text+"</em>"+"""
"""+self.base[index:]
        base=self.base
        self = open("page.html", "w+", encoding="utf-8")
        self.write(base)
        self.close()
    def anchor(self, link,text):
        self.link = link
        self.text = text
        index = self.base.find("</body>")
        self.base = self.base[:index] + '    <a href="' + self.link + '" target="_blank">' + self.text + '</a>'+"""
 """ + self.base[index:]
        base = self.base
        self = open("page.html", "w+", encoding="utf-8")
        self.write(base)
        self.close()
page=Document()
page.title("Html project")
page.heading("Heading of project",1)
page.heading("Small heading of project",6)
page.paragraph("Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1")
page.paragraph("Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2")
page.heading("Image of natural",3)
page.image("https://s1.1zoom.me/big3/640/Scenery_Mountains_Lake_Grasslands_Canada_Banff_512435_5071x3343.jpg",400,350)
page.heading('Song "Перемен"',3)
page.audio("Хлам/music.mp3")
page.br()
page.heading("Enter's field",3)
page.input("Search...")
page.br()
page.br()
page.textarea("Enter your impressions...")
page.heading("Lists",3)
page.ordered_list(3)
page.br()
page.br()
page.unordered_list(3)
page.heading("Strings",3)
page.strong("Strong string")
page.br()
page.br()
page.small("Small string")
page.br()
page.br()
page.emphasized("Emphasized string")
page.heading("Anchor",3)
page.anchor("https://docs.google.com/spreadsheets/d/1Kb4GUd7eCAL-PyjazXGn95UHLBDz1a23cf6zxh6GEaI/edit#gid=223114605","Google docs: 2020-fall-cs-students")
page.heading("Video of ending project",3)
page.video("Хлам/video.mp4",500)
import webbrowser
webbrowser.open("C:/Users/vadim/PycharmProjects/pythonProject1/page.html")
