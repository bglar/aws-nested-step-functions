# Serverless

## aws-nested-step-functions

Serverless project outlining the creation of nested aws step functions that pass context from parent to child.

https://docs.aws.amazon.com/step-functions/latest/dg/connect-stepfunctions.html

## SetUp Project

Clone the project: 
```
git clone git@github.com:bglar/aws-nested-step-functions.git
```

## Install Serverless Dependencies.

(Install npm if you don't have it already)

```
npm install
```

Deploy to AWS (Assuming you alredy have AWS set up)

```
serverless deploy
```

**NOTE:** This will deploy to a stage called `devbryan` so feel free to [change that](https://github.com/bglar/aws-nested-step-functions/blob/master/nested-step-functions/serverless.yml#L11) if that stage name does not suite you.
