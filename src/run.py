from bookshelf import app
import os

env = os.environ['FLASK_ENV'] or 'development'

if env == "development":
	app.config.update(
		TESTING=True,
		FLASK_DEBUG=True
	)

if __name__ == '__main__':
    app.run() 