class Document:
    def html(self,code=""):
        return str(f"""<!DOCTYPE html>
<html>
{code}
</html>""")
    def head(self,code=""):
        return str(f"""<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
{code}
</head>""")
    def body(self,code=""):
        return str(f"""<body>
{code}
</body>""")

    def title(self,text):
        return str(f"<title>{text}</title>")
    def paragraph(self,text):
        return str(f"<p>{text}</p>")
    def br(self):
        return str("<br>")
    def heading(self,text,number):
        return str(f"<h{number}>{text}</h{number}>")
    def image(self,link,width="",height=""):
        return str(f'<img src="{link}" width="{width}" height="{height}" >')
    def audio(self,link):
        return str(f"""<audio controls="">
        <source src="{link}" type="audio/mpeg">
    </audio>""")
    def video(self,link,width="",height=""):
        return str(f"""<video controls="" width="{width}" heigth="{height}">
        <source src="{link}">
    </video>""")
    def input(self,text):
        return str(f'<input placeholder="{text}">')
    def textarea(self, text):
        return str(f'<textarea placeholder="{text}"></textarea>')
    def ordered_list(self,elements):
        list ='<ol>' +"""
"""

        for i in range(elements):
            print("Enter ", i + 1, " element of list")
            data = str(input())
            list = list + f"       <li>{data}</li>" + """
"""

        list = list + "    </ol>"
        return str(list)
    def unordered_list(self,elements):
        list = '<ul>' + """
"""

        for i in range(elements):
            print("Enter ", i + 1, " element of list")
            data = str(input())
            list = list + f"       <li>{data}</li>" + """
"""

        list = list + "    </ul>"
        return str(list)
    def strong(self,text):
        return str(f"<strong>{text}</strong>")
    def small(self,text):
        return str(f"<small>{text}</small>")
    def emphasized(self,text):
        return str(f"<em>{text}</em>")
    def anchor(self, link,text):
        return str(f'<a href="{link}" target="_blank">{text}</a>')

page=Document()
output=page.html(f"""{page.head(f"    {page.title('Html project')}")}
{page.body(f'''    {page.heading("Heading of project",1)}
    {page.heading("Small heading of project",6)}
    {page.paragraph("Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1")}
    {page.paragraph("Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2")}
    {page.heading("Image of natural",3)}
    {page.image("https://s1.1zoom.me/big3/640/Scenery_Mountains_Lake_Grasslands_Canada_Banff_512435_5071x3343.jpg",400,350)}
    {page.heading('Song "Перемен"',3)}
    {page.audio("Хлам/music.mp3")}
    {page.br()}
    {page.heading("Enter's field",3)}
    {page.input("Search...")}
    {page.br()}
    {page.br()}
    {page.textarea("Enter your impressions...")}
    {page.heading("Lists",3)}
    {page.ordered_list(3)}
    {page.br()}
    {page.br()}
    {page.unordered_list(3)}
    {page.heading("Strings",3)}
    {page.strong("Strong string")}
    {page.br()}
    {page.br()}
    {page.small("Small string")}
    {page.br()}
    {page.br()}
    {page.emphasized("Emphasized string")}
    {page.heading("Anchor",3)}
    {page.anchor("https://docs.google.com/spreadsheets/d/1Kb4GUd7eCAL-PyjazXGn95UHLBDz1a23cf6zxh6GEaI/edit#gid=223114605","Google docs: 2020-fall-cs-students")}
    {page.heading("Nested tags",3)}
    {page.paragraph(page.emphasized(page.strong("This is emphasized and strong text")))}
    {page.paragraph(f"This is {page.small('small')} and {page.small(page.strong('small-strong'))} text")}
    {page.paragraph("This is customs text")}
    {page.heading("Video of ending project",3)}
    {page.video("Хлам/video.mp4",500)}''')}""")

html = open("page.html", "w+", encoding="utf-8")
html.write(output)
html.close()
import webbrowser
webbrowser.open("C:/Users/vadim/PycharmProjects/pythonProject1/page.html")