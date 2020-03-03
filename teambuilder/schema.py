import graphene
import team.schema
import graphql_jwt


class Query(team.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)


class Mutation(team.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
