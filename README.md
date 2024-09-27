## TRACE4PM - Tagging service


This project is part of TRACE4PM software stack, it aims to develop a user journey visualization application based on process mining. This service, called tagging, was developed to facilitate log labeling. The API will invoke its various functions whenever a user wants to download a tagging configuration file from the database, generate tags for a set of logs stored in a specific collection of the database, and display all previously saved tagging rules by downloading a configuration file.


### Architecture

In this project, the tagging service will be integrated into a microservices-based architecture. In this case, this service will communicate only with the API developed for this purpose. The API will receive requests from clients, use the service's functions to fulfill the request, and return the appropriate response to the client.

### Installation et Configuration

To use the tagging service in this project or any other, it should be installed as a regular Python module. In our case, with Poetry, simply follow these steps:

Include the service repository link in the project's configuration file (pyproject.toml) under the [tool.poetry.dependencies] section as follows: tagging = {git = "git@github.com:TRACE4PM/tagger.git"}
Install the service as a module with the following command: poetry add tagging
Import the service functions like any other Python module: from tagging.main import generate


### Fonctionnement du tagging

To enable the use of tagging, a set of rules must first be defined in a JSON file and uploaded to the database in a dedicated collection. The API will automatically call these rules and send them to the tagging service along with the logs to be tagged. Tagging primarily involves associating an action with each request in the logs. To achieve this, the service searches for keywords in each request, and based on their position, assigns an action to the request.

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
- `tag_name`: Represents the action to be assigned to a request if one of the conditions is met.
- `conditions`: Defines a list of conditions related to the action to be assigned.
- `number`: Represents the number of keywords to search for in each request.
- `first_keyword`: The first keyword to search for (if number is 1, this will be the only keyword to search for).
- `second_keyword`: The second keyword to search for (if number is 1, it will not be included in the conditions or search).
- `alternate_tag`: If the `first_keyword` is found before the `second_keyword` in a request, the action defined in the `tag_name` field will be assigned to the request. Otherwise, the action defined in the `alternate_tag field will be assigned to the request (if number is 1, there will be no `alternate_tag field as there will only be a first_keyword field).

You can add as many actions and conditions as needed. However, to ensure the service functions correctly and to avoid logical errors, follow these best practices:

- Respect the structure of the JSON file.
- Define the rules in a logical order (especially placing conditions with number: 2 before those with number: 1).
To add more rules related to other actions, simply separate them with a comma, as illustrated below:

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
    
### Auteur(s)

    - Nannito Junior ALCIME

