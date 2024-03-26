To run the server run (use your phishtank username as per https://www.phishtank.com/developer_info.php):

> PHISHTANK_USERNAME=<your_phishtank_username> docker compose up

Once the server is up, feel free to hit http://localhost:8000/docs to see the openapi documentation page.

A few sample queries are also available in the `test_main.http` file.

Notes:
1. I wasn't sure what TLD meant. On the internet it seems to mean just the ".com",
".net", i.e. everything that follows the last dot in the domain name. I decided to show the "base domain", i.e.
two sections instead of one - this would of course be a discussion to be had and specified.
2. I implemented a strict search of exact domain in the search route. It could just as much
have been a search for the searched word to just be a substring of the url - again this
could easily be achieved with a `LIKE` search with wildcards.
