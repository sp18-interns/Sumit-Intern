# Sumit-Intern

# Date 20-June-2022


## FIRST HALF
- ✅ Serializer
```
Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes 
that can then be easily rendered into JSON, XML or other content types. Serializers also provide deserialization, 
allowing parsed data to be converted back into complex types, after first validating the incoming data.
```

Declaring Serializer
```
from datetime import datetime

class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()

comment = Comment(email='leila@example.com', content='foo bar')
```
 
## VIDEOS 
- ✅ Udemy Boot Camp

## LINKS 
- ✅ [API-Guide](https://www.django-rest-framework.org/api-guide/serializers/)

## SECOND HALF

- ✅ Django Rest framework Hands-on
 ![alt text](restapi.png?raw=true)
- ✅ Microsoft Azure Task for Cost calculation
```
If you know the service requirment for your project then you can calculate the expenditure on Hourly,Monthly & yearly Basis
https://azure.microsoft.com/en-in/pricing/calculator/
```
## Example for Azure cost calculation for better understanding
![alt text](azure.png?raw=true)
```
In this case we have four service
1.App Service
2.Azure DevOps
3.Azure Monitor
4.Azure Data Lake Storage Gen1

Now go to Azure calculator and select these services to your cart & select for how much time you need these services and hit calculate
your cost estimation is ready 
```


## VIDEOS 
- ✅ Django Boot Camp Video

## ASSIGNMENT
- No major update on Assignment

## DOUBTS
- Nothing as of now

## LINKS 
- ✅ [DRF-Quickstart Guide](https://www.django-rest-framework.org/tutorial/quickstart/#quickstart)
- ✅ [Serializer](https://www.django-rest-framework.org/tutorial/1-serialization/)
- ✅ [Azure Calculator](https://azure.microsoft.com/en-in/pricing/calculator/)