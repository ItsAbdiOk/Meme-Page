# Random Meme

## Description
This project is a simple web application that displays random memes fetched from the Reddit API. It uses Flask, a Python web framework, to serve the application and render the meme content on a webpage.
![image](https://github.com/ItsAbdiOk/Meme-Page/assets/91463101/4b9a0eae-000f-4e95-8938-67d46bcedd21)

## Installation

### Clone the repository
```git clone https://github.com/ItsAbdiOk/Meme-Page.git```

### Install dependencies
```pip install -r requirements.txt```

### Obtain credentials
- Create a Reddit developer account and generate a client ID, client secret, and user agent. Fill in the corresponding fields in the `config.py` file.
- (Optional) If you want to use the Unsplash API to fetch random mountain images, obtain an access key and fill in the `UNSPLASH_ACCESS_KEY` field in the `config.py` file.

## Usage

1. Start the Flask development server:

2. Open your web browser and navigate to `http://localhost:80` to view the random meme.

## Project Structure

The project structure is as follows:

- `app.py`: The main Python script that sets up the Flask application and defines the routes.
- `templates/index.html`: The HTML template file that displays the random meme on the webpage.
- `config.py`: Configuration file containing API credentials and other settings.
- `requirements.txt`: A text file listing the required Python dependencies.

## Dependencies

The project relies on the following dependencies:

- Flask: A lightweight web framework for Python.
- praw: A Python wrapper for the Reddit API.
- requests: A library for making HTTP requests.

Install these dependencies using `pip` with the command mentioned in the installation section.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please create a new issue or submit a pull request.

