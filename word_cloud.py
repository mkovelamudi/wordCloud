from flask import Flask, request, render_template
import matplotlib.pyplot as pplot
from wordcloud import WordCloud
from io import BytesIO
import base64
import os

app = Flask(__name__, template_folder="templates")
img_folder = "/images"

@app.route('/', methods =["GET", "POST"])
def WORD_CLOUD():
    if request.method == "POST":
        data = request.form.get("test")
        wordcloud = WordCloud(width = 800, height = 800,
                background_color ='black',
                min_font_size = 8).generate(data)                      
        pplot.figure(figsize = (8, 8), facecolor = None)
        pplot.imshow(wordcloud)
        pplot.axis("off")
        pplot.tight_layout(pad = 0)
        temp_file = BytesIO()
        pplot.savefig(temp_file, format='png')
        encoded = base64.b64encode(temp_file.getvalue()).decode('utf-8')
        return render_template("image.html", img=encoded)
    return render_template("word_cloud.html")
if __name__=='__main__':
   app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))