# Jinja-based Text Generation

# Getting started

## Setup your environment

Install dependencies and setup the environment using [poetry](http://poetry.org)


```bash
poetry install # install dependencies
poetry shell # activate the Python environment
```

## Run the text generation

The `narrate` command requires an input file as argument and additional option that identifies the template
```bash
narrate INPUT_FILE -t <template-name>
```

Given the example data structure `table1.json`, you can generate the narrative with the following command:

```bash 
narrate narrate table1.json -t table
```

