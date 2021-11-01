"""
CLI commands and utilities
"""

from sentiment_server import create_app

app = create_app()


def runserver():
    """Run flask application"""
    app.run(debug=True, host="0.0.0.0", port=5000)



if __name__ == '__main__':
    runserver()