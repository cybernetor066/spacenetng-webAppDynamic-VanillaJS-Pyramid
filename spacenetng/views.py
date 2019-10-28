from pyramid.view import (
    view_config,
    view_defaults
)
from pyramid.response import Response


# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# Home view
@view_defaults(route_name='home')
class HomeViews(object):
    def __init__(self, request):
        self.request = request

    @view_config(renderer='../index.pt')
    def homepage(self):
        return {}



# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# Electronics category views

# ##########################################################################################################
# Create
@view_defaults(route_name='electronics_createNewPost')
class ElectronicsCreateNewPostViews(object):
    def __init__(self, request):
        self.request = request

    @view_config(renderer='templates/electronics_templates/electronics_createNewPost.pt')
    def electronics_createNewPost(self):
        return {}

    # # Perform operation on query params, return values and give the user a Response after creation of a new post
    # @view_config(request_method='POST', request_param='')
    # def electronics_createNewPost_response(self):
    #     return {}


# ##########################################################################################################
# Modify
@view_defaults(route_name='electronics_modifyPost1')
class ElectronicsModifyPostViews(object):
    def __init__(self, request):
        self.request = request

    @view_config(renderer='templates/electronics_templates/electronics_modifyPost1.pt')
    def electronics_modifyPost1(self):
        return {}

    # # response for modifyPost1 page, return this page if correct params were given, else throw error
    # @view_config(request_method='POST', request_param='', renderer='')
    # def electronics_modifyPost2(self):
    #     return {}

    # # Perform operation on query params from modifyPost2 page,
    # # return values and give the user a Response after creation of a new post
    # @view_config(request_method='POST', request_param='', renderer='')
    # def electronics_modifyPost2_response(self):
    #     return {}


# ##########################################################################################################
# View products
@view_defaults(route_name='electronics_viewProducts1')
class ElectronicsViewProductsViews(object):
    def __init__(self, request):
        self.request = request

    @view_config(renderer='templates/electronics_templates/electronics_viewProducts1.pt')
    def electronics_viewProducts1(self):
        return {}

    # Response from viewProducts1 page. get params from that page,
    # Perform query operations from database and return this page/pages as response/responses 
    @view_config(request_method='POST', request_param='electronics_view_submit', renderer='templates/electronics_templates/electronics_viewProducts2_page1.pt')
    def electronics_viewProducts2_page1(self):
        return {}

    # View pages(n)
    @view_config(route_name='electronics_viewProducts2_page1', renderer='templates/electronics_templates/electronics_viewProducts2_page1.pt')
    def electronics_viewProducts2_page11(self):
        return{}

    @view_config(route_name='electronics_viewProducts2_page2', renderer='templates/electronics_templates/electronics_viewProducts2_page2.pt')
    def electronics_viewProducts2_page2(self):
        return{}

    @view_config(route_name='electronics_viewProducts2_page3', renderer='templates/electronics_templates/electronics_viewProducts2_page3.pt')
    def electronics_viewProducts2_page3(self):
        return{}

    @view_config(route_name='electronics_viewProducts2_page4', renderer='templates/electronics_templates/electronics_viewProducts2_page4.pt')
    def electronics_viewProducts2_page4(self):
        return{}

    @view_config(route_name='electronics_viewProducts2_page5', renderer='templates/electronics_templates/electronics_viewProducts2_page5.pt')
    def electronics_viewProducts2_page5(self):
        return{}

























# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# Automobiles category views

# ##########################################################################################################
# Create
@view_defaults(route_name='automobiles_createNewPost')
class AutomobileCreateNewPostViews(object):
    def __init__(self, request):
        self.request = request


    @view_config(renderer='templates/automobiles_templates/automobiles_createNewPost.pt')
    def automobiles_createNewPost(self):
        return {}

    # # Perform operation on query params, return values and give the user a Response after creation of a new post
    # @view_config(request_method='POST', request_param='')
    # def automobiles_createNewPost_response(self):
    #     return {}


