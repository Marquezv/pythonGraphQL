import strawberry
from typing import Optional, List
from strawberry.fastapi import GraphQLRouter
from db_function import (
    create_pessoa,
    all_pessoa,
    create_livro,
    all_livro
)

@strawberry.type
class Pessoa:
    id: Optional[int]
    nome: str
    idade: int
    livros: List['Livro']

@strawberry.type
class Livro:
    id: Optional[int]
    titulo: str
    pessoa: Pessoa


@strawberry.type
class Query:
    all_pessoa: List[Pessoa] = strawberry.field(resolver=all_pessoa)
    all_livro: List[Livro] = strawberry.field(resolver=all_livro)

@strawberry.type
class Mutation:
    create_pessoa: Pessoa = strawberry.field(resolver=create_pessoa)
    create_livro: Livro = strawberry.field(resolver=create_livro)

schema = strawberry.Schema(
    query=Query,
    mutation=Mutation
)

graphql_app = GraphQLRouter(schema)
