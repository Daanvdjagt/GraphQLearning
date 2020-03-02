import graphene
from graphene_django import DjangoObjectType
from .models import *
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay.node.node import from_global_id  # for updating



class RoleNode(DjangoObjectType):
    class Meta:
        model = Role
        filter_fields = ['role_name']
        interfaces = (graphene.relay.Node,)




class Query(object):
    role= graphene.relay.Node.Field(RoleNode)
    all_roles = DjangoFilterConnectionField(RoleNode)
    
    user = graphene.relay.Node.Field(UserNode)
    all_users = DjangoFilterConnectionField(UserNode)

class CreateRole(graphene.relay.ClientIDMutation):
    role = graphene.Field(RoleNode)

    class Input:
        role_name = graphene.String()
    
    def mutate_and_get_payload(self, info, **input):
        role = Role(role_name=input.get('role_name'))
        role.save()
        return CreateRole(role=role)

class Mutation(graphene.AbstractType):
    create_role = CreateRole.Field()
  






