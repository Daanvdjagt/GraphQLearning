import graphene
import team.schema


class Query(team.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)


class Mutation(team.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
