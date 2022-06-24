# Bitcoin Behaviour Forcasting

L'objectif de ce projet est de tenter des methodes de Machine Learning pour determiner les actions à effectuer sur un marché financier. Ici nous choisissons par exemple le Bitcoin, la plus grosse cryptomonnaie et l'une des plus ancienne ce qui fait d'elle la plus attractive. 

En choisissant le bitcoin nous auront ainsi un historique de données relativement important.

Il existe un nombre incalculable d'approches, de methodes et de modeles qui essaye de resoudre ce probleme. Cela represente un domaine complexe encore au stade de recherche.

On cherchera plus à experimenter plusieurs approches que d'en choisir une et de faire le meilleur modele possible dessus.

Nous choisissons de separer notre travail en trois approches experimenté sur deux dataset avec une granularité differente :

*Nous utiliserons la librairie yfinance pour faciliter l'acquisition des données et permettre unactualisation simplifié*
- **1 donnée par jour** -> De 2017 à 2022 soit 1944 lignes. Suppression des données avant 2017 car on ne reviendra pas à un niveau de notoriété comme celui la.
- **1 donnée par heure** -> yfinance ne permet pas de recuperer plus de deux ans d'historique avec un intervalle de une heure. Cela nous fait donc un total de plus de 20 000 données soit 10 fois plus. Cet algo nous permettrais donc d'être plus reactif et de réaliser plus d'achat et de revente.

Nous pouvons aussi imaginer une frequence plus importante mais pour une question de limitition nous en resterons là.

#### Features (à etudier)
- **Return** : (Close t+1 / Close) - 1. Permet de d'eviter tous problemes d'echelles. Nous utiliserons les Return de tous les actifs comme features
- **Pearson Correlation** : Permet de voir les interactions entre les actifs dans une fenetre de temps (depend du dataset)
- **Synchrony** : synchronisation des mouvement les uns avec les autres
- **Google Trend** : le nombre de recherches sur google de "Bitcoin" et "btc". Recuperer grace à la librairie pytrends

Aussi, nous pouvons ajouter les données liées à la blockchain Bitcoin (données par jour) mais l'actualisation de ces données est plus laborieuse :
- **avg block size** : The average block size over the past 24 hours in megabytes.
- **cost per transaction** : Miners revenue divided by the number of transactions.
- **hash-rate** : The estimated number of terahashes per second the bitcoin network is performing in the last 24 hours.
- **miners revenue** : Total value in USD of coinbase block rewards and transaction fees paid to miners.
- **mvrv** : MVRV is calculated by dividing Market Value by Realised Value. In Realised Value, BTC prices are taken at the time they last moved, instead of the current price like in Market Value
- **nbr wallet on Blockchain.com** : The total number of unique Blockchain.com wallets created.
- **nvt** : NVT is computed by dividing the Network Value (= Market Value) by the total transactions volume in USD over the past 24hour.
- **transaction fees usd** :
*Source : https://www.blockchain.com/charts*


Nous souhaitions integrer les données liées à des actifs boursiers classique mais les marchés étant fermés les weekend et pendant de nombreuses heures par jours nous avons finalement choisit de ne pas en tenir compte.

#### Approches :

1. Regression du Return du Bitcoin à t+1
2. Classification binaire du Return du Bitcoin à t+1 (Return > ou < à 0) pour l'achat ou la revente 
3. Classification multiple du Return du Bitcoin à t+1 (Return =, > ou < à la moyenne des 30 dernieres valeurs de return) pour garder l'achat ou la revente.
C'est souvent ce dernier element qui n'est pas pris en compte, les frais liés à l'achat et à la vente étant important si de nombreuse achange sont fait, il est important de le prendre en compte. A voir si les performances seront impactées puisque on passe sur de la classification multiple.
