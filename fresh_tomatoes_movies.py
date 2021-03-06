import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>My video playlist</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

    <style type="text/css" media="screen">
    /*NAVIGATION MENU STYLE MOBILE*/
      * {
        margin: 0;
        padding: 0;
        outline: 0;
        box-sizing: border-box;
      }

      body {
        height: auto !important;
        height: 100%;
        min-height: 100%;
      }

      header {
        background-color: rgb(140, 193, 193);
        color: white;
        display: flex;
        flex-direction: column;
        text-align: center;
      }

      #logo {
        display: flex;
        justify-content: space-between;
        padding: 10px 15px;
      }

      #logo button {
        padding: 0;
        margin: 0;
        border: none;
        background: none;
        color: white;
        font-weight: bold;
        font-size: 15px;
        margin-top: 20px;
      }

      header > nav {
        background-color: white;
        color: #BE7403;
        flex: 1;
        /*display: none;*/
      }

      header .normal {
        display: none;
      }

      header .active {
        display: block;
      }

      header nav > ul {
        list-style-type: none;
      }

      header nav > ul > li {
        border-bottom: 0.5px dotted rgb(140, 193, 193);
        position: relative;
      }

      header li:hover a {
        background-color: rgb(140, 193, 193);
        color: white;
        border-top: 5px solid white;
        font-size: 20px;
      }

      header nav > ul > li > a {
        display: block;
        color: rgba(0,0,0,0.65);
        padding: 1.5rem 0;
        text-decoration: none;
        transition: 250ms all ease;
      }

      #menu-button:hover {
        background-color: white;
        color: rgb(140, 193, 193);
        padding: 5px;
        border-radius: 50%;
      }

      /*NAVIGATION MENU STYLE FULL*/
      @media only screen and (min-width: 600px) {

        header .normal {
          display: inline;
        }

        #menu-button {
          display: none;
        }

        header nav {
          background-color: rgb(140, 193, 193);
          text-align: right;

        }

        header nav > ul > li{
          display: inline;
        }

        header nav > ul > li > a {
          padding: 0 15px 5px 0;
          margin: 0;
          display: inline-block;
          color: white;
        }

        header li:hover a {
          border-top: none;
          font-size: 30px;
        }

        header .nav-active {
          font-size: 24px;
        }
      }

      /*CONTAINER RESPONSIVE STYLE*/
      .text-content {
        display: none;
      }

      .container {
        padding: 2em 3em;
        margin: 0 auto;
        max-width: 1200px;
        display: flex;
        flex-wrap: wrap;
        background-color: #E8E8E8;
        border: 1px solid #A9A9A9;
        text-align: center;
      }

      h2 {
        height: 35px;
        font-size: 1em;
        text-align: center;
        word-wrap: break-word;
        white-space: normal;
        max-width: 220px;
      }

      .movie-tile {
        padding: 0 0 1em 1em;
      }

      /*TRAILER CONTAINER STYLE*/
      #trailer {
        max-width: 1000px;
        max-height: 500px;
        /*background-color: #191919;*/
        padding: 1.5em;
        position: fixed;
        top: 0;
        bottom: 0;
        left: 0;
        right: 0;
        margin: auto;
      }

      .trailer-container {
        margin: 0 auto;
        padding: 0;
        width: 95%;
        display: flex;
        flex-wrap: wrap;
      }

      #trailer-video-container{
        margin: 10px;
        min-width: 300px;
        flex-grow: 2;
      }


      #trailer-video {
        width: 100%;
        height: 100%;
        max-width: 640px;
        max-height: 480px;
      }

      #trailer-description{
        padding: 15px;
        margin: 10px;
        max-height: 480px;
        max-width: 300px;
        background-color: white;
        color: rgb(140, 193, 193);
      }

      #trailer-description-name {
        margin: 10px auto;
        font-size: 28px;
      }

      #trailer-description-full {
        font-size: 18px;
      }

      .hanging-close {
        background: none;
        border: none;
        color: white;
        font-size: 28px;
        font-weight: 800;
      }

      .ratingDate {
        color: black;
        font-size: 18px;
        display: inline-block;
        padding: 0;
        margin: 0;
        padding-left: 10px;
      }

      /*NAVIGATION MENU STYLE FULL*/
      @media only screen and (max-width: 873px) {
        #trailer-description{
        max-width: 100%;
        max-width: 640px;
        }
      }
    </style>

    <script type="text/javascript" charset="utf-8">
      // Menu open closed
      function openCloseFunction() {
          var nav = document.getElementById("main-menu");
          if (nav.className === "normal") {
              nav.className = "active";
          } else {
                nav.className = "normal";}
      }

      function closeMenuFunction() {
          document.getElementById("main-menu").className = "normal";
      }

      //Get IMDB rating
      function imdbRating(id) {
          var imdbUrl = "http://www.theimdbapi.org/api/movie?movie_id=" + id;
          $.get(imdbUrl, function(data) {
              $("#trailer-rating").empty().prepend("<span><a href='http://www.imdb.com/title/" + id + "/?ref_=plg_rt_1'><img src='http://g-ecx.images-amazon.com/images/G/01/imdb/plugins/rating/images/imdb_46x22.png' alt='" + data.title + " on IMDb' /></a><p class='ratingDate'>" + data.rating + "</p></span>");
          });
      }

      // Pause the video when the modal is closed
      $(document).on("click", ".hanging-close, .modal-backdrop, .modal", function (event) {
          // Remove the src so the player itself gets removed, as this is the only
          // reliable way to ensure the video stops playing in IE
          $("#trailer-video-container").empty();
          $("#trailer-rating").empty();
          $("#trailer-description").hide();
      });

      // Start playing the video whenever the trailer modal is opened
      $(document).on("click", ".movie-tile", function (event) {
          var trailerDescriptionName = $(this).find("h2").text();
          $("#trailer-description-name").text(trailerDescriptionName);
          var trailerDescription = $(this).find("span").text();
          $("#trailer-description-full").text(trailerDescription);
          var trailerIMDBId = $(this).attr("data-trailer-imdb-id");
          imdbRating(trailerIMDBId);
          $("#trailer-description").show();
          var trailerYouTubeId = $(this).attr("data-trailer-youtube-id");
          var sourceUrl = "http://www.youtube.com/embed/" + trailerYouTubeId + "?autoplay=1&html5=1";
          $("#trailer-video-container").empty().append($("<iframe></iframe>", {
            "id": "trailer-video",
            "type": "text-html",
            "src": sourceUrl,
            "frameborder": 0
          }));
      });

      // Animate in the movies when the page loads
      $(document).ready(function () {
        $(".movie-tile").hide().first().show("fast", function showNext() {
          $(this).next("div").show("fast", showNext);
        });
      });
    </script>

