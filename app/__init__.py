from flask import Flask
from flask import render_template, url_for
from redis import Redis
from app.common.app_logger import AppLogger
from app.common.routes import bp_data

logger = AppLogger().get_logger()

app = Flask(__name__,
            static_url_path='',
            static_folder="static")
app.register_blueprint(bp_data)



# redis = Redis(host='redis', port=6379, decode_responses=True)

@app.route('/')
@app.route('/login')
def login():

    # redis.incr('hits')
    # counter = str(redis.get('hits'),'utf-8')

    logger.info("Got the login page.")
    return render_template("login.html")
    # return "skndasoidaoidoiajdmapmdoipasmd"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

@app.route('/index')
def index():

    return render_template("index.html")