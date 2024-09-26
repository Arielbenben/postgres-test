from flask import Flask
from controllers.target_controller import target_blue_print
from repository.database import create_tables, insert_into_all_tables


app = Flask(__name__)


if __name__ == '__main__':
    # create_tables()
    # insert_into_all_tables()

    app.register_blueprint(target_blue_print, url_prefix="/api/targets")
    app.run(debug=True)