# ##########################################################################################################
# Modify
@view_defaults(route_name='automobiles_modifyPost1')
class AutomobileModifyPostViews(object):
    def __init__(self, request):
        self.request = request

    @view_config(renderer='templates/automobiles_templates/automobiles_modifyPost1.pt')
    def automobiles_modifyPost1(self):
        return {}

    # # response for modifyPost1 page, return this page if correct params were given, else throw error
    # @view_config(request_method='POST', request_param='', renderer='')
    # def automobiles_modifyPost2(self):
    #     return {}

    # # Perform operation on query params from modifyPost2 page,
    # # return values and give the user a Response after creation of a new post
    # @view_config(request_method='POST', request_param='', renderer='')
    # def automobiles_modifyPost2_response(self):
    #     return {}

# ##########################################################################################################
# View products
@view_defaults(route_name='automobiles_viewProducts1')
class AutomobileViewProductsViews(object):
    def __init__(self, request):
        self.request = request

    @view_config(renderer='templates/automobiles_templates/automobiles_viewProducts1.pt')
    def automobiles_viewProducts1(self):
        return {}

    # Response from viewProducts1 page. get params from that page,
    # Perform query operations from database and return this page/pages as response/responses 
    @view_config(request_method='POST', request_param='automobiles_view_submit', renderer='templates/automobiles_templates/automobiles_viewProducts2_page1.pt')
    def automobiles_viewProducts2_page1(self):
        return {}

    # View pages(n)
    @view_config(route_name='automobiles_viewProducts2_page1', renderer='templates/automobiles_templates/automobiles_viewProducts2_page1.pt')
    def automobiles_viewProducts2_page11(self):
        return{}

    @view_config(route_name='automobiles_viewProducts2_page2', renderer='templates/automobiles_templates/automobiles_viewProducts2_page2.pt')
    def automobiles_viewProducts2_page2(self):
        return{}

    @view_config(route_name='automobiles_viewProducts2_page3', renderer='templates/automobiles_templates/automobiles_viewProducts2_page3.pt')
    def automobiles_viewProducts2_page3(self):
        return{}

    @view_config(route_name='automobiles_viewProducts2_page4', renderer='templates/automobiles_templates/automobiles_viewProducts2_page4.pt')
    def automobiles_viewProducts2_page4(self):
        return{}

    @view_config(route_name='automobiles_viewProducts2_page5', renderer='templates/automobiles_templates/automobiles_viewProducts2_page5.pt')
    def automobiles_viewProducts2_page5(self):
        return{}



























# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# Housing views

# ##########################################################################################################
# Create
@view_defaults(route_name='housing_createNewPost')
class HousingCreateNewPostViews(object):
    def __init__(self, request):
        self.request = request


    @view_config(renderer='templates/housing_templates/housing_createNewPost.pt')
    def housing_createNewPost(self):
        return {}

    # # Perform operation on query params, return values and give the user a Response after creation of a new post
    # @view_config(request_method='POST', request_param='')
    # def housing_createNewPost_response(self):
    #     return {}


# ##########################################################################################################
# Modify
@view_defaults(route_name='housing_modifyPost1')
class HousingModifyPostViews(object):
    def __init__(self, request):
        self.request = request

    @view_config(renderer='templates/housing_templates/housing_modifyPost1.pt')
    def housing_modifyPost1(self):
        return {}

    # # response for modifyPost1 page, return this page if correct params were given, else throw error
    # @view_config(request_method='POST', request_param='', renderer='')
    # def housing_modifyPost2(self):
    #     return {}

    # # Perform operation on query params from modifyPost2 page,
    # # return values and give the user a Response after creation of a new post
    # @view_config(request_method='POST', request_param='', renderer='')
    # def housing_modifyPost2_response(self):
    #     return {}

