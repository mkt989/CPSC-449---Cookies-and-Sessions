from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    # Retrieve the existing search history from the 'search_history' cookie
    search_history = request.cookies.get('search_history', '').split(',')
    
    return f"Search History: {', '.join(search_history)}"

@app.route('/search/<term>')
def search(term):
    # Retrieve the existing search history from the 'search_history' cookie
    search_history = request.cookies.get('search_history', '').split(',')
    
    # Append the new search term to the search history
    search_history.append(term)
    
    # Join search history into a comma-separated string and set it as a cookie
    response = make_response(f"Search Term: {term}")
    response.set_cookie('search_history', ','.join(search_history))
    
    return response

if __name__ == '__main__':
    app.run()
