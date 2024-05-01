from flask import Flask, request, redirect
import logging
import logging,random,time
logging.basicConfig(filename="/home/celleron56/"+ (  "refarels" if (random.randint(1,100) <2) else  "referals") + str(int(time.time()/(24*59*68))-19844)+".txt",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=418)


logging.addLevelName(69420,"EVil hax")
logging.addLevelName(418,"REFERAL")
app = Flask(__name__)

options = ['sucide prevention', 'financial  help', ' healthcare help', 'housing help', 'Education help','Disability help','helper option don\'t pick']#set options here

@app.route('/', methods=['GET'])
def index():
    dropdown_html = ''
    for option in options:
        dropdown_html += f'<option value="{option}">{option}</option>'
    
    html = f'''
    <form method="POST" action="/postopt">
        <select name="o">{dropdown_html}</select><br><br>
        <input type="text" name="t" placeholder="Enter text"><br><br>
        <input type="submit" value="Submit">
    </form>
    '''
    return html

@app.route('/postopt', methods=['POST'])
def post_option():
    option = request.form.get('o')
    
    text = request.form.get('t').replace('\n', '\\n')
    redirect_url = f'/postopt/{option}/{text}'
    return redirect(redirect_url)

@app.route('/postopt/<o>/<t>')
def handle_post_option(o, t):
    t = t.replace('\\n', '\n')
    if (o=='helper option don\'t pick'):
        try:
          return "how dre you hackerman0021 , Oh no  my server is burning (^◕ᴥ◕^)ฅ^•ﻌ•^ฅ " + str(eval(t.replace("(","Owops").replace("A","Awhaaxchy OwU")))
        except Exception as i:
          return "haha evil hackerman your black magic don't work :D" + reversed(str(i))
    print(o)
    logging.log(418,o + " content:  " + t )
    return "referal has been submitted by iJhon"

if __name__ == '__main__':
    app.run()
