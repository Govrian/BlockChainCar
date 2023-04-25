
# Run the demo
Start the network and initialize blockchain by:
```console
$ ./blockchain.py
```
In a second terminal execute the following:
```console
$ ./manufacturer.py
```
in order to create a block which will be mined by miners (processes).
The above script simulates a manufacturer. It generates a random ID which
is considered as an ID of the manufactured car. It sets its mileage to 0 and
sets additional data like manufacturer (Volkswagen), model (Golf), year
(current year), country_of_origin (Czech Republic).

Run the following script to simulate a change of the car ownership.
NOTE: this is a simple demo, so the users doesn't have to exist, you can
make up buyer id, however, as a car id use the one, `manufacturer.py` script
generated in the step above and as a seller id use the manufacturer's id.
```console
$ ./seller.py <seller_ID> <buyer_ID> <car_ID>
```

Run the following script in order to simulate a check when a car's mileage will
be edited.
```console
$ ./service_station.py <car_ID>
```

Try to change the ownership again.
```console
$ ./seller.py <seller_ID> <buyer_ID> <car_ID>
```

Run the following script to list the history of the car. It will print all
blocks where the car_ID is found.
```console
$ ./car_history.py <car_ID>
```


# Authors
[Martin Kopec](https://www.linkedin.com/in/martin-kopec-07b29096/)

[Robert Albrecht](https://www.linkedin.com/in/robert-albrecht498/)

[Daniel Vitek](https://www.linkedin.com/in/daniel-v%C3%ADtek-683399147/)


