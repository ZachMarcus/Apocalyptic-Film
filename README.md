# Apocalyptic Film

[Site Here](https://zmarcus.com/Apocalyptic-Film/)

## About
A high-level timeline showcasing apocalyptic films as they fall within larger societal events and eras - more xenophobia after 9/11, the popularity of environmental disaster as a topic of discussion throughout the cold war - you get the idea.

Also, a project from a university course on those sorts of films that I couldn't take down after the time I spent on this.


## Methodology

Pull data from the following:
 - [Kaggle](https://www.kaggle.com/tmdb/tmdb-movie-metadata)
 - [Grouplens](https://grouplens.org/datasets/movielens/)
 - [UCI](https://archive.ics.uci.edu/ml/datasets/Movie)

Select films according to the following methodology
 - Films must be US-based or similar, with American investment / actors
 - Films must be well-received, having achieved a positive return on investment or a strong cult following
 - Wikipedia pages for each film must contain terms such as "nuclear", "apocalyptic", "cyberpunk", "wasteland", "disaster", "science(-)fiction"

For each film, watch a trailer if available, read a critic's review, and read the synopsis. Comment on the film.

Identify important events which might have effects on film production and themes.

Then display those using vanilla web technologies + vis.js, without babel, ES6, AOT, fun web frameworks, or the like.

A potential future improvement could be to process film data programmatically, using NLTK or similar library for NLP.


