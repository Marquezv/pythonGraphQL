import strawberry
from typing import Optional, List
from strawberry.fastapi import GraphQLRouter
from db_function import (
    create_pessoa,
    all_pessoa
)

@strawberry.type
class Pessoa:
    id: Optional[int]
    nome: str
    idade: int

@strawberry.type
class Query:
    all_pessoa: List[Pessoa] = strawberry.field(resolver=all_pessoa)

@strawberry.type
class Mutation:
    create_pessoa: Pessoa = strawberry.field(resolver=create_pessoa)


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation
)

graphql_app = GraphQLRouter(schema)
