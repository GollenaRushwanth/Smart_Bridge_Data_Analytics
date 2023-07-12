# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def home():
#     tableau_link = "https://public.tableau.com/views/Wallmart_Sales_Story1/FinalStory?:language=en-US&:display_count=n&:origin=viz_share_link"  # Replace with your Tableau Public link
#     return render_template('index.html', tableau_link=tableau_link)

# if __name__ == '__main__':
#     app.run()

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/tableau_dashboard')
def tableau_dashboard():
    return render_template('index.html')

@app.route('/tableau_story')
def tableau_story():
    return render_template('index1.html')

if __name__ == '__main__':
    app.run(debug=True)