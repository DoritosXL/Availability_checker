Create .env file and add the following variables:
- USER
- PASSWORD
- RECEIVER

With the scraper it is possible to obtain more information. For example the price, description and even the delivery date.

The way I implemented this project is by running the python script at 12PM every day (if my computer is active). This can be done by adding it as a service in windows.

It is also possible to run the code on a timer with the 'time' import, instead of a windows service.
