"""Script to get PR(Pull Request) statistics from GitHub"""
import datetime
import requests

github_api_name = input("Input Github_login: ")
github_api_password = input("Input Github_password: ")


def help_f():
    """Display program manual"""
    print("""Usage:
   pr-stats [options] <user> [<repo>]
   pr-stats --version
   pr-stats (-h | --help)
Options:
   -h --help                     Show this screen.
   -q --quit                     Quit from the program.
      --version                  Print the program's installed version.
      --basic                    Basic statistics about merged/closed rate.
      --day-created              Analyze day of the week opened.
      --day-closed               Analyze day of the week closed.
      --hour-created             Analyze hour of the day opened.
      --hour-closed              Analyze hour of the day closed.
      --user-creating            Analyze user who opened.
      --attached-labels          Analyze attached labels.""")


help_f()

url = 'https://api.github.com/repos/alenaPy/devops_lab/pulls?state=all'
request = requests.get(url, params={'page': 1, 'per_page': 10},
                       auth=(github_api_name, github_api_password))
output = []
output += request.json()

while 'next' in request.links.keys():
    url = request.links['next']['url']
    request = requests.get(url,
                           auth=(github_api_name, github_api_password))
    output += request.json()


def version():
    """Display program version"""
    print('The program version is 1.0')


def day_created(data, value):
    """Display day of the week when pr was created"""
    date = data[value][:10].split('-')
    print('Day of the week ' + value + ': ' + str(
        datetime.datetime(int(date[0]), int(date[1]), int(date[2])).strftime("%a")))


def day_closed(data, value):
    """Display day of the week when pr was closed"""
    if data[value] is not None:
        day_created(data, value)


def basic(data):
    """Display basic statistics about merged/closed rate"""
    print("Pull request " + str(data["number"]) + " is: " + data["state"])
    if data["merged_at"] is not None:
        print("Pull request " + str(data["number"]) + " is: merged")


def hour(data, value):
    """Display hour of the day opened/closed"""
    print("Pull request " + str(data["number"]) + ": hour of the day " +
          str(value) + ' ' + data[value][11:13])


def user_creating(data):
    """Display user who opened"""
    print("Pull request " + str(data["number"]) + ": user who opened is: " +
          data["user"]["login"])


def attached_labels(data):
    """Display attached labels"""
    print("Pull request " + str(data["number"]) + ": attached labels: " +
          data["head"]["label"] + ', ' + data["base"]["label"])


def main_function(option, inputs, info):
    """Manage other methods"""
    for i in info:
        if i["user"]["login"] == inputs[2]:
            if option == '--day-created':
                day_created(i, "created_at")
            elif option == '--basic':
                basic(i)
            elif option == '--day-closed':
                day_closed(i, "closed_at")
            elif option == '--hour-created':
                hour(i, "created_at")
            elif option == '--user-creating':
                user_creating(i)
            elif option == '--hour-closed':
                hour(i, "closed_at")
            elif option == '--attached-labels':
                attached_labels(i)
            else:
                print("Error option, please input again (use pr-stats (-h | --help))")
                break


while True:
    try:
        commands = input().split(' ')
        if commands[0] != 'pr-stats':
            raise Exception("Error command, please input again (use pr-stats (-h | --help))")
        options = commands[1]
        if options == '--version':
            version()
        elif options == '-h' or options == '--help':
            help_f()
        elif options == '-q' or options == '--quit':
            break
        elif len(commands) == 3:
            main_function(options, commands, output)
    except Exception as error:
        print(error)

