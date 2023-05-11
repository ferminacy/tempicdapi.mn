from flask import Flask, request
import pandas as pd

df = pd.read_csv('./data/diagnosess2019.csv')

# df['payer'].value_counts()
# df.columns
# df['principal_diagnosis_code'].value_counts()

app = Flask(__name__)
@app.route('/', methods=["GET"])
def home():
    return 'this is an API service for MN details'

@app.route('/preview', methods=["GET"])
def preview():
    top10rows = df.head(10)
    result = top10rows.to_json(orient="records")
    return result

@app.route('/payer/<value>', methods=['GET'])
def payer(value):
   # filter_value = request.args.get(icdcode)
    filtered = df[df['payer'] == value]
  #  result = filtered.to_json(orient="records") 
    return filtered.to_json(orient="records") 

@app.route('/payer/<value>/sex/<value2>')
def payer2(value, value2):
    filtered = df[df['payer'] == value]
    filtered2 = filtered[filtered['sex'] == value2]
    return filtered2.to_json(orient="records")

if __name__ == '__main__':
    app.run(debug=True)