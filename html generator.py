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
    def title(self,text):
        index=self.base.find("</head>")
        self.base=self.base[:index]+"    <title>{}</title>".format(text)+"""
"""+self.base[index:]
    def paragraph(self,text):
        index = self.base.find("</body>")
        self.base = self.base[:index] + "    <p>{}</p>".format(text) + """
""" + self.base[index:]
    def br(self):
        index = self.base.find("</body>")
        self.base = self.base[:index] + "    <br>"+ """
""" + self.base[index:]
    def heading(self,text,number):
        index = self.base.find("</body>")
        self.base = self.base[:index] + "    <h{}>{}</h{}>".format(str(number),text,str(number)) + """
""" + self.base[index:]
    def image(self,link,width="",height=""):
        index = self.base.find("</body>")
        self.base = self.base[:index] + '    <img src="{}" width="{}" height="{}" >'.format(link,str(width),str(height)) + """
""" + self.base[index:]
    def audio(self,link):
        index = self.base.find("</body>")
        self.base = self.base[:index] + '    <audio controls="">'+"""
        """+'<source src="{}" type="audio/mpeg">'.format(link) + """
    </audio>""" + """
"""+self.base[index:]
    def video(self,link,width="",height=""):
        index = self.base.find("</body>")
        self.base = self.base[:index] + '    <video controls="" width="{}" heigth="{}">'.format(str(width),str(height)) + """
        """ + '<source src="{}">'.format(link) + """
    </video>""" + """
""" + self.base[index:]
    def input(self,text):
        index = self.base.find("</body>")
        self.base = self.base[:index] + '    <input placeholder="{}">'.format(text) + """
""" + self.base[index:]
    def textarea(self, text):
        index = self.base.find("</body>")
        self.base = self.base[:index] + '    <textarea placeholder="{}"></textarea>'.format(text)+"""
 """ + self.base[index:]
    def ordered_list(self,elements):
        index = self.base.find("</body>")
        self.base = self.base[:index] + '   <ol>' +"""
""" + self.base[index:]

        for i in range(elements):
            print("Enter ", i + 1, " element of list")
            data = str(input())
            index = self.base.find("</body>")
            self.base = self.base[:index] + "       <li>{}</li>".format(data) + """
""" + self.base[index:]

        index = self.base.find("</body>")
        self.base = self.base[:index] + "    </ol>" + """
""" + self.base[index:]
    def unordered_list(self,elements):
        index = self.base.find("</body>")
        self.base = self.base[:index] + '    <ul>' +"""
""" + self.base[index:]

        for i in range(elements):
            print("Enter ", i + 1, " element of list")
            data = str(input())
            index = self.base.find("</body>")
            self.base = self.base[:index] + "       <li>{}</li>".format(data) + """
""" + self.base[index:]

        index = self.base.find("</body>")
        self.base = self.base[:index] + "    </ul>" + """
""" + self.base[index:]
    def strong(self,text):
        index=self.base.find("</body>")
        self.base=self.base[:index]+"    <strong>{}</strong>".format(text)+"""
"""+self.base[index:]
    def small(self,text):
        index=self.base.find("</body>")
        self.base=self.base[:index]+"    <small>{}</small>".format(text)+"""
"""+self.base[index:]
    def emphasized(self,text):
        index=self.base.find("</body>")
        self.base=self.base[:index]+"    <em>{}</em>".format(text)+"""
"""+self.base[index:]
    def anchor(self, link,text):
        index = self.base.find("</body>")
        self.base = self.base[:index] + '    <a href="{}" target="_blank">{}</a>'.format(link,text)+"""
 """ + self.base[index:]

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

html = open("page.html", "w+", encoding="utf-8")
html.write(page.base)
html.close()
import webbrowser
webbrowser.open("C:/Users/vadim/PycharmProjects/pythonProject1/page.html")