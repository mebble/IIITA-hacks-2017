import nexmo
def function():
    client = nexmo.Client(key='3a9542ef', secret='e29280bddcd6e45f')
    client.send_message({
        'from': 'TheGitStars',
        'to': '918919067237',
        'text': 'Lanja'
    })
