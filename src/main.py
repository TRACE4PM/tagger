

def do_tagging(tags_config, requests):
    for position, request in enumerate(requests):
        request = request['request_url']
        tag_name = None
        for tag_config in tags_config:
            current_tag_name = tag_config['tag_name']
            current_conditions = tag_config['conditions']
            for condition in current_conditions:
                number = condition['number']
                first = None
                second = None
                alternate = None
                if number == 2:
                    first = condition['first_keyword']
                    second = condition['second_keyword']
                    alternate = condition['alternate_tag']
                    pos_first = request.find(first)
                    pos_second = request.find(second)
                    if (first in request and second in request):
                        if (pos_first < pos_second):
                            tag_name = current_tag_name
                        elif (pos_first > pos_second):
                            tag_name = alternate
                elif number == 1:
                    first = condition['first_keyword']
                    if(first in request):
                        tag_name = current_tag_name
                if tag_name:
                    break
            if tag_name:
                requests[position]['request_tag'] = tag_name
                break
        if not tag_name:
            requests[position]['request_tag'] = "Outliers"
    return requests

async def generate(tags_config, clients_logs):
    for i, log in enumerate(clients_logs):
        sessions = log['sessions']
        for j, session in enumerate(sessions):
            clients_logs[i]['sessions'][j]['requests'] = do_tagging(tags_config,session['requests'])
    return clients_logs