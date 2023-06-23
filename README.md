## Projet de Visualisation des Parcours Utilisateurs - Service Tagging

### Description du Projet

Ce projet vise à développer une application de visualisation des parcours utilisateurs basée sur la fouille de processus. L'objectif est de mieux comprendre les comportements des utilisateurs qui accèdent aux services et aux documents proposés par le portail Gallica de la Bibliothèque Nationale de France (BNF). Pour y arriver, il faut exploiter de grands volumes de logs provenant du portail.
Pour une compréhension et une analyse optimales de ces logs, il convient d'attribuer une action à chaque requête présente dans ces derniers. Ce service, nommé tagging, a été développé dans l'optique de faciliter l'étiquettage des logs. L'API fera appel à ses différentes fonctions à chaque fois qu'un utilisateur souhaite télécharger un fichier de configuration du tagging dans la base de données, générer le tagging pour un ensemble de logs présents dans une collection spécifique de la base de données et afficher l'ensemble des règles de tagging préalablement sauvegardées dans la base de données par le téléchargement d'un fichier de configuration.

### Architecture

Dans le cadre de ce projet, le service tagging sera intégré dans une architecture basée sur les microservices. Dans ce cas, ce service communiquera uniquement avec l'API développée à cet effet. L'API recevra les requêtes provenant des clients, utilisera les fonctions du service pour satisfaire cette requête et retourner pour finir la réponse adéquate au client.

### Technologies Utilisées

Pour la mise en place du service tagging, plusieurs technologies présentées ci-dessous ont été utilisées. Il s'agit de :

    Langage(s) de Programmation : Python
    Base de Données : MongoDB Normalement le service ne communique pas directement avec la base de données du projet. Pour le faire, il passe par l'API.
    Autre(s) outil(s) : Poetry

### Installation et Configuration

Pour utiliser le service tagging dans le projet ou n'importe quel autre, il faut juste l'installer comme un module (python) normale. Dans notre cas, avec poetry, il suffit d'exécuter les différentes étapes suivante :
    - Inclure le lien du dépôt du service dans le fichier de configuration (pyproject.toml) du projet dans la section [tool.poetry.dependencies] de la manière suivante (tagging = {git = "git@gitlab.univ-lr.fr:trace_clustering/services/tagging.git"})
    - Installer le service comme un module avec la commande suivante (poetry add tagging)
    - Importer les fonctions du service comme on importe n'importe quel module python (from tagging.main import generate)


### Fonctionnement du tagging
Pour permettre l'utilisation du tagging, un ensemble de règles doit être préalablement défini dans un fichier au format json et chargé au niveau de la base de données dans une collection dédiée créée préalablement. L'API fera ensuite appel automatiquement à ces règles et les transmettre au service tagging avec les logs à tagger.
Le tagging consiste surtout à associer une action à chaque requête présente dans les logs. Pour y arriver, le service va chercher des mots-clés dans chaque requête et suivant leur position, il attribuera une action à la requête.
Voici une idéé de la structure du fichier de configuration :
```json
[
    {
        "tag_name": "AdvancedSearch",
        "conditions": [
        {
            "number": 2,
            "first_keyword": "advancedSearch",
            "second_keyword": "/accueil/",
            "alternate_tag": "HomePage"
        },
        {
            "number": 2,
            "first_keyword": "advancedSearch",
            "second_keyword": "search",
            "alternate_tag": "AdvancedSearch"
        },
        {
            "number": 1,
            "first_keyword": "advanced"
        }
    ]
  }
]
```
    - tag_name : représente l'action à attribuer à une requête si l'une des conditions est vérifiée
    - conditions : permet de définir une liste de conditions relatives à l'action à attribuer
    - number : représente le nombre de mots-clés à rechercher dans chaque requête
    - first_keyword : le premier mot-clé à rechercher (quand le champ number est égal à 1, il sera l'unique mot-clé à rechercher)
    - second_keyword : le second mot-clé à rechercher (quand le champ number est égal à 1, il ne sera pas inclus dans les conditions ni dans la recherche)
    - alternate_tag : Si le `first_keyword` se trouve en première position par rapport au `second_keyword` dans une requête, l'action définie dans le champ `tag_name` sera attribuée à la requête. Dans le cas contraire, c'est à dire le `second_keyword` se trouve en première position par rapport au `first_keyword`, c'est l'action définie dans le champ `alternate_tag` qui sera attribuée à la requête (quand le champ number est égal à 1, il n'y aura pas de champ `alternate_tag` puisqu'il y aura uniquement le champ `first_keyword`).

On peut ajouter autant d'action et de conditions que l'on souhaite, mais pour un bon fonctionnement du service et pour éviter des `bugs` logiques, ces bonnes pratiques sont à suivre :
    - respecter la structure du fichier json
    - bien définir les règles dans un ordre logique (en prenant surtout le soin de placer les conditions avec `number: 2` avant celles avec `number: 1`)

Pour ajouter d'autres règles liéées à d'autres actions, il suffit de les séparer par une virgule comme illustré ci-dessous :
```json
[
    {
        "tag_name": "AccessGallicaBlog",
        "conditions": [
        {
            "number": 2,
            "first_keyword": "blog",
            "second_keyword": "/accueil/",
            "alternate_tag": "HomePage"
        },
        {
            "number": 2,
            "first_keyword": "blog",
            "second_keyword": "und",
            "alternate_tag": "CollectionNavigation"
        },
        {
            "number": 1,
            "first_keyword": "blog"
        }
        ]
    },
    {
        "tag_name": "AdvancedSearch",
        "conditions": [
        {
            "number": 2,
            "first_keyword": "advancedSearch",
            "second_keyword": "/accueil/",
            "alternate_tag": "HomePage"
        },
        {
            "number": 2,
            "first_keyword": "advancedSearch",
            "second_keyword": "search",
            "alternate_tag": "AdvancedSearch"
        },
        {
            "number": 1,
            "first_keyword": "advanced"
        }
    ]
  }
]
```
    

### Contributions et Améliorations

Les contributions à ce projet sont les bienvenues. Si vous souhaitez apporter des améliorations, veuillez suivre les étapes suivantes :

    Forkez le dépôt et clonez votre propre copie.
    Créez une branche pour vos modifications : git checkout -b feature/ma-nouvelle-fonctionnalite
    Effectuez les modifications nécessaires et testez-les de manière approfondie.
    Soumettez une pull request en expliquant en détail les modifications apportées et leur impact.

### Auteur(s)

    - Nannito Junior ALCIME

### Licence

Ce projet est sous licence L3I.
