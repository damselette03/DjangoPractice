import graphene
import restaurants.schema  # 导入您的应用的schema文件

class Query(restaurants.schema.Query , graphene.ObjectType):
    # 这个类将继承您的应用中的多个查询作为一个根查询
    pass

schema = graphene.Schema(query=Query)