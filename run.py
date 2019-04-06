from app import app

# pressed F5 for "Run" this
# pressed Ctrl + S for "Rerun" this
if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=5160,
            debug=True,
            threaded=True)