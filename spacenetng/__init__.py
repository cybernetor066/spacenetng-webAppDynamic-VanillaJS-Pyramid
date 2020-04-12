from pyramid.config import Configurator
# from pyramid.session import SignedCookieSessionFactory    # Establishing a session factory

def main(global_config, **settings):
    # Establishing a session factory
    # my_session = SignedCookieSessionFactory('itsclassified')
    # Use:
    # config = Configurator()
    # config.set_session_factory(my_session) Or:
    # config = Configurator(settings=settings, session_factory=my_session)

    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_route('home', '/')

    # Electronics category routes
    # ****************************************************************************************
    # Routes for Mother Classes
    config.add_route('electronics_createNewPost', '/electronics_createNewPost')
    config.add_route('electronics_modifyPost1', '/electronics_modifyPost1')
    config.add_route('electronics_modifyPost2', '/electronics_modifyPost2')
    config.add_route('electronics_viewProducts1', '/electronics_viewProducts1')

    # Routes for viewProducts_page(n) pages.
    config.add_route('electronics_viewProducts2_page1', '/electronics_viewProducts2_page1')
    config.add_route('electronics_viewProducts2_page2', '/electronics_viewProducts2_page2')
    config.add_route('electronics_viewProducts2_page3', '/electronics_viewProducts2_page3')
    config.add_route('electronics_viewProducts2_page4', '/electronics_viewProducts2_page4')
    config.add_route('electronics_viewProducts2_page5', '/electronics_viewProducts2_page5')



    # Automobiles category routes
    # ****************************************************************************************
    # Routes for Mother Classes
    config.add_route('automobiles_createNewPost', '/automobiles_createNewPost')
    config.add_route('automobiles_modifyPost1', '/automobiles_modifyPost1')
    config.add_route('automobiles_modifyPost2', '/automobiles_modifyPost2')
    config.add_route('automobiles_viewProducts1', '/automobiles_viewProducts1')

    # Routes for viewProducts_page(n) pages.
    config.add_route('automobiles_viewProducts2_page1', '/automobiles_viewProducts2_page1')
    config.add_route('automobiles_viewProducts2_page2', '/automobiles_viewProducts2_page2')
    config.add_route('automobiles_viewProducts2_page3', '/automobiles_viewProducts2_page3')
    config.add_route('automobiles_viewProducts2_page4', '/automobiles_viewProducts2_page4')
    config.add_route('automobiles_viewProducts2_page5', '/automobiles_viewProducts2_page5')



    # Housing catgegory routes
    # ****************************************************************************************
    # Routes for Mother Classes
    config.add_route('housing_createNewPost', '/housing_createNewPost')
    config.add_route('housing_modifyPost1', '/housing_modifyPost1')
    config.add_route('housing_modifyPost2', '/housing_modifyPost2')
    config.add_route('housing_viewProducts1', '/housing_viewProducts1')

    # Routes for viewProducts_page(n) pages.
    config.add_route('housing_viewProducts2_page1', '/housing_viewProducts2_page1')
    config.add_route('housing_viewProducts2_page2', '/housing_viewProducts2_page2')
    config.add_route('housing_viewProducts2_page3', '/housing_viewProducts2_page3')
    config.add_route('housing_viewProducts2_page4', '/housing_viewProducts2_page4')
    config.add_route('housing_viewProducts2_page5', '/housing_viewProducts2_page5')



    # Fashion category routes
    # ****************************************************************************************
    # Routes for Mother Classes
    config.add_route('fashion_createNewPost', '/fashion_createNewPost')
    config.add_route('fashion_modifyPost1', '/fashion_modifyPost1')
    config.add_route('fashion_modifyPost2', '/fashion_modifyPost2')
    config.add_route('fashion_viewProducts1', '/fashion_viewProducts1')

    # Routes for viewProducts_page(n) pages.
    config.add_route('fashion_viewProducts2_page1', '/fashion_viewProducts2_page1')
    config.add_route('fashion_viewProducts2_page2', '/fashion_viewProducts2_page2')
    config.add_route('fashion_viewProducts2_page3', '/fashion_viewProducts2_page3')
    config.add_route('fashion_viewProducts2_page4', '/fashion_viewProducts2_page4')
    config.add_route('fashion_viewProducts2_page5', '/fashion_viewProducts2_page5')


    # ADS.txt route
    # ****************************************************************************************
    config.add_route('adsDotTxt', '/ads.txt')


    # secureyst/login route
    # ****************************************************************************************
    config.add_route('secureystLogin', '/secureyst/login')

    # secureyst/signup route
    # ****************************************************************************************
    config.add_route('secureystSignup', '/secureyst/signup')


    # secureyst/questionaire route
    # ****************************************************************************************
    config.add_route('secureystQuestionaire', '/secureyst/questionaire')


    # ahsan route
    # ****************************************************************************************
    config.add_route('ahsanListings', '/ahsan/listings')

    # Other configurations
    # ****************************************************************************************
    config.add_static_view(name='static', path='spacenetng:static')
    config.scan('.views')
    return config.make_wsgi_app()