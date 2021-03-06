#!/usr/bin/python3

# Generate some javascript from the given csv files


import sys
import csv


# Starter for initializing the DataSet
instantiation = '''
// note that months are zero-based in the JavaScript Date object
var items = new vis.DataSet([
  // societal events, requiring start and end
'''
# then societal events
events = ''
# then a comment
intermediary = '''
  // films
'''
# then the films
films = '''
'''
# finally the closing of the file
closing = '''
]);'''




subgenre_instantiation = '''
// list of subgenres within apocalyptic films
var groups = new vis.DataSet([ // 1-indexed
'''
subgenre_ending = '''
]);
'''

list_of_subgenres = ['Societal Event']

def get_subgenres():
    ret = subgenre_instantiation
    ordering = 1
    for index, subgenre in enumerate(list_of_subgenres):
        ret += '{{id: {}, visible: true, content: "{}", value: {}}},'.format(
            index + 1, subgenre, ordering)
        ordering += 1
    ret += subgenre_ending
    return ret

def generate_event(event):
    event_title = event[0]
    event_start = event[1]
    event_end = event[2]
    #ret = '{{type: \'background\', start: new Date({}, 0), end: new Date({}, 0), content: "{}"}},'.format(
    #    event_start,
    #    event_end,
    #    event_title)
    #print(ret)
    # treat events like other films in order to display them appropriately
    # this is to prevent overlap issues with vis.js
    film_subgenre = 'Societal Event'
    group_id = list_of_subgenres.index(film_subgenre) + 1

    if event_start != event_end:
        ret = '{{start: new Date({}, 0), end: new Date({}, 0), title: "{}", content: "{}", group: {}}},'.format(
            event_start,
            event_end,
            event_title,
            event_title,
            group_id)
    else:
        ret = '{{start: new Date({}, 0), content: "{}", group: {}}},'.format(
            event_start,
            event_title,
            group_id)

    return ret


def generate_film(film):
    '''
    input looks like the following:
    ['Reign of Fire', '2002', 'Dragons', 'Ends with humanity picking up the pieces and rebuilding civilization', '', '', '', '', '', '', '']

    output is a string for the javascript
    side effect is tries to add the subgenre to the list of subgenres
    '''
    film_title = film[0].replace('"', '\'')
    film_year = film[1]
    film_subgenre = film[2]
    film_commentary = film[3].replace('"', '\'')
    if film_subgenre not in list_of_subgenres:
        list_of_subgenres.append(film_subgenre)
    group_id = list_of_subgenres.index(film_subgenre) + 1

    # print(film_title, film_year, film_subgenre, film_commentary)
    # title is actually the commentary, but that's what vis.js calls it
    ret = '{{start: new Date({}, 0), content: "{}", title: "{}", group: {}}},'.format(
        film_year,
        film_title,
        film_commentary,
        group_id)
    #print(ret)
    return ret


with open('events.csv') as event_file:
    events_reader = csv.reader(event_file, delimiter=',')
    is_header = True
    for event in events_reader:
        if is_header:
            is_header = False
            continue
        events += generate_event(event)

with open('films.csv') as film_file:
    film_reader = csv.reader(film_file, delimiter=',')
    is_header = True
    for film in film_reader:
        if is_header:
            is_header = False
            continue
        films += generate_film(film)
        #sys.exit()
    films = films[:-1] # remove the last trailing comma

    # write out films and background events to file
    output = instantiation + events + intermediary + films + closing
    with open('films.js', 'w+') as films_js:
        films_js.write(output)

    # now write out the subgenres to a separate file
    subgenre_output = get_subgenres()
    with open('subgenres.js', 'w+') as subgenres_js:
        subgenres_js.write(subgenre_output)




