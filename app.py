# github user activity
import requests

# set up the CLI to request username

program_active = True

github_api_url = 'https://api.github.com/users/'
while(program_active):
    username_input = input("Please enter the github user for whom you want to see the activity: ")

    try:
        req = requests.get(github_api_url + username_input + '/events')
        req.headers["content-type"] = 'application/json; charset=utf8'
        req.encoding = 'utf-8'

        json = req.json()
        print(json)

        program_active = False
    except:
        print("could not get github activity")
# TODO fetch github user activity using the username. Within try except, handle non-existent user gracefully



# TODO display user activity in a user friendly way
# TODO options to go back to see another user's activity or end the program
