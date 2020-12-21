class Html():
    def __init__(self, head="", body=""):
        self.output = f"""<!DOCTYPE html>
<html>
{head}
{body}
</html>"""
    def generate(self):
        return self.output
class Head():
     def __new__(self, code=""):
        return f"""<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
{code}
</head>"""
class Body():
    def __new__(self, code=""):
        return f"""<body>
{code}
</body>"""

class Title():
    def __new__(self,text=""):
        return f"<title>{text}</title>"
class Paragraph():
    def __new__(self, text=""):
        return f"<p>{text}</p>"
class Br():
    def __new__(self):
        return "<br>"
class Heading():
    def __new__(self,text,number):
        return f"<h{number}>{text}</h{number}>"
class Image():
    def __new__(self,link,width="",height=""):
        return f'<img src="{link}" width="{width}" height="{height}" >'
class Audio():
    def __new__(self,link):
        return f"""<audio controls="">
        <source src="{link}" type="audio/mpeg">
    </audio>"""
class Video():
    def __new__(self,link,width="",height=""):
        return f"""<video controls="" width="{width}" heigth="{height}">
        <source src="{link}">
    </video>"""
class Input():
    def __new__(self,text):
        return f'<input placeholder="{text}">'
class Textarea():
    def __new__(self, text):
        return f'<textarea placeholder="{text}"></textarea>'
class Ordered_list():
    def __new__(self,elements):
        list ='<ol>' +"""
"""

        for i in range(elements):
            print("Enter ", i + 1, " element of ordered list")
            data = str(input())
            list = list + f"       <li>{data}</li>" + """
"""

        list = list + "    </ol>"
        return list
class Unordered_list():
    def __new__(self,elements):
        list = '<ul>' + """
"""

        for i in range(elements):
            print("Enter ", i + 1, " element of unordered list")
            data = str(input())
            list = list + f"       <li>{data}</li>" + """
"""

        list = list + "    </ul>"
        return list
class Strong():
    def __new__(self,text):
        return f"<strong>{text}</strong>"
class Small():
    def __new__(self,text):
        return f"<small>{text}</small>"
class Emphasized():
    def __new__(self,text):
        return f"<em>{text}</em>"
class Anchor():
    def __new__(self, link,text):
        return f'<a href="{link}" target="_blank">{text}</a>'

page=Html(Head(f'    {Title("Html Project")}'),Body(f'''    {Heading("Heading of project",1)}
    {Heading("Small heading of project",6)}
    {Paragraph("Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1 Text 1")}
    {Paragraph("Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2 Text 2")}
    {Heading("Image of natural",3)}
    {Image("https://s1.1zoom.me/big3/640/Scenery_Mountains_Lake_Grasslands_Canada_Banff_512435_5071x3343.jpg",400,350)}
    {Heading('Song "Перемен"',3)}
    {Audio("Хлам/music.mp3")}
    {Br()}
    {Heading("Enter's field",3)}
    {Input("Search...")}
    {Br()}
    {Br()}
    {Textarea("Enter your impressions...")}
    {Heading("Lists",3)}
    {Ordered_list(3)}
    {Br()}
    {Br()}
    {Unordered_list(3)}
    {Heading("Strings",3)}
    {Strong("Strong string")}
    {Br()}
    {Br()}
    {Small("Small string")}
    {Br()}
    {Br()}
    {Emphasized("Emphasized string")}
    {Heading("Anchor",3)}
    {Anchor("https://docs.google.com/spreadsheets/d/1Kb4GUd7eCAL-PyjazXGn95UHLBDz1a23cf6zxh6GEaI/edit#gid=223114605","Google docs: 2020-fall-cs-students")}
    {Heading("Nested tags",3)}
    {Paragraph(Emphasized(Strong("This is emphasized and strong text")))}
    {Paragraph(f"This is {Small('small')} and {Small(Strong('small-strong'))} text")}
    {Paragraph("This is customs text")}
    {Heading("Video of ending project",3)}
    {Video("Хлам/video.mp4",500)}'''))

html = open("page.html", "w+", encoding="utf-8")
html.write(page.generate())
html.close()
import webbrowser
webbrowser.open("C:/Users/vadim/PycharmProjects/pythonProject1/page.html")