from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

def prediction(lst):
    filename = 'model/predictor.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    pred = model.predict([lst])
    return pred

@app.route('/', methods=['GET', 'POST'])
def index():
    pred = 0
    if request.method == 'POST':
        age = request.form['age']
        gender = request.form['gender']
        income = request.form['income']
        score = request.form['score']
        clicks = request.form['clicks']
        likes = request.form['likes']
        shares = request.form['shares']

        feature_list = []

        #values should input according to the indexes in the saved model
        feature_list.append(int(age))
        feature_list.append(int(income))
        feature_list.append(int(score))
        feature_list.append(int(clicks))
        feature_list.append(int(likes))
        feature_list.append(int(shares))

        gender_list = ['male','female']
        

        def traverse(lst, item):
            for i in lst:
                if i == item:
                    feature_list.append(1)
                else:
                    feature_list.append(0)

        traverse(gender_list, gender)
        

        pred = prediction(feature_list)
        

    return render_template('index.html', pred = pred)

if __name__ == '__main__':
    app.run(debug=True)