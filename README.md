
# Exécuter la démo
Démarrer le réseau et initialiser la blockchain par :


``console
$ ./blockchain.py
```
Dans un second terminal, exécutez ce qui suit :



``console
$ ./manufacturer.py
```


afin de créer un bloc qui sera miné par des mineurs (processus).
Le script ci-dessus simule un fabricant. Il génère un identifiant aléatoire qui
qui est considéré comme l'ID de la voiture fabriquée. Il fixe son kilométrage à 0 et
définit des données supplémentaires telles que le fabricant (Volkswagen), le modèle (Golf), l'année
(année en cours), pays_d'origine (République tchèque).

Exécutez le script suivant pour simuler un changement de propriétaire de la voiture.
REMARQUE : il s'agit d'une simple démonstration, il n'est donc pas nécessaire que les utilisateurs existent.
Vous pouvez inventer l'identifiant de l'acheteur, cependant, pour l'identifiant de la voiture, utilisez le script `manufacturer.py` généré à l'étape précédente.
généré dans l'étape précédente et comme identifiant du vendeur, utilisez l'identifiant du constructeur.


``console
$ ./seller.py <seller_ID> <buyer_ID> <car_ID>
```


Exécutez le script suivant afin de simuler une vérification lorsque le kilométrage d'une
d'une voiture.


```console
$ ./service_station.py <car_ID>
```


Pour changer le nombre de kilomètres sur la voiture 

```console
$ ./update_mileage.py <id_car> <Nombre de kilomètres>
```



Essayez à nouveau de changer de propriétaire.

``console
$ ./seller.py <seller_ID> <buyer_ID> <car_ID>
```


Exécutez le script suivant pour dresser la liste de l'historique de la voiture. Il affichera tous les blocs
blocs où l'identifiant de la voiture est trouvé.


```console
$ ./car_history.py <car_ID>
```

