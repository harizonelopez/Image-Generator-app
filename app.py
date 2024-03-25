
from flask import Flask, render_template
import requests

app = Flask(__name__)
app.secret_key = 'aladinh00-01montext'

def get_random_image():
    url = "https://api.unsplash.com/photos/random?client_id=-IFMpEhqG-4N4zuvG4MGoxgsk727kFry9zDIjGqHm0I"

    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
        image_url = data.get("urls", {}).get("regular")
        return image_url
    
    except Exception as e:
        print(f"Error fetching meme: {e}")
        
        return None

@app.route('/')
def home():
    image_url =  get_random_image()
    return render_template("home.html", image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)
