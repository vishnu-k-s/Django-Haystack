from django.shortcuts import render

# # Create your views here.
# from django.shortcuts import render
# from rest_framework.decorators import (
#     api_view, renderer_classes,
# )
# from .models import Customer
# from haystack.query import SearchQuerySet
 
# from rest_framework.response import Response
# # Create your views here.
 
 
# @api_view(['POST'])
# def search_customer(request):
#     name = request.data['name']
#     customer = SearchQuerySet().models(Customer).autocomplete(
#         first_name__startswith=name)
 
#     searched_data = []
#     for i in customer:
#         all_results = {"first_name": i.first_name,
#                        "last_name": i.last_name,
#                        "balance": i.balance,
#                        "status": i.customer_status,
#                        }
#         searched_data.append(all_results)
 
#     return Response(searched_data)