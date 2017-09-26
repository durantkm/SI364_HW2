## HW 2 
## SI 364 F17
## Due: September 26, 2017
## 500 points
##Kyle Durant

#####

## [PROBLEM 1]

## Edit the following Flask application code so that if you run the application locally and got to the URL http://localhost:5000/question, you see a form that asks you to enter your favorite number. Once you enter a number and submit it to the form, you should then see a web page that says "Double your favorite number is <number>". For example, if you enter 2 into the form, you should then see a page that says "Double your favorite number is 4". Careful about types in your Python code!
## You can assume a user will always enter a number only.

from flask import Flask, request, render_template
app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_to_you():
    return 'Howdy!'

@app.route('/question')
def enter_fav_number():
	return render_template("fav_num_form.html")

@app.route('/doubledresult', methods = ['GET', 'POST'])
def result_doubled():
	if request.method == 'GET':
 		result = request.args
 		return render_template("doubled_fav_num_result.html", result=result)



## [PROBLEM 2]

## Come up with your own interactive data exchange that you want to see happen dynamically in the Flask application, and build it into the above code for a Flask application. It should:
# - not be an exact repeat of something you did in class, but it can be similar
# - should include an HTML form (of any kind: text entry, radio button, checkbox... feel free to try out whatever you want)
# - should, on submission of data to the HTML form, show new data that depends upon the data entered into the submission form (text entered, radio button selected, etc). So if a user has to enter a number, it should do an operation on that number. If a user has to select a radio button representing a song name, it should do a search for that song in an API.
# You should feel free to be creative and do something fun for you -- 
# And use this opportunity to make sure you understand these steps: if you think going slowly and carefully writing out steps for a simpler data transaction, like Problem 1, will help build your understanding, you should definitely try that!

# You can assume that a user will give you the type of input/response you expect in your form; you do not need to handle errors or user confusion. (e.g. if your form asks for a name, you can assume a user will type a reasonable name; if your form asks for a number, you can assume a user will type a reasonable number; if your form asks the user to select a checkbox, you can assume they will do that.)

@app.route('/SIPaths')
def select_SIPath():
	return render_template("SI_PathForm.html")

@app.route('/SIPathClasses', methods = ['GET', 'POST'])
def response_SIPathClasses():
	if request.method == 'GET':
 		response = request.args
 		return render_template("SI_PathResponse.html", result=response)

if __name__ == '__main__':
    app.run()