</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
<body>
  <header>
    <div id="logo" class="menuUp">
      <h1>My Videos Playlist</h1>
      <button id="menu-button" type="button" onclick="openCloseFunction()">Go to</button>
    </div>
    <nav id="main-menu" class="normal">
      <ul>
        <li class="nav-active"><a href="fresh_tomatoes_movies.html">Movies</a></li>
        <li><a href="fresh_tomatoes_TVseries.html">TV Series</a></li>
      </ul>
    </nav>
  </header>
<!-- Trailer Video Modal -->
  <div class="modal" id="trailer">
    <button type="button" class="hanging-close" data-dismiss="modal" aria-hidden="true">
      <span aria-hidden="true">&times;</span>
    </button>
    <div class="modal-dialog trailer-container">
      <div class="scale-media" id="trailer-video-container">
      </div>
      <div id="trailer-description">
        <h2 id="trailer-description-name">
        </h2>
        <span id="trailer-description-full">
        </span>
        <br><br>
        <div id="trailer-rating">
        </div>
      </div>
    </div>
  </div>
<!-- Main Page Content -->
  <div class="container row-eq-height" onclick="closeMenuFunction()">
    {movie_tiles}
  </div>
</body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
  <div class="movie-tile text-center" data-trailer-imdb-id="{imbd_id}" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <button type="button" class="wrap-text-img">
      <img src="{poster_image_url}" width="220" height="342" alt="Poster of movie {movie_title}">
      <span class="text-content">{movie_storyline}</span>
    </button>
    <h2>{movie_title}</h2>
  </div>
'''

def create_movie_tiles_content(movies):
  # The HTML content for this section of the page
  content = ''
  for movie in movies:
    # Extract the youtube ID from the url
    youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
    youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
    trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

    # Append the tile for the movie with its content filled in
    content += movie_tile_content.format(
      movie_title=movie.title,
      movie_storyline=movie.storyline,
      poster_image_url=movie.poster_image_url,
      trailer_youtube_id=trailer_youtube_id,
      imbd_id=movie.imbd_id
    )
  return content

def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('fresh_tomatoes_movies.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2)  # open in a new tab, if possible
