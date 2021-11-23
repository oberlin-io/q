# Quranic Entity and Graph Model

## @id
The token's @id will usually be ArabTeX characters representing the token.
(https://en.wikipedia.org/wiki/ArabTeX).
In some cases, it will be an English token.

## Graph structure
Basic structure:
```source: [edge: [target]]```

In yaml:
```
- '@id': token1
  edges:
    - '@id': token2
      targets:
      - '@id': token3
        refs:
        - 000.000.000
```
