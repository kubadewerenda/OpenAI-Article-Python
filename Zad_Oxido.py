import openai
import re

API_KEY="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"

openai.api_key=API_KEY

def file_r(file):
    with open(file,"r",encoding="utf-8") as file:
        return file.read()

def file_s(content,file):
    with open(file,"w",encoding="utf-8") as file:
        file.write(content)

def html_struct():
    html_str="""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="index.css" >
    </head>
    <body>
                    
    </body>
    </html>
    """
    return html_str

def join_html(file_article,file_szablon):
    article_cnt=file_r(file_article)
    szablon_cnt=file_r(file_szablon)

    with open("podglad.html","w",encoding="utf-8") as file:
        file.write(szablon_cnt.replace("<body>",f"<body>\n{article_cnt}"))

def find_tags(file):
    with open(file, "r", encoding="utf-8") as file:
        content=file.read()

    tags=re.findall(r'</?(\w+)', content)

    return set(tags)

def get_response(prompt):
    response=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "user", "content": prompt}
            ]
    )

    return response.choices[0].message['content'].strip()

def OpenAiArticle():
    prompts=[]

    #------CZĘŚĆ 1
    artykul_text=file_r("Zadanie dla JJunior AI Developera - tresc artykulu.txt")
    prompts.append(f"""Przekształć poniższy artykuł na HTML. Użyj odpowiednich tagów HTML do strukturyzacji treści.
        Koniecznie znajdz miejsca, gdzie warto dodać grafiki, i obowiązkowo musisz wstawić w te miejsca <img src='image_placeholder.jpg' alt='opisz grafikę'/>
        oraz dodaj podpis pod grafiką(uzywajac odpowiedniego tagu html do podpisu zdjec)-to polecenie jest wymaganym warunkiem. Wygeneruj tylko kod do sekcji <body> i </body>,nie dodawaj znaczników <html>, <head> ani <body>
        to co ma być w body daj w znaczniku <article>.Przed odpowiedzeniem mi upewnij się,że napewno umieściłes gdzies zdjęcia <img>
        Artykuł:{artykul_text}""" )
    
    artykul_content=get_response(prompts[0])
    file_s(artykul_content,"artykul.html")

    #-----CZĘŚĆ DODATKOWA
    file_s(html_struct(),"szablon.html")
    tags=find_tags("artykul.html")

    prompts.append(f"""Wygeneruj mi zawartość pliku index.css, w ktorym znajdzie się zawaansowane formatowanie dla strony www,
        dodanie animacji(w stylu np.wolnego pojawiania się/wchodzenia od boku) oraz background-color  dla sekcji body i article wraz 
        z animowanym np.optacity,moga byc rowniez jakies border-radiusy. W przypadku animacji staraj sie kozystac z  @KeyFrames. Dodaj margin-left i margin-right po 20px.
        Fajnie jakby nagłowki np.h1 były wycentrowane i lepiej widoczne. pewnij się ze napewno wszystko działa.
        Tutaj masz tagi html pod które masz napisać kod:{tags}.Pamietaj,że nie może być nic wiecej niż kodu css.""")
    
    index_content=get_response(prompts[1])
    file_s(index_content,"index.css")

    join_html("artykul.html","szablon.html")

OpenAiArticle()

