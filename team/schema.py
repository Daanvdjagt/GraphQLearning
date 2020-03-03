import graphene
import team.users.schema


class Query(team.users.schema.Query, graphene.ObjectType):
    pass


class Mutation(team.users.schema.Mutation, graphene.ObjectType,):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
