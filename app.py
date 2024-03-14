from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB Atlas
client = MongoClient('mongodb+srv://username:password@cluster5.xdjzlt2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster5')
db = client.get_database()  # Replace with your database name
collection = db['collectionname']  # Replace with your collection name

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/data')
def get_filtered_data():
    # Get filter parameters from request
    end_year = request.args.get('Year')
    likelihood = request.args.get('Likelihood')
    relevance = request.args.get('Relevance')
    topics = request.args.get('Topics')
    sector = request.args.get('Sector')
    region = request.args.get('Region')
    pest = request.args.get('PEST')
    source = request.args.get('Source')
    swot = request.args.get('SWOT')
    country = request.args.get('Country')
    city = request.args.get('City')
    # Add more filters as needed

    # Construct MongoDB query based on filter parameters
    query = {}
    if end_year:
        query['Year'] = {'$lte': int(end_year)}
    if likelihood:
        query['Likelihood'] = likelihood
    if relevance:
        query['Relevance'] = relevance
    if topics:
        query['Topics'] = topics
    if sector:
        query['Sector'] = sector
    if region:
        query['Region'] = region
    if pest:
        query['PEST'] = pest
    if source:
        query['Source'] = source
    if swot:
        query['SWOT'] = swot
    if country:
        query['Country'] = country
    if city:
        query['City'] = city
    # Add more conditions for other filters

    # Retrieve filtered data from MongoDB collection
    data = list(collection.find(query, {'_id': 0}))

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
