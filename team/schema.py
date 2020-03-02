import graphene
from graphene_django import DjangoObjectType
from .models import *
from django.contrib.auth import get_user_model



class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()
        

class Query(object):
    users = graphene.List(UserType)
    def resolve_users(self, info, **kwargs):
        return get_user_model().objects.all()


   

class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required =True)
        password = graphene.String(required=True)
        email = graphene.String(required= True)
    
    def mutate(self, info, username, password, email):
        user = get_user_model() (
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()
        return CreateUser(user=user)

class Mutation(graphene.AbstractType):
    create_user = CreateUser.Field()
  





