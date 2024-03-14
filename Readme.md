# Data Visualization Dashboard with Flask and MongoDB

This project is a web-based data visualization dashboard built using Flask as the backend framework and MongoDB as the database. It allows users to filter and visualize data stored in the MongoDB database.

## Features

- **Dashboard Interface**: Users can interact with the data through a web-based dashboard interface.
- **Dynamic Filtering**: Users can filter the data based on various criteria such as Year, Likelihood, Relevance, etc.
- **Data Visualization**: The filtered data is visualized using bar charts, providing users with insights into different aspects of the data.
- **Backend API**: The Flask application serves as a backend API that handles requests for filtered data from the MongoDB database.

## Prerequisites

Before running the project, make sure you have the following installed:

- Python (>=3.6)
- Flask
- pymongo
- MongoDB (running locally or accessible via MongoDB Atlas)

## Installation

1. Clone the repository:

git clone https://github.com/yadavvishal/data-visualization-dashboard.git

2. Install dependencies:
   pip install -r requirements.txt

3. Set up MongoDB:

- Install MongoDB locally or create a MongoDB Atlas account.
- Update the MongoDB connection string in `app.py` to connect to your database.

## Usage

1. Start the Flask application:
   python app.py

2. Access the dashboard in your web browser at `http://localhost:5000`.

3. Use the filters in the dashboard to interact with and visualize the data.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request.