# ##########################################################################################################
# View products
@view_defaults(route_name='housing_viewProducts1')
class HousingViewProductsViews(object):
    def __init__(self, request):
        self.request = request

    @view_config(renderer='templates/housing_templates/housing_viewProducts1.pt')
    def housing_viewProducts1(self):
        return {}

    # Response from viewProducts1 page. get params from that page,
    # Perform query operations from database and return this page/pages as response/responses 
    @view_config(request_method='POST', request_param='housing_view_submit', renderer='templates/housing_templates/housing_viewProducts2_page1.pt')
    def housing_viewProducts2_page1(self):
        return {}

    # View pages(n)
    @view_config(route_name='housing_viewProducts2_page1', renderer='templates/housing_templates/housing_viewProducts2_page1.pt')
    def housing_viewProducts2_page11(self):
        return{}

    @view_config(route_name='housing_viewProducts2_page2', renderer='templates/housing_templates/housing_viewProducts2_page2.pt')
    def housing_viewProducts2_page2(self):
        return{}

    @view_config(route_name='housing_viewProducts2_page3', renderer='templates/housing_templates/housing_viewProducts2_page3.pt')
    def housing_viewProducts2_page3(self):
        return{}

    @view_config(route_name='housing_viewProducts2_page4', renderer='templates/housing_templates/housing_viewProducts2_page4.pt')
    def housing_viewProducts2_page4(self):
        return{}

    @view_config(route_name='housing_viewProducts2_page5', renderer='templates/housing_templates/housing_viewProducts2_page5.pt')
    def housing_viewProducts2_page5(self):
        return{}























# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# Fashion views

# ##########################################################################################################
# Create
@view_defaults(route_name='fashion_createNewPost')
class FashionCreateNewPostViews(object):
    def __init__(self, request):
        self.request = request

    @view_config(renderer='templates/fashion_templates/fashion_createNewPost.pt')
    def fashion_createNewPost(self):
        return {}

    # # Perform operation on query params, return values and give the user a Response after creation of a new post
    # @view_config(request_method='POST', request_param='')
    # def fashion_createNewPost_response(self):
    #     return {}

# ##########################################################################################################
# Modify
@view_defaults(route_name='fashion_modifyPost1')
class FashionModifyPostViews(object):
    def __init__(self, request):
        self.request = request

    @view_config(renderer='templates/fashion_templates/fashion_modifyPost1.pt')
    def fashion_modifyPost1(self):
        return {}

    # # response for modifyPost1 page, return this page if correct params were given, else throw error
    # @view_config(request_method='POST', request_param='', renderer='')
    # def fashion_modifyPost2(self):
    #     return {}

    # # Perform operation on query params from modifyPost2 page,
    # # return values and give the user a Response after creation of a new post
    # @view_config(request_method='POST', request_param='', renderer='')
    # def fashion_modifyPost2_response(self):
    #     return {}

# ##########################################################################################################
# View products
@view_defaults(route_name='fashion_viewProducts1')
class FashionViewProductsViews(object):
    def __init__(self, request):
        self.request = request

    @view_config(renderer='templates/fashion_templates/fashion_viewProducts1.pt')
    def fashion_viewProducts1(self):
        return {}

    # Response from viewProducts1 page. get params from that page,
    # Perform query operations from database and return this page/pages as response/responses 
    @view_config(request_method='POST', request_param='fashion_view_submit', renderer='templates/fashion_templates/fashion_viewProducts2_page1.pt')
    def fashion_viewProducts2_page1(self):
        return {}

    # View pages(n)
    @view_config(route_name='fashion_viewProducts2_page1', renderer='templates/fashion_templates/fashion_viewProducts2_page1.pt')
    def fashion_viewProducts2_page11(self):
        return{}

    @view_config(route_name='fashion_viewProducts2_page2', renderer='templates/fashion_templates/fashion_viewProducts2_page2.pt')
    def fashion_viewProducts2_page2(self):
        return{}

    @view_config(route_name='fashion_viewProducts2_page3', renderer='templates/fashion_templates/fashion_viewProducts2_page3.pt')
    def fashion_viewProducts2_page3(self):
        return{}

    @view_config(route_name='fashion_viewProducts2_page4', renderer='templates/fashion_templates/fashion_viewProducts2_page4.pt')
    def fashion_viewProducts2_page4(self):
        return{}

    @view_config(route_name='fashion_viewProducts2_page5', renderer='templates/fashion_templates/fashion_viewProducts2_page5.pt')
    def fashion_viewProducts2_page5(self):
        return{}








































# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************