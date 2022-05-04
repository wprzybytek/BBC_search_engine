from flask import Flask, request
from flask_cors import CORS
from os.path import exists
import find_articles
import process_dataset

app = Flask(__name__)
CORS(app)


@app.route('/articles', methods=['POST'])
def get_articles():
    request_data = request.get_data(as_text=True)
    return find_articles.main(request_data), 200, {'ContentType': 'application/json'}


if __name__ == '__main__':
    if not exists('./data/bow.npy') or not exists('./data/words.npy'):
        process_dataset.main()

    app.run()
