## How to package lambda(python)

```bash
cd lambda/<function>
pip install -r requirements.txt -t . # install on this directory
zip -r "<name>.zip" .
```

## Bootstraping DynamoDB GeoHash Table

```bash
cd scripts
AWS_PROFILE=<your_profile> python3 create_dynamo.py
```