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
societal_events = ''
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

list_of_subgenres = []

def get_subgenres():
    ret = subgenre_instantiation
    for index, subgenre in enumerate(list_of_subgenres):
        ret += '{{id: {}, content: "{}"}},'.format(
            index + 1,
            subgenre)
    ret += subgenre_ending
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
    output = instantiation + societal_events + intermediary + films + closing
    with open('films.js', 'w+') as films_js:
        films_js.write(output)

    # now write out the subgenres to a separate file
    subgenre_output = get_subgenres()
    with open('subgenres.js', 'w+') as subgenres_js:
        subgenres_js.write(subgenre_output)




