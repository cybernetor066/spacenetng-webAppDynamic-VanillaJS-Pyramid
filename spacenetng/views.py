from pyramid.view import (
    view_config,
    view_defaults
)
from pyramid.response import Response


# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# HOME VIEWS
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************

# ########################################################################################################################
# ########################################################################################################################
# ########################################################################################################################
# Home
@view_defaults(route_name='home')
class HomeViews(object):
    def __init__(self, request):
        self.request = request



    @view_config(renderer='../index.pt')
    def homepage(self):
        # *****************************************************
        import pymongo
        from pymongo import MongoClient
        import gridfs
        from gridfs import GridFS
        # Extract connection string from enviroment variables
        import os
        from dotenv import load_dotenv
        load_dotenv()
        connection_string = os.environ['MY_CONNECTION_STRING']
        # Open database connection and get or create a database called spacenetng_database
        import dns
        client = MongoClient('%s' % connection_string)
        db = client.spacenetng_database


        # Create or open a text based records collection called electronics_text_collection
        electronics_text_collection = db.electronics_text_collection

        # Establish gridfs collection connection
        # Creating or getting an electronics gridfs collection called 'electronics_images_collection'
        # (Getting the GridFS object)
        electronics_image_collection = GridFS(db, "electronics_images_collection")

        # Retrieve document record from database operation
        electronics_collection = electronics_text_collection.find().sort([("_id", pymongo.DESCENDING)]).limit(2) #This returns 2 records

        # Push documents into a list
        electronics_collection_list = []
        for record in electronics_collection:
            electronics_collection_list.append(record)

        electronics_document1 = electronics_collection_list[0]

        # Extracting images
        # For the images for document1
        electronics_document1_images_list_rawFile = []
        for image_name in electronics_document1["Images"]:
            electronics_document1_images_list_rawFile.append(electronics_image_collection.get_last_version(filename=image_name))

        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document1
        #######################

        # For the text strings,
        electronics_collection_document1_productID = electronics_document1["Product ID"]
        electronics_collection_document1_username = electronics_document1["Username"]
        electronics_collection_document1_state = electronics_document1["State"]
        electronics_collection_document1_city = electronics_document1["City"]
        electronics_collection_document1_description = electronics_document1["Description"]
        electronics_collection_document1_mobile = electronics_document1["Mobile"]
        electronics_collection_document1_email = electronics_document1["Email"]
        electronics_collection_document1_category = electronics_document1["Category"]
        electronics_collection_document1_condition = electronics_document1["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        electronics_document1_images_UTF8_list = []

        for raw_image in electronics_document1_images_list_rawFile:
            electronics_document1_binaryImage = raw_image.read()
            electronics_document1_base64Image = codecs.encode(electronics_document1_binaryImage, 'base64')
            electronics_document1_UTF8Image = electronics_document1_base64Image.decode('utf-8')
            electronics_document1_images_UTF8_list.append(electronics_document1_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        electronics_collection_document1_imageA = electronics_document1_images_UTF8_list[0]

        try:
            electronics_collection_document1_imageB = electronics_document1_images_UTF8_list[1]
        except:
            electronics_collection_document1_imageB = electronics_document1_images_UTF8_list[0]

        try:
            electronics_collection_document1_imageC = electronics_document1_images_UTF8_list[2]
        except:
            electronics_collection_document1_imageC = electronics_document1_images_UTF8_list[0]

        try:
            electronics_collection_document1_imageD = electronics_document1_images_UTF8_list[3]
        except:
            electronics_collection_document1_imageD = electronics_document1_images_UTF8_list[0]       
        
        try:
            electronics_collection_document1_imageE = electronics_document1_images_UTF8_list[4]
        except:
            electronics_collection_document1_imageE = electronics_document1_images_UTF8_list[0]

        # next Operation
        electronics_productID1 = electronics_collection_document1_productID
        electronics_username1 = electronics_collection_document1_username
        electronics_state1 = electronics_collection_document1_state 
        electronics_city1 = electronics_collection_document1_city
        electronics_description1 = electronics_collection_document1_description
        electronics_mobile1 = electronics_collection_document1_mobile
        electronics_email1 = electronics_collection_document1_email
        electronics_category1 = electronics_collection_document1_category
        electronics_condition1 = electronics_collection_document1_condition
        electronics_image1A = electronics_collection_document1_imageA
        electronics_image1B = electronics_collection_document1_imageB
        electronics_image1C = electronics_collection_document1_imageC
        electronics_image1D = electronics_collection_document1_imageD
        electronics_image1E = electronics_collection_document1_imageE


        # Create or open a text based records collection called automobiles_text_collection
        automobiles_text_collection = db.automobiles_text_collection

        # Establish gridfs collection connection
        # Creating or getting an automobiles gridfs collection called 'automobiles_images_collection'
        # (Getting the GridFS object)
        automobiles_image_collection = GridFS(db, "automobiles_images_collection")

        # Retrieve document record from database operation
        automobiles_collection = automobiles_text_collection.find().sort([("_id", pymongo.DESCENDING)]).limit(2) #This returns 2 records

        # Push documents into a list
        automobiles_collection_list = []
        for record in automobiles_collection:
            automobiles_collection_list.append(record)

        automobiles_document1 = automobiles_collection_list[0]

        # Extracting images
        # For the images for document1
        automobiles_document1_images_list_rawFile = []
        for image_name in automobiles_document1["Images"]:
            automobiles_document1_images_list_rawFile.append(automobiles_image_collection.get_last_version(filename=image_name))

        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document1
        #######################

        # For the text strings,
        automobiles_collection_document1_productID = automobiles_document1["Product ID"]
        automobiles_collection_document1_username = automobiles_document1["Username"]
        automobiles_collection_document1_state = automobiles_document1["State"]
        automobiles_collection_document1_city = automobiles_document1["City"]
        automobiles_collection_document1_description = automobiles_document1["Description"]
        automobiles_collection_document1_mobile = automobiles_document1["Mobile"]
        automobiles_collection_document1_email = automobiles_document1["Email"]
        automobiles_collection_document1_category = automobiles_document1["Category"]
        automobiles_collection_document1_condition = automobiles_document1["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        automobiles_document1_images_UTF8_list = []

        for raw_image in automobiles_document1_images_list_rawFile:
            automobiles_document1_binaryImage = raw_image.read()
            automobiles_document1_base64Image = codecs.encode(automobiles_document1_binaryImage, 'base64')
            automobiles_document1_UTF8Image = automobiles_document1_base64Image.decode('utf-8')
            automobiles_document1_images_UTF8_list.append(automobiles_document1_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        automobiles_collection_document1_imageA = automobiles_document1_images_UTF8_list[0]

        try:
            automobiles_collection_document1_imageB = automobiles_document1_images_UTF8_list[1]
        except:
            automobiles_collection_document1_imageB = automobiles_document1_images_UTF8_list[0]

        try:
            automobiles_collection_document1_imageC = automobiles_document1_images_UTF8_list[2]
        except:
            automobiles_collection_document1_imageC = automobiles_document1_images_UTF8_list[0]

        try:
            automobiles_collection_document1_imageD = automobiles_document1_images_UTF8_list[3]
        except:
            automobiles_collection_document1_imageD = automobiles_document1_images_UTF8_list[0]       
        
        try:
            automobiles_collection_document1_imageE = automobiles_document1_images_UTF8_list[4]
        except:
            automobiles_collection_document1_imageE = automobiles_document1_images_UTF8_list[0]

        # next Operation
        automobiles_productID1 = automobiles_collection_document1_productID
        automobiles_username1 = automobiles_collection_document1_username
        automobiles_state1 = automobiles_collection_document1_state 
        automobiles_city1 = automobiles_collection_document1_city
        automobiles_description1 = automobiles_collection_document1_description
        automobiles_mobile1 = automobiles_collection_document1_mobile
        automobiles_email1 = automobiles_collection_document1_email
        automobiles_category1 = automobiles_collection_document1_category
        automobiles_condition1 = automobiles_collection_document1_condition
        automobiles_image1A = automobiles_collection_document1_imageA
        automobiles_image1B = automobiles_collection_document1_imageB
        automobiles_image1C = automobiles_collection_document1_imageC
        automobiles_image1D = automobiles_collection_document1_imageD
        automobiles_image1E = automobiles_collection_document1_imageE


        # Create or open a text based records collection called housing_text_collection
        housing_text_collection = db.housing_text_collection

        # Establish gridfs collection connection
        # Creating or getting an housing gridfs collection called 'housing_images_collection'
        # (Getting the GridFS object)
        housing_image_collection = GridFS(db, "housing_images_collection")

        # Retrieve document record from database operation
        housing_collection = housing_text_collection.find().sort([("_id", pymongo.DESCENDING)]).limit(2) #This returns 2 records

        # Push documents into a list
        housing_collection_list = []
        for record in housing_collection:
            housing_collection_list.append(record)

        housing_document1 = housing_collection_list[0]

        # Extracting images
        # For the images for document1
        housing_document1_images_list_rawFile = []
        for image_name in housing_document1["Images"]:
            housing_document1_images_list_rawFile.append(housing_image_collection.get_last_version(filename=image_name))

        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document1
        #######################

        # For the text strings,
        housing_collection_document1_productID = housing_document1["Product ID"]
        housing_collection_document1_username = housing_document1["Username"]
        housing_collection_document1_state = housing_document1["State"]
        housing_collection_document1_city = housing_document1["City"]
        housing_collection_document1_description = housing_document1["Description"]
        housing_collection_document1_mobile = housing_document1["Mobile"]
        housing_collection_document1_email = housing_document1["Email"]
        housing_collection_document1_category = housing_document1["Category"]
        housing_collection_document1_condition = housing_document1["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        housing_document1_images_UTF8_list = []

        for raw_image in housing_document1_images_list_rawFile:
            housing_document1_binaryImage = raw_image.read()
            housing_document1_base64Image = codecs.encode(housing_document1_binaryImage, 'base64')
            housing_document1_UTF8Image = housing_document1_base64Image.decode('utf-8')
            housing_document1_images_UTF8_list.append(housing_document1_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        housing_collection_document1_imageA = housing_document1_images_UTF8_list[0]

        try:
            housing_collection_document1_imageB = housing_document1_images_UTF8_list[1]
        except:
            housing_collection_document1_imageB = housing_document1_images_UTF8_list[0]

        try:
            housing_collection_document1_imageC = housing_document1_images_UTF8_list[2]
        except:
            housing_collection_document1_imageC = housing_document1_images_UTF8_list[0]

        try:
            housing_collection_document1_imageD = housing_document1_images_UTF8_list[3]
        except:
            housing_collection_document1_imageD = housing_document1_images_UTF8_list[0]       
        
        try:
            housing_collection_document1_imageE = housing_document1_images_UTF8_list[4]
        except:
            housing_collection_document1_imageE = housing_document1_images_UTF8_list[0]

        # next Operation
        housing_productID1 = housing_collection_document1_productID
        housing_username1 = housing_collection_document1_username
        housing_state1 = housing_collection_document1_state 
        housing_city1 = housing_collection_document1_city
        housing_description1 = housing_collection_document1_description
        housing_mobile1 = housing_collection_document1_mobile
        housing_email1 = housing_collection_document1_email
        housing_category1 = housing_collection_document1_category
        housing_condition1 = housing_collection_document1_condition
        housing_image1A = housing_collection_document1_imageA
        housing_image1B = housing_collection_document1_imageB
        housing_image1C = housing_collection_document1_imageC
        housing_image1D = housing_collection_document1_imageD
        housing_image1E = housing_collection_document1_imageE


        # Create or open a text based records collection called fashion_text_collection
        fashion_text_collection = db.fashion_text_collection

        # Establish gridfs collection connection
        # Creating or getting an fashion gridfs collection called 'fashion_images_collection'
        # (Getting the GridFS object)
        fashion_image_collection = GridFS(db, "fashion_images_collection")

        # Retrieve document record from database operation
        fashion_collection = fashion_text_collection.find().sort([("_id", pymongo.DESCENDING)]).limit(2) #This returns 2 records

        # Push documents into a list
        fashion_collection_list = []
        for record in fashion_collection:
            fashion_collection_list.append(record)

        fashion_document1 = fashion_collection_list[0]

        # Extracting images
        # For the images for document1
        fashion_document1_images_list_rawFile = []
        for image_name in fashion_document1["Images"]:
            fashion_document1_images_list_rawFile.append(fashion_image_collection.get_last_version(filename=image_name))

        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document1
        #######################

        # For the text strings,
        fashion_collection_document1_productID = fashion_document1["Product ID"]
        fashion_collection_document1_username = fashion_document1["Username"]
        fashion_collection_document1_state = fashion_document1["State"]
        fashion_collection_document1_city = fashion_document1["City"]
        fashion_collection_document1_description = fashion_document1["Description"]
        fashion_collection_document1_mobile = fashion_document1["Mobile"]
        fashion_collection_document1_email = fashion_document1["Email"]
        fashion_collection_document1_category = fashion_document1["Category"]
        fashion_collection_document1_condition = fashion_document1["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        fashion_document1_images_UTF8_list = []

        for raw_image in fashion_document1_images_list_rawFile:
            fashion_document1_binaryImage = raw_image.read()
            fashion_document1_base64Image = codecs.encode(fashion_document1_binaryImage, 'base64')
            fashion_document1_UTF8Image = fashion_document1_base64Image.decode('utf-8')
            fashion_document1_images_UTF8_list.append(fashion_document1_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        fashion_collection_document1_imageA = fashion_document1_images_UTF8_list[0]

        try:
            fashion_collection_document1_imageB = fashion_document1_images_UTF8_list[1]
        except:
            fashion_collection_document1_imageB = fashion_document1_images_UTF8_list[0]

        try:
            fashion_collection_document1_imageC = fashion_document1_images_UTF8_list[2]
        except:
            fashion_collection_document1_imageC = fashion_document1_images_UTF8_list[0]

        try:
            fashion_collection_document1_imageD = fashion_document1_images_UTF8_list[3]
        except:
            fashion_collection_document1_imageD = fashion_document1_images_UTF8_list[0]       
        
        try:
            fashion_collection_document1_imageE = fashion_document1_images_UTF8_list[4]
        except:
            fashion_collection_document1_imageE = fashion_document1_images_UTF8_list[0]

        # next Operation
        fashion_productID1 = fashion_collection_document1_productID
        fashion_username1 = fashion_collection_document1_username
        fashion_state1 = fashion_collection_document1_state 
        fashion_city1 = fashion_collection_document1_city
        fashion_description1 = fashion_collection_document1_description
        fashion_mobile1 = fashion_collection_document1_mobile
        fashion_email1 = fashion_collection_document1_email
        fashion_category1 = fashion_collection_document1_category
        fashion_condition1 = fashion_collection_document1_condition
        fashion_image1A = fashion_collection_document1_imageA
        fashion_image1B = fashion_collection_document1_imageB
        fashion_image1C = fashion_collection_document1_imageC
        fashion_image1D = fashion_collection_document1_imageD
        fashion_image1E = fashion_collection_document1_imageE        


        # clean up client resources and disconnect from mongodb
        client.close()

        return {
            'electronics_productID1' : electronics_productID1,
            'electronics_username1': electronics_username1,
            'electronics_state1' : electronics_state1,
            'electronics_city1' : electronics_city1,
            'electronics_description1' : electronics_description1,
            'electronics_mobile1' : electronics_mobile1,
            'electronics_email1' : electronics_email1,
            'electronics_category1' : electronics_category1,
            'electronics_condition1' : electronics_condition1,
            'electronics_image1A' : electronics_image1A,
            'electronics_image1B' : electronics_image1B,
            'electronics_image1C' : electronics_image1C,
            'electronics_image1D' : electronics_image1D,
            'electronics_image1E' : electronics_image1E,

            'automobiles_productID1' : automobiles_productID1,
            'automobiles_username1': automobiles_username1,
            'automobiles_state1' : automobiles_state1,
            'automobiles_city1' : automobiles_city1,
            'automobiles_description1' : automobiles_description1,
            'automobiles_mobile1' : automobiles_mobile1,
            'automobiles_email1' : automobiles_email1,
            'automobiles_category1' : automobiles_category1,
            'automobiles_condition1' : automobiles_condition1,
            'automobiles_image1A' : automobiles_image1A,
            'automobiles_image1B' : automobiles_image1B,
            'automobiles_image1C' : automobiles_image1C,
            'automobiles_image1D' : automobiles_image1D,
            'automobiles_image1E' : automobiles_image1E,

            'housing_productID1' : housing_productID1,
            'housing_username1': housing_username1,
            'housing_state1' : housing_state1,
            'housing_city1' : housing_city1,
            'housing_description1' : housing_description1,
            'housing_mobile1' : housing_mobile1,
            'housing_email1' : housing_email1,
            'housing_category1' : housing_category1,
            'housing_condition1' : housing_condition1,
            'housing_image1A' : housing_image1A,
            'housing_image1B' : housing_image1B,
            'housing_image1C' : housing_image1C,
            'housing_image1D' : housing_image1D,
            'housing_image1E' : housing_image1E,

            'fashion_productID1' : fashion_productID1,
            'fashion_username1': fashion_username1,
            'fashion_state1' : fashion_state1,
            'fashion_city1' : fashion_city1,
            'fashion_description1' : fashion_description1,
            'fashion_mobile1' : fashion_mobile1,
            'fashion_email1' : fashion_email1,
            'fashion_category1' : fashion_category1,
            'fashion_condition1' : fashion_condition1,
            'fashion_image1A' : fashion_image1A,
            'fashion_image1B' : fashion_image1B,
            'fashion_image1C' : fashion_image1C,
            'fashion_image1D' : fashion_image1D,
            'fashion_image1E' : fashion_image1E,
            
            }










# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ADS_TXT VIEWS
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************
@view_defaults(route_name='adsDotTxt')
class AdsDotTxt(object):
    def __init__(self, request):
        self.request = request

    @view_config(renderer='../ads.txt')
    def AdsTxt(self):
        return {}














# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ELECTRONICS VIEWS
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************

# ########################################################################################################################
# ########################################################################################################################
# ########################################################################################################################
# Create
@view_defaults(route_name='electronics_createNewPost')
class ElectronicsCreateNewPostViews(object):
    def __init__(self, request):
        self.request = request

    # *************************************************************************************************************
    # *************************************************************************************************************
    @view_config(renderer='templates/electronics_templates/electronics_createNewPost.pt')
    def electronics_createNewPost(self):
        return {}


    # *************************************************************************************************************
    # *************************************************************************************************************
    # # Perform operation on query params, send values to the database and give the user a Response after creation 
    # of a new post.
    @view_config(request_method='POST', request_param='electronics_create_submitButton')
    def electronics_createNewPost_response(self):
        from pyramid.httpexceptions import HTTPFound

        # Collect variables from form fields
        # Get text items from form page
        electronics_create_username = self.request.params['electronics_create_username']
        electronics_create_statesList = self.request.params['electronics_create_statesList']
        electronics_create_city = self.request.params['electronics_create_city']
        electronics_create_textarea = self.request.params['electronics_create_textarea']
        electronics_create_mobile = self.request.params['electronics_create_mobile']
        electronics_create_email = self.request.params['electronics_create_email']
        electronics_create_category = self.request.params['electronics_create_category']
        electronics_create_condition = self.request.params['electronics_create_condition']

        # Get images from form page
        electronics_create_images = self.request.POST.getall('electronics_create_images')

        # Use this for our rest API insertion operation
        electronics_create_images_names_list = []
        for electronics_create_image_name in electronics_create_images:
            electronics_create_images_names_list.append(electronics_create_image_name.filename)

        # use this for gridFS insertion operation
        electronics_create_images_list = []
        for electronics_create_image in electronics_create_images:
            electronics_create_images_list.append(electronics_create_image)


        # Create other backend variables
        # create Product ID
        from .myModules import ran_gen_a
        electronics_create_productID = ran_gen_a(8, "AEIOSODMG23")


        # Create a UUID number
        import uuid
        electronics_create_privateUUID = uuid.uuid4()

        # Get specific date
        import datetime
        electronics_create_dateTime = datetime.datetime.utcnow()


        # Create our RES API structure and push data to the RES
        electronics_resAPI_json = {
            "Private UUID": "",
            "Product ID": "",
            "Username": "",
            "State": "",
            "City": "",
            "Description": "",
            "Mobile": "",
            "Email": "",
            "Category": "",
            "Condition": "",
            "Images": [],
            "date": "",
        }


        electronics_resAPI_json["Private UUID"] = electronics_create_privateUUID
        electronics_resAPI_json["Product ID"] = electronics_create_productID
        electronics_resAPI_json["Username"] = electronics_create_username
        electronics_resAPI_json["State"] = electronics_create_statesList
        electronics_resAPI_json["City"] = electronics_create_city
        electronics_resAPI_json["Description"] = electronics_create_textarea
        electronics_resAPI_json["Mobile"] = electronics_create_mobile
        electronics_resAPI_json["Email"] = electronics_create_email
        electronics_resAPI_json["Category"] = electronics_create_category
        electronics_resAPI_json["Condition"] = electronics_create_condition
        electronics_resAPI_json["Images"] = electronics_create_images_names_list
        electronics_resAPI_json["date"] = electronics_create_dateTime



        # Initialise database connection and perform CRUD operation on text and images
        # Perform CRUD operation on text strings
        import pymongo
        from pymongo import MongoClient
        # Extract connection string from enviroment variables
        import os
        from dotenv import load_dotenv
        load_dotenv()
        connection_string = os.environ['MY_CONNECTION_STRING']
        # Open database connection and get or create a database called spacenetng_database
        import dns
        client = MongoClient('%s' % connection_string)
        db = client.spacenetng_database

        # Create or open a text based records collection called electronics_text_collection
        text_collection= db.electronics_text_collection

        # Insert API into database and close our connected client's connection
        text_collection.insert_one(electronics_resAPI_json)


        # Perform CRUD operation on images
        import gridfs
        from gridfs import GridFS

        # Creating or getting an electronics gridfs collection called 'electronics_images_collection'
        # (Getting the GridFS object)
        image_collection = GridFS(db, "electronics_images_collection")

        # Inserting files into gridfs and close our connected client's connection
        for image in electronics_create_images_list:
            image_collection.put(image.file, filename=image.filename)

        # Close our database connection and free up resources.
        client.close()


        # # ############################################################################################
        # # Send private UUID to user's Email using login details and gmail server using inbuilt python email package
        import smtplib, os, sys
        from smtplib import SMTP
        from email.message import EmailMessage
        from dotenv import load_dotenv
        load_dotenv()

        try:
            email_content = ("""\
            Hello %s, thanks for posting on spacenetng platform, an online commercial market place where buyers and sellers
            meet to carry out business transactions. Please be advised, a private user UUID has been created for you which 
            you can use to update or delete your post and it should be kept confidential.\n
            Here is your Seceret hey: %s\n
            For support and enquiries please contact us via our contact details found on our contact page in our website.\n
            Thanks for using this service, we hope to serve you better!!.
            """
            % (electronics_create_username, electronics_create_privateUUID)
            
            )

            msg = EmailMessage()
            msg.set_content(email_content)

            msg['Subject'] = 'Your UUID from Spacenetng'
            msg['From'] = 'spacenetngbase@gmail.com'
            msg['To'] = electronics_create_email

            server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server_ssl.ehlo()

            email = os.environ['MY_EMAIL_ADDRESS']
            passWord = os.environ['MY_EMAIL_PASSWORD']

            server_ssl.login(email, passWord)
            server_ssl.send_message(msg)       
            server_ssl.quit()   # Terminate the SMTP session and free up resources       
            
            # Or And,
            # print('Message sent successfully!!')

        except:
            pass
            # Or
            # print X

        finally:
            pass


        ######################################################
        # Redirect user to view what he/she has just posted                      
        body = (
            "<html style=\"color: green; background-color: whitesmoke; \">"
            "<head><meta http-equiv=\"refresh\" content=\"6;url=/electronics_viewProducts2_page1\"></head>"
            "<body>"
            "<h4>Thanks for using our service, your post has been recorded successfully!! "
            "<br />"
            "You will be redirected shortly.</h4>"
            "</body>"
            "</html>"
        )

        return Response(body)





# ########################################################################################################################
# ########################################################################################################################
# ########################################################################################################################
# Modify
@view_defaults(route_name='electronics_modifyPost1')
class ElectronicsModifyPostViews(object):
    def __init__(self, request):
        self.request = request


    # *************************************************************************************************************
    # *************************************************************************************************************
    @view_config(renderer='templates/electronics_templates/electronics_modifyPost1.pt')
    def electronics_modifyPost1(self):
        return {'user_warning': ''}



    # *************************************************************************************************************
    # *************************************************************************************************************
    # Handler method for modifyPost1 page form field input validation for edit mode
    # Redirect to modifyPost2 page if valid private uuid was given, else throw error.
    @view_config(request_method='POST', request_param='electronics_modify1_editButton', renderer='templates/electronics_templates/electronics_modifyPost1.pt')
    def electronics_modifyPost1_update_handler(self):
        from pyramid.renderers import render
        from pyramid.response import Response
        from pyramid.httpexceptions import HTTPFound
        import pymongo
        from pymongo import MongoClient
        from bson import ObjectId
        from uuid import UUID
        # Extract connection string from enviroment variables
        import os
        from dotenv import load_dotenv
        load_dotenv()
        connection_string = os.environ['MY_CONNECTION_STRING']
        # Open database connection and get or create a database called spacenetng_database
        import dns
        client = MongoClient('%s' % connection_string)
        db = client.spacenetng_database

        # Create or open a text based records collection called electronics_text_collection
        text_collection= db.electronics_text_collection


        electronics_update_privateUUID = self.request.params['electronics_modify1_privateUUID']

        try:
            text_collection.find_one({'Private UUID': UUID(electronics_update_privateUUID)})
            result1 = render('templates/electronics_templates/electronics_modifyPost2.pt' , {'private_UUID': electronics_update_privateUUID, 'user_warning': ''}, request=self.request)
            return Response(result1)

        except:
            # Re-render form page and throw an error message saying "Invalid Private UUID entered!!"
            return {'user_warning': 'Invalid Private UUID entered!!'}

        client.close()
            



    # *************************************************************************************************************
    # *************************************************************************************************************
    # Handler method for modifyPost1 page form field input validation for delete mode
    @view_config(request_method='POST', request_param='electronics_modify1_deleteButton', renderer='templates/electronics_templates/electronics_modifyPost1.pt')
    def electronics_modifyPost1_delete_handler(self):
        from pyramid.renderers import render
        from pyramid.response import Response
        from pyramid.httpexceptions import HTTPFound
        import pymongo
        from pymongo import MongoClient
        from bson import ObjectId
        from uuid import UUID
        # Extract connection string from enviroment variables
        import os
        from dotenv import load_dotenv
        load_dotenv()
        connection_string = os.environ['MY_CONNECTION_STRING']
        # Open database connection and get or create a database called spacenetng_database
        import dns
        client = MongoClient('%s' % connection_string)
        db = client.spacenetng_database

        # Create or open a text based records collection called electronics_text_collection
        text_collection= db.electronics_text_collection


        # Perform CRUD operation on images
        import gridfs
        from gridfs import GridFS

        # Creating or getting an electronics gridfs collection called 'electronics_images_collection'
        # (Getting the GridFS object)
        image_collection = GridFS(db, "electronics_images_collection")


        electronics_delete_privateUUID = self.request.params['electronics_modify1_privateUUID']

        # # Delete operation................................................................................
        # Perform a find() query operation on a document using the private UUID for delete permision,
        # and then obtain its "_id" field.

        try:
            # Delete operation on the main text collection initialisation
            res0 = text_collection.find_one({'Private UUID': UUID(electronics_delete_privateUUID)})
            res1 = res0['_id']    # Obtaining the '_id' attribute diff from that of gridfs

            # Delete operation On image collection
            # Obtain the '_id' values each on all images from the image collection
            # then perform the delete and/or replacement operation

            # Delete images in collection first before deleting the actual collection
            image_names_list_toDelete = res0['Images']

            for name in image_names_list_toDelete:
                res2 = image_collection.find_one({'filename': name})
                res3 = res2._id    # Obtaining the '_id' attribute
                image_collection.delete(ObjectId(res3))  # Delete format for files in gridfs

            # text collection delete
            text_collection.delete_one({'_id': ObjectId(res1)})
            client.close()

            body = (
                "<html style=\"color: green; background-color: whitesmoke; \">"
                "<head><meta http-equiv=\"refresh\" content=\"6;url=/\"></head>"
                "<body>"
                "<h4>Thanks for using our service, your post has been deleted successfully!! "
                "<br />"
                "You will be redirected shortly.</h4>"
                "</body>"
                "</html>"
            )

            return Response(body)


        except:
            # Re-render form page and throw an error message saying "Invalid Private UUID entered!!"
            return {'user_warning': 'Invalid Private UUID entered!!'}






    # *************************************************************************************************************
    # *************************************************************************************************************
    # # response for modifyPost1 page, return this page if correct params were given in modifyPost1 page.
    @view_config(route_name='electronics_modifyPost2', renderer='templates/electronics_templates/electronics_modifyPost2.pt')
    def electronics_modifyPost2(self):
        return {}



    # *************************************************************************************************************
    # *************************************************************************************************************
    # Perform operation on query params from modifyPost2 page,
    # return values and give the user a Response after creation of a new post
    @view_config(request_method='POST', request_param='electronics_update_submitButton')
    def electronics_modifyPost2_response(self):
        # -----------------------------------------------------------------------------------------------------------------
        # Updating and deleting records in database
        from pyramid.response import Response
        from pyramid.httpexceptions import HTTPFound
        import pymongo
        from pymongo import MongoClient
        from bson import ObjectId
        from uuid import UUID
        # Extract connection string from enviroment variables
        import os
        from dotenv import load_dotenv
        load_dotenv()
        connection_string = os.environ['MY_CONNECTION_STRING']
        # Open database connection and get or create a database called spacenetng_database
        import dns
        client = MongoClient('%s' % connection_string)
        db = client.spacenetng_database

        # Create or open a text based records collection called electronics_text_collection
        text_collection= db.electronics_text_collection


        # Perform CRUD operation on images
        import gridfs
        from gridfs import GridFS

        # Creating or getting an electronics gridfs collection called 'electronics_images_collection'
        # (Getting the GridFS object)
        image_collection = GridFS(db, "electronics_images_collection")


        # Perform CRUD Operation
        # Get specific date
        import datetime
        electronics_update_dateTime = datetime.datetime.utcnow()

        electronics_resAPI_json = {
            "Username": "",
            "State": "",
            "City": "",
            "Description": "",
            "Mobile": "",
            "Email": "",
            "Category": "",
            "Condition": "",
            "Images": [],
            "date": "",
            }

        #######################
        # Collect variables from form fields
        #######################

        # Get text items from form page
        electronics_update_username = self.request.params['electronics_update_username']
        electronics_update_statesList = self.request.params['electronics_update_statesList']
        electronics_update_city = self.request.params['electronics_update_city']
        electronics_update_textarea = self.request.params['electronics_update_textarea']
        electronics_update_mobile = self.request.params['electronics_update_mobile']
        electronics_update_email = self.request.params['electronics_update_email']
        electronics_update_category = self.request.params['electronics_update_category']
        electronics_update_condition = self.request.params['electronics_update_condition']
           
        # Get images from form page
        electronics_update_images = self.request.POST.getall('electronics_update_images')

        # Use this for our rest API insertion operation
        electronics_update_images_names_list = []
        for electronics_update_image_name in electronics_update_images:
            electronics_update_images_names_list.append(electronics_update_image_name.filename)

        # use this for gridFS insertion operation
        electronics_update_images_list = []
        for electronics_update_image in electronics_update_images:
            electronics_update_images_list.append(electronics_update_image)



        electronics_resAPI_json["Username"] = electronics_update_username
        electronics_resAPI_json["State"] = electronics_update_statesList
        electronics_resAPI_json["City"] = electronics_update_city
        electronics_resAPI_json["Description"] = electronics_update_textarea
        electronics_resAPI_json["Mobile"] = electronics_update_mobile
        electronics_resAPI_json["Email"] = electronics_update_email
        electronics_resAPI_json["Category"] = electronics_update_category
        electronics_resAPI_json["Condition"] = electronics_update_condition
        electronics_resAPI_json["Images"] = electronics_update_images_names_list
        electronics_resAPI_json["date"] = electronics_update_dateTime




        # Update operation.........................................................................
        # Update API in database and close our connected client's connection
        # Perform a find() query operation on a document using the private UUID to locate the particular document,
        # and then obtain its "_id" field.
        electronics_update_privateUUID = self.request.params['electronics_update_privateUUID']

        # Inititalise overall collection query using the text collection
        res1 = text_collection.find_one({'Private UUID': UUID(electronics_update_privateUUID)})
        res2 = res1['_id']         # Obtaining the '_id' attribute diff from that of gridfs


        # Before inserting files, query for previous images previously inside database,
        # delete all images there and replace/update with the new one.

        # Obtain the '_id' values each on all images from the image collection
        # then perform the delete operation followed by the replacement operation
        image_names_list_toDelete = res1['Images']

        # Delete images already present first before updating the main collection
        # delete image collection
        for name in image_names_list_toDelete:
            res3 = image_collection.find_one({'filename': name})
            res4 = res3._id    # Obtaining the '_id' attribute
            image_collection.delete(ObjectId(res4))  # Delete format for files in gridfs


        # Main text collection update
        text_collection.update_one({'_id': ObjectId(res2)}, {"$set": electronics_resAPI_json})

        # then also update the image collection with the new images
        for image in electronics_update_images_list:
            image_collection.put(image.file, filename=image.filename) # The update operation

            

        # Close our database connection and free up resources.
        client.close()

        body = (
            "<html style=\"color: green; background-color: whitesmoke; \">"
            "<head><meta http-equiv=\"refresh\" content=\"6;url=/\"></head>"
            "<body>"
            "<h4>Thanks for using our service, your post has been updated successfully!! "
            "<br />"
            "You will be redirected shortly.</h4>"
            "</body>"
            "</html>"
        )

        return Response(body)



# ########################################################################################################################
# ########################################################################################################################
# ########################################################################################################################
# View products
@view_defaults(route_name='electronics_viewProducts1')
class ElectronicsViewProductsViews(object):
    def __init__(self, request):
        self.request = request


    # *************************************************************************************************************
    # *************************************************************************************************************
    @view_config(renderer='templates/electronics_templates/electronics_viewProducts1.pt')
    def electronics_viewProducts1(self):
        return {}


    # *************************************************************************************************************
    # *************************************************************************************************************
    # Response from viewProducts1 page and validate with records in database 
    @view_config(request_method='POST', request_param='electronics_view_submit')
    def electronics_viewProducts2_page1A(self):
        from pyramid.httpexceptions import HTTPFound
        # Perform some database matching on sub categories and redirect to the appropriate renderer.
        return HTTPFound(location='electronics_viewProducts2_page1')


    # *************************************************************************************************************
    # *************************************************************************************************************
    @view_config(route_name='electronics_viewProducts2_page1', renderer='templates/electronics_templates/electronics_viewProducts2_page1.pt')
    def electronics_viewProducts2_page1B(self):
        import pymongo
        from pymongo import MongoClient
        import gridfs
        from gridfs import GridFS
        # Extract connection string from enviroment variables
        import os
        from dotenv import load_dotenv
        load_dotenv()
        connection_string = os.environ['MY_CONNECTION_STRING']
        # Open database connection and get or create a database called spacenetng_database
        import dns
        client1 = MongoClient('%s' % connection_string)
        db = client1.spacenetng_database

        # Create or open a text based records collection called electronics_text_collection
        text_collection_electronics = db.electronics_text_collection

        # Establish gridfs collection connection
        # Creating or getting an electronics gridfs collection called 'electronics_images_collection'
        # (Getting the GridFS object)
        image_collection_electronics = GridFS(db, "electronics_images_collection")

        # Retrieve document record from database operation
        electronics_collection = text_collection_electronics.find().sort([("_id", pymongo.DESCENDING)]).limit(5) #This returns 25 records

        # Push documents into a list
        electronics_collection_list = []

        for record in electronics_collection:
            electronics_collection_list.append(record)

        document1 = electronics_collection_list[0]
        document2 = electronics_collection_list[1]
        document3 = electronics_collection_list[2]
        document4 = electronics_collection_list[3]
        document5 = electronics_collection_list[4]
        

        # Extracting images
        # The images for document1
        document1_images_list_rawFile = []
        for image_name in document1["Images"]:
            document1_images_list_rawFile.append(image_collection_electronics.get_last_version(filename=image_name))

        # For the images for document2
        document2_images_list_rawFile = []
        for image_name in document2["Images"]:
            document2_images_list_rawFile.append(image_collection_electronics.get_last_version(filename=image_name))

        # The images for document3
        document3_images_list_rawFile = []
        for image_name in document3["Images"]:
            document3_images_list_rawFile.append(image_collection_electronics.get_last_version(filename=image_name))

        # The images for document4
        document4_images_list_rawFile = []
        for image_name in document4["Images"]:
            document4_images_list_rawFile.append(image_collection_electronics.get_last_version(filename=image_name))

        # The images for document5
        document5_images_list_rawFile = []
        for image_name in document5["Images"]:
            document5_images_list_rawFile.append(image_collection_electronics.get_last_version(filename=image_name))



        ##############################################
        # Collecting record from individual documents
        ##############################################
        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document1
        #######################

        # For the text strings,
        electronics_collection_document1_productID = document1["Product ID"]
        electronics_collection_document1_username = document1["Username"]
        electronics_collection_document1_state = document1["State"]
        electronics_collection_document1_city = document1["City"]
        electronics_collection_document1_description = document1["Description"]
        electronics_collection_document1_mobile = document1["Mobile"]
        electronics_collection_document1_email = document1["Email"]
        electronics_collection_document1_category = document1["Category"]
        electronics_collection_document1_condition = document1["Condition"]



        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document1_images_UTF8_list = []

        for raw_image in document1_images_list_rawFile:
            document1_binaryImage = raw_image.read()
            document1_base64Image = codecs.encode(document1_binaryImage, 'base64')
            document1_UTF8Image = document1_base64Image.decode('utf-8')
            document1_images_UTF8_list.append(document1_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        electronics_collection_document1_imageA = document1_images_UTF8_list[0]

        try:
            electronics_collection_document1_imageB = document1_images_UTF8_list[1]
        except:
            electronics_collection_document1_imageB = document1_images_UTF8_list[0]

        try:
            electronics_collection_document1_imageC = document1_images_UTF8_list[2]
        except:
            electronics_collection_document1_imageC = document1_images_UTF8_list[0]

        try:
            electronics_collection_document1_imageD = document1_images_UTF8_list[3]
        except:
            electronics_collection_document1_imageD = document1_images_UTF8_list[0]       
        
        try:
            electronics_collection_document1_imageE = document1_images_UTF8_list[4]
        except:
            electronics_collection_document1_imageE = document1_images_UTF8_list[0]





        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document2
        #######################

        # For the text strings,
        electronics_collection_document2_productID = document2["Product ID"]
        electronics_collection_document2_username = document2["Username"]
        electronics_collection_document2_state = document2["State"]
        electronics_collection_document2_city = document2["City"]
        electronics_collection_document2_description = document2["Description"]
        electronics_collection_document2_mobile = document2["Mobile"]
        electronics_collection_document2_email = document2["Email"]
        electronics_collection_document2_category = document2["Category"]
        electronics_collection_document2_condition = document2["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document2_images_UTF8_list = []

        for raw_image in document2_images_list_rawFile:
            document2_binaryImage = raw_image.read()
            document2_base64Image = codecs.encode(document2_binaryImage, 'base64')
            document2_UTF8Image = document2_base64Image.decode('utf-8')
            document2_images_UTF8_list.append(document2_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        electronics_collection_document2_imageA = document2_images_UTF8_list[0]

        try:
            electronics_collection_document2_imageB = document2_images_UTF8_list[1]
        except:
            electronics_collection_document2_imageB = document2_images_UTF8_list[0]

        try:
            electronics_collection_document2_imageC = document2_images_UTF8_list[2]
        except:
            electronics_collection_document2_imageC = document2_images_UTF8_list[0]

        try:
            electronics_collection_document2_imageD = document2_images_UTF8_list[3]
        except:
            electronics_collection_document2_imageD = document2_images_UTF8_list[0]       
        
        try:
            electronics_collection_document2_imageE = document2_images_UTF8_list[4]
        except:
            electronics_collection_document2_imageE = document2_images_UTF8_list[0]





        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document3
        #######################

        # For the text strings,
        electronics_collection_document3_productID = document3["Product ID"]
        electronics_collection_document3_username = document3["Username"]
        electronics_collection_document3_state = document3["State"]
        electronics_collection_document3_city = document3["City"]
        electronics_collection_document3_description = document3["Description"]
        electronics_collection_document3_mobile = document3["Mobile"]
        electronics_collection_document3_email = document3["Email"]
        electronics_collection_document3_category = document3["Category"]
        electronics_collection_document3_condition = document3["Condition"]

        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document3_images_UTF8_list = []

        for raw_image in document3_images_list_rawFile:
            document3_binaryImage = raw_image.read()
            document3_base64Image = codecs.encode(document3_binaryImage, 'base64')
            document3_UTF8Image = document3_base64Image.decode('utf-8')
            document3_images_UTF8_list.append(document3_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        electronics_collection_document3_imageA = document3_images_UTF8_list[0]

        try:
            electronics_collection_document3_imageB = document3_images_UTF8_list[1]
        except:
            electronics_collection_document3_imageB = document3_images_UTF8_list[0]

        try:
            electronics_collection_document3_imageC = document3_images_UTF8_list[2]
        except:
            electronics_collection_document3_imageC = document3_images_UTF8_list[0]

        try:
            electronics_collection_document3_imageD = document3_images_UTF8_list[3]
        except:
            electronics_collection_document3_imageD = document3_images_UTF8_list[0]       
        
        try:
            electronics_collection_document3_imageE = document3_images_UTF8_list[4]
        except:
            electronics_collection_document3_imageE = document3_images_UTF8_list[0]





        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document4
        #######################

        # For the text strings,
        electronics_collection_document4_productID = document4["Product ID"]
        electronics_collection_document4_username = document4["Username"]
        electronics_collection_document4_state = document4["State"]
        electronics_collection_document4_city = document4["City"]
        electronics_collection_document4_description = document4["Description"]
        electronics_collection_document4_mobile = document4["Mobile"]
        electronics_collection_document4_email = document4["Email"]
        electronics_collection_document4_category = document4["Category"]
        electronics_collection_document4_condition = document4["Condition"]

        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document4_images_UTF8_list = []

        for raw_image in document4_images_list_rawFile:
            document4_binaryImage = raw_image.read()
            document4_base64Image = codecs.encode(document4_binaryImage, 'base64')
            document4_UTF8Image = document4_base64Image.decode('utf-8')
            document4_images_UTF8_list.append(document4_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        electronics_collection_document4_imageA = document4_images_UTF8_list[0]

        try:
            electronics_collection_document4_imageB = document4_images_UTF8_list[1]
        except:
            electronics_collection_document4_imageB = document4_images_UTF8_list[0]

        try:
            electronics_collection_document4_imageC = document4_images_UTF8_list[2]
        except:
            electronics_collection_document4_imageC = document4_images_UTF8_list[0]

        try:
            electronics_collection_document4_imageD = document4_images_UTF8_list[3]
        except:
            electronics_collection_document4_imageD = document4_images_UTF8_list[0]       
        
        try:
            electronics_collection_document4_imageE = document4_images_UTF8_list[4]
        except:
            electronics_collection_document4_imageE = document4_images_UTF8_list[0]




        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document5
        #######################

        # For the text strings,
        electronics_collection_document5_productID = document5["Product ID"]
        electronics_collection_document5_username = document5["Username"]
        electronics_collection_document5_state = document5["State"]
        electronics_collection_document5_city = document5["City"]
        electronics_collection_document5_description = document5["Description"]
        electronics_collection_document5_mobile = document5["Mobile"]
        electronics_collection_document5_email = document5["Email"]
        electronics_collection_document5_category = document5["Category"]
        electronics_collection_document5_condition = document5["Condition"]

        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document5_images_UTF8_list = []

        for raw_image in document5_images_list_rawFile:
            document5_binaryImage = raw_image.read()
            document5_base64Image = codecs.encode(document5_binaryImage, 'base64')
            document5_UTF8Image = document5_base64Image.decode('utf-8')
            document5_images_UTF8_list.append(document5_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        electronics_collection_document5_imageA = document5_images_UTF8_list[0]

        try:
            electronics_collection_document5_imageB = document5_images_UTF8_list[1]
        except:
            electronics_collection_document5_imageB = document5_images_UTF8_list[0]

        try:
            electronics_collection_document5_imageC = document5_images_UTF8_list[2]
        except:
            electronics_collection_document5_imageC = document5_images_UTF8_list[0]

        try:
            electronics_collection_document5_imageD = document5_images_UTF8_list[3]
        except:
            electronics_collection_document5_imageD = document5_images_UTF8_list[0]       
        
        try:
            electronics_collection_document5_imageE = document5_images_UTF8_list[4]
        except:
            electronics_collection_document5_imageE = document5_images_UTF8_list[0]

        
        # Close our database connection and free up resources.
        client1.close()

        # Pack all return variables into a JSON Structure and use for return
        return {
            
            'productID1' : electronics_collection_document1_productID,
            'username1' : electronics_collection_document1_username,
            'state1' : electronics_collection_document1_state,
            'city1' : electronics_collection_document1_city,
            'description1' : electronics_collection_document1_description,
            'mobile1' : electronics_collection_document1_mobile,
            'email1' : electronics_collection_document1_email,
            'category1' : electronics_collection_document1_category,
            'condition1': electronics_collection_document1_condition,
            'image1A' : electronics_collection_document1_imageA,
            'image1B' : electronics_collection_document1_imageB,
            'image1C' : electronics_collection_document1_imageC,
            'image1D': electronics_collection_document1_imageD,
            'image1E': electronics_collection_document1_imageE,

            'productID2' : electronics_collection_document2_productID,
            'username2' : electronics_collection_document2_username,
            'state2' : electronics_collection_document2_state,
            'city2' : electronics_collection_document2_city,
            'description2' : electronics_collection_document2_description,
            'mobile2' : electronics_collection_document2_mobile,
            'email2' : electronics_collection_document2_email,
            'category2' : electronics_collection_document2_category,
            'condition2': electronics_collection_document2_condition,
            'image2A' : electronics_collection_document2_imageA,
            'image2B' : electronics_collection_document2_imageB,
            'image2C' : electronics_collection_document2_imageC,
            'image2D': electronics_collection_document2_imageD,
            'image2E': electronics_collection_document2_imageE,

            'productID3' : electronics_collection_document3_productID,
            'username3' : electronics_collection_document3_username,
            'state3' : electronics_collection_document3_state,
            'city3' : electronics_collection_document3_city,
            'description3' : electronics_collection_document3_description,
            'mobile3' : electronics_collection_document3_mobile,
            'email3' : electronics_collection_document3_email,
            'category3' : electronics_collection_document3_category,
            'condition3': electronics_collection_document3_condition,
            'image3A' : electronics_collection_document3_imageA,
            'image3B' : electronics_collection_document3_imageB,
            'image3C' : electronics_collection_document3_imageC,
            'image3D': electronics_collection_document3_imageD,
            'image3E': electronics_collection_document3_imageE,

            'productID4' : electronics_collection_document4_productID,
            'username4' : electronics_collection_document4_username,
            'state4' : electronics_collection_document4_state,
            'city4' : electronics_collection_document4_city,
            'description4' : electronics_collection_document4_description,
            'mobile4' : electronics_collection_document4_mobile,
            'email4' : electronics_collection_document4_email,
            'category4' : electronics_collection_document4_category,
            'condition4': electronics_collection_document4_condition,
            'image4A' : electronics_collection_document4_imageA,
            'image4B' : electronics_collection_document4_imageB,
            'image4C' : electronics_collection_document4_imageC,
            'image4D': electronics_collection_document4_imageD,
            'image4E': electronics_collection_document4_imageE,

            'productID5' : electronics_collection_document5_productID,
            'username5' : electronics_collection_document5_username,
            'state5' : electronics_collection_document5_state,
            'city5' : electronics_collection_document5_city,
            'description5' : electronics_collection_document5_description,
            'mobile5' : electronics_collection_document5_mobile,
            'email5' : electronics_collection_document5_email,
            'category5' : electronics_collection_document5_category,
            'condition5': electronics_collection_document5_condition,
            'image5A' : electronics_collection_document5_imageA,
            'image5B' : electronics_collection_document5_imageB,
            'image5C' : electronics_collection_document5_imageC,
            'image5D': electronics_collection_document5_imageD,
            'image5E': electronics_collection_document5_imageE,
            }


    # View pages....(n)
    # *************************************************************************************************************
    # *************************************************************************************************************
    @view_config(route_name='electronics_viewProducts2_page2', renderer='templates/electronics_templates/electronics_viewProducts2_page2.pt')
    def electronics_viewProducts2_page2(self):
        import pymongo
        from pymongo import MongoClient
        import gridfs
        from gridfs import GridFS
        # Extract connection string from enviroment variables
        import os
        from dotenv import load_dotenv
        load_dotenv()
        connection_string = os.environ['MY_CONNECTION_STRING']
        # Open database connection and get or create a database called spacenetng_database
        import dns
        client2 = MongoClient('%s' % connection_string)
        db = client2.spacenetng_database

        # Create or open a text based records collection called electronics_text_collection
        text_collection_electronics = db.electronics_text_collection

        # Establish gridfs collection connection
        # Creating or getting an electronics gridfs collection called 'electronics_images_collection'
        # (Getting the GridFS object)
        image_collection_electronics = GridFS(db, "electronics_images_collection")

        # Retrieve document record from database operation
        electronics_collection = text_collection_electronics.find().sort([("_id", pymongo.DESCENDING)]).skip(5).limit(5) #This returns 25 records

        # Push documents into a list
        electronics_collection_list = []

        for record in electronics_collection:
            electronics_collection_list.append(record)

        document6 = electronics_collection_list[0]
        document7 = electronics_collection_list[1]
        document8 = electronics_collection_list[2]
        document9 = electronics_collection_list[3]
        document10 = electronics_collection_list[4]



        # The images for document6
        document6_images_list_rawFile = []
        for image_name in document6["Images"]:
            document6_images_list_rawFile.append(image_collection_electronics.get_last_version(filename=image_name))

        # The images for document7
        document7_images_list_rawFile = []
        for image_name in document7["Images"]:
            document7_images_list_rawFile.append(image_collection_electronics.get_last_version(filename=image_name))

        # The images for document8
        document8_images_list_rawFile = []
        for image_name in document8["Images"]:
            document8_images_list_rawFile.append(image_collection_electronics.get_last_version(filename=image_name))

        # The images for document9
        document9_images_list_rawFile = []
        for image_name in document9["Images"]:
            document9_images_list_rawFile.append(image_collection_electronics.get_last_version(filename=image_name))

        # The images for document10
        document10_images_list_rawFile = []
        for image_name in document10["Images"]:
            document10_images_list_rawFile.append(image_collection_electronics.get_last_version(filename=image_name))


        ##############################################
        # Collecting record from individual documents
        ##############################################
        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document6
        #######################

        # For the text strings,
        electronics_collection_document6_productID = document6["Product ID"]
        electronics_collection_document6_username = document6["Username"]
        electronics_collection_document6_state = document6["State"]
        electronics_collection_document6_city = document6["City"]
        electronics_collection_document6_description = document6["Description"]
        electronics_collection_document6_mobile = document6["Mobile"]
        electronics_collection_document6_email = document6["Email"]
        electronics_collection_document6_category = document6["Category"]
        electronics_collection_document6_condition = document6["Condition"]



        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document6_images_UTF8_list = []

        for raw_image in document6_images_list_rawFile:
            document6_binaryImage = raw_image.read()
            document6_base64Image = codecs.encode(document6_binaryImage, 'base64')
            document6_UTF8Image = document6_base64Image.decode('utf-8')
            document6_images_UTF8_list.append(document6_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        electronics_collection_document6_imageA = document6_images_UTF8_list[0]

        try:
            electronics_collection_document6_imageB = document6_images_UTF8_list[1]
        except:
            electronics_collection_document6_imageB = document6_images_UTF8_list[0]

        try:
            electronics_collection_document6_imageC = document6_images_UTF8_list[2]
        except:
            electronics_collection_document6_imageC = document6_images_UTF8_list[0]

        try:
            electronics_collection_document6_imageD = document6_images_UTF8_list[3]
        except:
            electronics_collection_document6_imageD = document6_images_UTF8_list[0]       
        
        try:
            electronics_collection_document6_imageE = document6_images_UTF8_list[4]
        except:
            electronics_collection_document6_imageE = document6_images_UTF8_list[0]





        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document7
        #######################

        # For the text strings,
        electronics_collection_document7_productID = document7["Product ID"]
        electronics_collection_document7_username = document7["Username"]
        electronics_collection_document7_state = document7["State"]
        electronics_collection_document7_city = document7["City"]
        electronics_collection_document7_description = document7["Description"]
        electronics_collection_document7_mobile = document7["Mobile"]
        electronics_collection_document7_email = document7["Email"]
        electronics_collection_document7_category = document7["Category"]
        electronics_collection_document7_condition = document7["Condition"]



        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document7_images_UTF8_list = []

        for raw_image in document7_images_list_rawFile:
            document7_binaryImage = raw_image.read()
            document7_base64Image = codecs.encode(document7_binaryImage, 'base64')
            document7_UTF8Image = document7_base64Image.decode('utf-8')
            document7_images_UTF8_list.append(document7_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        electronics_collection_document7_imageA = document7_images_UTF8_list[0]

        try:
            electronics_collection_document7_imageB = document7_images_UTF8_list[1]
        except:
            electronics_collection_document7_imageB = document7_images_UTF8_list[0]

        try:
            electronics_collection_document7_imageC = document7_images_UTF8_list[2]
        except:
            electronics_collection_document7_imageC = document7_images_UTF8_list[0]

        try:
            electronics_collection_document7_imageD = document7_images_UTF8_list[3]
        except:
            electronics_collection_document7_imageD = document7_images_UTF8_list[0]       
        
        try:
            electronics_collection_document7_imageE = document7_images_UTF8_list[4]
        except:
            electronics_collection_document7_imageE = document7_images_UTF8_list[0]




        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document8
        #######################

        # For the text strings,
        electronics_collection_document8_productID = document8["Product ID"]
        electronics_collection_document8_username = document8["Username"]
        electronics_collection_document8_state = document8["State"]
        electronics_collection_document8_city = document8["City"]
        electronics_collection_document8_description = document8["Description"]
        electronics_collection_document8_mobile = document8["Mobile"]
        electronics_collection_document8_email = document8["Email"]
        electronics_collection_document8_category = document8["Category"]
        electronics_collection_document8_condition = document8["Condition"]

   
        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document8_images_UTF8_list = []

        for raw_image in document8_images_list_rawFile:
            document8_binaryImage = raw_image.read()
            document8_base64Image = codecs.encode(document8_binaryImage, 'base64')
            document8_UTF8Image = document8_base64Image.decode('utf-8')
            document8_images_UTF8_list.append(document8_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        electronics_collection_document8_imageA = document8_images_UTF8_list[0]

        try:
            electronics_collection_document8_imageB = document8_images_UTF8_list[1]
        except:
            electronics_collection_document8_imageB = document8_images_UTF8_list[0]

        try:
            electronics_collection_document8_imageC = document8_images_UTF8_list[2]
        except:
            electronics_collection_document8_imageC = document8_images_UTF8_list[0]

        try:
            electronics_collection_document8_imageD = document8_images_UTF8_list[3]
        except:
            electronics_collection_document8_imageD = document8_images_UTF8_list[0]       
        
        try:
            electronics_collection_document8_imageE = document8_images_UTF8_list[4]
        except:
            electronics_collection_document8_imageE = document8_images_UTF8_list[0]




        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document9
        #######################

        # For the text strings,
        electronics_collection_document9_productID = document9["Product ID"]
        electronics_collection_document9_username = document9["Username"]
        electronics_collection_document9_state = document9["State"]
        electronics_collection_document9_city = document9["City"]
        electronics_collection_document9_description = document9["Description"]
        electronics_collection_document9_mobile = document9["Mobile"]
        electronics_collection_document9_email = document9["Email"]
        electronics_collection_document9_category = document9["Category"]
        electronics_collection_document9_condition = document9["Condition"]



        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document9_images_UTF8_list = []

        for raw_image in document9_images_list_rawFile:
            document9_binaryImage = raw_image.read()
            document9_base64Image = codecs.encode(document9_binaryImage, 'base64')
            document9_UTF8Image = document9_base64Image.decode('utf-8')
            document9_images_UTF8_list.append(document9_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        electronics_collection_document9_imageA = document9_images_UTF8_list[0]

        try:
            electronics_collection_document9_imageB = document9_images_UTF8_list[1]
        except:
            electronics_collection_document9_imageB = document9_images_UTF8_list[0]

        try:
            electronics_collection_document9_imageC = document9_images_UTF8_list[2]
        except:
            electronics_collection_document9_imageC = document9_images_UTF8_list[0]

        try:
            electronics_collection_document9_imageD = document9_images_UTF8_list[3]
        except:
            electronics_collection_document9_imageD = document9_images_UTF8_list[0]       
        
        try:
            electronics_collection_document9_imageE = document9_images_UTF8_list[4]
        except:
            electronics_collection_document9_imageE = document9_images_UTF8_list[0]


        # For document10
        #######################

        # For the text strings,
        electronics_collection_document10_productID = document10["Product ID"]
        electronics_collection_document10_username = document10["Username"]
        electronics_collection_document10_state = document10["State"]
        electronics_collection_document10_city = document10["City"]
        electronics_collection_document10_description = document10["Description"]
        electronics_collection_document10_mobile = document10["Mobile"]
        electronics_collection_document10_email = document10["Email"]
        electronics_collection_document10_category = document10["Category"]
        electronics_collection_document10_condition = document10["Condition"]



        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document10_images_UTF8_list = []

        for raw_image in document10_images_list_rawFile:
            document10_binaryImage = raw_image.read()
            document10_base64Image = codecs.encode(document10_binaryImage, 'base64')
            document10_UTF8Image = document10_base64Image.decode('utf-8')
            document10_images_UTF8_list.append(document10_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        electronics_collection_document10_imageA = document10_images_UTF8_list[0]

        try:
            electronics_collection_document10_imageB = document10_images_UTF8_list[1]
        except:
            electronics_collection_document10_imageB = document10_images_UTF8_list[0]

        try:
            electronics_collection_document10_imageC = document10_images_UTF8_list[2]
        except:
            electronics_collection_document10_imageC = document10_images_UTF8_list[0]

        try:
            electronics_collection_document10_imageD = document10_images_UTF8_list[3]
        except:
            electronics_collection_document10_imageD = document10_images_UTF8_list[0]       
        
        try:
            electronics_collection_document10_imageE = document10_images_UTF8_list[4]
        except:
            electronics_collection_document10_imageE = document10_images_UTF8_list[0]

        # Close our database connection and free up resources.
        client2.close()

        # Pack all return variables into a JSON Structure and use for return
        return{
            'productID6' : electronics_collection_document6_productID,
            'username6' : electronics_collection_document6_username,
            'state6' : electronics_collection_document6_state,
            'city6' : electronics_collection_document6_city,
            'description6' : electronics_collection_document6_description,
            'mobile6' : electronics_collection_document6_mobile,
            'email6' : electronics_collection_document6_email,
            'category6' : electronics_collection_document6_category,
            'condition6': electronics_collection_document6_condition,
            'image6A' : electronics_collection_document6_imageA,
            'image6B' : electronics_collection_document6_imageB,
            'image6C' : electronics_collection_document6_imageC,
            'image6D': electronics_collection_document6_imageD,
            'image6E': electronics_collection_document6_imageE,

            'productID7' : electronics_collection_document7_productID,
            'username7' : electronics_collection_document7_username,
            'state7' : electronics_collection_document7_state,
            'city7' : electronics_collection_document7_city,
            'description7' : electronics_collection_document7_description,
            'mobile7' : electronics_collection_document7_mobile,
            'email7' : electronics_collection_document7_email,
            'category7' : electronics_collection_document7_category,
            'condition7': electronics_collection_document7_condition,
            'image7A' : electronics_collection_document7_imageA,
            'image7B' : electronics_collection_document7_imageB,
            'image7C' : electronics_collection_document7_imageC,
            'image7D': electronics_collection_document7_imageD,
            'image7E': electronics_collection_document7_imageE,

            'productID8' : electronics_collection_document8_productID,
            'username8' : electronics_collection_document8_username,
            'state8' : electronics_collection_document8_state,
            'city8' : electronics_collection_document8_city,
            'description8' : electronics_collection_document8_description,
            'mobile8' : electronics_collection_document8_mobile,
            'email8' : electronics_collection_document8_email,
            'category8' : electronics_collection_document8_category,
            'condition8': electronics_collection_document8_condition,
            'image8A' : electronics_collection_document8_imageA,
            'image8B' : electronics_collection_document8_imageB,
            'image8C' : electronics_collection_document8_imageC,
            'image8D': electronics_collection_document8_imageD,
            'image8E': electronics_collection_document8_imageE,

            'productID9' : electronics_collection_document9_productID,
            'username9' : electronics_collection_document9_username,
            'state9' : electronics_collection_document9_state,
            'city9' : electronics_collection_document9_city,
            'description9' : electronics_collection_document9_description,
            'mobile9' : electronics_collection_document9_mobile,
            'email9' : electronics_collection_document9_email,
            'category9' : electronics_collection_document9_category,
            'condition9': electronics_collection_document9_condition,
            'image9A' : electronics_collection_document9_imageA,
            'image9B' : electronics_collection_document9_imageB,
            'image9C' : electronics_collection_document9_imageC,
            'image9D': electronics_collection_document9_imageD,
            'image9E': electronics_collection_document9_imageE,

            'productID10' : electronics_collection_document10_productID,
            'username10' : electronics_collection_document10_username,
            'state10' : electronics_collection_document10_state,
            'city10' : electronics_collection_document10_city,
            'description10' : electronics_collection_document10_description,
            'mobile10' : electronics_collection_document10_mobile,
            'email10' : electronics_collection_document10_email,
            'category10' : electronics_collection_document10_category,
            'condition10': electronics_collection_document10_condition,
            'image10A' : electronics_collection_document10_imageA,
            'image10B' : electronics_collection_document10_imageB,
            'image10C' : electronics_collection_document10_imageC,
            'image10D': electronics_collection_document10_imageD,
            'image10E': electronics_collection_document10_imageE,            
        }





    # *************************************************************************************************************
    # *************************************************************************************************************
    @view_config(route_name='electronics_viewProducts2_page3', renderer='templates/electronics_templates/electronics_viewProducts2_page3.pt')
    def electronics_viewProducts2_page3(self):
        import pymongo
        from pymongo import MongoClient
        import gridfs
        from gridfs import GridFS
        # Extract connection string from enviroment variables
        import os
        from dotenv import load_dotenv
        load_dotenv()
        connection_string = os.environ['MY_CONNECTION_STRING']
        # Open database connection and get or create a database called spacenetng_database
        import dns
        client3 = MongoClient('%s' % connection_string)
        db = client3.spacenetng_database

        # Create or open a text based records collection called electronics_text_collection
        text_collection_electronics = db.electronics_text_collection

        # Establish gridfs collection connection
        # Creating or getting an electronics gridfs collection called 'electronics_images_collection'
        # (Getting the GridFS object)
        image_collection_electronics = GridFS(db, "electronics_images_collection")

        # Retrieve document record from database operation
        electronics_collection = text_collection_electronics.find().sort([("_id", pymongo.DESCENDING)]).skip(10).limit(5) #This returns 25 records

        # Push documents into a list
        electronics_collection_list = []

        for record in electronics_collection:
            electronics_collection_list.append(record)



        document11 = electronics_collection_list[0]
        document12 = electronics_collection_list[1]
        document13 = electronics_collection_list[2]
        document14 = electronics_collection_list[3]
        document15 = electronics_collection_list[4]

        # Extracting images
        # The images for document11
        document11_images_list_rawFile = []
        for image_name in document11["Images"]:
            document11_images_list_rawFile.append(image_collection_electronics.get_last_version(filename=image_name))

        # The images for document12
        document12_images_list_rawFile = []
        for image_name in document12["Images"]:
            document12_images_list_rawFile.append(image_collection_electronics.get_last_version(filename=image_name))

        # The images for document13
        document13_images_list_rawFile = []
        for image_name in document13["Images"]:
            document13_images_list_rawFile.append(image_collection_electronics.get_last_version(filename=image_name))

        # The images for document14
        document14_images_list_rawFile = []
        for image_name in document14["Images"]:
            document14_images_list_rawFile.append(image_collection_electronics.get_last_version(filename=image_name))

        # The images for document15
        document15_images_list_rawFile = []
        for image_name in document15["Images"]:
            document15_images_list_rawFile.append(image_collection_electronics.get_last_version(filename=image_name))



        ##############################################
        # Collecting record from individual documents
        ##############################################
        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document11
        #######################

        # For the text strings,
        electronics_collection_document11_productID = document11["Product ID"]
        electronics_collection_document11_username = document11["Username"]
        electronics_collection_document11_state = document11["State"]
        electronics_collection_document11_city = document11["City"]
        electronics_collection_document11_description = document11["Description"]
        electronics_collection_document11_mobile = document11["Mobile"]
        electronics_collection_document11_email = document11["Email"]
        electronics_collection_document11_category = document11["Category"]
        electronics_collection_document11_condition = document11["Condition"]

        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document11_images_UTF8_list = []

        for raw_image in document11_images_list_rawFile:
            document11_binaryImage = raw_image.read()
            document11_base64Image = codecs.encode(document11_binaryImage, 'base64')
            document11_UTF8Image = document11_base64Image.decode('utf-8')
            document11_images_UTF8_list.append(document11_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        electronics_collection_document11_imageA = document11_images_UTF8_list[0]

        try:
            electronics_collection_document11_imageB = document11_images_UTF8_list[1]
        except:
            electronics_collection_document11_imageB = document11_images_UTF8_list[0]

        try:
            electronics_collection_document11_imageC = document11_images_UTF8_list[2]
        except:
            electronics_collection_document11_imageC = document11_images_UTF8_list[0]

        try:
            electronics_collection_document11_imageD = document11_images_UTF8_list[3]
        except:
            electronics_collection_document11_imageD = document11_images_UTF8_list[0]       
        
        try:
            electronics_collection_document11_imageE = document11_images_UTF8_list[4]
        except:
            electronics_collection_document11_imageE = document11_images_UTF8_list[0]





        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document12
        #######################

        # For the text strings,
        electronics_collection_document12_productID = document12["Product ID"]
        electronics_collection_document12_username = document12["Username"]
        electronics_collection_document12_state = document12["State"]
        electronics_collection_document12_city = document12["City"]
        electronics_collection_document12_description = document12["Description"]
        electronics_collection_document12_mobile = document12["Mobile"]
        electronics_collection_document12_email = document12["Email"]
        electronics_collection_document12_category = document12["Category"]
        electronics_collection_document12_condition = document12["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document12_images_UTF8_list = []

        for raw_image in document12_images_list_rawFile:
            document12_binaryImage = raw_image.read()
            document12_base64Image = codecs.encode(document12_binaryImage, 'base64')
            document12_UTF8Image = document12_base64Image.decode('utf-8')
            document12_images_UTF8_list.append(document12_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        electronics_collection_document12_imageA = document12_images_UTF8_list[0]

        try:
            electronics_collection_document12_imageB = document12_images_UTF8_list[1]
        except:
            electronics_collection_document12_imageB = document12_images_UTF8_list[0]

        try:
            electronics_collection_document12_imageC = document12_images_UTF8_list[2]
        except:
            electronics_collection_document12_imageC = document12_images_UTF8_list[0]

        try:
            electronics_collection_document12_imageD = document12_images_UTF8_list[3]
        except:
            electronics_collection_document12_imageD = document12_images_UTF8_list[0]       
        
        try:
            electronics_collection_document12_imageE = document12_images_UTF8_list[4]
        except:
            electronics_collection_document12_imageE = document12_images_UTF8_list[0]





        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document13
        #######################

        # For the text strings,
        electronics_collection_document13_productID = document13["Product ID"]
        electronics_collection_document13_username = document13["Username"]
        electronics_collection_document13_state = document13["State"]
        electronics_collection_document13_city = document13["City"]
        electronics_collection_document13_description = document13["Description"]
        electronics_collection_document13_mobile = document13["Mobile"]
        electronics_collection_document13_email = document13["Email"]
        electronics_collection_document13_category = document13["Category"]
        electronics_collection_document13_condition = document13["Condition"]

        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document13_images_UTF8_list = []

        for raw_image in document13_images_list_rawFile:
            document13_binaryImage = raw_image.read()
            document13_base64Image = codecs.encode(document13_binaryImage, 'base64')
            document13_UTF8Image = document13_base64Image.decode('utf-8')
            document13_images_UTF8_list.append(document13_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        electronics_collection_document13_imageA = document13_images_UTF8_list[0]

        try:
            electronics_collection_document13_imageB = document13_images_UTF8_list[1]
        except:
            electronics_collection_document13_imageB = document13_images_UTF8_list[0]

        try:
            electronics_collection_document13_imageC = document13_images_UTF8_list[2]
        except:
            electronics_collection_document13_imageC = document13_images_UTF8_list[0]

        try:
            electronics_collection_document13_imageD = document13_images_UTF8_list[3]
        except:
            electronics_collection_document13_imageD = document13_images_UTF8_list[0]       
        
        try:
            electronics_collection_document13_imageE = document13_images_UTF8_list[4]
        except:
            electronics_collection_document13_imageE = document13_images_UTF8_list[0]




        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document14
        #######################

        # For the text strings,
        electronics_collection_document14_productID = document14["Product ID"]
        electronics_collection_document14_username = document14["Username"]
        electronics_collection_document14_state = document14["State"]
        electronics_collection_document14_city = document14["City"]
        electronics_collection_document14_description = document14["Description"]
        electronics_collection_document14_mobile = document14["Mobile"]
        electronics_collection_document14_email = document14["Email"]
        electronics_collection_document14_category = document14["Category"]
        electronics_collection_document14_condition = document14["Condition"]

        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document14_images_UTF8_list = []

        for raw_image in document14_images_list_rawFile:
            document14_binaryImage = raw_image.read()
            document14_base64Image = codecs.encode(document14_binaryImage, 'base64')
            document14_UTF8Image = document14_base64Image.decode('utf-8')
            document14_images_UTF8_list.append(document14_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        electronics_collection_document14_imageA = document14_images_UTF8_list[0]

        try:
            electronics_collection_document14_imageB = document14_images_UTF8_list[1]
        except:
            electronics_collection_document14_imageB = document14_images_UTF8_list[0]

        try:
            electronics_collection_document14_imageC = document14_images_UTF8_list[2]
        except:
            electronics_collection_document14_imageC = document14_images_UTF8_list[0]

        try:
            electronics_collection_document14_imageD = document14_images_UTF8_list[3]
        except:
            electronics_collection_document14_imageD = document14_images_UTF8_list[0]       
        
        try:
            electronics_collection_document14_imageE = document14_images_UTF8_list[4]
        except:
            electronics_collection_document14_imageE = document14_images_UTF8_list[0]






        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document15
        #######################

        # For the text strings,
        electronics_collection_document15_productID = document15["Product ID"]
        electronics_collection_document15_username = document15["Username"]
        electronics_collection_document15_state = document15["State"]
        electronics_collection_document15_city = document15["City"]
        electronics_collection_document15_description = document15["Description"]
        electronics_collection_document15_mobile = document15["Mobile"]
        electronics_collection_document15_email = document15["Email"]
        electronics_collection_document15_category = document15["Category"]
        electronics_collection_document15_condition = document15["Condition"]



        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document15_images_UTF8_list = []

        for raw_image in document15_images_list_rawFile:
            document15_binaryImage = raw_image.read()
            document15_base64Image = codecs.encode(document15_binaryImage, 'base64')
            document15_UTF8Image = document15_base64Image.decode('utf-8')
            document15_images_UTF8_list.append(document15_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        electronics_collection_document15_imageA = document15_images_UTF8_list[0]

        try:
            electronics_collection_document15_imageB = document15_images_UTF8_list[1]
        except:
            electronics_collection_document15_imageB = document15_images_UTF8_list[0]

        try:
            electronics_collection_document15_imageC = document15_images_UTF8_list[2]
        except:
            electronics_collection_document15_imageC = document15_images_UTF8_list[0]

        try:
            electronics_collection_document15_imageD = document15_images_UTF8_list[3]
        except:
            electronics_collection_document15_imageD = document15_images_UTF8_list[0]       
        
        try:
            electronics_collection_document15_imageE = document15_images_UTF8_list[4]
        except:
            electronics_collection_document15_imageE = document15_images_UTF8_list[0]

        # Close our database connection and free up resources.
        client3.close()

        # Pack all return variables into a JSON Structure and use for return
        return{
            'productID11' : electronics_collection_document11_productID,
            'username11' : electronics_collection_document11_username,
            'state11' : electronics_collection_document11_state,
            'city11' : electronics_collection_document11_city,
            'description11' : electronics_collection_document11_description,
            'mobile11' : electronics_collection_document11_mobile,
            'email11' : electronics_collection_document11_email,
            'category11' : electronics_collection_document11_category,
            'condition11': electronics_collection_document11_condition,
            'image11A' : electronics_collection_document11_imageA,
            'image11B' : electronics_collection_document11_imageB,
            'image11C' : electronics_collection_document11_imageC,
            'image11D': electronics_collection_document11_imageD,
            'image11E': electronics_collection_document11_imageE,

            'productID12' : electronics_collection_document12_productID,
            'username12' : electronics_collection_document12_username,
            'state12' : electronics_collection_document12_state,
            'city12' : electronics_collection_document12_city,
            'description12' : electronics_collection_document12_description,
            'mobile12' : electronics_collection_document12_mobile,
            'email12' : electronics_collection_document12_email,
            'category12' : electronics_collection_document12_category,
            'condition12': electronics_collection_document12_condition,
            'image12A' : electronics_collection_document12_imageA,
            'image12B' : electronics_collection_document12_imageB,
            'image12C' : electronics_collection_document12_imageC,
            'image12D': electronics_collection_document12_imageD,
            'image12E': electronics_collection_document12_imageE,

            'productID13' : electronics_collection_document13_productID,
            'username13' : electronics_collection_document13_username,
            'state13' : electronics_collection_document13_state,
            'city13' : electronics_collection_document13_city,
            'description13' : electronics_collection_document13_description,
            'mobile13' : electronics_collection_document13_mobile,
            'email13' : electronics_collection_document13_email,
            'category13' : electronics_collection_document13_category,
            'condition13': electronics_collection_document13_condition,
            'image13A' : electronics_collection_document13_imageA,
            'image13B' : electronics_collection_document13_imageB,
            'image13C' : electronics_collection_document13_imageC,
            'image13D': electronics_collection_document13_imageD,
            'image13E': electronics_collection_document13_imageE,

            'productID14' : electronics_collection_document14_productID,
            'username14' : electronics_collection_document14_username,
            'state14' : electronics_collection_document14_state,
            'city14' : electronics_collection_document14_city,
            'description14' : electronics_collection_document14_description,
            'mobile14' : electronics_collection_document14_mobile,
            'email14' : electronics_collection_document14_email,
            'category14' : electronics_collection_document14_category,
            'condition14': electronics_collection_document14_condition,
            'image14A' : electronics_collection_document14_imageA,
            'image14B' : electronics_collection_document14_imageB,
            'image14C' : electronics_collection_document14_imageC,
            'image14D': electronics_collection_document14_imageD,
            'image14E': electronics_collection_document14_imageE,

            'productID15' : electronics_collection_document15_productID,
            'username15' : electronics_collection_document15_username,
            'state15' : electronics_collection_document15_state,
            'city15' : electronics_collection_document15_city,
            'description15' : electronics_collection_document15_description,
            'mobile15' : electronics_collection_document15_mobile,
            'email15' : electronics_collection_document15_email,
            'category15' : electronics_collection_document15_category,
            'condition15': electronics_collection_document15_condition,
            'image15A' : electronics_collection_document15_imageA,
            'image15B' : electronics_collection_document15_imageB,
            'image15C' : electronics_collection_document15_imageC,
            'image15D': electronics_collection_document15_imageD,
            'image15E': electronics_collection_document15_imageE,
        }


    # *************************************************************************************************************
    # *************************************************************************************************************        
    @view_config(route_name='electronics_viewProducts2_page4', renderer='templates/electronics_templates/electronics_viewProducts2_page4.pt')
    def electronics_viewProducts2_page4(self):
        import pymongo
        from pymongo import MongoClient
        import gridfs
        from gridfs import GridFS
        # Extract connection string from enviroment variables
        import os
        from dotenv import load_dotenv
        load_dotenv()
        connection_string = os.environ['MY_CONNECTION_STRING']
        # Open database connection and get or create a database called spacenetng_database
        import dns
        client4 = MongoClient('%s' % connection_string)
        db = client4.spacenetng_database

        # Create or open a text based records collection called electronics_text_collection
        text_collection_electronics = db.electronics_text_collection

        # Establish gridfs collection connection
        # Creating or getting an electronics gridfs collection called 'electronics_images_collection'
        # (Getting the GridFS object)
        image_collection_electronics = GridFS(db, "electronics_images_collection")

        # Retrieve document record from database operation
        electronics_collection = text_collection_electronics.find().sort([("_id", pymongo.DESCENDING)]).skip(15).limit(5) #This returns 25 records

        # Push documents into a list
        electronics_collection_list = []

        for record in electronics_collection:
            electronics_collection_list.append(record)

        document16 = electronics_collection_list[0]
        document17 = electronics_collection_list[1]
        document18 = electronics_collection_list[2]
        document19 = electronics_collection_list[3]
        document20 = electronics_collection_list[4]


        # Extracting images
        # The images for document16
        document16_images_list_rawFile = []
        for image_name in document16["Images"]:
            document16_images_list_rawFile.append(image_collection_electronics.get_last_version(filename=image_name))

        # The images for document17
        document17_images_list_rawFile = []
        for image_name in document17["Images"]:
            document17_images_list_rawFile.append(image_collection_electronics.get_last_version(filename=image_name))

        # The images for document18
        document18_images_list_rawFile = []
        for image_name in document18["Images"]:
            document18_images_list_rawFile.append(image_collection_electronics.get_last_version(filename=image_name))

        # The images for document19
        document19_images_list_rawFile = []
        for image_name in document19["Images"]:
            document19_images_list_rawFile.append(image_collection_electronics.get_last_version(filename=image_name))

        # The images for document20
        document20_images_list_rawFile = []
        for image_name in document20["Images"]:
            document20_images_list_rawFile.append(image_collection_electronics.get_last_version(filename=image_name))


        ##############################################
        # Collecting record from individual documents
        ##############################################
        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document16
        #######################

        # For the text strings,
        electronics_collection_document16_productID = document16["Product ID"]
        electronics_collection_document16_username = document16["Username"]
        electronics_collection_document16_state = document16["State"]
        electronics_collection_document16_city = document16["City"]
        electronics_collection_document16_description = document16["Description"]
        electronics_collection_document16_mobile = document16["Mobile"]
        electronics_collection_document16_email = document16["Email"]
        electronics_collection_document16_category = document16["Category"]
        electronics_collection_document16_condition = document16["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document16_images_UTF8_list = []

        for raw_image in document16_images_list_rawFile:
            document16_binaryImage = raw_image.read()
            document16_base64Image = codecs.encode(document16_binaryImage, 'base64')
            document16_UTF8Image = document16_base64Image.decode('utf-8')
            document16_images_UTF8_list.append(document16_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        electronics_collection_document16_imageA = document16_images_UTF8_list[0]

        try:
            electronics_collection_document16_imageB = document16_images_UTF8_list[1]
        except:
            electronics_collection_document16_imageB = document16_images_UTF8_list[0]

        try:
            electronics_collection_document16_imageC = document16_images_UTF8_list[2]
        except:
            electronics_collection_document16_imageC = document16_images_UTF8_list[0]

        try:
            electronics_collection_document16_imageD = document16_images_UTF8_list[3]
        except:
            electronics_collection_document16_imageD = document16_images_UTF8_list[0]       
        
        try:
            electronics_collection_document16_imageE = document16_images_UTF8_list[4]
        except:
            electronics_collection_document16_imageE = document16_images_UTF8_list[0]




        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document17
        #######################

        # For the text strings,
        electronics_collection_document17_productID = document17["Product ID"]
        electronics_collection_document17_username = document17["Username"]
        electronics_collection_document17_state = document17["State"]
        electronics_collection_document17_city = document17["City"]
        electronics_collection_document17_description = document17["Description"]
        electronics_collection_document17_mobile = document17["Mobile"]
        electronics_collection_document17_email = document17["Email"]
        electronics_collection_document17_category = document17["Category"]
        electronics_collection_document17_condition = document17["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document17_images_UTF8_list = []

        for raw_image in document17_images_list_rawFile:
            document17_binaryImage = raw_image.read()
            document17_base64Image = codecs.encode(document17_binaryImage, 'base64')
            document17_UTF8Image = document17_base64Image.decode('utf-8')
            document17_images_UTF8_list.append(document17_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        electronics_collection_document17_imageA = document17_images_UTF8_list[0]

        try:
            electronics_collection_document17_imageB = document17_images_UTF8_list[1]
        except:
            electronics_collection_document17_imageB = document17_images_UTF8_list[0]

        try:
            electronics_collection_document17_imageC = document17_images_UTF8_list[2]
        except:
            electronics_collection_document17_imageC = document17_images_UTF8_list[0]

        try:
            electronics_collection_document17_imageD = document17_images_UTF8_list[3]
        except:
            electronics_collection_document17_imageD = document17_images_UTF8_list[0]       
        
        try:
            electronics_collection_document17_imageE = document17_images_UTF8_list[4]
        except:
            electronics_collection_document17_imageE = document17_images_UTF8_list[0]





        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document18
        #######################

        # For the text strings,
        electronics_collection_document18_productID = document18["Product ID"]
        electronics_collection_document18_username = document18["Username"]
        electronics_collection_document18_state = document18["State"]
        electronics_collection_document18_city = document18["City"]
        electronics_collection_document18_description = document18["Description"]
        electronics_collection_document18_mobile = document18["Mobile"]
        electronics_collection_document18_email = document18["Email"]
        electronics_collection_document18_category = document18["Category"]
        electronics_collection_document18_condition = document18["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document18_images_UTF8_list = []

        for raw_image in document18_images_list_rawFile:
            document18_binaryImage = raw_image.read()
            document18_base64Image = codecs.encode(document18_binaryImage, 'base64')
            document18_UTF8Image = document18_base64Image.decode('utf-8')
            document18_images_UTF8_list.append(document18_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        electronics_collection_document18_imageA = document18_images_UTF8_list[0]

        try:
            electronics_collection_document18_imageB = document18_images_UTF8_list[1]
        except:
            electronics_collection_document18_imageB = document18_images_UTF8_list[0]

        try:
            electronics_collection_document18_imageC = document18_images_UTF8_list[2]
        except:
            electronics_collection_document18_imageC = document18_images_UTF8_list[0]

        try:
            electronics_collection_document18_imageD = document18_images_UTF8_list[3]
        except:
            electronics_collection_document18_imageD = document18_images_UTF8_list[0]       
        
        try:
            electronics_collection_document18_imageE = document18_images_UTF8_list[4]
        except:
            electronics_collection_document18_imageE = document18_images_UTF8_list[0]





        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document19
        #######################

        # For the text strings,
        electronics_collection_document19_productID = document19["Product ID"]
        electronics_collection_document19_username = document19["Username"]
        electronics_collection_document19_state = document19["State"]
        electronics_collection_document19_city = document19["City"]
        electronics_collection_document19_description = document19["Description"]
        electronics_collection_document19_mobile = document19["Mobile"]
        electronics_collection_document19_email = document19["Email"]
        electronics_collection_document19_category = document19["Category"]
        electronics_collection_document19_condition = document19["Condition"]

        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document19_images_UTF8_list = []

        for raw_image in document19_images_list_rawFile:
            document19_binaryImage = raw_image.read()
            document19_base64Image = codecs.encode(document19_binaryImage, 'base64')
            document19_UTF8Image = document19_base64Image.decode('utf-8')
            document19_images_UTF8_list.append(document19_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        electronics_collection_document19_imageA = document19_images_UTF8_list[0]

        try:
            electronics_collection_document19_imageB = document19_images_UTF8_list[1]
        except:
            electronics_collection_document19_imageB = document19_images_UTF8_list[0]

        try:
            electronics_collection_document19_imageC = document19_images_UTF8_list[2]
        except:
            electronics_collection_document19_imageC = document19_images_UTF8_list[0]

        try:
            electronics_collection_document19_imageD = document19_images_UTF8_list[3]
        except:
            electronics_collection_document19_imageD = document19_images_UTF8_list[0]       
        
        try:
            electronics_collection_document19_imageE = document19_images_UTF8_list[4]
        except:
            electronics_collection_document19_imageE = document19_images_UTF8_list[0]




        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document20
        #######################

        # For the text strings,
        electronics_collection_document20_productID = document20["Product ID"]
        electronics_collection_document20_username = document20["Username"]
        electronics_collection_document20_state = document20["State"]
        electronics_collection_document20_city = document20["City"]
        electronics_collection_document20_description = document20["Description"]
        electronics_collection_document20_mobile = document20["Mobile"]
        electronics_collection_document20_email = document20["Email"]
        electronics_collection_document20_category = document20["Category"]
        electronics_collection_document20_condition = document20["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document20_images_UTF8_list = []

        for raw_image in document20_images_list_rawFile:
            document20_binaryImage = raw_image.read()
            document20_base64Image = codecs.encode(document20_binaryImage, 'base64')
            document20_UTF8Image = document20_base64Image.decode('utf-8')
            document20_images_UTF8_list.append(document20_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        electronics_collection_document20_imageA = document20_images_UTF8_list[0]

        try:
            electronics_collection_document20_imageB = document20_images_UTF8_list[1]
        except:
            electronics_collection_document20_imageB = document20_images_UTF8_list[0]

        try:
            electronics_collection_document20_imageC = document20_images_UTF8_list[2]
        except:
            electronics_collection_document20_imageC = document20_images_UTF8_list[0]

        try:
            electronics_collection_document20_imageD = document20_images_UTF8_list[3]
        except:
            electronics_collection_document20_imageD = document20_images_UTF8_list[0]       
        
        try:
            electronics_collection_document20_imageE = document20_images_UTF8_list[4]
        except:
            electronics_collection_document20_imageE = document20_images_UTF8_list[0]


        # Close our database connection and free up resources.
        client4.close()

        # Pack all return variables into a JSON Structure and use for return
        return{
            'productID16' : electronics_collection_document16_productID,
            'username16' : electronics_collection_document16_username,
            'state16' : electronics_collection_document16_state,
            'city16' : electronics_collection_document16_city,
            'description16' : electronics_collection_document16_description,
            'mobile16' : electronics_collection_document16_mobile,
            'email16' : electronics_collection_document16_email,
            'category16' : electronics_collection_document16_category,
            'condition16': electronics_collection_document16_condition,
            'image16A' : electronics_collection_document16_imageA,
            'image16B' : electronics_collection_document16_imageB,
            'image16C' : electronics_collection_document16_imageC,
            'image16D': electronics_collection_document16_imageD,
            'image16E': electronics_collection_document16_imageE,

            'productID17' : electronics_collection_document17_productID,
            'username17' : electronics_collection_document17_username,
            'state17' : electronics_collection_document17_state,
            'city17' : electronics_collection_document17_city,
            'description17' : electronics_collection_document17_description,
            'mobile17' : electronics_collection_document17_mobile,
            'email17' : electronics_collection_document17_email,
            'category17' : electronics_collection_document17_category,
            'condition17': electronics_collection_document17_condition,
            'image17A' : electronics_collection_document17_imageA,
            'image17B' : electronics_collection_document17_imageB,
            'image17C' : electronics_collection_document17_imageC,
            'image17D': electronics_collection_document17_imageD,
            'image17E': electronics_collection_document17_imageE,

            'productID18' : electronics_collection_document18_productID,
            'username18' : electronics_collection_document18_username,
            'state18' : electronics_collection_document18_state,
            'city18' : electronics_collection_document18_city,
            'description18' : electronics_collection_document18_description,
            'mobile18' : electronics_collection_document18_mobile,
            'email18' : electronics_collection_document18_email,
            'category18' : electronics_collection_document18_category,
            'condition18': electronics_collection_document18_condition,
            'image18A' : electronics_collection_document18_imageA,
            'image18B' : electronics_collection_document18_imageB,
            'image18C' : electronics_collection_document18_imageC,
            'image18D': electronics_collection_document18_imageD,
            'image18E': electronics_collection_document18_imageE,

            'productID19' : electronics_collection_document19_productID,
            'username19' : electronics_collection_document19_username,
            'state19' : electronics_collection_document19_state,
            'city19' : electronics_collection_document19_city,
            'description19' : electronics_collection_document19_description,
            'mobile19' : electronics_collection_document19_mobile,
            'email19' : electronics_collection_document19_email,
            'category19' : electronics_collection_document19_category,
            'condition19': electronics_collection_document19_condition,
            'image19A' : electronics_collection_document19_imageA,
            'image19B' : electronics_collection_document19_imageB,
            'image19C' : electronics_collection_document19_imageC,
            'image19D': electronics_collection_document19_imageD,
            'image19E': electronics_collection_document19_imageE,

            'productID20' : electronics_collection_document20_productID,
            'username20' : electronics_collection_document20_username,
            'state20' : electronics_collection_document20_state,
            'city20' : electronics_collection_document20_city,
            'description20' : electronics_collection_document20_description,
            'mobile20' : electronics_collection_document20_mobile,
            'email20' : electronics_collection_document20_email,
            'category20' : electronics_collection_document20_category,
            'condition20': electronics_collection_document20_condition,
            'image20A' : electronics_collection_document20_imageA,
            'image20B' : electronics_collection_document20_imageB,
            'image20C' : electronics_collection_document20_imageC,
            'image20D': electronics_collection_document20_imageD,
            'image20E': electronics_collection_document20_imageE,
        }






    # *************************************************************************************************************
    # *************************************************************************************************************
    @view_config(route_name='electronics_viewProducts2_page5', renderer='templates/electronics_templates/electronics_viewProducts2_page5.pt')
    def electronics_viewProducts2_page5(self):
        import pymongo
        from pymongo import MongoClient
        import gridfs
        from gridfs import GridFS
        # Extract connection string from enviroment variables
        import os
        from dotenv import load_dotenv
        load_dotenv()
        connection_string = os.environ['MY_CONNECTION_STRING']
        # Open database connection and get or create a database called spacenetng_database
        import dns
        client5 = MongoClient('%s' % connection_string)
        db = client5.spacenetng_database

        # Create or open a text based records collection called electronics_text_collection
        text_collection_electronics = db.electronics_text_collection

        # Establish gridfs collection connection
        # Creating or getting an electronics gridfs collection called 'electronics_images_collection'
        # (Getting the GridFS object)
        image_collection_electronics = GridFS(db, "electronics_images_collection")

        # Retrieve document record from database operation
        electronics_collection = text_collection_electronics.find().sort([("_id", pymongo.DESCENDING)]).skip(20).limit(5) #This returns 25 records

        # Push documents into a list
        electronics_collection_list = []

        for record in electronics_collection:
            electronics_collection_list.append(record)

        document21 = electronics_collection_list[0]
        document22 = electronics_collection_list[1]
        document23 = electronics_collection_list[2]
        document24 = electronics_collection_list[3]
        document25 = electronics_collection_list[4]


        # Extracting images
        # The images for document21
        document21_images_list_rawFile = []
        for image_name in document21["Images"]:
            document21_images_list_rawFile.append(image_collection_electronics.get_last_version(filename=image_name))

        # The images for document22
        document22_images_list_rawFile = []
        for image_name in document22["Images"]:
            document22_images_list_rawFile.append(image_collection_electronics.get_last_version(filename=image_name))

        # The images for document23
        document23_images_list_rawFile = []
        for image_name in document23["Images"]:
            document23_images_list_rawFile.append(image_collection_electronics.get_last_version(filename=image_name))

        # The images for document24
        document24_images_list_rawFile = []
        for image_name in document24["Images"]:
            document24_images_list_rawFile.append(image_collection_electronics.get_last_version(filename=image_name))

        # The images for document25
        document25_images_list_rawFile = []
        for image_name in document25["Images"]:
            document25_images_list_rawFile.append(image_collection_electronics.get_last_version(filename=image_name))


        ##############################################
        # Collecting record from individual documents
        ##############################################
        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document21
        #######################

        # For the text strings,
        electronics_collection_document21_productID = document21["Product ID"]
        electronics_collection_document21_username = document21["Username"]
        electronics_collection_document21_state = document21["State"]
        electronics_collection_document21_city = document21["City"]
        electronics_collection_document21_description = document21["Description"]
        electronics_collection_document21_mobile = document21["Mobile"]
        electronics_collection_document21_email = document21["Email"]
        electronics_collection_document21_category = document21["Category"]
        electronics_collection_document21_condition = document21["Condition"]



        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document21_images_UTF8_list = []

        for raw_image in document21_images_list_rawFile:
            document21_binaryImage = raw_image.read()
            document21_base64Image = codecs.encode(document21_binaryImage, 'base64')
            document21_UTF8Image = document21_base64Image.decode('utf-8')
            document21_images_UTF8_list.append(document21_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        electronics_collection_document21_imageA = document21_images_UTF8_list[0]

        try:
            electronics_collection_document21_imageB = document21_images_UTF8_list[1]
        except:
            electronics_collection_document21_imageB = document21_images_UTF8_list[0]

        try:
            electronics_collection_document21_imageC = document21_images_UTF8_list[2]
        except:
            electronics_collection_document21_imageC = document21_images_UTF8_list[0]

        try:
            electronics_collection_document21_imageD = document21_images_UTF8_list[3]
        except:
            electronics_collection_document21_imageD = document21_images_UTF8_list[0]       
        
        try:
            electronics_collection_document21_imageE = document21_images_UTF8_list[4]
        except:
            electronics_collection_document21_imageE = document21_images_UTF8_list[0]





        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document22
        #######################

        # For the text strings,
        electronics_collection_document22_productID = document22["Product ID"]
        electronics_collection_document22_username = document22["Username"]
        electronics_collection_document22_state = document22["State"]
        electronics_collection_document22_city = document22["City"]
        electronics_collection_document22_description = document22["Description"]
        electronics_collection_document22_mobile = document22["Mobile"]
        electronics_collection_document22_email = document22["Email"]
        electronics_collection_document22_category = document22["Category"]
        electronics_collection_document22_condition = document22["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document22_images_UTF8_list = []

        for raw_image in document22_images_list_rawFile:
            document22_binaryImage = raw_image.read()
            document22_base64Image = codecs.encode(document22_binaryImage, 'base64')
            document22_UTF8Image = document22_base64Image.decode('utf-8')
            document22_images_UTF8_list.append(document22_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        electronics_collection_document22_imageA = document22_images_UTF8_list[0]

        try:
            electronics_collection_document22_imageB = document22_images_UTF8_list[1]
        except:
            electronics_collection_document22_imageB = document22_images_UTF8_list[0]

        try:
            electronics_collection_document22_imageC = document22_images_UTF8_list[2]
        except:
            electronics_collection_document22_imageC = document22_images_UTF8_list[0]

        try:
            electronics_collection_document22_imageD = document22_images_UTF8_list[3]
        except:
            electronics_collection_document22_imageD = document22_images_UTF8_list[0]       
        
        try:
            electronics_collection_document22_imageE = document22_images_UTF8_list[4]
        except:
            electronics_collection_document22_imageE = document22_images_UTF8_list[0]






        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document23
        #######################

        # For the text strings,
        electronics_collection_document23_productID = document23["Product ID"]
        electronics_collection_document23_username = document23["Username"]
        electronics_collection_document23_state = document23["State"]
        electronics_collection_document23_city = document23["City"]
        electronics_collection_document23_description = document23["Description"]
        electronics_collection_document23_mobile = document23["Mobile"]
        electronics_collection_document23_email = document23["Email"]
        electronics_collection_document23_category = document23["Category"]
        electronics_collection_document23_condition = document23["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document23_images_UTF8_list = []

        for raw_image in document23_images_list_rawFile:
            document23_binaryImage = raw_image.read()
            document23_base64Image = codecs.encode(document23_binaryImage, 'base64')
            document23_UTF8Image = document23_base64Image.decode('utf-8')
            document23_images_UTF8_list.append(document23_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        electronics_collection_document23_imageA = document23_images_UTF8_list[0]

        try:
            electronics_collection_document23_imageB = document23_images_UTF8_list[1]
        except:
            electronics_collection_document23_imageB = document23_images_UTF8_list[0]

        try:
            electronics_collection_document23_imageC = document23_images_UTF8_list[2]
        except:
            electronics_collection_document23_imageC = document23_images_UTF8_list[0]

        try:
            electronics_collection_document23_imageD = document23_images_UTF8_list[3]
        except:
            electronics_collection_document23_imageD = document23_images_UTF8_list[0]       
        
        try:
            electronics_collection_document23_imageE = document23_images_UTF8_list[4]
        except:
            electronics_collection_document23_imageE = document23_images_UTF8_list[0]





        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document24
        #######################

        # For the text strings,
        electronics_collection_document24_productID = document24["Product ID"]
        electronics_collection_document24_username = document24["Username"]
        electronics_collection_document24_state = document24["State"]
        electronics_collection_document24_city = document24["City"]
        electronics_collection_document24_description = document24["Description"]
        electronics_collection_document24_mobile = document24["Mobile"]
        electronics_collection_document24_email = document24["Email"]
        electronics_collection_document24_category = document24["Category"]
        electronics_collection_document24_condition = document24["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document24_images_UTF8_list = []

        for raw_image in document24_images_list_rawFile:
            document24_binaryImage = raw_image.read()
            document24_base64Image = codecs.encode(document24_binaryImage, 'base64')
            document24_UTF8Image = document24_base64Image.decode('utf-8')
            document24_images_UTF8_list.append(document24_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        electronics_collection_document24_imageA = document24_images_UTF8_list[0]

        try:
            electronics_collection_document24_imageB = document24_images_UTF8_list[1]
        except:
            electronics_collection_document24_imageB = document24_images_UTF8_list[0]

        try:
            electronics_collection_document24_imageC = document24_images_UTF8_list[2]
        except:
            electronics_collection_document24_imageC = document24_images_UTF8_list[0]

        try:
            electronics_collection_document24_imageD = document24_images_UTF8_list[3]
        except:
            electronics_collection_document24_imageD = document24_images_UTF8_list[0]       
        
        try:
            electronics_collection_document24_imageE = document24_images_UTF8_list[4]
        except:
            electronics_collection_document24_imageE = document24_images_UTF8_list[0]






        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document25
        #######################

        # For the text strings,
        electronics_collection_document25_productID = document25["Product ID"]
        electronics_collection_document25_username = document25["Username"]
        electronics_collection_document25_state = document25["State"]
        electronics_collection_document25_city = document25["City"]
        electronics_collection_document25_description = document25["Description"]
        electronics_collection_document25_mobile = document25["Mobile"]
        electronics_collection_document25_email = document25["Email"]
        electronics_collection_document25_category = document25["Category"]
        electronics_collection_document25_condition = document25["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document25_images_UTF8_list = []

        for raw_image in document25_images_list_rawFile:
            document25_binaryImage = raw_image.read()
            document25_base64Image = codecs.encode(document25_binaryImage, 'base64')
            document25_UTF8Image = document25_base64Image.decode('utf-8')
            document25_images_UTF8_list.append(document25_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        electronics_collection_document25_imageA = document25_images_UTF8_list[0]

        try:
            electronics_collection_document25_imageB = document25_images_UTF8_list[1]
        except:
            electronics_collection_document25_imageB = document25_images_UTF8_list[0]

        try:
            electronics_collection_document25_imageC = document25_images_UTF8_list[2]
        except:
            electronics_collection_document25_imageC = document25_images_UTF8_list[0]

        try:
            electronics_collection_document25_imageD = document25_images_UTF8_list[3]
        except:
            electronics_collection_document25_imageD = document25_images_UTF8_list[0]       
        
        try:
            electronics_collection_document25_imageE = document25_images_UTF8_list[4]
        except:
            electronics_collection_document25_imageE = document25_images_UTF8_list[0]

        # Close our database connection and free up resources.
        client5.close()

        # Pack all return variables into a JSON Structure and use for return
        return{
            'productID21' : electronics_collection_document21_productID,
            'username21' : electronics_collection_document21_username,
            'state21' : electronics_collection_document21_state,
            'city21' : electronics_collection_document21_city,
            'description21' : electronics_collection_document21_description,
            'mobile21' : electronics_collection_document21_mobile,
            'email21' : electronics_collection_document21_email,
            'category21' : electronics_collection_document21_category,
            'condition21': electronics_collection_document21_condition,
            'image21A' : electronics_collection_document21_imageA,
            'image21B' : electronics_collection_document21_imageB,
            'image21C' : electronics_collection_document21_imageC,
            'image21D': electronics_collection_document21_imageD,
            'image21E': electronics_collection_document21_imageE,

            'productID22' : electronics_collection_document22_productID,
            'username22' : electronics_collection_document22_username,
            'state22' : electronics_collection_document22_state,
            'city22' : electronics_collection_document22_city,
            'description22' : electronics_collection_document22_description,
            'mobile22' : electronics_collection_document22_mobile,
            'email22' : electronics_collection_document22_email,
            'category22' : electronics_collection_document22_category,
            'condition22': electronics_collection_document22_condition,
            'image22A' : electronics_collection_document22_imageA,
            'image22B' : electronics_collection_document22_imageB,
            'image22C' : electronics_collection_document22_imageC,
            'image22D': electronics_collection_document22_imageD,
            'image22E': electronics_collection_document22_imageE,

            'productID23' : electronics_collection_document23_productID,
            'username23' : electronics_collection_document23_username,
            'state23' : electronics_collection_document23_state,
            'city23' : electronics_collection_document23_city,
            'description23' : electronics_collection_document23_description,
            'mobile23' : electronics_collection_document23_mobile,
            'email23' : electronics_collection_document23_email,
            'category23' : electronics_collection_document23_category,
            'condition23': electronics_collection_document23_condition,
            'image23A' : electronics_collection_document23_imageA,
            'image23B' : electronics_collection_document23_imageB,
            'image23C' : electronics_collection_document23_imageC,
            'image23D': electronics_collection_document23_imageD,
            'image23E': electronics_collection_document23_imageE,

            'productID24' : electronics_collection_document24_productID,
            'username24' : electronics_collection_document24_username,
            'state24' : electronics_collection_document24_state,
            'city24' : electronics_collection_document24_city,
            'description24' : electronics_collection_document24_description,
            'mobile24' : electronics_collection_document24_mobile,
            'email24' : electronics_collection_document24_email,
            'category24' : electronics_collection_document24_category,
            'condition24': electronics_collection_document24_condition,
            'image24A' : electronics_collection_document24_imageA,
            'image24B' : electronics_collection_document24_imageB,
            'image24C' : electronics_collection_document24_imageC,
            'image24D': electronics_collection_document24_imageD,
            'image24E': electronics_collection_document24_imageE,

            'productID25' : electronics_collection_document25_productID,
            'username25' : electronics_collection_document25_username,
            'state25' : electronics_collection_document25_state,
            'city25' : electronics_collection_document25_city,
            'description25' : electronics_collection_document25_description,
            'mobile25' : electronics_collection_document25_mobile,
            'email25' : electronics_collection_document25_email,
            'category25' : electronics_collection_document25_category,
            'condition25': electronics_collection_document25_condition,
            'image25A' : electronics_collection_document25_imageA,
            'image25B' : electronics_collection_document25_imageB,
            'image25C' : electronics_collection_document25_imageC,
            'image25D': electronics_collection_document25_imageD,
            'image25E': electronics_collection_document25_imageE,
        }

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
# AUTOMOBILES VIEWS
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************

# ########################################################################################################################
# ########################################################################################################################
# ########################################################################################################################
# Create
@view_defaults(route_name='automobiles_createNewPost')
class AutomobilesCreateNewPostViews(object):
    def __init__(self, request):
        self.request = request

    # *************************************************************************************************************
    # *************************************************************************************************************
    @view_config(renderer='templates/automobiles_templates/automobiles_createNewPost.pt')
    def automobiles_createNewPost(self):
        return {}


    # *************************************************************************************************************
    # *************************************************************************************************************
    # # Perform operation on query params, send values to the database and give the user a Response after creation 
    # of a new post.
    @view_config(request_method='POST', request_param='automobiles_create_submitButton')
    def automobiles_createNewPost_response(self):
        from pyramid.httpexceptions import HTTPFound

        # Collect variables from form fields
        # Get text items from form page
        automobiles_create_username = self.request.params['automobiles_create_username']
        automobiles_create_statesList = self.request.params['automobiles_create_statesList']
        automobiles_create_city = self.request.params['automobiles_create_city']
        automobiles_create_textarea = self.request.params['automobiles_create_textarea']
        automobiles_create_mobile = self.request.params['automobiles_create_mobile']
        automobiles_create_email = self.request.params['automobiles_create_email']
        automobiles_create_category = self.request.params['automobiles_create_category']
        automobiles_create_condition = self.request.params['automobiles_create_condition']

        # Get images from form page
        automobiles_create_images = self.request.POST.getall('automobiles_create_images')

        # Use this for our rest API insertion operation
        automobiles_create_images_names_list = []
        for automobiles_create_image_name in automobiles_create_images:
            automobiles_create_images_names_list.append(automobiles_create_image_name.filename)

        # use this for gridFS insertion operation
        automobiles_create_images_list = []
        for automobiles_create_image in automobiles_create_images:
            automobiles_create_images_list.append(automobiles_create_image)


        # Create other backend variables
        # create Product ID
        from .myModules import ran_gen_a
        automobiles_create_productID = ran_gen_a(8, "AEIOSODMG23")


        # Create a UUID number
        import uuid
        automobiles_create_privateUUID = uuid.uuid4()

        # Get specific date
        import datetime
        automobiles_create_dateTime = datetime.datetime.utcnow()


        # Create our RES API structure and push data to the RES
        automobiles_resAPI_json = {
            "Private UUID": "",
            "Product ID": "",
            "Username": "",
            "State": "",
            "City": "",
            "Description": "",
            "Mobile": "",
            "Email": "",
            "Category": "",
            "Condition": "",
            "Images": [],
            "date": "",
        }


        automobiles_resAPI_json["Private UUID"] = automobiles_create_privateUUID
        automobiles_resAPI_json["Product ID"] = automobiles_create_productID
        automobiles_resAPI_json["Username"] = automobiles_create_username
        automobiles_resAPI_json["State"] = automobiles_create_statesList
        automobiles_resAPI_json["City"] = automobiles_create_city
        automobiles_resAPI_json["Description"] = automobiles_create_textarea
        automobiles_resAPI_json["Mobile"] = automobiles_create_mobile
        automobiles_resAPI_json["Email"] = automobiles_create_email
        automobiles_resAPI_json["Category"] = automobiles_create_category
        automobiles_resAPI_json["Condition"] = automobiles_create_condition
        automobiles_resAPI_json["Images"] = automobiles_create_images_names_list
        automobiles_resAPI_json["date"] = automobiles_create_dateTime



        # Initialise database connection and perform CRUD operation on text and images
        # Perform CRUD operation on text strings
        import pymongo
        from pymongo import MongoClient
        # Extract connection string from enviroment variables
        import os
        from dotenv import load_dotenv
        load_dotenv()
        connection_string = os.environ['MY_CONNECTION_STRING']
        # Open database connection and get or create a database called spacenetng_database
        import dns
        client = MongoClient('%s' % connection_string)
        db = client.spacenetng_database

        # Create or open a text based records collection called automobiles_text_collection
        text_collection= db.automobiles_text_collection

        # Insert API into database and close our connected client's connection
        text_collection.insert_one(automobiles_resAPI_json)


        # Perform CRUD operation on images
        import gridfs
        from gridfs import GridFS

        # Creating or getting an automobiles gridfs collection called 'automobiles_images_collection'
        # (Getting the GridFS object)
        image_collection = GridFS(db, "automobiles_images_collection")

        # Inserting files into gridfs and close our connected client's connection
        for image in automobiles_create_images_list:
            image_collection.put(image.file, filename=image.filename)

        # Close our database connection and free up resources.
        client.close()


        # # ############################################################################################
        # # Send private UUID to user's Email using login details and gmail server using inbuilt python email package
        import smtplib, os, sys
        from smtplib import SMTP
        from email.message import EmailMessage
        from dotenv import load_dotenv
        load_dotenv()

        try:
            email_content = ("""\
            Hello %s, thanks for posting on spacenetng platform, an online commercial market place where buyers and sellers
            meet to carry out business transactions. Please be advised, a private user UUID has been created for you which 
            you can use to update or delete your post and it should be kept confidential.\n
            Here is your Seceret hey: %s\n
            For support and enquiries please contact us via our contact details found on our contact page in our website.\n
            Thanks for using this service, we hope to serve you better!!.
            """
            % (automobiles_create_username, automobiles_create_privateUUID)
            
            )

            msg = EmailMessage()
            msg.set_content(email_content)

            msg['Subject'] = 'Your UUID from Spacenetng'
            msg['From'] = 'spacenetngbase@gmail.com'
            msg['To'] = automobiles_create_email

            server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server_ssl.ehlo()

            email = os.environ['MY_EMAIL_ADDRESS']
            passWord = os.environ['MY_EMAIL_PASSWORD']

            server_ssl.login(email, passWord)
            server_ssl.send_message(msg)       
            server_ssl.quit()   # Terminate the SMTP session and free up resources       
            
            # Or And,
            # print('Message sent successfully!!')

        except:
            pass
            # Or
            # print X

        finally:
            pass


        ######################################################
        # Redirect user to view what he/she has just posted                      
        body = (
            "<html style=\"color: green; background-color: whitesmoke; \">"
            "<head><meta http-equiv=\"refresh\" content=\"6;url=/automobiles_viewProducts2_page1\"></head>"
            "<body>"
            "<h4>Thanks for using our service, your post has been recorded successfully!! "
            "<br />"
            "You will be redirected shortly.</h4>"
            "</body>"
            "</html>"
        )

        return Response(body)





# ########################################################################################################################
# ########################################################################################################################
# ########################################################################################################################
# Modify
@view_defaults(route_name='automobiles_modifyPost1')
class AutomobilesModifyPostViews(object):
    def __init__(self, request):
        self.request = request


    # *************************************************************************************************************
    # *************************************************************************************************************
    @view_config(renderer='templates/automobiles_templates/automobiles_modifyPost1.pt')
    def automobiles_modifyPost1(self):
        return {'user_warning': ''}



    # *************************************************************************************************************
    # *************************************************************************************************************
    # Handler method for modifyPost1 page form field input validation for edit mode
    # Redirect to modifyPost2 page if valid private uuid was given, else throw error.
    @view_config(request_method='POST', request_param='automobiles_modify1_editButton', renderer='templates/automobiles_templates/automobiles_modifyPost1.pt')
    def automobiles_modifyPost1_update_handler(self):
        from pyramid.renderers import render
        from pyramid.response import Response
        from pyramid.httpexceptions import HTTPFound
        import pymongo
        from pymongo import MongoClient
        from bson import ObjectId
        from uuid import UUID
        # Extract connection string from enviroment variables
        import os
        from dotenv import load_dotenv
        load_dotenv()
        connection_string = os.environ['MY_CONNECTION_STRING']
        # Open database connection and get or create a database called spacenetng_database
        import dns
        client = MongoClient('%s' % connection_string)
        db = client.spacenetng_database

        # Create or open a text based records collection called automobiles_text_collection
        text_collection= db.automobiles_text_collection


        automobiles_update_privateUUID = self.request.params['automobiles_modify1_privateUUID']

        try:
            text_collection.find_one({'Private UUID': UUID(automobiles_update_privateUUID)})
            result1 = render('templates/automobiles_templates/automobiles_modifyPost2.pt' , {'private_UUID': automobiles_update_privateUUID, 'user_warning': ''}, request=self.request)
            return Response(result1)

        except:
            # Re-render form page and throw an error message saying "Invalid Private UUID entered!!"
            return {'user_warning': 'Invalid Private UUID entered!!'}

        client.close()
            



    # *************************************************************************************************************
    # *************************************************************************************************************
    # Handler method for modifyPost1 page form field input validation for delete mode
    @view_config(request_method='POST', request_param='automobiles_modify1_deleteButton', renderer='templates/automobiles_templates/automobiles_modifyPost1.pt')
    def automobiles_modifyPost1_delete_handler(self):
        from pyramid.renderers import render
        from pyramid.response import Response
        from pyramid.httpexceptions import HTTPFound
        import pymongo
        from pymongo import MongoClient
        from bson import ObjectId
        from uuid import UUID
        # Extract connection string from enviroment variables
        import os
        from dotenv import load_dotenv
        load_dotenv()
        connection_string = os.environ['MY_CONNECTION_STRING']
        # Open database connection and get or create a database called spacenetng_database
        import dns
        client = MongoClient('%s' % connection_string)
        db = client.spacenetng_database

        # Create or open a text based records collection called automobiles_text_collection
        text_collection= db.automobiles_text_collection


        # Perform CRUD operation on images
        import gridfs
        from gridfs import GridFS

        # Creating or getting an automobiles gridfs collection called 'automobiles_images_collection'
        # (Getting the GridFS object)
        image_collection = GridFS(db, "automobiles_images_collection")


        automobiles_delete_privateUUID = self.request.params['automobiles_modify1_privateUUID']

        # # Delete operation................................................................................
        # Perform a find() query operation on a document using the private UUID for delete permision,
        # and then obtain its "_id" field.

        try:
            # Delete operation on the main text collection initialisation
            res0 = text_collection.find_one({'Private UUID': UUID(automobiles_delete_privateUUID)})
            res1 = res0['_id']    # Obtaining the '_id' attribute diff from that of gridfs

            # Delete operation On image collection
            # Obtain the '_id' values each on all images from the image collection
            # then perform the delete and/or replacement operation

            # Delete images in collection first before deleting the actual collection
            image_names_list_toDelete = res0['Images']

            for name in image_names_list_toDelete:
                res2 = image_collection.find_one({'filename': name})
                res3 = res2._id    # Obtaining the '_id' attribute
                image_collection.delete(ObjectId(res3))  # Delete format for files in gridfs

            # text collection delete
            text_collection.delete_one({'_id': ObjectId(res1)})
            client.close()

            body = (
                "<html style=\"color: green; background-color: whitesmoke; \">"
                "<head><meta http-equiv=\"refresh\" content=\"6;url=/\"></head>"
                "<body>"
                "<h4>Thanks for using our service, your post has been deleted successfully!! "
                "<br />"
                "You will be redirected shortly.</h4>"
                "</body>"
                "</html>"
            )

            return Response(body)


        except:
            # Re-render form page and throw an error message saying "Invalid Private UUID entered!!"
            return {'user_warning': 'Invalid Private UUID entered!!'}






    # *************************************************************************************************************
    # *************************************************************************************************************
    # # response for modifyPost1 page, return this page if correct params were given in modifyPost1 page.
    @view_config(route_name='automobiles_modifyPost2', renderer='templates/automobiles_templates/automobiles_modifyPost2.pt')
    def automobiles_modifyPost2(self):
        return {}



    # *************************************************************************************************************
    # *************************************************************************************************************
    # Perform operation on query params from modifyPost2 page,
    # return values and give the user a Response after creation of a new post
    @view_config(request_method='POST', request_param='automobiles_update_submitButton')
    def automobiles_modifyPost2_response(self):
        # -----------------------------------------------------------------------------------------------------------------
        # Updating and deleting records in database
        from pyramid.response import Response
        from pyramid.httpexceptions import HTTPFound
        import pymongo
        from pymongo import MongoClient
        from bson import ObjectId
        from uuid import UUID
        # Extract connection string from enviroment variables
        import os
        from dotenv import load_dotenv
        load_dotenv()
        connection_string = os.environ['MY_CONNECTION_STRING']
        # Open database connection and get or create a database called spacenetng_database
        import dns
        client = MongoClient('%s' % connection_string)
        db = client.spacenetng_database

        # Create or open a text based records collection called automobiles_text_collection
        text_collection= db.automobiles_text_collection


        # Perform CRUD operation on images
        import gridfs
        from gridfs import GridFS

        # Creating or getting an automobiles gridfs collection called 'automobiles_images_collection'
        # (Getting the GridFS object)
        image_collection = GridFS(db, "automobiles_images_collection")


        # Perform CRUD Operation
        # Get specific date
        import datetime
        automobiles_update_dateTime = datetime.datetime.utcnow()

        automobiles_resAPI_json = {
            "Username": "",
            "State": "",
            "City": "",
            "Description": "",
            "Mobile": "",
            "Email": "",
            "Category": "",
            "Condition": "",
            "Images": [],
            "date": "",
            }

        #######################
        # Collect variables from form fields
        #######################

        # Get text items from form page
        automobiles_update_username = self.request.params['automobiles_update_username']
        automobiles_update_statesList = self.request.params['automobiles_update_statesList']
        automobiles_update_city = self.request.params['automobiles_update_city']
        automobiles_update_textarea = self.request.params['automobiles_update_textarea']
        automobiles_update_mobile = self.request.params['automobiles_update_mobile']
        automobiles_update_email = self.request.params['automobiles_update_email']
        automobiles_update_category = self.request.params['automobiles_update_category']
        automobiles_update_condition = self.request.params['automobiles_update_condition']
           
        # Get images from form page
        automobiles_update_images = self.request.POST.getall('automobiles_update_images')

        # Use this for our rest API insertion operation
        automobiles_update_images_names_list = []
        for automobiles_update_image_name in automobiles_update_images:
            automobiles_update_images_names_list.append(automobiles_update_image_name.filename)

        # use this for gridFS insertion operation
        automobiles_update_images_list = []
        for automobiles_update_image in automobiles_update_images:
            automobiles_update_images_list.append(automobiles_update_image)



        automobiles_resAPI_json["Username"] = automobiles_update_username
        automobiles_resAPI_json["State"] = automobiles_update_statesList
        automobiles_resAPI_json["City"] = automobiles_update_city
        automobiles_resAPI_json["Description"] = automobiles_update_textarea
        automobiles_resAPI_json["Mobile"] = automobiles_update_mobile
        automobiles_resAPI_json["Email"] = automobiles_update_email
        automobiles_resAPI_json["Category"] = automobiles_update_category
        automobiles_resAPI_json["Condition"] = automobiles_update_condition
        automobiles_resAPI_json["Images"] = automobiles_update_images_names_list
        automobiles_resAPI_json["date"] = automobiles_update_dateTime




        # Update operation.........................................................................
        # Update API in database and close our connected client's connection
        # Perform a find() query operation on a document using the private UUID to locate the particular document,
        # and then obtain its "_id" field.
        automobiles_update_privateUUID = self.request.params['automobiles_update_privateUUID']

        # Inititalise overall collection query using the text collection
        res1 = text_collection.find_one({'Private UUID': UUID(automobiles_update_privateUUID)})
        res2 = res1['_id']         # Obtaining the '_id' attribute diff from that of gridfs


        # Before inserting files, query for previous images previously inside database,
        # delete all images there and replace/update with the new one.

        # Obtain the '_id' values each on all images from the image collection
        # then perform the delete operation followed by the replacement operation
        image_names_list_toDelete = res1['Images']

        # Delete images already present first before updating the main collection
        # delete image collection
        for name in image_names_list_toDelete:
            res3 = image_collection.find_one({'filename': name})
            res4 = res3._id    # Obtaining the '_id' attribute
            image_collection.delete(ObjectId(res4))  # Delete format for files in gridfs


        # Main text collection update
        text_collection.update_one({'_id': ObjectId(res2)}, {"$set": automobiles_resAPI_json})

        # then also update the image collection with the new images
        for image in automobiles_update_images_list:
            image_collection.put(image.file, filename=image.filename) # The update operation

            

        # Close our database connection and free up resources.
        client.close()

        body = (
            "<html style=\"color: green; background-color: whitesmoke; \">"
            "<head><meta http-equiv=\"refresh\" content=\"6;url=/\"></head>"
            "<body>"
            "<h4>Thanks for using our service, your post has been updated successfully!! "
            "<br />"
            "You will be redirected shortly.</h4>"
            "</body>"
            "</html>"
        )

        return Response(body)



# ########################################################################################################################
# ########################################################################################################################
# ########################################################################################################################
# View products
@view_defaults(route_name='automobiles_viewProducts1')
class AutomobilesViewProductsViews(object):
    def __init__(self, request):
        self.request = request


    # *************************************************************************************************************
    # *************************************************************************************************************
    @view_config(renderer='templates/automobiles_templates/automobiles_viewProducts1.pt')
    def automobiles_viewProducts1(self):
        return {}


    # *************************************************************************************************************
    # *************************************************************************************************************
    # Response from viewProducts1 page and validate with records in database 
    @view_config(request_method='POST', request_param='automobiles_view_submit')
    def automobiles_viewProducts2_page1A(self):
        from pyramid.httpexceptions import HTTPFound
        # Perform some database matching on sub categories and redirect to the appropriate renderer.
        return HTTPFound(location='automobiles_viewProducts2_page1')


    # *************************************************************************************************************
    # *************************************************************************************************************
    @view_config(route_name='automobiles_viewProducts2_page1', renderer='templates/automobiles_templates/automobiles_viewProducts2_page1.pt')
    def automobiles_viewProducts2_page1B(self):
        import pymongo
        from pymongo import MongoClient
        import gridfs
        from gridfs import GridFS
        # Extract connection string from enviroment variables
        import os
        from dotenv import load_dotenv
        load_dotenv()
        connection_string = os.environ['MY_CONNECTION_STRING']
        # Open database connection and get or create a database called spacenetng_database
        import dns
        client1 = MongoClient('%s' % connection_string)
        db = client1.spacenetng_database

        # Create or open a text based records collection called automobiles_text_collection
        text_collection_automobiles = db.automobiles_text_collection

        # Establish gridfs collection connection
        # Creating or getting an automobiles gridfs collection called 'automobiles_images_collection'
        # (Getting the GridFS object)
        image_collection_automobiles = GridFS(db, "automobiles_images_collection")

        # Retrieve document record from database operation
        automobiles_collection = text_collection_automobiles.find().sort([("_id", pymongo.DESCENDING)]).limit(5) #This returns 25 records

        # Push documents into a list
        automobiles_collection_list = []

        for record in automobiles_collection:
            automobiles_collection_list.append(record)

        document1 = automobiles_collection_list[0]
        document2 = automobiles_collection_list[1]
        document3 = automobiles_collection_list[2]
        document4 = automobiles_collection_list[3]
        document5 = automobiles_collection_list[4]
        

        # Extracting images
        # The images for document1
        document1_images_list_rawFile = []
        for image_name in document1["Images"]:
            document1_images_list_rawFile.append(image_collection_automobiles.get_last_version(filename=image_name))

        # For the images for document2
        document2_images_list_rawFile = []
        for image_name in document2["Images"]:
            document2_images_list_rawFile.append(image_collection_automobiles.get_last_version(filename=image_name))

        # The images for document3
        document3_images_list_rawFile = []
        for image_name in document3["Images"]:
            document3_images_list_rawFile.append(image_collection_automobiles.get_last_version(filename=image_name))

        # The images for document4
        document4_images_list_rawFile = []
        for image_name in document4["Images"]:
            document4_images_list_rawFile.append(image_collection_automobiles.get_last_version(filename=image_name))

        # The images for document5
        document5_images_list_rawFile = []
        for image_name in document5["Images"]:
            document5_images_list_rawFile.append(image_collection_automobiles.get_last_version(filename=image_name))



        ##############################################
        # Collecting record from individual documents
        ##############################################
        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document1
        #######################

        # For the text strings,
        automobiles_collection_document1_productID = document1["Product ID"]
        automobiles_collection_document1_username = document1["Username"]
        automobiles_collection_document1_state = document1["State"]
        automobiles_collection_document1_city = document1["City"]
        automobiles_collection_document1_description = document1["Description"]
        automobiles_collection_document1_mobile = document1["Mobile"]
        automobiles_collection_document1_email = document1["Email"]
        automobiles_collection_document1_category = document1["Category"]
        automobiles_collection_document1_condition = document1["Condition"]



        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document1_images_UTF8_list = []

        for raw_image in document1_images_list_rawFile:
            document1_binaryImage = raw_image.read()
            document1_base64Image = codecs.encode(document1_binaryImage, 'base64')
            document1_UTF8Image = document1_base64Image.decode('utf-8')
            document1_images_UTF8_list.append(document1_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        automobiles_collection_document1_imageA = document1_images_UTF8_list[0]

        try:
            automobiles_collection_document1_imageB = document1_images_UTF8_list[1]
        except:
            automobiles_collection_document1_imageB = document1_images_UTF8_list[0]

        try:
            automobiles_collection_document1_imageC = document1_images_UTF8_list[2]
        except:
            automobiles_collection_document1_imageC = document1_images_UTF8_list[0]

        try:
            automobiles_collection_document1_imageD = document1_images_UTF8_list[3]
        except:
            automobiles_collection_document1_imageD = document1_images_UTF8_list[0]       
        
        try:
            automobiles_collection_document1_imageE = document1_images_UTF8_list[4]
        except:
            automobiles_collection_document1_imageE = document1_images_UTF8_list[0]





        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document2
        #######################

        # For the text strings,
        automobiles_collection_document2_productID = document2["Product ID"]
        automobiles_collection_document2_username = document2["Username"]
        automobiles_collection_document2_state = document2["State"]
        automobiles_collection_document2_city = document2["City"]
        automobiles_collection_document2_description = document2["Description"]
        automobiles_collection_document2_mobile = document2["Mobile"]
        automobiles_collection_document2_email = document2["Email"]
        automobiles_collection_document2_category = document2["Category"]
        automobiles_collection_document2_condition = document2["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document2_images_UTF8_list = []

        for raw_image in document2_images_list_rawFile:
            document2_binaryImage = raw_image.read()
            document2_base64Image = codecs.encode(document2_binaryImage, 'base64')
            document2_UTF8Image = document2_base64Image.decode('utf-8')
            document2_images_UTF8_list.append(document2_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        automobiles_collection_document2_imageA = document2_images_UTF8_list[0]

        try:
            automobiles_collection_document2_imageB = document2_images_UTF8_list[1]
        except:
            automobiles_collection_document2_imageB = document2_images_UTF8_list[0]

        try:
            automobiles_collection_document2_imageC = document2_images_UTF8_list[2]
        except:
            automobiles_collection_document2_imageC = document2_images_UTF8_list[0]

        try:
            automobiles_collection_document2_imageD = document2_images_UTF8_list[3]
        except:
            automobiles_collection_document2_imageD = document2_images_UTF8_list[0]       
        
        try:
            automobiles_collection_document2_imageE = document2_images_UTF8_list[4]
        except:
            automobiles_collection_document2_imageE = document2_images_UTF8_list[0]





        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document3
        #######################

        # For the text strings,
        automobiles_collection_document3_productID = document3["Product ID"]
        automobiles_collection_document3_username = document3["Username"]
        automobiles_collection_document3_state = document3["State"]
        automobiles_collection_document3_city = document3["City"]
        automobiles_collection_document3_description = document3["Description"]
        automobiles_collection_document3_mobile = document3["Mobile"]
        automobiles_collection_document3_email = document3["Email"]
        automobiles_collection_document3_category = document3["Category"]
        automobiles_collection_document3_condition = document3["Condition"]

        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document3_images_UTF8_list = []

        for raw_image in document3_images_list_rawFile:
            document3_binaryImage = raw_image.read()
            document3_base64Image = codecs.encode(document3_binaryImage, 'base64')
            document3_UTF8Image = document3_base64Image.decode('utf-8')
            document3_images_UTF8_list.append(document3_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        automobiles_collection_document3_imageA = document3_images_UTF8_list[0]

        try:
            automobiles_collection_document3_imageB = document3_images_UTF8_list[1]
        except:
            automobiles_collection_document3_imageB = document3_images_UTF8_list[0]

        try:
            automobiles_collection_document3_imageC = document3_images_UTF8_list[2]
        except:
            automobiles_collection_document3_imageC = document3_images_UTF8_list[0]

        try:
            automobiles_collection_document3_imageD = document3_images_UTF8_list[3]
        except:
            automobiles_collection_document3_imageD = document3_images_UTF8_list[0]       
        
        try:
            automobiles_collection_document3_imageE = document3_images_UTF8_list[4]
        except:
            automobiles_collection_document3_imageE = document3_images_UTF8_list[0]





        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document4
        #######################

        # For the text strings,
        automobiles_collection_document4_productID = document4["Product ID"]
        automobiles_collection_document4_username = document4["Username"]
        automobiles_collection_document4_state = document4["State"]
        automobiles_collection_document4_city = document4["City"]
        automobiles_collection_document4_description = document4["Description"]
        automobiles_collection_document4_mobile = document4["Mobile"]
        automobiles_collection_document4_email = document4["Email"]
        automobiles_collection_document4_category = document4["Category"]
        automobiles_collection_document4_condition = document4["Condition"]

        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document4_images_UTF8_list = []

        for raw_image in document4_images_list_rawFile:
            document4_binaryImage = raw_image.read()
            document4_base64Image = codecs.encode(document4_binaryImage, 'base64')
            document4_UTF8Image = document4_base64Image.decode('utf-8')
            document4_images_UTF8_list.append(document4_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        automobiles_collection_document4_imageA = document4_images_UTF8_list[0]

        try:
            automobiles_collection_document4_imageB = document4_images_UTF8_list[1]
        except:
            automobiles_collection_document4_imageB = document4_images_UTF8_list[0]

        try:
            automobiles_collection_document4_imageC = document4_images_UTF8_list[2]
        except:
            automobiles_collection_document4_imageC = document4_images_UTF8_list[0]

        try:
            automobiles_collection_document4_imageD = document4_images_UTF8_list[3]
        except:
            automobiles_collection_document4_imageD = document4_images_UTF8_list[0]       
        
        try:
            automobiles_collection_document4_imageE = document4_images_UTF8_list[4]
        except:
            automobiles_collection_document4_imageE = document4_images_UTF8_list[0]




        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document5
        #######################

        # For the text strings,
        automobiles_collection_document5_productID = document5["Product ID"]
        automobiles_collection_document5_username = document5["Username"]
        automobiles_collection_document5_state = document5["State"]
        automobiles_collection_document5_city = document5["City"]
        automobiles_collection_document5_description = document5["Description"]
        automobiles_collection_document5_mobile = document5["Mobile"]
        automobiles_collection_document5_email = document5["Email"]
        automobiles_collection_document5_category = document5["Category"]
        automobiles_collection_document5_condition = document5["Condition"]

        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document5_images_UTF8_list = []

        for raw_image in document5_images_list_rawFile:
            document5_binaryImage = raw_image.read()
            document5_base64Image = codecs.encode(document5_binaryImage, 'base64')
            document5_UTF8Image = document5_base64Image.decode('utf-8')
            document5_images_UTF8_list.append(document5_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        automobiles_collection_document5_imageA = document5_images_UTF8_list[0]

        try:
            automobiles_collection_document5_imageB = document5_images_UTF8_list[1]
        except:
            automobiles_collection_document5_imageB = document5_images_UTF8_list[0]

        try:
            automobiles_collection_document5_imageC = document5_images_UTF8_list[2]
        except:
            automobiles_collection_document5_imageC = document5_images_UTF8_list[0]

        try:
            automobiles_collection_document5_imageD = document5_images_UTF8_list[3]
        except:
            automobiles_collection_document5_imageD = document5_images_UTF8_list[0]       
        
        try:
            automobiles_collection_document5_imageE = document5_images_UTF8_list[4]
        except:
            automobiles_collection_document5_imageE = document5_images_UTF8_list[0]

        
        # Close our database connection and free up resources.
        client1.close()

        # Pack all return variables into a JSON Structure and use for return
        return {
            
            'productID1' : automobiles_collection_document1_productID,
            'username1' : automobiles_collection_document1_username,
            'state1' : automobiles_collection_document1_state,
            'city1' : automobiles_collection_document1_city,
            'description1' : automobiles_collection_document1_description,
            'mobile1' : automobiles_collection_document1_mobile,
            'email1' : automobiles_collection_document1_email,
            'category1' : automobiles_collection_document1_category,
            'condition1': automobiles_collection_document1_condition,
            'image1A' : automobiles_collection_document1_imageA,
            'image1B' : automobiles_collection_document1_imageB,
            'image1C' : automobiles_collection_document1_imageC,
            'image1D': automobiles_collection_document1_imageD,
            'image1E': automobiles_collection_document1_imageE,

            'productID2' : automobiles_collection_document2_productID,
            'username2' : automobiles_collection_document2_username,
            'state2' : automobiles_collection_document2_state,
            'city2' : automobiles_collection_document2_city,
            'description2' : automobiles_collection_document2_description,
            'mobile2' : automobiles_collection_document2_mobile,
            'email2' : automobiles_collection_document2_email,
            'category2' : automobiles_collection_document2_category,
            'condition2': automobiles_collection_document2_condition,
            'image2A' : automobiles_collection_document2_imageA,
            'image2B' : automobiles_collection_document2_imageB,
            'image2C' : automobiles_collection_document2_imageC,
            'image2D': automobiles_collection_document2_imageD,
            'image2E': automobiles_collection_document2_imageE,

            'productID3' : automobiles_collection_document3_productID,
            'username3' : automobiles_collection_document3_username,
            'state3' : automobiles_collection_document3_state,
            'city3' : automobiles_collection_document3_city,
            'description3' : automobiles_collection_document3_description,
            'mobile3' : automobiles_collection_document3_mobile,
            'email3' : automobiles_collection_document3_email,
            'category3' : automobiles_collection_document3_category,
            'condition3': automobiles_collection_document3_condition,
            'image3A' : automobiles_collection_document3_imageA,
            'image3B' : automobiles_collection_document3_imageB,
            'image3C' : automobiles_collection_document3_imageC,
            'image3D': automobiles_collection_document3_imageD,
            'image3E': automobiles_collection_document3_imageE,

            'productID4' : automobiles_collection_document4_productID,
            'username4' : automobiles_collection_document4_username,
            'state4' : automobiles_collection_document4_state,
            'city4' : automobiles_collection_document4_city,
            'description4' : automobiles_collection_document4_description,
            'mobile4' : automobiles_collection_document4_mobile,
            'email4' : automobiles_collection_document4_email,
            'category4' : automobiles_collection_document4_category,
            'condition4': automobiles_collection_document4_condition,
            'image4A' : automobiles_collection_document4_imageA,
            'image4B' : automobiles_collection_document4_imageB,
            'image4C' : automobiles_collection_document4_imageC,
            'image4D': automobiles_collection_document4_imageD,
            'image4E': automobiles_collection_document4_imageE,

            'productID5' : automobiles_collection_document5_productID,
            'username5' : automobiles_collection_document5_username,
            'state5' : automobiles_collection_document5_state,
            'city5' : automobiles_collection_document5_city,
            'description5' : automobiles_collection_document5_description,
            'mobile5' : automobiles_collection_document5_mobile,
            'email5' : automobiles_collection_document5_email,
            'category5' : automobiles_collection_document5_category,
            'condition5': automobiles_collection_document5_condition,
            'image5A' : automobiles_collection_document5_imageA,
            'image5B' : automobiles_collection_document5_imageB,
            'image5C' : automobiles_collection_document5_imageC,
            'image5D': automobiles_collection_document5_imageD,
            'image5E': automobiles_collection_document5_imageE,
            }


    # View pages....(n)
    # *************************************************************************************************************
    # *************************************************************************************************************
    @view_config(route_name='automobiles_viewProducts2_page2', renderer='templates/automobiles_templates/automobiles_viewProducts2_page2.pt')
    def automobiles_viewProducts2_page2(self):
        import pymongo
        from pymongo import MongoClient
        import gridfs
        from gridfs import GridFS
        # Extract connection string from enviroment variables
        import os
        from dotenv import load_dotenv
        load_dotenv()
        connection_string = os.environ['MY_CONNECTION_STRING']
        # Open database connection and get or create a database called spacenetng_database
        import dns
        client2 = MongoClient('%s' % connection_string)
        db = client2.spacenetng_database

        # Create or open a text based records collection called automobiles_text_collection
        text_collection_automobiles = db.automobiles_text_collection

        # Establish gridfs collection connection
        # Creating or getting an automobiles gridfs collection called 'automobiles_images_collection'
        # (Getting the GridFS object)
        image_collection_automobiles = GridFS(db, "automobiles_images_collection")

        # Retrieve document record from database operation
        automobiles_collection = text_collection_automobiles.find().sort([("_id", pymongo.DESCENDING)]).skip(5).limit(5) #This returns 25 records

        # Push documents into a list
        automobiles_collection_list = []

        for record in automobiles_collection:
            automobiles_collection_list.append(record)

        document6 = automobiles_collection_list[0]
        document7 = automobiles_collection_list[1]
        document8 = automobiles_collection_list[2]
        document9 = automobiles_collection_list[3]
        document10 = automobiles_collection_list[4]



        # The images for document6
        document6_images_list_rawFile = []
        for image_name in document6["Images"]:
            document6_images_list_rawFile.append(image_collection_automobiles.get_last_version(filename=image_name))

        # The images for document7
        document7_images_list_rawFile = []
        for image_name in document7["Images"]:
            document7_images_list_rawFile.append(image_collection_automobiles.get_last_version(filename=image_name))

        # The images for document8
        document8_images_list_rawFile = []
        for image_name in document8["Images"]:
            document8_images_list_rawFile.append(image_collection_automobiles.get_last_version(filename=image_name))

        # The images for document9
        document9_images_list_rawFile = []
        for image_name in document9["Images"]:
            document9_images_list_rawFile.append(image_collection_automobiles.get_last_version(filename=image_name))

        # The images for document10
        document10_images_list_rawFile = []
        for image_name in document10["Images"]:
            document10_images_list_rawFile.append(image_collection_automobiles.get_last_version(filename=image_name))


        ##############################################
        # Collecting record from individual documents
        ##############################################
        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document6
        #######################

        # For the text strings,
        automobiles_collection_document6_productID = document6["Product ID"]
        automobiles_collection_document6_username = document6["Username"]
        automobiles_collection_document6_state = document6["State"]
        automobiles_collection_document6_city = document6["City"]
        automobiles_collection_document6_description = document6["Description"]
        automobiles_collection_document6_mobile = document6["Mobile"]
        automobiles_collection_document6_email = document6["Email"]
        automobiles_collection_document6_category = document6["Category"]
        automobiles_collection_document6_condition = document6["Condition"]



        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document6_images_UTF8_list = []

        for raw_image in document6_images_list_rawFile:
            document6_binaryImage = raw_image.read()
            document6_base64Image = codecs.encode(document6_binaryImage, 'base64')
            document6_UTF8Image = document6_base64Image.decode('utf-8')
            document6_images_UTF8_list.append(document6_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        automobiles_collection_document6_imageA = document6_images_UTF8_list[0]

        try:
            automobiles_collection_document6_imageB = document6_images_UTF8_list[1]
        except:
            automobiles_collection_document6_imageB = document6_images_UTF8_list[0]

        try:
            automobiles_collection_document6_imageC = document6_images_UTF8_list[2]
        except:
            automobiles_collection_document6_imageC = document6_images_UTF8_list[0]

        try:
            automobiles_collection_document6_imageD = document6_images_UTF8_list[3]
        except:
            automobiles_collection_document6_imageD = document6_images_UTF8_list[0]       
        
        try:
            automobiles_collection_document6_imageE = document6_images_UTF8_list[4]
        except:
            automobiles_collection_document6_imageE = document6_images_UTF8_list[0]





        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document7
        #######################

        # For the text strings,
        automobiles_collection_document7_productID = document7["Product ID"]
        automobiles_collection_document7_username = document7["Username"]
        automobiles_collection_document7_state = document7["State"]
        automobiles_collection_document7_city = document7["City"]
        automobiles_collection_document7_description = document7["Description"]
        automobiles_collection_document7_mobile = document7["Mobile"]
        automobiles_collection_document7_email = document7["Email"]
        automobiles_collection_document7_category = document7["Category"]
        automobiles_collection_document7_condition = document7["Condition"]



        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document7_images_UTF8_list = []

        for raw_image in document7_images_list_rawFile:
            document7_binaryImage = raw_image.read()
            document7_base64Image = codecs.encode(document7_binaryImage, 'base64')
            document7_UTF8Image = document7_base64Image.decode('utf-8')
            document7_images_UTF8_list.append(document7_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        automobiles_collection_document7_imageA = document7_images_UTF8_list[0]

        try:
            automobiles_collection_document7_imageB = document7_images_UTF8_list[1]
        except:
            automobiles_collection_document7_imageB = document7_images_UTF8_list[0]

        try:
            automobiles_collection_document7_imageC = document7_images_UTF8_list[2]
        except:
            automobiles_collection_document7_imageC = document7_images_UTF8_list[0]

        try:
            automobiles_collection_document7_imageD = document7_images_UTF8_list[3]
        except:
            automobiles_collection_document7_imageD = document7_images_UTF8_list[0]       
        
        try:
            automobiles_collection_document7_imageE = document7_images_UTF8_list[4]
        except:
            automobiles_collection_document7_imageE = document7_images_UTF8_list[0]




        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document8
        #######################

        # For the text strings,
        automobiles_collection_document8_productID = document8["Product ID"]
        automobiles_collection_document8_username = document8["Username"]
        automobiles_collection_document8_state = document8["State"]
        automobiles_collection_document8_city = document8["City"]
        automobiles_collection_document8_description = document8["Description"]
        automobiles_collection_document8_mobile = document8["Mobile"]
        automobiles_collection_document8_email = document8["Email"]
        automobiles_collection_document8_category = document8["Category"]
        automobiles_collection_document8_condition = document8["Condition"]

   
        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document8_images_UTF8_list = []

        for raw_image in document8_images_list_rawFile:
            document8_binaryImage = raw_image.read()
            document8_base64Image = codecs.encode(document8_binaryImage, 'base64')
            document8_UTF8Image = document8_base64Image.decode('utf-8')
            document8_images_UTF8_list.append(document8_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        automobiles_collection_document8_imageA = document8_images_UTF8_list[0]

        try:
            automobiles_collection_document8_imageB = document8_images_UTF8_list[1]
        except:
            automobiles_collection_document8_imageB = document8_images_UTF8_list[0]

        try:
            automobiles_collection_document8_imageC = document8_images_UTF8_list[2]
        except:
            automobiles_collection_document8_imageC = document8_images_UTF8_list[0]

        try:
            automobiles_collection_document8_imageD = document8_images_UTF8_list[3]
        except:
            automobiles_collection_document8_imageD = document8_images_UTF8_list[0]       
        
        try:
            automobiles_collection_document8_imageE = document8_images_UTF8_list[4]
        except:
            automobiles_collection_document8_imageE = document8_images_UTF8_list[0]




        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document9
        #######################

        # For the text strings,
        automobiles_collection_document9_productID = document9["Product ID"]
        automobiles_collection_document9_username = document9["Username"]
        automobiles_collection_document9_state = document9["State"]
        automobiles_collection_document9_city = document9["City"]
        automobiles_collection_document9_description = document9["Description"]
        automobiles_collection_document9_mobile = document9["Mobile"]
        automobiles_collection_document9_email = document9["Email"]
        automobiles_collection_document9_category = document9["Category"]
        automobiles_collection_document9_condition = document9["Condition"]



        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document9_images_UTF8_list = []

        for raw_image in document9_images_list_rawFile:
            document9_binaryImage = raw_image.read()
            document9_base64Image = codecs.encode(document9_binaryImage, 'base64')
            document9_UTF8Image = document9_base64Image.decode('utf-8')
            document9_images_UTF8_list.append(document9_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        automobiles_collection_document9_imageA = document9_images_UTF8_list[0]

        try:
            automobiles_collection_document9_imageB = document9_images_UTF8_list[1]
        except:
            automobiles_collection_document9_imageB = document9_images_UTF8_list[0]

        try:
            automobiles_collection_document9_imageC = document9_images_UTF8_list[2]
        except:
            automobiles_collection_document9_imageC = document9_images_UTF8_list[0]

        try:
            automobiles_collection_document9_imageD = document9_images_UTF8_list[3]
        except:
            automobiles_collection_document9_imageD = document9_images_UTF8_list[0]       
        
        try:
            automobiles_collection_document9_imageE = document9_images_UTF8_list[4]
        except:
            automobiles_collection_document9_imageE = document9_images_UTF8_list[0]


        # For document10
        #######################

        # For the text strings,
        automobiles_collection_document10_productID = document10["Product ID"]
        automobiles_collection_document10_username = document10["Username"]
        automobiles_collection_document10_state = document10["State"]
        automobiles_collection_document10_city = document10["City"]
        automobiles_collection_document10_description = document10["Description"]
        automobiles_collection_document10_mobile = document10["Mobile"]
        automobiles_collection_document10_email = document10["Email"]
        automobiles_collection_document10_category = document10["Category"]
        automobiles_collection_document10_condition = document10["Condition"]



        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document10_images_UTF8_list = []

        for raw_image in document10_images_list_rawFile:
            document10_binaryImage = raw_image.read()
            document10_base64Image = codecs.encode(document10_binaryImage, 'base64')
            document10_UTF8Image = document10_base64Image.decode('utf-8')
            document10_images_UTF8_list.append(document10_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        automobiles_collection_document10_imageA = document10_images_UTF8_list[0]

        try:
            automobiles_collection_document10_imageB = document10_images_UTF8_list[1]
        except:
            automobiles_collection_document10_imageB = document10_images_UTF8_list[0]

        try:
            automobiles_collection_document10_imageC = document10_images_UTF8_list[2]
        except:
            automobiles_collection_document10_imageC = document10_images_UTF8_list[0]

        try:
            automobiles_collection_document10_imageD = document10_images_UTF8_list[3]
        except:
            automobiles_collection_document10_imageD = document10_images_UTF8_list[0]       
        
        try:
            automobiles_collection_document10_imageE = document10_images_UTF8_list[4]
        except:
            automobiles_collection_document10_imageE = document10_images_UTF8_list[0]

        # Close our database connection and free up resources.
        client2.close()

        # Pack all return variables into a JSON Structure and use for return
        return{
            'productID6' : automobiles_collection_document6_productID,
            'username6' : automobiles_collection_document6_username,
            'state6' : automobiles_collection_document6_state,
            'city6' : automobiles_collection_document6_city,
            'description6' : automobiles_collection_document6_description,
            'mobile6' : automobiles_collection_document6_mobile,
            'email6' : automobiles_collection_document6_email,
            'category6' : automobiles_collection_document6_category,
            'condition6': automobiles_collection_document6_condition,
            'image6A' : automobiles_collection_document6_imageA,
            'image6B' : automobiles_collection_document6_imageB,
            'image6C' : automobiles_collection_document6_imageC,
            'image6D': automobiles_collection_document6_imageD,
            'image6E': automobiles_collection_document6_imageE,

            'productID7' : automobiles_collection_document7_productID,
            'username7' : automobiles_collection_document7_username,
            'state7' : automobiles_collection_document7_state,
            'city7' : automobiles_collection_document7_city,
            'description7' : automobiles_collection_document7_description,
            'mobile7' : automobiles_collection_document7_mobile,
            'email7' : automobiles_collection_document7_email,
            'category7' : automobiles_collection_document7_category,
            'condition7': automobiles_collection_document7_condition,
            'image7A' : automobiles_collection_document7_imageA,
            'image7B' : automobiles_collection_document7_imageB,
            'image7C' : automobiles_collection_document7_imageC,
            'image7D': automobiles_collection_document7_imageD,
            'image7E': automobiles_collection_document7_imageE,

            'productID8' : automobiles_collection_document8_productID,
            'username8' : automobiles_collection_document8_username,
            'state8' : automobiles_collection_document8_state,
            'city8' : automobiles_collection_document8_city,
            'description8' : automobiles_collection_document8_description,
            'mobile8' : automobiles_collection_document8_mobile,
            'email8' : automobiles_collection_document8_email,
            'category8' : automobiles_collection_document8_category,
            'condition8': automobiles_collection_document8_condition,
            'image8A' : automobiles_collection_document8_imageA,
            'image8B' : automobiles_collection_document8_imageB,
            'image8C' : automobiles_collection_document8_imageC,
            'image8D': automobiles_collection_document8_imageD,
            'image8E': automobiles_collection_document8_imageE,

            'productID9' : automobiles_collection_document9_productID,
            'username9' : automobiles_collection_document9_username,
            'state9' : automobiles_collection_document9_state,
            'city9' : automobiles_collection_document9_city,
            'description9' : automobiles_collection_document9_description,
            'mobile9' : automobiles_collection_document9_mobile,
            'email9' : automobiles_collection_document9_email,
            'category9' : automobiles_collection_document9_category,
            'condition9': automobiles_collection_document9_condition,
            'image9A' : automobiles_collection_document9_imageA,
            'image9B' : automobiles_collection_document9_imageB,
            'image9C' : automobiles_collection_document9_imageC,
            'image9D': automobiles_collection_document9_imageD,
            'image9E': automobiles_collection_document9_imageE,

            'productID10' : automobiles_collection_document10_productID,
            'username10' : automobiles_collection_document10_username,
            'state10' : automobiles_collection_document10_state,
            'city10' : automobiles_collection_document10_city,
            'description10' : automobiles_collection_document10_description,
            'mobile10' : automobiles_collection_document10_mobile,
            'email10' : automobiles_collection_document10_email,
            'category10' : automobiles_collection_document10_category,
            'condition10': automobiles_collection_document10_condition,
            'image10A' : automobiles_collection_document10_imageA,
            'image10B' : automobiles_collection_document10_imageB,
            'image10C' : automobiles_collection_document10_imageC,
            'image10D': automobiles_collection_document10_imageD,
            'image10E': automobiles_collection_document10_imageE,            
        }





    # *************************************************************************************************************
    # *************************************************************************************************************
    @view_config(route_name='automobiles_viewProducts2_page3', renderer='templates/automobiles_templates/automobiles_viewProducts2_page3.pt')
    def automobiles_viewProducts2_page3(self):
        import pymongo
        from pymongo import MongoClient
        import gridfs
        from gridfs import GridFS
        # Extract connection string from enviroment variables
        import os
        from dotenv import load_dotenv
        load_dotenv()
        connection_string = os.environ['MY_CONNECTION_STRING']
        # Open database connection and get or create a database called spacenetng_database
        import dns
        client3 = MongoClient('%s' % connection_string)
        db = client3.spacenetng_database

        # Create or open a text based records collection called automobiles_text_collection
        text_collection_automobiles = db.automobiles_text_collection

        # Establish gridfs collection connection
        # Creating or getting an automobiles gridfs collection called 'automobiles_images_collection'
        # (Getting the GridFS object)
        image_collection_automobiles = GridFS(db, "automobiles_images_collection")

        # Retrieve document record from database operation
        automobiles_collection = text_collection_automobiles.find().sort([("_id", pymongo.DESCENDING)]).skip(10).limit(5) #This returns 25 records

        # Push documents into a list
        automobiles_collection_list = []

        for record in automobiles_collection:
            automobiles_collection_list.append(record)



        document11 = automobiles_collection_list[0]
        document12 = automobiles_collection_list[1]
        document13 = automobiles_collection_list[2]
        document14 = automobiles_collection_list[3]
        document15 = automobiles_collection_list[4]

        # Extracting images
        # The images for document11
        document11_images_list_rawFile = []
        for image_name in document11["Images"]:
            document11_images_list_rawFile.append(image_collection_automobiles.get_last_version(filename=image_name))

        # The images for document12
        document12_images_list_rawFile = []
        for image_name in document12["Images"]:
            document12_images_list_rawFile.append(image_collection_automobiles.get_last_version(filename=image_name))

        # The images for document13
        document13_images_list_rawFile = []
        for image_name in document13["Images"]:
            document13_images_list_rawFile.append(image_collection_automobiles.get_last_version(filename=image_name))

        # The images for document14
        document14_images_list_rawFile = []
        for image_name in document14["Images"]:
            document14_images_list_rawFile.append(image_collection_automobiles.get_last_version(filename=image_name))

        # The images for document15
        document15_images_list_rawFile = []
        for image_name in document15["Images"]:
            document15_images_list_rawFile.append(image_collection_automobiles.get_last_version(filename=image_name))



        ##############################################
        # Collecting record from individual documents
        ##############################################
        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document11
        #######################

        # For the text strings,
        automobiles_collection_document11_productID = document11["Product ID"]
        automobiles_collection_document11_username = document11["Username"]
        automobiles_collection_document11_state = document11["State"]
        automobiles_collection_document11_city = document11["City"]
        automobiles_collection_document11_description = document11["Description"]
        automobiles_collection_document11_mobile = document11["Mobile"]
        automobiles_collection_document11_email = document11["Email"]
        automobiles_collection_document11_category = document11["Category"]
        automobiles_collection_document11_condition = document11["Condition"]

        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document11_images_UTF8_list = []

        for raw_image in document11_images_list_rawFile:
            document11_binaryImage = raw_image.read()
            document11_base64Image = codecs.encode(document11_binaryImage, 'base64')
            document11_UTF8Image = document11_base64Image.decode('utf-8')
            document11_images_UTF8_list.append(document11_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        automobiles_collection_document11_imageA = document11_images_UTF8_list[0]

        try:
            automobiles_collection_document11_imageB = document11_images_UTF8_list[1]
        except:
            automobiles_collection_document11_imageB = document11_images_UTF8_list[0]

        try:
            automobiles_collection_document11_imageC = document11_images_UTF8_list[2]
        except:
            automobiles_collection_document11_imageC = document11_images_UTF8_list[0]

        try:
            automobiles_collection_document11_imageD = document11_images_UTF8_list[3]
        except:
            automobiles_collection_document11_imageD = document11_images_UTF8_list[0]       
        
        try:
            automobiles_collection_document11_imageE = document11_images_UTF8_list[4]
        except:
            automobiles_collection_document11_imageE = document11_images_UTF8_list[0]





        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document12
        #######################

        # For the text strings,
        automobiles_collection_document12_productID = document12["Product ID"]
        automobiles_collection_document12_username = document12["Username"]
        automobiles_collection_document12_state = document12["State"]
        automobiles_collection_document12_city = document12["City"]
        automobiles_collection_document12_description = document12["Description"]
        automobiles_collection_document12_mobile = document12["Mobile"]
        automobiles_collection_document12_email = document12["Email"]
        automobiles_collection_document12_category = document12["Category"]
        automobiles_collection_document12_condition = document12["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document12_images_UTF8_list = []

        for raw_image in document12_images_list_rawFile:
            document12_binaryImage = raw_image.read()
            document12_base64Image = codecs.encode(document12_binaryImage, 'base64')
            document12_UTF8Image = document12_base64Image.decode('utf-8')
            document12_images_UTF8_list.append(document12_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        automobiles_collection_document12_imageA = document12_images_UTF8_list[0]

        try:
            automobiles_collection_document12_imageB = document12_images_UTF8_list[1]
        except:
            automobiles_collection_document12_imageB = document12_images_UTF8_list[0]

        try:
            automobiles_collection_document12_imageC = document12_images_UTF8_list[2]
        except:
            automobiles_collection_document12_imageC = document12_images_UTF8_list[0]

        try:
            automobiles_collection_document12_imageD = document12_images_UTF8_list[3]
        except:
            automobiles_collection_document12_imageD = document12_images_UTF8_list[0]       
        
        try:
            automobiles_collection_document12_imageE = document12_images_UTF8_list[4]
        except:
            automobiles_collection_document12_imageE = document12_images_UTF8_list[0]





        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document13
        #######################

        # For the text strings,
        automobiles_collection_document13_productID = document13["Product ID"]
        automobiles_collection_document13_username = document13["Username"]
        automobiles_collection_document13_state = document13["State"]
        automobiles_collection_document13_city = document13["City"]
        automobiles_collection_document13_description = document13["Description"]
        automobiles_collection_document13_mobile = document13["Mobile"]
        automobiles_collection_document13_email = document13["Email"]
        automobiles_collection_document13_category = document13["Category"]
        automobiles_collection_document13_condition = document13["Condition"]

        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document13_images_UTF8_list = []

        for raw_image in document13_images_list_rawFile:
            document13_binaryImage = raw_image.read()
            document13_base64Image = codecs.encode(document13_binaryImage, 'base64')
            document13_UTF8Image = document13_base64Image.decode('utf-8')
            document13_images_UTF8_list.append(document13_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        automobiles_collection_document13_imageA = document13_images_UTF8_list[0]

        try:
            automobiles_collection_document13_imageB = document13_images_UTF8_list[1]
        except:
            automobiles_collection_document13_imageB = document13_images_UTF8_list[0]

        try:
            automobiles_collection_document13_imageC = document13_images_UTF8_list[2]
        except:
            automobiles_collection_document13_imageC = document13_images_UTF8_list[0]

        try:
            automobiles_collection_document13_imageD = document13_images_UTF8_list[3]
        except:
            automobiles_collection_document13_imageD = document13_images_UTF8_list[0]       
        
        try:
            automobiles_collection_document13_imageE = document13_images_UTF8_list[4]
        except:
            automobiles_collection_document13_imageE = document13_images_UTF8_list[0]




        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document14
        #######################

        # For the text strings,
        automobiles_collection_document14_productID = document14["Product ID"]
        automobiles_collection_document14_username = document14["Username"]
        automobiles_collection_document14_state = document14["State"]
        automobiles_collection_document14_city = document14["City"]
        automobiles_collection_document14_description = document14["Description"]
        automobiles_collection_document14_mobile = document14["Mobile"]
        automobiles_collection_document14_email = document14["Email"]
        automobiles_collection_document14_category = document14["Category"]
        automobiles_collection_document14_condition = document14["Condition"]

        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document14_images_UTF8_list = []

        for raw_image in document14_images_list_rawFile:
            document14_binaryImage = raw_image.read()
            document14_base64Image = codecs.encode(document14_binaryImage, 'base64')
            document14_UTF8Image = document14_base64Image.decode('utf-8')
            document14_images_UTF8_list.append(document14_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        automobiles_collection_document14_imageA = document14_images_UTF8_list[0]

        try:
            automobiles_collection_document14_imageB = document14_images_UTF8_list[1]
        except:
            automobiles_collection_document14_imageB = document14_images_UTF8_list[0]

        try:
            automobiles_collection_document14_imageC = document14_images_UTF8_list[2]
        except:
            automobiles_collection_document14_imageC = document14_images_UTF8_list[0]

        try:
            automobiles_collection_document14_imageD = document14_images_UTF8_list[3]
        except:
            automobiles_collection_document14_imageD = document14_images_UTF8_list[0]       
        
        try:
            automobiles_collection_document14_imageE = document14_images_UTF8_list[4]
        except:
            automobiles_collection_document14_imageE = document14_images_UTF8_list[0]






        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document15
        #######################

        # For the text strings,
        automobiles_collection_document15_productID = document15["Product ID"]
        automobiles_collection_document15_username = document15["Username"]
        automobiles_collection_document15_state = document15["State"]
        automobiles_collection_document15_city = document15["City"]
        automobiles_collection_document15_description = document15["Description"]
        automobiles_collection_document15_mobile = document15["Mobile"]
        automobiles_collection_document15_email = document15["Email"]
        automobiles_collection_document15_category = document15["Category"]
        automobiles_collection_document15_condition = document15["Condition"]



        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document15_images_UTF8_list = []

        for raw_image in document15_images_list_rawFile:
            document15_binaryImage = raw_image.read()
            document15_base64Image = codecs.encode(document15_binaryImage, 'base64')
            document15_UTF8Image = document15_base64Image.decode('utf-8')
            document15_images_UTF8_list.append(document15_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        automobiles_collection_document15_imageA = document15_images_UTF8_list[0]

        try:
            automobiles_collection_document15_imageB = document15_images_UTF8_list[1]
        except:
            automobiles_collection_document15_imageB = document15_images_UTF8_list[0]

        try:
            automobiles_collection_document15_imageC = document15_images_UTF8_list[2]
        except:
            automobiles_collection_document15_imageC = document15_images_UTF8_list[0]

        try:
            automobiles_collection_document15_imageD = document15_images_UTF8_list[3]
        except:
            automobiles_collection_document15_imageD = document15_images_UTF8_list[0]       
        
        try:
            automobiles_collection_document15_imageE = document15_images_UTF8_list[4]
        except:
            automobiles_collection_document15_imageE = document15_images_UTF8_list[0]

        # Close our database connection and free up resources.
        client3.close()

        # Pack all return variables into a JSON Structure and use for return
        return{
            'productID11' : automobiles_collection_document11_productID,
            'username11' : automobiles_collection_document11_username,
            'state11' : automobiles_collection_document11_state,
            'city11' : automobiles_collection_document11_city,
            'description11' : automobiles_collection_document11_description,
            'mobile11' : automobiles_collection_document11_mobile,
            'email11' : automobiles_collection_document11_email,
            'category11' : automobiles_collection_document11_category,
            'condition11': automobiles_collection_document11_condition,
            'image11A' : automobiles_collection_document11_imageA,
            'image11B' : automobiles_collection_document11_imageB,
            'image11C' : automobiles_collection_document11_imageC,
            'image11D': automobiles_collection_document11_imageD,
            'image11E': automobiles_collection_document11_imageE,

            'productID12' : automobiles_collection_document12_productID,
            'username12' : automobiles_collection_document12_username,
            'state12' : automobiles_collection_document12_state,
            'city12' : automobiles_collection_document12_city,
            'description12' : automobiles_collection_document12_description,
            'mobile12' : automobiles_collection_document12_mobile,
            'email12' : automobiles_collection_document12_email,
            'category12' : automobiles_collection_document12_category,
            'condition12': automobiles_collection_document12_condition,
            'image12A' : automobiles_collection_document12_imageA,
            'image12B' : automobiles_collection_document12_imageB,
            'image12C' : automobiles_collection_document12_imageC,
            'image12D': automobiles_collection_document12_imageD,
            'image12E': automobiles_collection_document12_imageE,

            'productID13' : automobiles_collection_document13_productID,
            'username13' : automobiles_collection_document13_username,
            'state13' : automobiles_collection_document13_state,
            'city13' : automobiles_collection_document13_city,
            'description13' : automobiles_collection_document13_description,
            'mobile13' : automobiles_collection_document13_mobile,
            'email13' : automobiles_collection_document13_email,
            'category13' : automobiles_collection_document13_category,
            'condition13': automobiles_collection_document13_condition,
            'image13A' : automobiles_collection_document13_imageA,
            'image13B' : automobiles_collection_document13_imageB,
            'image13C' : automobiles_collection_document13_imageC,
            'image13D': automobiles_collection_document13_imageD,
            'image13E': automobiles_collection_document13_imageE,

            'productID14' : automobiles_collection_document14_productID,
            'username14' : automobiles_collection_document14_username,
            'state14' : automobiles_collection_document14_state,
            'city14' : automobiles_collection_document14_city,
            'description14' : automobiles_collection_document14_description,
            'mobile14' : automobiles_collection_document14_mobile,
            'email14' : automobiles_collection_document14_email,
            'category14' : automobiles_collection_document14_category,
            'condition14': automobiles_collection_document14_condition,
            'image14A' : automobiles_collection_document14_imageA,
            'image14B' : automobiles_collection_document14_imageB,
            'image14C' : automobiles_collection_document14_imageC,
            'image14D': automobiles_collection_document14_imageD,
            'image14E': automobiles_collection_document14_imageE,

            'productID15' : automobiles_collection_document15_productID,
            'username15' : automobiles_collection_document15_username,
            'state15' : automobiles_collection_document15_state,
            'city15' : automobiles_collection_document15_city,
            'description15' : automobiles_collection_document15_description,
            'mobile15' : automobiles_collection_document15_mobile,
            'email15' : automobiles_collection_document15_email,
            'category15' : automobiles_collection_document15_category,
            'condition15': automobiles_collection_document15_condition,
            'image15A' : automobiles_collection_document15_imageA,
            'image15B' : automobiles_collection_document15_imageB,
            'image15C' : automobiles_collection_document15_imageC,
            'image15D': automobiles_collection_document15_imageD,
            'image15E': automobiles_collection_document15_imageE,
        }


    # *************************************************************************************************************
    # *************************************************************************************************************        
    @view_config(route_name='automobiles_viewProducts2_page4', renderer='templates/automobiles_templates/automobiles_viewProducts2_page4.pt')
    def automobiles_viewProducts2_page4(self):
        import pymongo
        from pymongo import MongoClient
        import gridfs
        from gridfs import GridFS
        # Extract connection string from enviroment variables
        import os
        from dotenv import load_dotenv
        load_dotenv()
        connection_string = os.environ['MY_CONNECTION_STRING']
        # Open database connection and get or create a database called spacenetng_database
        import dns
        client4 = MongoClient('%s' % connection_string)
        db = client4.spacenetng_database

        # Create or open a text based records collection called automobiles_text_collection
        text_collection_automobiles = db.automobiles_text_collection

        # Establish gridfs collection connection
        # Creating or getting an automobiles gridfs collection called 'automobiles_images_collection'
        # (Getting the GridFS object)
        image_collection_automobiles = GridFS(db, "automobiles_images_collection")

        # Retrieve document record from database operation
        automobiles_collection = text_collection_automobiles.find().sort([("_id", pymongo.DESCENDING)]).skip(15).limit(5) #This returns 25 records

        # Push documents into a list
        automobiles_collection_list = []

        for record in automobiles_collection:
            automobiles_collection_list.append(record)

        document16 = automobiles_collection_list[0]
        document17 = automobiles_collection_list[1]
        document18 = automobiles_collection_list[2]
        document19 = automobiles_collection_list[3]
        document20 = automobiles_collection_list[4]


        # Extracting images
        # The images for document16
        document16_images_list_rawFile = []
        for image_name in document16["Images"]:
            document16_images_list_rawFile.append(image_collection_automobiles.get_last_version(filename=image_name))

        # The images for document17
        document17_images_list_rawFile = []
        for image_name in document17["Images"]:
            document17_images_list_rawFile.append(image_collection_automobiles.get_last_version(filename=image_name))

        # The images for document18
        document18_images_list_rawFile = []
        for image_name in document18["Images"]:
            document18_images_list_rawFile.append(image_collection_automobiles.get_last_version(filename=image_name))

        # The images for document19
        document19_images_list_rawFile = []
        for image_name in document19["Images"]:
            document19_images_list_rawFile.append(image_collection_automobiles.get_last_version(filename=image_name))

        # The images for document20
        document20_images_list_rawFile = []
        for image_name in document20["Images"]:
            document20_images_list_rawFile.append(image_collection_automobiles.get_last_version(filename=image_name))


        ##############################################
        # Collecting record from individual documents
        ##############################################
        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document16
        #######################

        # For the text strings,
        automobiles_collection_document16_productID = document16["Product ID"]
        automobiles_collection_document16_username = document16["Username"]
        automobiles_collection_document16_state = document16["State"]
        automobiles_collection_document16_city = document16["City"]
        automobiles_collection_document16_description = document16["Description"]
        automobiles_collection_document16_mobile = document16["Mobile"]
        automobiles_collection_document16_email = document16["Email"]
        automobiles_collection_document16_category = document16["Category"]
        automobiles_collection_document16_condition = document16["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document16_images_UTF8_list = []

        for raw_image in document16_images_list_rawFile:
            document16_binaryImage = raw_image.read()
            document16_base64Image = codecs.encode(document16_binaryImage, 'base64')
            document16_UTF8Image = document16_base64Image.decode('utf-8')
            document16_images_UTF8_list.append(document16_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        automobiles_collection_document16_imageA = document16_images_UTF8_list[0]

        try:
            automobiles_collection_document16_imageB = document16_images_UTF8_list[1]
        except:
            automobiles_collection_document16_imageB = document16_images_UTF8_list[0]

        try:
            automobiles_collection_document16_imageC = document16_images_UTF8_list[2]
        except:
            automobiles_collection_document16_imageC = document16_images_UTF8_list[0]

        try:
            automobiles_collection_document16_imageD = document16_images_UTF8_list[3]
        except:
            automobiles_collection_document16_imageD = document16_images_UTF8_list[0]       
        
        try:
            automobiles_collection_document16_imageE = document16_images_UTF8_list[4]
        except:
            automobiles_collection_document16_imageE = document16_images_UTF8_list[0]




        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document17
        #######################

        # For the text strings,
        automobiles_collection_document17_productID = document17["Product ID"]
        automobiles_collection_document17_username = document17["Username"]
        automobiles_collection_document17_state = document17["State"]
        automobiles_collection_document17_city = document17["City"]
        automobiles_collection_document17_description = document17["Description"]
        automobiles_collection_document17_mobile = document17["Mobile"]
        automobiles_collection_document17_email = document17["Email"]
        automobiles_collection_document17_category = document17["Category"]
        automobiles_collection_document17_condition = document17["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document17_images_UTF8_list = []

        for raw_image in document17_images_list_rawFile:
            document17_binaryImage = raw_image.read()
            document17_base64Image = codecs.encode(document17_binaryImage, 'base64')
            document17_UTF8Image = document17_base64Image.decode('utf-8')
            document17_images_UTF8_list.append(document17_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        automobiles_collection_document17_imageA = document17_images_UTF8_list[0]

        try:
            automobiles_collection_document17_imageB = document17_images_UTF8_list[1]
        except:
            automobiles_collection_document17_imageB = document17_images_UTF8_list[0]

        try:
            automobiles_collection_document17_imageC = document17_images_UTF8_list[2]
        except:
            automobiles_collection_document17_imageC = document17_images_UTF8_list[0]

        try:
            automobiles_collection_document17_imageD = document17_images_UTF8_list[3]
        except:
            automobiles_collection_document17_imageD = document17_images_UTF8_list[0]       
        
        try:
            automobiles_collection_document17_imageE = document17_images_UTF8_list[4]
        except:
            automobiles_collection_document17_imageE = document17_images_UTF8_list[0]





        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document18
        #######################

        # For the text strings,
        automobiles_collection_document18_productID = document18["Product ID"]
        automobiles_collection_document18_username = document18["Username"]
        automobiles_collection_document18_state = document18["State"]
        automobiles_collection_document18_city = document18["City"]
        automobiles_collection_document18_description = document18["Description"]
        automobiles_collection_document18_mobile = document18["Mobile"]
        automobiles_collection_document18_email = document18["Email"]
        automobiles_collection_document18_category = document18["Category"]
        automobiles_collection_document18_condition = document18["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document18_images_UTF8_list = []

        for raw_image in document18_images_list_rawFile:
            document18_binaryImage = raw_image.read()
            document18_base64Image = codecs.encode(document18_binaryImage, 'base64')
            document18_UTF8Image = document18_base64Image.decode('utf-8')
            document18_images_UTF8_list.append(document18_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        automobiles_collection_document18_imageA = document18_images_UTF8_list[0]

        try:
            automobiles_collection_document18_imageB = document18_images_UTF8_list[1]
        except:
            automobiles_collection_document18_imageB = document18_images_UTF8_list[0]

        try:
            automobiles_collection_document18_imageC = document18_images_UTF8_list[2]
        except:
            automobiles_collection_document18_imageC = document18_images_UTF8_list[0]

        try:
            automobiles_collection_document18_imageD = document18_images_UTF8_list[3]
        except:
            automobiles_collection_document18_imageD = document18_images_UTF8_list[0]       
        
        try:
            automobiles_collection_document18_imageE = document18_images_UTF8_list[4]
        except:
            automobiles_collection_document18_imageE = document18_images_UTF8_list[0]





        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document19
        #######################

        # For the text strings,
        automobiles_collection_document19_productID = document19["Product ID"]
        automobiles_collection_document19_username = document19["Username"]
        automobiles_collection_document19_state = document19["State"]
        automobiles_collection_document19_city = document19["City"]
        automobiles_collection_document19_description = document19["Description"]
        automobiles_collection_document19_mobile = document19["Mobile"]
        automobiles_collection_document19_email = document19["Email"]
        automobiles_collection_document19_category = document19["Category"]
        automobiles_collection_document19_condition = document19["Condition"]

        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document19_images_UTF8_list = []

        for raw_image in document19_images_list_rawFile:
            document19_binaryImage = raw_image.read()
            document19_base64Image = codecs.encode(document19_binaryImage, 'base64')
            document19_UTF8Image = document19_base64Image.decode('utf-8')
            document19_images_UTF8_list.append(document19_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        automobiles_collection_document19_imageA = document19_images_UTF8_list[0]

        try:
            automobiles_collection_document19_imageB = document19_images_UTF8_list[1]
        except:
            automobiles_collection_document19_imageB = document19_images_UTF8_list[0]

        try:
            automobiles_collection_document19_imageC = document19_images_UTF8_list[2]
        except:
            automobiles_collection_document19_imageC = document19_images_UTF8_list[0]

        try:
            automobiles_collection_document19_imageD = document19_images_UTF8_list[3]
        except:
            automobiles_collection_document19_imageD = document19_images_UTF8_list[0]       
        
        try:
            automobiles_collection_document19_imageE = document19_images_UTF8_list[4]
        except:
            automobiles_collection_document19_imageE = document19_images_UTF8_list[0]




        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document20
        #######################

        # For the text strings,
        automobiles_collection_document20_productID = document20["Product ID"]
        automobiles_collection_document20_username = document20["Username"]
        automobiles_collection_document20_state = document20["State"]
        automobiles_collection_document20_city = document20["City"]
        automobiles_collection_document20_description = document20["Description"]
        automobiles_collection_document20_mobile = document20["Mobile"]
        automobiles_collection_document20_email = document20["Email"]
        automobiles_collection_document20_category = document20["Category"]
        automobiles_collection_document20_condition = document20["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document20_images_UTF8_list = []

        for raw_image in document20_images_list_rawFile:
            document20_binaryImage = raw_image.read()
            document20_base64Image = codecs.encode(document20_binaryImage, 'base64')
            document20_UTF8Image = document20_base64Image.decode('utf-8')
            document20_images_UTF8_list.append(document20_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        automobiles_collection_document20_imageA = document20_images_UTF8_list[0]

        try:
            automobiles_collection_document20_imageB = document20_images_UTF8_list[1]
        except:
            automobiles_collection_document20_imageB = document20_images_UTF8_list[0]

        try:
            automobiles_collection_document20_imageC = document20_images_UTF8_list[2]
        except:
            automobiles_collection_document20_imageC = document20_images_UTF8_list[0]

        try:
            automobiles_collection_document20_imageD = document20_images_UTF8_list[3]
        except:
            automobiles_collection_document20_imageD = document20_images_UTF8_list[0]       
        
        try:
            automobiles_collection_document20_imageE = document20_images_UTF8_list[4]
        except:
            automobiles_collection_document20_imageE = document20_images_UTF8_list[0]


        # Close our database connection and free up resources.
        client4.close()

        # Pack all return variables into a JSON Structure and use for return
        return{
            'productID16' : automobiles_collection_document16_productID,
            'username16' : automobiles_collection_document16_username,
            'state16' : automobiles_collection_document16_state,
            'city16' : automobiles_collection_document16_city,
            'description16' : automobiles_collection_document16_description,
            'mobile16' : automobiles_collection_document16_mobile,
            'email16' : automobiles_collection_document16_email,
            'category16' : automobiles_collection_document16_category,
            'condition16': automobiles_collection_document16_condition,
            'image16A' : automobiles_collection_document16_imageA,
            'image16B' : automobiles_collection_document16_imageB,
            'image16C' : automobiles_collection_document16_imageC,
            'image16D': automobiles_collection_document16_imageD,
            'image16E': automobiles_collection_document16_imageE,

            'productID17' : automobiles_collection_document17_productID,
            'username17' : automobiles_collection_document17_username,
            'state17' : automobiles_collection_document17_state,
            'city17' : automobiles_collection_document17_city,
            'description17' : automobiles_collection_document17_description,
            'mobile17' : automobiles_collection_document17_mobile,
            'email17' : automobiles_collection_document17_email,
            'category17' : automobiles_collection_document17_category,
            'condition17': automobiles_collection_document17_condition,
            'image17A' : automobiles_collection_document17_imageA,
            'image17B' : automobiles_collection_document17_imageB,
            'image17C' : automobiles_collection_document17_imageC,
            'image17D': automobiles_collection_document17_imageD,
            'image17E': automobiles_collection_document17_imageE,

            'productID18' : automobiles_collection_document18_productID,
            'username18' : automobiles_collection_document18_username,
            'state18' : automobiles_collection_document18_state,
            'city18' : automobiles_collection_document18_city,
            'description18' : automobiles_collection_document18_description,
            'mobile18' : automobiles_collection_document18_mobile,
            'email18' : automobiles_collection_document18_email,
            'category18' : automobiles_collection_document18_category,
            'condition18': automobiles_collection_document18_condition,
            'image18A' : automobiles_collection_document18_imageA,
            'image18B' : automobiles_collection_document18_imageB,
            'image18C' : automobiles_collection_document18_imageC,
            'image18D': automobiles_collection_document18_imageD,
            'image18E': automobiles_collection_document18_imageE,

            'productID19' : automobiles_collection_document19_productID,
            'username19' : automobiles_collection_document19_username,
            'state19' : automobiles_collection_document19_state,
            'city19' : automobiles_collection_document19_city,
            'description19' : automobiles_collection_document19_description,
            'mobile19' : automobiles_collection_document19_mobile,
            'email19' : automobiles_collection_document19_email,
            'category19' : automobiles_collection_document19_category,
            'condition19': automobiles_collection_document19_condition,
            'image19A' : automobiles_collection_document19_imageA,
            'image19B' : automobiles_collection_document19_imageB,
            'image19C' : automobiles_collection_document19_imageC,
            'image19D': automobiles_collection_document19_imageD,
            'image19E': automobiles_collection_document19_imageE,

            'productID20' : automobiles_collection_document20_productID,
            'username20' : automobiles_collection_document20_username,
            'state20' : automobiles_collection_document20_state,
            'city20' : automobiles_collection_document20_city,
            'description20' : automobiles_collection_document20_description,
            'mobile20' : automobiles_collection_document20_mobile,
            'email20' : automobiles_collection_document20_email,
            'category20' : automobiles_collection_document20_category,
            'condition20': automobiles_collection_document20_condition,
            'image20A' : automobiles_collection_document20_imageA,
            'image20B' : automobiles_collection_document20_imageB,
            'image20C' : automobiles_collection_document20_imageC,
            'image20D': automobiles_collection_document20_imageD,
            'image20E': automobiles_collection_document20_imageE,
        }






    # *************************************************************************************************************
    # *************************************************************************************************************
    @view_config(route_name='automobiles_viewProducts2_page5', renderer='templates/automobiles_templates/automobiles_viewProducts2_page5.pt')
    def automobiles_viewProducts2_page5(self):
        import pymongo
        from pymongo import MongoClient
        import gridfs
        from gridfs import GridFS
        # Extract connection string from enviroment variables
        import os
        from dotenv import load_dotenv
        load_dotenv()
        connection_string = os.environ['MY_CONNECTION_STRING']
        # Open database connection and get or create a database called spacenetng_database
        import dns
        client5 = MongoClient('%s' % connection_string)
        db = client5.spacenetng_database

        # Create or open a text based records collection called automobiles_text_collection
        text_collection_automobiles = db.automobiles_text_collection

        # Establish gridfs collection connection
        # Creating or getting an automobiles gridfs collection called 'automobiles_images_collection'
        # (Getting the GridFS object)
        image_collection_automobiles = GridFS(db, "automobiles_images_collection")

        # Retrieve document record from database operation
        automobiles_collection = text_collection_automobiles.find().sort([("_id", pymongo.DESCENDING)]).skip(20).limit(5) #This returns 25 records

        # Push documents into a list
        automobiles_collection_list = []

        for record in automobiles_collection:
            automobiles_collection_list.append(record)

        document21 = automobiles_collection_list[0]
        document22 = automobiles_collection_list[1]
        document23 = automobiles_collection_list[2]
        document24 = automobiles_collection_list[3]
        document25 = automobiles_collection_list[4]


        # Extracting images
        # The images for document21
        document21_images_list_rawFile = []
        for image_name in document21["Images"]:
            document21_images_list_rawFile.append(image_collection_automobiles.get_last_version(filename=image_name))

        # The images for document22
        document22_images_list_rawFile = []
        for image_name in document22["Images"]:
            document22_images_list_rawFile.append(image_collection_automobiles.get_last_version(filename=image_name))

        # The images for document23
        document23_images_list_rawFile = []
        for image_name in document23["Images"]:
            document23_images_list_rawFile.append(image_collection_automobiles.get_last_version(filename=image_name))

        # The images for document24
        document24_images_list_rawFile = []
        for image_name in document24["Images"]:
            document24_images_list_rawFile.append(image_collection_automobiles.get_last_version(filename=image_name))

        # The images for document25
        document25_images_list_rawFile = []
        for image_name in document25["Images"]:
            document25_images_list_rawFile.append(image_collection_automobiles.get_last_version(filename=image_name))


        ##############################################
        # Collecting record from individual documents
        ##############################################
        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document21
        #######################

        # For the text strings,
        automobiles_collection_document21_productID = document21["Product ID"]
        automobiles_collection_document21_username = document21["Username"]
        automobiles_collection_document21_state = document21["State"]
        automobiles_collection_document21_city = document21["City"]
        automobiles_collection_document21_description = document21["Description"]
        automobiles_collection_document21_mobile = document21["Mobile"]
        automobiles_collection_document21_email = document21["Email"]
        automobiles_collection_document21_category = document21["Category"]
        automobiles_collection_document21_condition = document21["Condition"]



        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document21_images_UTF8_list = []

        for raw_image in document21_images_list_rawFile:
            document21_binaryImage = raw_image.read()
            document21_base64Image = codecs.encode(document21_binaryImage, 'base64')
            document21_UTF8Image = document21_base64Image.decode('utf-8')
            document21_images_UTF8_list.append(document21_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        automobiles_collection_document21_imageA = document21_images_UTF8_list[0]

        try:
            automobiles_collection_document21_imageB = document21_images_UTF8_list[1]
        except:
            automobiles_collection_document21_imageB = document21_images_UTF8_list[0]

        try:
            automobiles_collection_document21_imageC = document21_images_UTF8_list[2]
        except:
            automobiles_collection_document21_imageC = document21_images_UTF8_list[0]

        try:
            automobiles_collection_document21_imageD = document21_images_UTF8_list[3]
        except:
            automobiles_collection_document21_imageD = document21_images_UTF8_list[0]       
        
        try:
            automobiles_collection_document21_imageE = document21_images_UTF8_list[4]
        except:
            automobiles_collection_document21_imageE = document21_images_UTF8_list[0]





        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document22
        #######################

        # For the text strings,
        automobiles_collection_document22_productID = document22["Product ID"]
        automobiles_collection_document22_username = document22["Username"]
        automobiles_collection_document22_state = document22["State"]
        automobiles_collection_document22_city = document22["City"]
        automobiles_collection_document22_description = document22["Description"]
        automobiles_collection_document22_mobile = document22["Mobile"]
        automobiles_collection_document22_email = document22["Email"]
        automobiles_collection_document22_category = document22["Category"]
        automobiles_collection_document22_condition = document22["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document22_images_UTF8_list = []

        for raw_image in document22_images_list_rawFile:
            document22_binaryImage = raw_image.read()
            document22_base64Image = codecs.encode(document22_binaryImage, 'base64')
            document22_UTF8Image = document22_base64Image.decode('utf-8')
            document22_images_UTF8_list.append(document22_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        automobiles_collection_document22_imageA = document22_images_UTF8_list[0]

        try:
            automobiles_collection_document22_imageB = document22_images_UTF8_list[1]
        except:
            automobiles_collection_document22_imageB = document22_images_UTF8_list[0]

        try:
            automobiles_collection_document22_imageC = document22_images_UTF8_list[2]
        except:
            automobiles_collection_document22_imageC = document22_images_UTF8_list[0]

        try:
            automobiles_collection_document22_imageD = document22_images_UTF8_list[3]
        except:
            automobiles_collection_document22_imageD = document22_images_UTF8_list[0]       
        
        try:
            automobiles_collection_document22_imageE = document22_images_UTF8_list[4]
        except:
            automobiles_collection_document22_imageE = document22_images_UTF8_list[0]






        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document23
        #######################

        # For the text strings,
        automobiles_collection_document23_productID = document23["Product ID"]
        automobiles_collection_document23_username = document23["Username"]
        automobiles_collection_document23_state = document23["State"]
        automobiles_collection_document23_city = document23["City"]
        automobiles_collection_document23_description = document23["Description"]
        automobiles_collection_document23_mobile = document23["Mobile"]
        automobiles_collection_document23_email = document23["Email"]
        automobiles_collection_document23_category = document23["Category"]
        automobiles_collection_document23_condition = document23["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document23_images_UTF8_list = []

        for raw_image in document23_images_list_rawFile:
            document23_binaryImage = raw_image.read()
            document23_base64Image = codecs.encode(document23_binaryImage, 'base64')
            document23_UTF8Image = document23_base64Image.decode('utf-8')
            document23_images_UTF8_list.append(document23_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        automobiles_collection_document23_imageA = document23_images_UTF8_list[0]

        try:
            automobiles_collection_document23_imageB = document23_images_UTF8_list[1]
        except:
            automobiles_collection_document23_imageB = document23_images_UTF8_list[0]

        try:
            automobiles_collection_document23_imageC = document23_images_UTF8_list[2]
        except:
            automobiles_collection_document23_imageC = document23_images_UTF8_list[0]

        try:
            automobiles_collection_document23_imageD = document23_images_UTF8_list[3]
        except:
            automobiles_collection_document23_imageD = document23_images_UTF8_list[0]       
        
        try:
            automobiles_collection_document23_imageE = document23_images_UTF8_list[4]
        except:
            automobiles_collection_document23_imageE = document23_images_UTF8_list[0]





        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document24
        #######################

        # For the text strings,
        automobiles_collection_document24_productID = document24["Product ID"]
        automobiles_collection_document24_username = document24["Username"]
        automobiles_collection_document24_state = document24["State"]
        automobiles_collection_document24_city = document24["City"]
        automobiles_collection_document24_description = document24["Description"]
        automobiles_collection_document24_mobile = document24["Mobile"]
        automobiles_collection_document24_email = document24["Email"]
        automobiles_collection_document24_category = document24["Category"]
        automobiles_collection_document24_condition = document24["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document24_images_UTF8_list = []

        for raw_image in document24_images_list_rawFile:
            document24_binaryImage = raw_image.read()
            document24_base64Image = codecs.encode(document24_binaryImage, 'base64')
            document24_UTF8Image = document24_base64Image.decode('utf-8')
            document24_images_UTF8_list.append(document24_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        automobiles_collection_document24_imageA = document24_images_UTF8_list[0]

        try:
            automobiles_collection_document24_imageB = document24_images_UTF8_list[1]
        except:
            automobiles_collection_document24_imageB = document24_images_UTF8_list[0]

        try:
            automobiles_collection_document24_imageC = document24_images_UTF8_list[2]
        except:
            automobiles_collection_document24_imageC = document24_images_UTF8_list[0]

        try:
            automobiles_collection_document24_imageD = document24_images_UTF8_list[3]
        except:
            automobiles_collection_document24_imageD = document24_images_UTF8_list[0]       
        
        try:
            automobiles_collection_document24_imageE = document24_images_UTF8_list[4]
        except:
            automobiles_collection_document24_imageE = document24_images_UTF8_list[0]






        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document25
        #######################

        # For the text strings,
        automobiles_collection_document25_productID = document25["Product ID"]
        automobiles_collection_document25_username = document25["Username"]
        automobiles_collection_document25_state = document25["State"]
        automobiles_collection_document25_city = document25["City"]
        automobiles_collection_document25_description = document25["Description"]
        automobiles_collection_document25_mobile = document25["Mobile"]
        automobiles_collection_document25_email = document25["Email"]
        automobiles_collection_document25_category = document25["Category"]
        automobiles_collection_document25_condition = document25["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document25_images_UTF8_list = []

        for raw_image in document25_images_list_rawFile:
            document25_binaryImage = raw_image.read()
            document25_base64Image = codecs.encode(document25_binaryImage, 'base64')
            document25_UTF8Image = document25_base64Image.decode('utf-8')
            document25_images_UTF8_list.append(document25_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        automobiles_collection_document25_imageA = document25_images_UTF8_list[0]

        try:
            automobiles_collection_document25_imageB = document25_images_UTF8_list[1]
        except:
            automobiles_collection_document25_imageB = document25_images_UTF8_list[0]

        try:
            automobiles_collection_document25_imageC = document25_images_UTF8_list[2]
        except:
            automobiles_collection_document25_imageC = document25_images_UTF8_list[0]

        try:
            automobiles_collection_document25_imageD = document25_images_UTF8_list[3]
        except:
            automobiles_collection_document25_imageD = document25_images_UTF8_list[0]       
        
        try:
            automobiles_collection_document25_imageE = document25_images_UTF8_list[4]
        except:
            automobiles_collection_document25_imageE = document25_images_UTF8_list[0]

        # Close our database connection and free up resources.
        client5.close()

        # Pack all return variables into a JSON Structure and use for return
        return{
            'productID21' : automobiles_collection_document21_productID,
            'username21' : automobiles_collection_document21_username,
            'state21' : automobiles_collection_document21_state,
            'city21' : automobiles_collection_document21_city,
            'description21' : automobiles_collection_document21_description,
            'mobile21' : automobiles_collection_document21_mobile,
            'email21' : automobiles_collection_document21_email,
            'category21' : automobiles_collection_document21_category,
            'condition21': automobiles_collection_document21_condition,
            'image21A' : automobiles_collection_document21_imageA,
            'image21B' : automobiles_collection_document21_imageB,
            'image21C' : automobiles_collection_document21_imageC,
            'image21D': automobiles_collection_document21_imageD,
            'image21E': automobiles_collection_document21_imageE,

            'productID22' : automobiles_collection_document22_productID,
            'username22' : automobiles_collection_document22_username,
            'state22' : automobiles_collection_document22_state,
            'city22' : automobiles_collection_document22_city,
            'description22' : automobiles_collection_document22_description,
            'mobile22' : automobiles_collection_document22_mobile,
            'email22' : automobiles_collection_document22_email,
            'category22' : automobiles_collection_document22_category,
            'condition22': automobiles_collection_document22_condition,
            'image22A' : automobiles_collection_document22_imageA,
            'image22B' : automobiles_collection_document22_imageB,
            'image22C' : automobiles_collection_document22_imageC,
            'image22D': automobiles_collection_document22_imageD,
            'image22E': automobiles_collection_document22_imageE,

            'productID23' : automobiles_collection_document23_productID,
            'username23' : automobiles_collection_document23_username,
            'state23' : automobiles_collection_document23_state,
            'city23' : automobiles_collection_document23_city,
            'description23' : automobiles_collection_document23_description,
            'mobile23' : automobiles_collection_document23_mobile,
            'email23' : automobiles_collection_document23_email,
            'category23' : automobiles_collection_document23_category,
            'condition23': automobiles_collection_document23_condition,
            'image23A' : automobiles_collection_document23_imageA,
            'image23B' : automobiles_collection_document23_imageB,
            'image23C' : automobiles_collection_document23_imageC,
            'image23D': automobiles_collection_document23_imageD,
            'image23E': automobiles_collection_document23_imageE,

            'productID24' : automobiles_collection_document24_productID,
            'username24' : automobiles_collection_document24_username,
            'state24' : automobiles_collection_document24_state,
            'city24' : automobiles_collection_document24_city,
            'description24' : automobiles_collection_document24_description,
            'mobile24' : automobiles_collection_document24_mobile,
            'email24' : automobiles_collection_document24_email,
            'category24' : automobiles_collection_document24_category,
            'condition24': automobiles_collection_document24_condition,
            'image24A' : automobiles_collection_document24_imageA,
            'image24B' : automobiles_collection_document24_imageB,
            'image24C' : automobiles_collection_document24_imageC,
            'image24D': automobiles_collection_document24_imageD,
            'image24E': automobiles_collection_document24_imageE,

            'productID25' : automobiles_collection_document25_productID,
            'username25' : automobiles_collection_document25_username,
            'state25' : automobiles_collection_document25_state,
            'city25' : automobiles_collection_document25_city,
            'description25' : automobiles_collection_document25_description,
            'mobile25' : automobiles_collection_document25_mobile,
            'email25' : automobiles_collection_document25_email,
            'category25' : automobiles_collection_document25_category,
            'condition25': automobiles_collection_document25_condition,
            'image25A' : automobiles_collection_document25_imageA,
            'image25B' : automobiles_collection_document25_imageB,
            'image25C' : automobiles_collection_document25_imageC,
            'image25D': automobiles_collection_document25_imageD,
            'image25E': automobiles_collection_document25_imageE,
        }

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
# HOUSING VIEWS
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************

# ########################################################################################################################
# ########################################################################################################################
# ########################################################################################################################
# Create
@view_defaults(route_name='housing_createNewPost')
class HousingCreateNewPostViews(object):
    def __init__(self, request):
        self.request = request

    # *************************************************************************************************************
    # *************************************************************************************************************
    @view_config(renderer='templates/housing_templates/housing_createNewPost.pt')
    def housing_createNewPost(self):
        return {}


    # *************************************************************************************************************
    # *************************************************************************************************************
    # # Perform operation on query params, send values to the database and give the user a Response after creation 
    # of a new post.
    @view_config(request_method='POST', request_param='housing_create_submitButton')
    def housing_createNewPost_response(self):
        from pyramid.httpexceptions import HTTPFound

        # Collect variables from form fields
        # Get text items from form page
        housing_create_username = self.request.params['housing_create_username']
        housing_create_statesList = self.request.params['housing_create_statesList']
        housing_create_city = self.request.params['housing_create_city']
        housing_create_textarea = self.request.params['housing_create_textarea']
        housing_create_mobile = self.request.params['housing_create_mobile']
        housing_create_email = self.request.params['housing_create_email']
        housing_create_category = self.request.params['housing_create_category']
        housing_create_condition = self.request.params['housing_create_condition']

        # Get images from form page
        housing_create_images = self.request.POST.getall('housing_create_images')

        # Use this for our rest API insertion operation
        housing_create_images_names_list = []
        for housing_create_image_name in housing_create_images:
            housing_create_images_names_list.append(housing_create_image_name.filename)

        # use this for gridFS insertion operation
        housing_create_images_list = []
        for housing_create_image in housing_create_images:
            housing_create_images_list.append(housing_create_image)


        # Create other backend variables
        # create Product ID
        from .myModules import ran_gen_a
        housing_create_productID = ran_gen_a(8, "AEIOSODMG23")


        # Create a UUID number
        import uuid
        housing_create_privateUUID = uuid.uuid4()

        # Get specific date
        import datetime
        housing_create_dateTime = datetime.datetime.utcnow()


        # Create our RES API structure and push data to the RES
        housing_resAPI_json = {
            "Private UUID": "",
            "Product ID": "",
            "Username": "",
            "State": "",
            "City": "",
            "Description": "",
            "Mobile": "",
            "Email": "",
            "Category": "",
            "Condition": "",
            "Images": [],
            "date": "",
        }


        housing_resAPI_json["Private UUID"] = housing_create_privateUUID
        housing_resAPI_json["Product ID"] = housing_create_productID
        housing_resAPI_json["Username"] = housing_create_username
        housing_resAPI_json["State"] = housing_create_statesList
        housing_resAPI_json["City"] = housing_create_city
        housing_resAPI_json["Description"] = housing_create_textarea
        housing_resAPI_json["Mobile"] = housing_create_mobile
        housing_resAPI_json["Email"] = housing_create_email
        housing_resAPI_json["Category"] = housing_create_category
        housing_resAPI_json["Condition"] = housing_create_condition
        housing_resAPI_json["Images"] = housing_create_images_names_list
        housing_resAPI_json["date"] = housing_create_dateTime



        # Initialise database connection and perform CRUD operation on text and images
        # Perform CRUD operation on text strings
        import pymongo
        from pymongo import MongoClient
        # Extract connection string from enviroment variables
        import os
        from dotenv import load_dotenv
        load_dotenv()
        connection_string = os.environ['MY_CONNECTION_STRING']
        # Open database connection and get or create a database called spacenetng_database
        import dns
        client = MongoClient('%s' % connection_string)
        db = client.spacenetng_database

        # Create or open a text based records collection called housing_text_collection
        text_collection= db.housing_text_collection

        # Insert API into database and close our connected client's connection
        text_collection.insert_one(housing_resAPI_json)


        # Perform CRUD operation on images
        import gridfs
        from gridfs import GridFS

        # Creating or getting an housing gridfs collection called 'housing_images_collection'
        # (Getting the GridFS object)
        image_collection = GridFS(db, "housing_images_collection")

        # Inserting files into gridfs and close our connected client's connection
        for image in housing_create_images_list:
            image_collection.put(image.file, filename=image.filename)

        # Close our database connection and free up resources.
        client.close()


        # # ############################################################################################
        # # Send private UUID to user's Email using login details and gmail server using inbuilt python email package
        import smtplib, os, sys
        from smtplib import SMTP
        from email.message import EmailMessage
        from dotenv import load_dotenv
        load_dotenv()

        try:
            email_content = ("""\
            Hello %s, thanks for posting on spacenetng platform, an online commercial market place where buyers and sellers
            meet to carry out business transactions. Please be advised, a private user UUID has been created for you which 
            you can use to update or delete your post and it should be kept confidential.\n
            Here is your Seceret hey: %s\n
            For support and enquiries please contact us via our contact details found on our contact page in our website.\n
            Thanks for using this service, we hope to serve you better!!.
            """
            % (housing_create_username, housing_create_privateUUID)
            
            )

            msg = EmailMessage()
            msg.set_content(email_content)

            msg['Subject'] = 'Your UUID from Spacenetng'
            msg['From'] = 'spacenetngbase@gmail.com'
            msg['To'] = housing_create_email

            server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server_ssl.ehlo()

            email = os.environ['MY_EMAIL_ADDRESS']
            passWord = os.environ['MY_EMAIL_PASSWORD']

            server_ssl.login(email, passWord)
            server_ssl.send_message(msg)       
            server_ssl.quit()   # Terminate the SMTP session and free up resources       
            
            # Or And,
            # print('Message sent successfully!!')

        except:
            pass
            # Or
            # print X

        finally:
            pass


        ######################################################
        # Redirect user to view what he/she has just posted                      
        body = (
            "<html style=\"color: green; background-color: whitesmoke; \">"
            "<head><meta http-equiv=\"refresh\" content=\"6;url=/housing_viewProducts2_page1\"></head>"
            "<body>"
            "<h4>Thanks for using our service, your post has been recorded successfully!! "
            "<br />"
            "You will be redirected shortly.</h4>"
            "</body>"
            "</html>"
        )

        return Response(body)





# ########################################################################################################################
# ########################################################################################################################
# ########################################################################################################################
# Modify
@view_defaults(route_name='housing_modifyPost1')
class HousingModifyPostViews(object):
    def __init__(self, request):
        self.request = request


    # *************************************************************************************************************
    # *************************************************************************************************************
    @view_config(renderer='templates/housing_templates/housing_modifyPost1.pt')
    def housing_modifyPost1(self):
        return {'user_warning': ''}



    # *************************************************************************************************************
    # *************************************************************************************************************
    # Handler method for modifyPost1 page form field input validation for edit mode
    # Redirect to modifyPost2 page if valid private uuid was given, else throw error.
    @view_config(request_method='POST', request_param='housing_modify1_editButton', renderer='templates/housing_templates/housing_modifyPost1.pt')
    def housing_modifyPost1_update_handler(self):
        from pyramid.renderers import render
        from pyramid.response import Response
        from pyramid.httpexceptions import HTTPFound
        import pymongo
        from pymongo import MongoClient
        from bson import ObjectId
        from uuid import UUID
        # Extract connection string from enviroment variables
        import os
        from dotenv import load_dotenv
        load_dotenv()
        connection_string = os.environ['MY_CONNECTION_STRING']
        # Open database connection and get or create a database called spacenetng_database
        import dns
        client = MongoClient('%s' % connection_string)
        db = client.spacenetng_database

        # Create or open a text based records collection called housing_text_collection
        text_collection= db.housing_text_collection


        housing_update_privateUUID = self.request.params['housing_modify1_privateUUID']

        try:
            text_collection.find_one({'Private UUID': UUID(housing_update_privateUUID)})
            result1 = render('templates/housing_templates/housing_modifyPost2.pt' , {'private_UUID': housing_update_privateUUID, 'user_warning': ''}, request=self.request)
            return Response(result1)

        except:
            # Re-render form page and throw an error message saying "Invalid Private UUID entered!!"
            return {'user_warning': 'Invalid Private UUID entered!!'}

        client.close()
            



    # *************************************************************************************************************
    # *************************************************************************************************************
    # Handler method for modifyPost1 page form field input validation for delete mode
    @view_config(request_method='POST', request_param='housing_modify1_deleteButton', renderer='templates/housing_templates/housing_modifyPost1.pt')
    def housing_modifyPost1_delete_handler(self):
        from pyramid.renderers import render
        from pyramid.response import Response
        from pyramid.httpexceptions import HTTPFound
        import pymongo
        from pymongo import MongoClient
        from bson import ObjectId
        from uuid import UUID
        # Extract connection string from enviroment variables
        import os
        from dotenv import load_dotenv
        load_dotenv()
        connection_string = os.environ['MY_CONNECTION_STRING']
        # Open database connection and get or create a database called spacenetng_database
        import dns
        client = MongoClient('%s' % connection_string)
        db = client.spacenetng_database

        # Create or open a text based records collection called housing_text_collection
        text_collection= db.housing_text_collection


        # Perform CRUD operation on images
        import gridfs
        from gridfs import GridFS

        # Creating or getting an housing gridfs collection called 'housing_images_collection'
        # (Getting the GridFS object)
        image_collection = GridFS(db, "housing_images_collection")


        housing_delete_privateUUID = self.request.params['housing_modify1_privateUUID']

        # # Delete operation................................................................................
        # Perform a find() query operation on a document using the private UUID for delete permision,
        # and then obtain its "_id" field.

        try:
            # Delete operation on the main text collection initialisation
            res0 = text_collection.find_one({'Private UUID': UUID(housing_delete_privateUUID)})
            res1 = res0['_id']    # Obtaining the '_id' attribute diff from that of gridfs

            # Delete operation On image collection
            # Obtain the '_id' values each on all images from the image collection
            # then perform the delete and/or replacement operation

            # Delete images in collection first before deleting the actual collection
            image_names_list_toDelete = res0['Images']

            for name in image_names_list_toDelete:
                res2 = image_collection.find_one({'filename': name})
                res3 = res2._id    # Obtaining the '_id' attribute
                image_collection.delete(ObjectId(res3))  # Delete format for files in gridfs

            # text collection delete
            text_collection.delete_one({'_id': ObjectId(res1)})
            client.close()

            body = (
                "<html style=\"color: green; background-color: whitesmoke; \">"
                "<head><meta http-equiv=\"refresh\" content=\"6;url=/\"></head>"
                "<body>"
                "<h4>Thanks for using our service, your post has been deleted successfully!! "
                "<br />"
                "You will be redirected shortly.</h4>"
                "</body>"
                "</html>"
            )

            return Response(body)


        except:
            # Re-render form page and throw an error message saying "Invalid Private UUID entered!!"
            return {'user_warning': 'Invalid Private UUID entered!!'}






    # *************************************************************************************************************
    # *************************************************************************************************************
    # # response for modifyPost1 page, return this page if correct params were given in modifyPost1 page.
    @view_config(route_name='housing_modifyPost2', renderer='templates/housing_templates/housing_modifyPost2.pt')
    def housing_modifyPost2(self):
        return {}



    # *************************************************************************************************************
    # *************************************************************************************************************
    # Perform operation on query params from modifyPost2 page,
    # return values and give the user a Response after creation of a new post
    @view_config(request_method='POST', request_param='housing_update_submitButton')
    def housing_modifyPost2_response(self):
        # -----------------------------------------------------------------------------------------------------------------
        # Updating and deleting records in database
        from pyramid.response import Response
        from pyramid.httpexceptions import HTTPFound
        import pymongo
        from pymongo import MongoClient
        from bson import ObjectId
        from uuid import UUID
        # Extract connection string from enviroment variables
        import os
        from dotenv import load_dotenv
        load_dotenv()
        connection_string = os.environ['MY_CONNECTION_STRING']
        # Open database connection and get or create a database called spacenetng_database
        import dns
        client = MongoClient('%s' % connection_string)
        db = client.spacenetng_database

        # Create or open a text based records collection called housing_text_collection
        text_collection= db.housing_text_collection


        # Perform CRUD operation on images
        import gridfs
        from gridfs import GridFS

        # Creating or getting an housing gridfs collection called 'housing_images_collection'
        # (Getting the GridFS object)
        image_collection = GridFS(db, "housing_images_collection")


        # Perform CRUD Operation
        # Get specific date
        import datetime
        housing_update_dateTime = datetime.datetime.utcnow()

        housing_resAPI_json = {
            "Username": "",
            "State": "",
            "City": "",
            "Description": "",
            "Mobile": "",
            "Email": "",
            "Category": "",
            "Condition": "",
            "Images": [],
            "date": "",
            }

        #######################
        # Collect variables from form fields
        #######################

        # Get text items from form page
        housing_update_username = self.request.params['housing_update_username']
        housing_update_statesList = self.request.params['housing_update_statesList']
        housing_update_city = self.request.params['housing_update_city']
        housing_update_textarea = self.request.params['housing_update_textarea']
        housing_update_mobile = self.request.params['housing_update_mobile']
        housing_update_email = self.request.params['housing_update_email']
        housing_update_category = self.request.params['housing_update_category']
        housing_update_condition = self.request.params['housing_update_condition']
           
        # Get images from form page
        housing_update_images = self.request.POST.getall('housing_update_images')

        # Use this for our rest API insertion operation
        housing_update_images_names_list = []
        for housing_update_image_name in housing_update_images:
            housing_update_images_names_list.append(housing_update_image_name.filename)

        # use this for gridFS insertion operation
        housing_update_images_list = []
        for housing_update_image in housing_update_images:
            housing_update_images_list.append(housing_update_image)



        housing_resAPI_json["Username"] = housing_update_username
        housing_resAPI_json["State"] = housing_update_statesList
        housing_resAPI_json["City"] = housing_update_city
        housing_resAPI_json["Description"] = housing_update_textarea
        housing_resAPI_json["Mobile"] = housing_update_mobile
        housing_resAPI_json["Email"] = housing_update_email
        housing_resAPI_json["Category"] = housing_update_category
        housing_resAPI_json["Condition"] = housing_update_condition
        housing_resAPI_json["Images"] = housing_update_images_names_list
        housing_resAPI_json["date"] = housing_update_dateTime




        # Update operation.........................................................................
        # Update API in database and close our connected client's connection
        # Perform a find() query operation on a document using the private UUID to locate the particular document,
        # and then obtain its "_id" field.
        housing_update_privateUUID = self.request.params['housing_update_privateUUID']

        # Inititalise overall collection query using the text collection
        res1 = text_collection.find_one({'Private UUID': UUID(housing_update_privateUUID)})
        res2 = res1['_id']         # Obtaining the '_id' attribute diff from that of gridfs


        # Before inserting files, query for previous images previously inside database,
        # delete all images there and replace/update with the new one.

        # Obtain the '_id' values each on all images from the image collection
        # then perform the delete operation followed by the replacement operation
        image_names_list_toDelete = res1['Images']

        # Delete images already present first before updating the main collection
        # delete image collection
        for name in image_names_list_toDelete:
            res3 = image_collection.find_one({'filename': name})
            res4 = res3._id    # Obtaining the '_id' attribute
            image_collection.delete(ObjectId(res4))  # Delete format for files in gridfs


        # Main text collection update
        text_collection.update_one({'_id': ObjectId(res2)}, {"$set": housing_resAPI_json})

        # then also update the image collection with the new images
        for image in housing_update_images_list:
            image_collection.put(image.file, filename=image.filename) # The update operation

            

        # Close our database connection and free up resources.
        client.close()

        body = (
            "<html style=\"color: green; background-color: whitesmoke; \">"
            "<head><meta http-equiv=\"refresh\" content=\"6;url=/\"></head>"
            "<body>"
            "<h4>Thanks for using our service, your post has been updated successfully!! "
            "<br />"
            "You will be redirected shortly.</h4>"
            "</body>"
            "</html>"
        )

        return Response(body)



# ########################################################################################################################
# ########################################################################################################################
# ########################################################################################################################
# View products
@view_defaults(route_name='housing_viewProducts1')
class HousingViewProductsViews(object):
    def __init__(self, request):
        self.request = request


    # *************************************************************************************************************
    # *************************************************************************************************************
    @view_config(renderer='templates/housing_templates/housing_viewProducts1.pt')
    def housing_viewProducts1(self):
        return {}


    # *************************************************************************************************************
    # *************************************************************************************************************
    # Response from viewProducts1 page and validate with records in database 
    @view_config(request_method='POST', request_param='housing_view_submit')
    def housing_viewProducts2_page1A(self):
        from pyramid.httpexceptions import HTTPFound
        # Perform some database matching on sub categories and redirect to the appropriate renderer.
        return HTTPFound(location='housing_viewProducts2_page1')

    # *************************************************************************************************************
    # *************************************************************************************************************
    @view_config(route_name='housing_viewProducts2_page1', renderer='templates/housing_templates/housing_viewProducts2_page1.pt')
    def housing_viewProducts2_page1B(self):
        import pymongo
        from pymongo import MongoClient
        import gridfs
        from gridfs import GridFS
        # Extract connection string from enviroment variables
        import os
        from dotenv import load_dotenv
        load_dotenv()
        connection_string = os.environ['MY_CONNECTION_STRING']
        # Open database connection and get or create a database called spacenetng_database
        import dns
        client1 = MongoClient('%s' % connection_string)
        db = client1.spacenetng_database

        # Create or open a text based records collection called housing_text_collection
        text_collection_housing = db.housing_text_collection

        # Establish gridfs collection connection
        # Creating or getting an housing gridfs collection called 'housing_images_collection'
        # (Getting the GridFS object)
        image_collection_housing = GridFS(db, "housing_images_collection")

        # Retrieve document record from database operation
        housing_collection = text_collection_housing.find().sort([("_id", pymongo.DESCENDING)]).limit(5) #This returns 25 records

        # Push documents into a list
        housing_collection_list = []

        for record in housing_collection:
            housing_collection_list.append(record)

        document1 = housing_collection_list[0]
        document2 = housing_collection_list[1]
        document3 = housing_collection_list[2]
        document4 = housing_collection_list[3]
        document5 = housing_collection_list[4]
        

        # Extracting images
        # The images for document1
        document1_images_list_rawFile = []
        for image_name in document1["Images"]:
            document1_images_list_rawFile.append(image_collection_housing.get_last_version(filename=image_name))

        # For the images for document2
        document2_images_list_rawFile = []
        for image_name in document2["Images"]:
            document2_images_list_rawFile.append(image_collection_housing.get_last_version(filename=image_name))

        # The images for document3
        document3_images_list_rawFile = []
        for image_name in document3["Images"]:
            document3_images_list_rawFile.append(image_collection_housing.get_last_version(filename=image_name))

        # The images for document4
        document4_images_list_rawFile = []
        for image_name in document4["Images"]:
            document4_images_list_rawFile.append(image_collection_housing.get_last_version(filename=image_name))

        # The images for document5
        document5_images_list_rawFile = []
        for image_name in document5["Images"]:
            document5_images_list_rawFile.append(image_collection_housing.get_last_version(filename=image_name))



        ##############################################
        # Collecting record from individual documents
        ##############################################
        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document1
        #######################

        # For the text strings,
        housing_collection_document1_productID = document1["Product ID"]
        housing_collection_document1_username = document1["Username"]
        housing_collection_document1_state = document1["State"]
        housing_collection_document1_city = document1["City"]
        housing_collection_document1_description = document1["Description"]
        housing_collection_document1_mobile = document1["Mobile"]
        housing_collection_document1_email = document1["Email"]
        housing_collection_document1_category = document1["Category"]
        housing_collection_document1_condition = document1["Condition"]



        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document1_images_UTF8_list = []

        for raw_image in document1_images_list_rawFile:
            document1_binaryImage = raw_image.read()
            document1_base64Image = codecs.encode(document1_binaryImage, 'base64')
            document1_UTF8Image = document1_base64Image.decode('utf-8')
            document1_images_UTF8_list.append(document1_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        housing_collection_document1_imageA = document1_images_UTF8_list[0]

        try:
            housing_collection_document1_imageB = document1_images_UTF8_list[1]
        except:
            housing_collection_document1_imageB = document1_images_UTF8_list[0]

        try:
            housing_collection_document1_imageC = document1_images_UTF8_list[2]
        except:
            housing_collection_document1_imageC = document1_images_UTF8_list[0]

        try:
            housing_collection_document1_imageD = document1_images_UTF8_list[3]
        except:
            housing_collection_document1_imageD = document1_images_UTF8_list[0]       
        
        try:
            housing_collection_document1_imageE = document1_images_UTF8_list[4]
        except:
            housing_collection_document1_imageE = document1_images_UTF8_list[0]





        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document2
        #######################

        # For the text strings,
        housing_collection_document2_productID = document2["Product ID"]
        housing_collection_document2_username = document2["Username"]
        housing_collection_document2_state = document2["State"]
        housing_collection_document2_city = document2["City"]
        housing_collection_document2_description = document2["Description"]
        housing_collection_document2_mobile = document2["Mobile"]
        housing_collection_document2_email = document2["Email"]
        housing_collection_document2_category = document2["Category"]
        housing_collection_document2_condition = document2["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document2_images_UTF8_list = []

        for raw_image in document2_images_list_rawFile:
            document2_binaryImage = raw_image.read()
            document2_base64Image = codecs.encode(document2_binaryImage, 'base64')
            document2_UTF8Image = document2_base64Image.decode('utf-8')
            document2_images_UTF8_list.append(document2_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        housing_collection_document2_imageA = document2_images_UTF8_list[0]

        try:
            housing_collection_document2_imageB = document2_images_UTF8_list[1]
        except:
            housing_collection_document2_imageB = document2_images_UTF8_list[0]

        try:
            housing_collection_document2_imageC = document2_images_UTF8_list[2]
        except:
            housing_collection_document2_imageC = document2_images_UTF8_list[0]

        try:
            housing_collection_document2_imageD = document2_images_UTF8_list[3]
        except:
            housing_collection_document2_imageD = document2_images_UTF8_list[0]       
        
        try:
            housing_collection_document2_imageE = document2_images_UTF8_list[4]
        except:
            housing_collection_document2_imageE = document2_images_UTF8_list[0]





        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document3
        #######################

        # For the text strings,
        housing_collection_document3_productID = document3["Product ID"]
        housing_collection_document3_username = document3["Username"]
        housing_collection_document3_state = document3["State"]
        housing_collection_document3_city = document3["City"]
        housing_collection_document3_description = document3["Description"]
        housing_collection_document3_mobile = document3["Mobile"]
        housing_collection_document3_email = document3["Email"]
        housing_collection_document3_category = document3["Category"]
        housing_collection_document3_condition = document3["Condition"]

        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document3_images_UTF8_list = []

        for raw_image in document3_images_list_rawFile:
            document3_binaryImage = raw_image.read()
            document3_base64Image = codecs.encode(document3_binaryImage, 'base64')
            document3_UTF8Image = document3_base64Image.decode('utf-8')
            document3_images_UTF8_list.append(document3_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        housing_collection_document3_imageA = document3_images_UTF8_list[0]

        try:
            housing_collection_document3_imageB = document3_images_UTF8_list[1]
        except:
            housing_collection_document3_imageB = document3_images_UTF8_list[0]

        try:
            housing_collection_document3_imageC = document3_images_UTF8_list[2]
        except:
            housing_collection_document3_imageC = document3_images_UTF8_list[0]

        try:
            housing_collection_document3_imageD = document3_images_UTF8_list[3]
        except:
            housing_collection_document3_imageD = document3_images_UTF8_list[0]       
        
        try:
            housing_collection_document3_imageE = document3_images_UTF8_list[4]
        except:
            housing_collection_document3_imageE = document3_images_UTF8_list[0]





        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document4
        #######################

        # For the text strings,
        housing_collection_document4_productID = document4["Product ID"]
        housing_collection_document4_username = document4["Username"]
        housing_collection_document4_state = document4["State"]
        housing_collection_document4_city = document4["City"]
        housing_collection_document4_description = document4["Description"]
        housing_collection_document4_mobile = document4["Mobile"]
        housing_collection_document4_email = document4["Email"]
        housing_collection_document4_category = document4["Category"]
        housing_collection_document4_condition = document4["Condition"]

        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document4_images_UTF8_list = []

        for raw_image in document4_images_list_rawFile:
            document4_binaryImage = raw_image.read()
            document4_base64Image = codecs.encode(document4_binaryImage, 'base64')
            document4_UTF8Image = document4_base64Image.decode('utf-8')
            document4_images_UTF8_list.append(document4_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        housing_collection_document4_imageA = document4_images_UTF8_list[0]

        try:
            housing_collection_document4_imageB = document4_images_UTF8_list[1]
        except:
            housing_collection_document4_imageB = document4_images_UTF8_list[0]

        try:
            housing_collection_document4_imageC = document4_images_UTF8_list[2]
        except:
            housing_collection_document4_imageC = document4_images_UTF8_list[0]

        try:
            housing_collection_document4_imageD = document4_images_UTF8_list[3]
        except:
            housing_collection_document4_imageD = document4_images_UTF8_list[0]       
        
        try:
            housing_collection_document4_imageE = document4_images_UTF8_list[4]
        except:
            housing_collection_document4_imageE = document4_images_UTF8_list[0]




        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document5
        #######################

        # For the text strings,
        housing_collection_document5_productID = document5["Product ID"]
        housing_collection_document5_username = document5["Username"]
        housing_collection_document5_state = document5["State"]
        housing_collection_document5_city = document5["City"]
        housing_collection_document5_description = document5["Description"]
        housing_collection_document5_mobile = document5["Mobile"]
        housing_collection_document5_email = document5["Email"]
        housing_collection_document5_category = document5["Category"]
        housing_collection_document5_condition = document5["Condition"]

        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document5_images_UTF8_list = []

        for raw_image in document5_images_list_rawFile:
            document5_binaryImage = raw_image.read()
            document5_base64Image = codecs.encode(document5_binaryImage, 'base64')
            document5_UTF8Image = document5_base64Image.decode('utf-8')
            document5_images_UTF8_list.append(document5_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        housing_collection_document5_imageA = document5_images_UTF8_list[0]

        try:
            housing_collection_document5_imageB = document5_images_UTF8_list[1]
        except:
            housing_collection_document5_imageB = document5_images_UTF8_list[0]

        try:
            housing_collection_document5_imageC = document5_images_UTF8_list[2]
        except:
            housing_collection_document5_imageC = document5_images_UTF8_list[0]

        try:
            housing_collection_document5_imageD = document5_images_UTF8_list[3]
        except:
            housing_collection_document5_imageD = document5_images_UTF8_list[0]       
        
        try:
            housing_collection_document5_imageE = document5_images_UTF8_list[4]
        except:
            housing_collection_document5_imageE = document5_images_UTF8_list[0]

        
        # Close our database connection and free up resources.
        client1.close()

        # Pack all return variables into a JSON Structure and use for return
        return {
            
            'productID1' : housing_collection_document1_productID,
            'username1' : housing_collection_document1_username,
            'state1' : housing_collection_document1_state,
            'city1' : housing_collection_document1_city,
            'description1' : housing_collection_document1_description,
            'mobile1' : housing_collection_document1_mobile,
            'email1' : housing_collection_document1_email,
            'category1' : housing_collection_document1_category,
            'condition1': housing_collection_document1_condition,
            'image1A' : housing_collection_document1_imageA,
            'image1B' : housing_collection_document1_imageB,
            'image1C' : housing_collection_document1_imageC,
            'image1D': housing_collection_document1_imageD,
            'image1E': housing_collection_document1_imageE,

            'productID2' : housing_collection_document2_productID,
            'username2' : housing_collection_document2_username,
            'state2' : housing_collection_document2_state,
            'city2' : housing_collection_document2_city,
            'description2' : housing_collection_document2_description,
            'mobile2' : housing_collection_document2_mobile,
            'email2' : housing_collection_document2_email,
            'category2' : housing_collection_document2_category,
            'condition2': housing_collection_document2_condition,
            'image2A' : housing_collection_document2_imageA,
            'image2B' : housing_collection_document2_imageB,
            'image2C' : housing_collection_document2_imageC,
            'image2D': housing_collection_document2_imageD,
            'image2E': housing_collection_document2_imageE,

            'productID3' : housing_collection_document3_productID,
            'username3' : housing_collection_document3_username,
            'state3' : housing_collection_document3_state,
            'city3' : housing_collection_document3_city,
            'description3' : housing_collection_document3_description,
            'mobile3' : housing_collection_document3_mobile,
            'email3' : housing_collection_document3_email,
            'category3' : housing_collection_document3_category,
            'condition3': housing_collection_document3_condition,
            'image3A' : housing_collection_document3_imageA,
            'image3B' : housing_collection_document3_imageB,
            'image3C' : housing_collection_document3_imageC,
            'image3D': housing_collection_document3_imageD,
            'image3E': housing_collection_document3_imageE,

            'productID4' : housing_collection_document4_productID,
            'username4' : housing_collection_document4_username,
            'state4' : housing_collection_document4_state,
            'city4' : housing_collection_document4_city,
            'description4' : housing_collection_document4_description,
            'mobile4' : housing_collection_document4_mobile,
            'email4' : housing_collection_document4_email,
            'category4' : housing_collection_document4_category,
            'condition4': housing_collection_document4_condition,
            'image4A' : housing_collection_document4_imageA,
            'image4B' : housing_collection_document4_imageB,
            'image4C' : housing_collection_document4_imageC,
            'image4D': housing_collection_document4_imageD,
            'image4E': housing_collection_document4_imageE,

            'productID5' : housing_collection_document5_productID,
            'username5' : housing_collection_document5_username,
            'state5' : housing_collection_document5_state,
            'city5' : housing_collection_document5_city,
            'description5' : housing_collection_document5_description,
            'mobile5' : housing_collection_document5_mobile,
            'email5' : housing_collection_document5_email,
            'category5' : housing_collection_document5_category,
            'condition5': housing_collection_document5_condition,
            'image5A' : housing_collection_document5_imageA,
            'image5B' : housing_collection_document5_imageB,
            'image5C' : housing_collection_document5_imageC,
            'image5D': housing_collection_document5_imageD,
            'image5E': housing_collection_document5_imageE,
            }


    # View pages....(n)
    # *************************************************************************************************************
    # *************************************************************************************************************
    @view_config(route_name='housing_viewProducts2_page2', renderer='templates/housing_templates/housing_viewProducts2_page2.pt')
    def housing_viewProducts2_page2(self):
        import pymongo
        from pymongo import MongoClient
        import gridfs
        from gridfs import GridFS
        # Extract connection string from enviroment variables
        import os
        from dotenv import load_dotenv
        load_dotenv()
        connection_string = os.environ['MY_CONNECTION_STRING']
        # Open database connection and get or create a database called spacenetng_database
        import dns
        client2 = MongoClient('%s' % connection_string)
        db = client2.spacenetng_database

        # Create or open a text based records collection called housing_text_collection
        text_collection_housing = db.housing_text_collection

        # Establish gridfs collection connection
        # Creating or getting an housing gridfs collection called 'housing_images_collection'
        # (Getting the GridFS object)
        image_collection_housing = GridFS(db, "housing_images_collection")

        # Retrieve document record from database operation
        housing_collection = text_collection_housing.find().sort([("_id", pymongo.DESCENDING)]).skip(5).limit(5) #This returns 25 records

        # Push documents into a list
        housing_collection_list = []

        for record in housing_collection:
            housing_collection_list.append(record)

        document6 = housing_collection_list[0]
        document7 = housing_collection_list[1]
        document8 = housing_collection_list[2]
        document9 = housing_collection_list[3]
        document10 = housing_collection_list[4]



        # The images for document6
        document6_images_list_rawFile = []
        for image_name in document6["Images"]:
            document6_images_list_rawFile.append(image_collection_housing.get_last_version(filename=image_name))

        # The images for document7
        document7_images_list_rawFile = []
        for image_name in document7["Images"]:
            document7_images_list_rawFile.append(image_collection_housing.get_last_version(filename=image_name))

        # The images for document8
        document8_images_list_rawFile = []
        for image_name in document8["Images"]:
            document8_images_list_rawFile.append(image_collection_housing.get_last_version(filename=image_name))

        # The images for document9
        document9_images_list_rawFile = []
        for image_name in document9["Images"]:
            document9_images_list_rawFile.append(image_collection_housing.get_last_version(filename=image_name))

        # The images for document10
        document10_images_list_rawFile = []
        for image_name in document10["Images"]:
            document10_images_list_rawFile.append(image_collection_housing.get_last_version(filename=image_name))


        ##############################################
        # Collecting record from individual documents
        ##############################################
        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document6
        #######################

        # For the text strings,
        housing_collection_document6_productID = document6["Product ID"]
        housing_collection_document6_username = document6["Username"]
        housing_collection_document6_state = document6["State"]
        housing_collection_document6_city = document6["City"]
        housing_collection_document6_description = document6["Description"]
        housing_collection_document6_mobile = document6["Mobile"]
        housing_collection_document6_email = document6["Email"]
        housing_collection_document6_category = document6["Category"]
        housing_collection_document6_condition = document6["Condition"]



        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document6_images_UTF8_list = []

        for raw_image in document6_images_list_rawFile:
            document6_binaryImage = raw_image.read()
            document6_base64Image = codecs.encode(document6_binaryImage, 'base64')
            document6_UTF8Image = document6_base64Image.decode('utf-8')
            document6_images_UTF8_list.append(document6_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        housing_collection_document6_imageA = document6_images_UTF8_list[0]

        try:
            housing_collection_document6_imageB = document6_images_UTF8_list[1]
        except:
            housing_collection_document6_imageB = document6_images_UTF8_list[0]

        try:
            housing_collection_document6_imageC = document6_images_UTF8_list[2]
        except:
            housing_collection_document6_imageC = document6_images_UTF8_list[0]

        try:
            housing_collection_document6_imageD = document6_images_UTF8_list[3]
        except:
            housing_collection_document6_imageD = document6_images_UTF8_list[0]       
        
        try:
            housing_collection_document6_imageE = document6_images_UTF8_list[4]
        except:
            housing_collection_document6_imageE = document6_images_UTF8_list[0]





        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document7
        #######################

        # For the text strings,
        housing_collection_document7_productID = document7["Product ID"]
        housing_collection_document7_username = document7["Username"]
        housing_collection_document7_state = document7["State"]
        housing_collection_document7_city = document7["City"]
        housing_collection_document7_description = document7["Description"]
        housing_collection_document7_mobile = document7["Mobile"]
        housing_collection_document7_email = document7["Email"]
        housing_collection_document7_category = document7["Category"]
        housing_collection_document7_condition = document7["Condition"]



        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document7_images_UTF8_list = []

        for raw_image in document7_images_list_rawFile:
            document7_binaryImage = raw_image.read()
            document7_base64Image = codecs.encode(document7_binaryImage, 'base64')
            document7_UTF8Image = document7_base64Image.decode('utf-8')
            document7_images_UTF8_list.append(document7_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        housing_collection_document7_imageA = document7_images_UTF8_list[0]

        try:
            housing_collection_document7_imageB = document7_images_UTF8_list[1]
        except:
            housing_collection_document7_imageB = document7_images_UTF8_list[0]

        try:
            housing_collection_document7_imageC = document7_images_UTF8_list[2]
        except:
            housing_collection_document7_imageC = document7_images_UTF8_list[0]

        try:
            housing_collection_document7_imageD = document7_images_UTF8_list[3]
        except:
            housing_collection_document7_imageD = document7_images_UTF8_list[0]       
        
        try:
            housing_collection_document7_imageE = document7_images_UTF8_list[4]
        except:
            housing_collection_document7_imageE = document7_images_UTF8_list[0]




        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document8
        #######################

        # For the text strings,
        housing_collection_document8_productID = document8["Product ID"]
        housing_collection_document8_username = document8["Username"]
        housing_collection_document8_state = document8["State"]
        housing_collection_document8_city = document8["City"]
        housing_collection_document8_description = document8["Description"]
        housing_collection_document8_mobile = document8["Mobile"]
        housing_collection_document8_email = document8["Email"]
        housing_collection_document8_category = document8["Category"]
        housing_collection_document8_condition = document8["Condition"]

   
        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document8_images_UTF8_list = []

        for raw_image in document8_images_list_rawFile:
            document8_binaryImage = raw_image.read()
            document8_base64Image = codecs.encode(document8_binaryImage, 'base64')
            document8_UTF8Image = document8_base64Image.decode('utf-8')
            document8_images_UTF8_list.append(document8_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        housing_collection_document8_imageA = document8_images_UTF8_list[0]

        try:
            housing_collection_document8_imageB = document8_images_UTF8_list[1]
        except:
            housing_collection_document8_imageB = document8_images_UTF8_list[0]

        try:
            housing_collection_document8_imageC = document8_images_UTF8_list[2]
        except:
            housing_collection_document8_imageC = document8_images_UTF8_list[0]

        try:
            housing_collection_document8_imageD = document8_images_UTF8_list[3]
        except:
            housing_collection_document8_imageD = document8_images_UTF8_list[0]       
        
        try:
            housing_collection_document8_imageE = document8_images_UTF8_list[4]
        except:
            housing_collection_document8_imageE = document8_images_UTF8_list[0]




        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document9
        #######################

        # For the text strings,
        housing_collection_document9_productID = document9["Product ID"]
        housing_collection_document9_username = document9["Username"]
        housing_collection_document9_state = document9["State"]
        housing_collection_document9_city = document9["City"]
        housing_collection_document9_description = document9["Description"]
        housing_collection_document9_mobile = document9["Mobile"]
        housing_collection_document9_email = document9["Email"]
        housing_collection_document9_category = document9["Category"]
        housing_collection_document9_condition = document9["Condition"]



        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document9_images_UTF8_list = []

        for raw_image in document9_images_list_rawFile:
            document9_binaryImage = raw_image.read()
            document9_base64Image = codecs.encode(document9_binaryImage, 'base64')
            document9_UTF8Image = document9_base64Image.decode('utf-8')
            document9_images_UTF8_list.append(document9_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        housing_collection_document9_imageA = document9_images_UTF8_list[0]

        try:
            housing_collection_document9_imageB = document9_images_UTF8_list[1]
        except:
            housing_collection_document9_imageB = document9_images_UTF8_list[0]

        try:
            housing_collection_document9_imageC = document9_images_UTF8_list[2]
        except:
            housing_collection_document9_imageC = document9_images_UTF8_list[0]

        try:
            housing_collection_document9_imageD = document9_images_UTF8_list[3]
        except:
            housing_collection_document9_imageD = document9_images_UTF8_list[0]       
        
        try:
            housing_collection_document9_imageE = document9_images_UTF8_list[4]
        except:
            housing_collection_document9_imageE = document9_images_UTF8_list[0]


        # For document10
        #######################

        # For the text strings,
        housing_collection_document10_productID = document10["Product ID"]
        housing_collection_document10_username = document10["Username"]
        housing_collection_document10_state = document10["State"]
        housing_collection_document10_city = document10["City"]
        housing_collection_document10_description = document10["Description"]
        housing_collection_document10_mobile = document10["Mobile"]
        housing_collection_document10_email = document10["Email"]
        housing_collection_document10_category = document10["Category"]
        housing_collection_document10_condition = document10["Condition"]



        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document10_images_UTF8_list = []

        for raw_image in document10_images_list_rawFile:
            document10_binaryImage = raw_image.read()
            document10_base64Image = codecs.encode(document10_binaryImage, 'base64')
            document10_UTF8Image = document10_base64Image.decode('utf-8')
            document10_images_UTF8_list.append(document10_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        housing_collection_document10_imageA = document10_images_UTF8_list[0]

        try:
            housing_collection_document10_imageB = document10_images_UTF8_list[1]
        except:
            housing_collection_document10_imageB = document10_images_UTF8_list[0]

        try:
            housing_collection_document10_imageC = document10_images_UTF8_list[2]
        except:
            housing_collection_document10_imageC = document10_images_UTF8_list[0]

        try:
            housing_collection_document10_imageD = document10_images_UTF8_list[3]
        except:
            housing_collection_document10_imageD = document10_images_UTF8_list[0]       
        
        try:
            housing_collection_document10_imageE = document10_images_UTF8_list[4]
        except:
            housing_collection_document10_imageE = document10_images_UTF8_list[0]

        # Close our database connection and free up resources.
        client2.close()

        # Pack all return variables into a JSON Structure and use for return
        return{
            'productID6' : housing_collection_document6_productID,
            'username6' : housing_collection_document6_username,
            'state6' : housing_collection_document6_state,
            'city6' : housing_collection_document6_city,
            'description6' : housing_collection_document6_description,
            'mobile6' : housing_collection_document6_mobile,
            'email6' : housing_collection_document6_email,
            'category6' : housing_collection_document6_category,
            'condition6': housing_collection_document6_condition,
            'image6A' : housing_collection_document6_imageA,
            'image6B' : housing_collection_document6_imageB,
            'image6C' : housing_collection_document6_imageC,
            'image6D': housing_collection_document6_imageD,
            'image6E': housing_collection_document6_imageE,

            'productID7' : housing_collection_document7_productID,
            'username7' : housing_collection_document7_username,
            'state7' : housing_collection_document7_state,
            'city7' : housing_collection_document7_city,
            'description7' : housing_collection_document7_description,
            'mobile7' : housing_collection_document7_mobile,
            'email7' : housing_collection_document7_email,
            'category7' : housing_collection_document7_category,
            'condition7': housing_collection_document7_condition,
            'image7A' : housing_collection_document7_imageA,
            'image7B' : housing_collection_document7_imageB,
            'image7C' : housing_collection_document7_imageC,
            'image7D': housing_collection_document7_imageD,
            'image7E': housing_collection_document7_imageE,

            'productID8' : housing_collection_document8_productID,
            'username8' : housing_collection_document8_username,
            'state8' : housing_collection_document8_state,
            'city8' : housing_collection_document8_city,
            'description8' : housing_collection_document8_description,
            'mobile8' : housing_collection_document8_mobile,
            'email8' : housing_collection_document8_email,
            'category8' : housing_collection_document8_category,
            'condition8': housing_collection_document8_condition,
            'image8A' : housing_collection_document8_imageA,
            'image8B' : housing_collection_document8_imageB,
            'image8C' : housing_collection_document8_imageC,
            'image8D': housing_collection_document8_imageD,
            'image8E': housing_collection_document8_imageE,

            'productID9' : housing_collection_document9_productID,
            'username9' : housing_collection_document9_username,
            'state9' : housing_collection_document9_state,
            'city9' : housing_collection_document9_city,
            'description9' : housing_collection_document9_description,
            'mobile9' : housing_collection_document9_mobile,
            'email9' : housing_collection_document9_email,
            'category9' : housing_collection_document9_category,
            'condition9': housing_collection_document9_condition,
            'image9A' : housing_collection_document9_imageA,
            'image9B' : housing_collection_document9_imageB,
            'image9C' : housing_collection_document9_imageC,
            'image9D': housing_collection_document9_imageD,
            'image9E': housing_collection_document9_imageE,

            'productID10' : housing_collection_document10_productID,
            'username10' : housing_collection_document10_username,
            'state10' : housing_collection_document10_state,
            'city10' : housing_collection_document10_city,
            'description10' : housing_collection_document10_description,
            'mobile10' : housing_collection_document10_mobile,
            'email10' : housing_collection_document10_email,
            'category10' : housing_collection_document10_category,
            'condition10': housing_collection_document10_condition,
            'image10A' : housing_collection_document10_imageA,
            'image10B' : housing_collection_document10_imageB,
            'image10C' : housing_collection_document10_imageC,
            'image10D': housing_collection_document10_imageD,
            'image10E': housing_collection_document10_imageE,            
        }





    # *************************************************************************************************************
    # *************************************************************************************************************
    @view_config(route_name='housing_viewProducts2_page3', renderer='templates/housing_templates/housing_viewProducts2_page3.pt')
    def housing_viewProducts2_page3(self):
        import pymongo
        from pymongo import MongoClient
        import gridfs
        from gridfs import GridFS
        # Extract connection string from enviroment variables
        import os
        from dotenv import load_dotenv
        load_dotenv()
        connection_string = os.environ['MY_CONNECTION_STRING']
        # Open database connection and get or create a database called spacenetng_database
        import dns
        client3 = MongoClient('%s' % connection_string)
        db = client3.spacenetng_database

        # Create or open a text based records collection called housing_text_collection
        text_collection_housing = db.housing_text_collection

        # Establish gridfs collection connection
        # Creating or getting an housing gridfs collection called 'housing_images_collection'
        # (Getting the GridFS object)
        image_collection_housing = GridFS(db, "housing_images_collection")

        # Retrieve document record from database operation
        housing_collection = text_collection_housing.find().sort([("_id", pymongo.DESCENDING)]).skip(10).limit(5) #This returns 25 records

        # Push documents into a list
        housing_collection_list = []

        for record in housing_collection:
            housing_collection_list.append(record)



        document11 = housing_collection_list[0]
        document12 = housing_collection_list[1]
        document13 = housing_collection_list[2]
        document14 = housing_collection_list[3]
        document15 = housing_collection_list[4]

        # Extracting images
        # The images for document11
        document11_images_list_rawFile = []
        for image_name in document11["Images"]:
            document11_images_list_rawFile.append(image_collection_housing.get_last_version(filename=image_name))

        # The images for document12
        document12_images_list_rawFile = []
        for image_name in document12["Images"]:
            document12_images_list_rawFile.append(image_collection_housing.get_last_version(filename=image_name))

        # The images for document13
        document13_images_list_rawFile = []
        for image_name in document13["Images"]:
            document13_images_list_rawFile.append(image_collection_housing.get_last_version(filename=image_name))

        # The images for document14
        document14_images_list_rawFile = []
        for image_name in document14["Images"]:
            document14_images_list_rawFile.append(image_collection_housing.get_last_version(filename=image_name))

        # The images for document15
        document15_images_list_rawFile = []
        for image_name in document15["Images"]:
            document15_images_list_rawFile.append(image_collection_housing.get_last_version(filename=image_name))



        ##############################################
        # Collecting record from individual documents
        ##############################################
        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document11
        #######################

        # For the text strings,
        housing_collection_document11_productID = document11["Product ID"]
        housing_collection_document11_username = document11["Username"]
        housing_collection_document11_state = document11["State"]
        housing_collection_document11_city = document11["City"]
        housing_collection_document11_description = document11["Description"]
        housing_collection_document11_mobile = document11["Mobile"]
        housing_collection_document11_email = document11["Email"]
        housing_collection_document11_category = document11["Category"]
        housing_collection_document11_condition = document11["Condition"]

        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document11_images_UTF8_list = []

        for raw_image in document11_images_list_rawFile:
            document11_binaryImage = raw_image.read()
            document11_base64Image = codecs.encode(document11_binaryImage, 'base64')
            document11_UTF8Image = document11_base64Image.decode('utf-8')
            document11_images_UTF8_list.append(document11_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        housing_collection_document11_imageA = document11_images_UTF8_list[0]

        try:
            housing_collection_document11_imageB = document11_images_UTF8_list[1]
        except:
            housing_collection_document11_imageB = document11_images_UTF8_list[0]

        try:
            housing_collection_document11_imageC = document11_images_UTF8_list[2]
        except:
            housing_collection_document11_imageC = document11_images_UTF8_list[0]

        try:
            housing_collection_document11_imageD = document11_images_UTF8_list[3]
        except:
            housing_collection_document11_imageD = document11_images_UTF8_list[0]       
        
        try:
            housing_collection_document11_imageE = document11_images_UTF8_list[4]
        except:
            housing_collection_document11_imageE = document11_images_UTF8_list[0]





        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document12
        #######################

        # For the text strings,
        housing_collection_document12_productID = document12["Product ID"]
        housing_collection_document12_username = document12["Username"]
        housing_collection_document12_state = document12["State"]
        housing_collection_document12_city = document12["City"]
        housing_collection_document12_description = document12["Description"]
        housing_collection_document12_mobile = document12["Mobile"]
        housing_collection_document12_email = document12["Email"]
        housing_collection_document12_category = document12["Category"]
        housing_collection_document12_condition = document12["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document12_images_UTF8_list = []

        for raw_image in document12_images_list_rawFile:
            document12_binaryImage = raw_image.read()
            document12_base64Image = codecs.encode(document12_binaryImage, 'base64')
            document12_UTF8Image = document12_base64Image.decode('utf-8')
            document12_images_UTF8_list.append(document12_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        housing_collection_document12_imageA = document12_images_UTF8_list[0]

        try:
            housing_collection_document12_imageB = document12_images_UTF8_list[1]
        except:
            housing_collection_document12_imageB = document12_images_UTF8_list[0]

        try:
            housing_collection_document12_imageC = document12_images_UTF8_list[2]
        except:
            housing_collection_document12_imageC = document12_images_UTF8_list[0]

        try:
            housing_collection_document12_imageD = document12_images_UTF8_list[3]
        except:
            housing_collection_document12_imageD = document12_images_UTF8_list[0]       
        
        try:
            housing_collection_document12_imageE = document12_images_UTF8_list[4]
        except:
            housing_collection_document12_imageE = document12_images_UTF8_list[0]





        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document13
        #######################

        # For the text strings,
        housing_collection_document13_productID = document13["Product ID"]
        housing_collection_document13_username = document13["Username"]
        housing_collection_document13_state = document13["State"]
        housing_collection_document13_city = document13["City"]
        housing_collection_document13_description = document13["Description"]
        housing_collection_document13_mobile = document13["Mobile"]
        housing_collection_document13_email = document13["Email"]
        housing_collection_document13_category = document13["Category"]
        housing_collection_document13_condition = document13["Condition"]

        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document13_images_UTF8_list = []

        for raw_image in document13_images_list_rawFile:
            document13_binaryImage = raw_image.read()
            document13_base64Image = codecs.encode(document13_binaryImage, 'base64')
            document13_UTF8Image = document13_base64Image.decode('utf-8')
            document13_images_UTF8_list.append(document13_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        housing_collection_document13_imageA = document13_images_UTF8_list[0]

        try:
            housing_collection_document13_imageB = document13_images_UTF8_list[1]
        except:
            housing_collection_document13_imageB = document13_images_UTF8_list[0]

        try:
            housing_collection_document13_imageC = document13_images_UTF8_list[2]
        except:
            housing_collection_document13_imageC = document13_images_UTF8_list[0]

        try:
            housing_collection_document13_imageD = document13_images_UTF8_list[3]
        except:
            housing_collection_document13_imageD = document13_images_UTF8_list[0]       
        
        try:
            housing_collection_document13_imageE = document13_images_UTF8_list[4]
        except:
            housing_collection_document13_imageE = document13_images_UTF8_list[0]




        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document14
        #######################

        # For the text strings,
        housing_collection_document14_productID = document14["Product ID"]
        housing_collection_document14_username = document14["Username"]
        housing_collection_document14_state = document14["State"]
        housing_collection_document14_city = document14["City"]
        housing_collection_document14_description = document14["Description"]
        housing_collection_document14_mobile = document14["Mobile"]
        housing_collection_document14_email = document14["Email"]
        housing_collection_document14_category = document14["Category"]
        housing_collection_document14_condition = document14["Condition"]

        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document14_images_UTF8_list = []

        for raw_image in document14_images_list_rawFile:
            document14_binaryImage = raw_image.read()
            document14_base64Image = codecs.encode(document14_binaryImage, 'base64')
            document14_UTF8Image = document14_base64Image.decode('utf-8')
            document14_images_UTF8_list.append(document14_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        housing_collection_document14_imageA = document14_images_UTF8_list[0]

        try:
            housing_collection_document14_imageB = document14_images_UTF8_list[1]
        except:
            housing_collection_document14_imageB = document14_images_UTF8_list[0]

        try:
            housing_collection_document14_imageC = document14_images_UTF8_list[2]
        except:
            housing_collection_document14_imageC = document14_images_UTF8_list[0]

        try:
            housing_collection_document14_imageD = document14_images_UTF8_list[3]
        except:
            housing_collection_document14_imageD = document14_images_UTF8_list[0]       
        
        try:
            housing_collection_document14_imageE = document14_images_UTF8_list[4]
        except:
            housing_collection_document14_imageE = document14_images_UTF8_list[0]






        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document15
        #######################

        # For the text strings,
        housing_collection_document15_productID = document15["Product ID"]
        housing_collection_document15_username = document15["Username"]
        housing_collection_document15_state = document15["State"]
        housing_collection_document15_city = document15["City"]
        housing_collection_document15_description = document15["Description"]
        housing_collection_document15_mobile = document15["Mobile"]
        housing_collection_document15_email = document15["Email"]
        housing_collection_document15_category = document15["Category"]
        housing_collection_document15_condition = document15["Condition"]



        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document15_images_UTF8_list = []

        for raw_image in document15_images_list_rawFile:
            document15_binaryImage = raw_image.read()
            document15_base64Image = codecs.encode(document15_binaryImage, 'base64')
            document15_UTF8Image = document15_base64Image.decode('utf-8')
            document15_images_UTF8_list.append(document15_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        housing_collection_document15_imageA = document15_images_UTF8_list[0]

        try:
            housing_collection_document15_imageB = document15_images_UTF8_list[1]
        except:
            housing_collection_document15_imageB = document15_images_UTF8_list[0]

        try:
            housing_collection_document15_imageC = document15_images_UTF8_list[2]
        except:
            housing_collection_document15_imageC = document15_images_UTF8_list[0]

        try:
            housing_collection_document15_imageD = document15_images_UTF8_list[3]
        except:
            housing_collection_document15_imageD = document15_images_UTF8_list[0]       
        
        try:
            housing_collection_document15_imageE = document15_images_UTF8_list[4]
        except:
            housing_collection_document15_imageE = document15_images_UTF8_list[0]

        # Close our database connection and free up resources.
        client3.close()

        # Pack all return variables into a JSON Structure and use for return
        return{
            'productID11' : housing_collection_document11_productID,
            'username11' : housing_collection_document11_username,
            'state11' : housing_collection_document11_state,
            'city11' : housing_collection_document11_city,
            'description11' : housing_collection_document11_description,
            'mobile11' : housing_collection_document11_mobile,
            'email11' : housing_collection_document11_email,
            'category11' : housing_collection_document11_category,
            'condition11': housing_collection_document11_condition,
            'image11A' : housing_collection_document11_imageA,
            'image11B' : housing_collection_document11_imageB,
            'image11C' : housing_collection_document11_imageC,
            'image11D': housing_collection_document11_imageD,
            'image11E': housing_collection_document11_imageE,

            'productID12' : housing_collection_document12_productID,
            'username12' : housing_collection_document12_username,
            'state12' : housing_collection_document12_state,
            'city12' : housing_collection_document12_city,
            'description12' : housing_collection_document12_description,
            'mobile12' : housing_collection_document12_mobile,
            'email12' : housing_collection_document12_email,
            'category12' : housing_collection_document12_category,
            'condition12': housing_collection_document12_condition,
            'image12A' : housing_collection_document12_imageA,
            'image12B' : housing_collection_document12_imageB,
            'image12C' : housing_collection_document12_imageC,
            'image12D': housing_collection_document12_imageD,
            'image12E': housing_collection_document12_imageE,

            'productID13' : housing_collection_document13_productID,
            'username13' : housing_collection_document13_username,
            'state13' : housing_collection_document13_state,
            'city13' : housing_collection_document13_city,
            'description13' : housing_collection_document13_description,
            'mobile13' : housing_collection_document13_mobile,
            'email13' : housing_collection_document13_email,
            'category13' : housing_collection_document13_category,
            'condition13': housing_collection_document13_condition,
            'image13A' : housing_collection_document13_imageA,
            'image13B' : housing_collection_document13_imageB,
            'image13C' : housing_collection_document13_imageC,
            'image13D': housing_collection_document13_imageD,
            'image13E': housing_collection_document13_imageE,

            'productID14' : housing_collection_document14_productID,
            'username14' : housing_collection_document14_username,
            'state14' : housing_collection_document14_state,
            'city14' : housing_collection_document14_city,
            'description14' : housing_collection_document14_description,
            'mobile14' : housing_collection_document14_mobile,
            'email14' : housing_collection_document14_email,
            'category14' : housing_collection_document14_category,
            'condition14': housing_collection_document14_condition,
            'image14A' : housing_collection_document14_imageA,
            'image14B' : housing_collection_document14_imageB,
            'image14C' : housing_collection_document14_imageC,
            'image14D': housing_collection_document14_imageD,
            'image14E': housing_collection_document14_imageE,

            'productID15' : housing_collection_document15_productID,
            'username15' : housing_collection_document15_username,
            'state15' : housing_collection_document15_state,
            'city15' : housing_collection_document15_city,
            'description15' : housing_collection_document15_description,
            'mobile15' : housing_collection_document15_mobile,
            'email15' : housing_collection_document15_email,
            'category15' : housing_collection_document15_category,
            'condition15': housing_collection_document15_condition,
            'image15A' : housing_collection_document15_imageA,
            'image15B' : housing_collection_document15_imageB,
            'image15C' : housing_collection_document15_imageC,
            'image15D': housing_collection_document15_imageD,
            'image15E': housing_collection_document15_imageE,
        }


    # *************************************************************************************************************
    # *************************************************************************************************************        
    @view_config(route_name='housing_viewProducts2_page4', renderer='templates/housing_templates/housing_viewProducts2_page4.pt')
    def housing_viewProducts2_page4(self):
        import pymongo
        from pymongo import MongoClient
        import gridfs
        from gridfs import GridFS
        # Extract connection string from enviroment variables
        import os
        from dotenv import load_dotenv
        load_dotenv()
        connection_string = os.environ['MY_CONNECTION_STRING']
        # Open database connection and get or create a database called spacenetng_database
        import dns
        client4 = MongoClient('%s' % connection_string)
        db = client4.spacenetng_database

        # Create or open a text based records collection called housing_text_collection
        text_collection_housing = db.housing_text_collection

        # Establish gridfs collection connection
        # Creating or getting an housing gridfs collection called 'housing_images_collection'
        # (Getting the GridFS object)
        image_collection_housing = GridFS(db, "housing_images_collection")

        # Retrieve document record from database operation
        housing_collection = text_collection_housing.find().sort([("_id", pymongo.DESCENDING)]).skip(15).limit(5) #This returns 25 records

        # Push documents into a list
        housing_collection_list = []

        for record in housing_collection:
            housing_collection_list.append(record)

        document16 = housing_collection_list[0]
        document17 = housing_collection_list[1]
        document18 = housing_collection_list[2]
        document19 = housing_collection_list[3]
        document20 = housing_collection_list[4]


        # Extracting images
        # The images for document16
        document16_images_list_rawFile = []
        for image_name in document16["Images"]:
            document16_images_list_rawFile.append(image_collection_housing.get_last_version(filename=image_name))

        # The images for document17
        document17_images_list_rawFile = []
        for image_name in document17["Images"]:
            document17_images_list_rawFile.append(image_collection_housing.get_last_version(filename=image_name))

        # The images for document18
        document18_images_list_rawFile = []
        for image_name in document18["Images"]:
            document18_images_list_rawFile.append(image_collection_housing.get_last_version(filename=image_name))

        # The images for document19
        document19_images_list_rawFile = []
        for image_name in document19["Images"]:
            document19_images_list_rawFile.append(image_collection_housing.get_last_version(filename=image_name))

        # The images for document20
        document20_images_list_rawFile = []
        for image_name in document20["Images"]:
            document20_images_list_rawFile.append(image_collection_housing.get_last_version(filename=image_name))


        ##############################################
        # Collecting record from individual documents
        ##############################################
        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document16
        #######################

        # For the text strings,
        housing_collection_document16_productID = document16["Product ID"]
        housing_collection_document16_username = document16["Username"]
        housing_collection_document16_state = document16["State"]
        housing_collection_document16_city = document16["City"]
        housing_collection_document16_description = document16["Description"]
        housing_collection_document16_mobile = document16["Mobile"]
        housing_collection_document16_email = document16["Email"]
        housing_collection_document16_category = document16["Category"]
        housing_collection_document16_condition = document16["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document16_images_UTF8_list = []

        for raw_image in document16_images_list_rawFile:
            document16_binaryImage = raw_image.read()
            document16_base64Image = codecs.encode(document16_binaryImage, 'base64')
            document16_UTF8Image = document16_base64Image.decode('utf-8')
            document16_images_UTF8_list.append(document16_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        housing_collection_document16_imageA = document16_images_UTF8_list[0]

        try:
            housing_collection_document16_imageB = document16_images_UTF8_list[1]
        except:
            housing_collection_document16_imageB = document16_images_UTF8_list[0]

        try:
            housing_collection_document16_imageC = document16_images_UTF8_list[2]
        except:
            housing_collection_document16_imageC = document16_images_UTF8_list[0]

        try:
            housing_collection_document16_imageD = document16_images_UTF8_list[3]
        except:
            housing_collection_document16_imageD = document16_images_UTF8_list[0]       
        
        try:
            housing_collection_document16_imageE = document16_images_UTF8_list[4]
        except:
            housing_collection_document16_imageE = document16_images_UTF8_list[0]




        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document17
        #######################

        # For the text strings,
        housing_collection_document17_productID = document17["Product ID"]
        housing_collection_document17_username = document17["Username"]
        housing_collection_document17_state = document17["State"]
        housing_collection_document17_city = document17["City"]
        housing_collection_document17_description = document17["Description"]
        housing_collection_document17_mobile = document17["Mobile"]
        housing_collection_document17_email = document17["Email"]
        housing_collection_document17_category = document17["Category"]
        housing_collection_document17_condition = document17["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document17_images_UTF8_list = []

        for raw_image in document17_images_list_rawFile:
            document17_binaryImage = raw_image.read()
            document17_base64Image = codecs.encode(document17_binaryImage, 'base64')
            document17_UTF8Image = document17_base64Image.decode('utf-8')
            document17_images_UTF8_list.append(document17_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        housing_collection_document17_imageA = document17_images_UTF8_list[0]

        try:
            housing_collection_document17_imageB = document17_images_UTF8_list[1]
        except:
            housing_collection_document17_imageB = document17_images_UTF8_list[0]

        try:
            housing_collection_document17_imageC = document17_images_UTF8_list[2]
        except:
            housing_collection_document17_imageC = document17_images_UTF8_list[0]

        try:
            housing_collection_document17_imageD = document17_images_UTF8_list[3]
        except:
            housing_collection_document17_imageD = document17_images_UTF8_list[0]       
        
        try:
            housing_collection_document17_imageE = document17_images_UTF8_list[4]
        except:
            housing_collection_document17_imageE = document17_images_UTF8_list[0]





        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document18
        #######################

        # For the text strings,
        housing_collection_document18_productID = document18["Product ID"]
        housing_collection_document18_username = document18["Username"]
        housing_collection_document18_state = document18["State"]
        housing_collection_document18_city = document18["City"]
        housing_collection_document18_description = document18["Description"]
        housing_collection_document18_mobile = document18["Mobile"]
        housing_collection_document18_email = document18["Email"]
        housing_collection_document18_category = document18["Category"]
        housing_collection_document18_condition = document18["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document18_images_UTF8_list = []

        for raw_image in document18_images_list_rawFile:
            document18_binaryImage = raw_image.read()
            document18_base64Image = codecs.encode(document18_binaryImage, 'base64')
            document18_UTF8Image = document18_base64Image.decode('utf-8')
            document18_images_UTF8_list.append(document18_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        housing_collection_document18_imageA = document18_images_UTF8_list[0]

        try:
            housing_collection_document18_imageB = document18_images_UTF8_list[1]
        except:
            housing_collection_document18_imageB = document18_images_UTF8_list[0]

        try:
            housing_collection_document18_imageC = document18_images_UTF8_list[2]
        except:
            housing_collection_document18_imageC = document18_images_UTF8_list[0]

        try:
            housing_collection_document18_imageD = document18_images_UTF8_list[3]
        except:
            housing_collection_document18_imageD = document18_images_UTF8_list[0]       
        
        try:
            housing_collection_document18_imageE = document18_images_UTF8_list[4]
        except:
            housing_collection_document18_imageE = document18_images_UTF8_list[0]





        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document19
        #######################

        # For the text strings,
        housing_collection_document19_productID = document19["Product ID"]
        housing_collection_document19_username = document19["Username"]
        housing_collection_document19_state = document19["State"]
        housing_collection_document19_city = document19["City"]
        housing_collection_document19_description = document19["Description"]
        housing_collection_document19_mobile = document19["Mobile"]
        housing_collection_document19_email = document19["Email"]
        housing_collection_document19_category = document19["Category"]
        housing_collection_document19_condition = document19["Condition"]

        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document19_images_UTF8_list = []

        for raw_image in document19_images_list_rawFile:
            document19_binaryImage = raw_image.read()
            document19_base64Image = codecs.encode(document19_binaryImage, 'base64')
            document19_UTF8Image = document19_base64Image.decode('utf-8')
            document19_images_UTF8_list.append(document19_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        housing_collection_document19_imageA = document19_images_UTF8_list[0]

        try:
            housing_collection_document19_imageB = document19_images_UTF8_list[1]
        except:
            housing_collection_document19_imageB = document19_images_UTF8_list[0]

        try:
            housing_collection_document19_imageC = document19_images_UTF8_list[2]
        except:
            housing_collection_document19_imageC = document19_images_UTF8_list[0]

        try:
            housing_collection_document19_imageD = document19_images_UTF8_list[3]
        except:
            housing_collection_document19_imageD = document19_images_UTF8_list[0]       
        
        try:
            housing_collection_document19_imageE = document19_images_UTF8_list[4]
        except:
            housing_collection_document19_imageE = document19_images_UTF8_list[0]




        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document20
        #######################

        # For the text strings,
        housing_collection_document20_productID = document20["Product ID"]
        housing_collection_document20_username = document20["Username"]
        housing_collection_document20_state = document20["State"]
        housing_collection_document20_city = document20["City"]
        housing_collection_document20_description = document20["Description"]
        housing_collection_document20_mobile = document20["Mobile"]
        housing_collection_document20_email = document20["Email"]
        housing_collection_document20_category = document20["Category"]
        housing_collection_document20_condition = document20["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document20_images_UTF8_list = []

        for raw_image in document20_images_list_rawFile:
            document20_binaryImage = raw_image.read()
            document20_base64Image = codecs.encode(document20_binaryImage, 'base64')
            document20_UTF8Image = document20_base64Image.decode('utf-8')
            document20_images_UTF8_list.append(document20_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        housing_collection_document20_imageA = document20_images_UTF8_list[0]

        try:
            housing_collection_document20_imageB = document20_images_UTF8_list[1]
        except:
            housing_collection_document20_imageB = document20_images_UTF8_list[0]

        try:
            housing_collection_document20_imageC = document20_images_UTF8_list[2]
        except:
            housing_collection_document20_imageC = document20_images_UTF8_list[0]

        try:
            housing_collection_document20_imageD = document20_images_UTF8_list[3]
        except:
            housing_collection_document20_imageD = document20_images_UTF8_list[0]       
        
        try:
            housing_collection_document20_imageE = document20_images_UTF8_list[4]
        except:
            housing_collection_document20_imageE = document20_images_UTF8_list[0]


        # Close our database connection and free up resources.
        client4.close()

        # Pack all return variables into a JSON Structure and use for return
        return{
            'productID16' : housing_collection_document16_productID,
            'username16' : housing_collection_document16_username,
            'state16' : housing_collection_document16_state,
            'city16' : housing_collection_document16_city,
            'description16' : housing_collection_document16_description,
            'mobile16' : housing_collection_document16_mobile,
            'email16' : housing_collection_document16_email,
            'category16' : housing_collection_document16_category,
            'condition16': housing_collection_document16_condition,
            'image16A' : housing_collection_document16_imageA,
            'image16B' : housing_collection_document16_imageB,
            'image16C' : housing_collection_document16_imageC,
            'image16D': housing_collection_document16_imageD,
            'image16E': housing_collection_document16_imageE,

            'productID17' : housing_collection_document17_productID,
            'username17' : housing_collection_document17_username,
            'state17' : housing_collection_document17_state,
            'city17' : housing_collection_document17_city,
            'description17' : housing_collection_document17_description,
            'mobile17' : housing_collection_document17_mobile,
            'email17' : housing_collection_document17_email,
            'category17' : housing_collection_document17_category,
            'condition17': housing_collection_document17_condition,
            'image17A' : housing_collection_document17_imageA,
            'image17B' : housing_collection_document17_imageB,
            'image17C' : housing_collection_document17_imageC,
            'image17D': housing_collection_document17_imageD,
            'image17E': housing_collection_document17_imageE,

            'productID18' : housing_collection_document18_productID,
            'username18' : housing_collection_document18_username,
            'state18' : housing_collection_document18_state,
            'city18' : housing_collection_document18_city,
            'description18' : housing_collection_document18_description,
            'mobile18' : housing_collection_document18_mobile,
            'email18' : housing_collection_document18_email,
            'category18' : housing_collection_document18_category,
            'condition18': housing_collection_document18_condition,
            'image18A' : housing_collection_document18_imageA,
            'image18B' : housing_collection_document18_imageB,
            'image18C' : housing_collection_document18_imageC,
            'image18D': housing_collection_document18_imageD,
            'image18E': housing_collection_document18_imageE,

            'productID19' : housing_collection_document19_productID,
            'username19' : housing_collection_document19_username,
            'state19' : housing_collection_document19_state,
            'city19' : housing_collection_document19_city,
            'description19' : housing_collection_document19_description,
            'mobile19' : housing_collection_document19_mobile,
            'email19' : housing_collection_document19_email,
            'category19' : housing_collection_document19_category,
            'condition19': housing_collection_document19_condition,
            'image19A' : housing_collection_document19_imageA,
            'image19B' : housing_collection_document19_imageB,
            'image19C' : housing_collection_document19_imageC,
            'image19D': housing_collection_document19_imageD,
            'image19E': housing_collection_document19_imageE,

            'productID20' : housing_collection_document20_productID,
            'username20' : housing_collection_document20_username,
            'state20' : housing_collection_document20_state,
            'city20' : housing_collection_document20_city,
            'description20' : housing_collection_document20_description,
            'mobile20' : housing_collection_document20_mobile,
            'email20' : housing_collection_document20_email,
            'category20' : housing_collection_document20_category,
            'condition20': housing_collection_document20_condition,
            'image20A' : housing_collection_document20_imageA,
            'image20B' : housing_collection_document20_imageB,
            'image20C' : housing_collection_document20_imageC,
            'image20D': housing_collection_document20_imageD,
            'image20E': housing_collection_document20_imageE,
        }






    # *************************************************************************************************************
    # *************************************************************************************************************
    @view_config(route_name='housing_viewProducts2_page5', renderer='templates/housing_templates/housing_viewProducts2_page5.pt')
    def housing_viewProducts2_page5(self):
        import pymongo
        from pymongo import MongoClient
        import gridfs
        from gridfs import GridFS
        # Extract connection string from enviroment variables
        import os
        from dotenv import load_dotenv
        load_dotenv()
        connection_string = os.environ['MY_CONNECTION_STRING']
        # Open database connection and get or create a database called spacenetng_database
        import dns
        client5 = MongoClient('%s' % connection_string)
        db = client5.spacenetng_database

        # Create or open a text based records collection called housing_text_collection
        text_collection_housing = db.housing_text_collection

        # Establish gridfs collection connection
        # Creating or getting an housing gridfs collection called 'housing_images_collection'
        # (Getting the GridFS object)
        image_collection_housing = GridFS(db, "housing_images_collection")

        # Retrieve document record from database operation
        housing_collection = text_collection_housing.find().sort([("_id", pymongo.DESCENDING)]).skip(20).limit(5) #This returns 25 records

        # Push documents into a list
        housing_collection_list = []

        for record in housing_collection:
            housing_collection_list.append(record)

        document21 = housing_collection_list[0]
        document22 = housing_collection_list[1]
        document23 = housing_collection_list[2]
        document24 = housing_collection_list[3]
        document25 = housing_collection_list[4]


        # Extracting images
        # The images for document21
        document21_images_list_rawFile = []
        for image_name in document21["Images"]:
            document21_images_list_rawFile.append(image_collection_housing.get_last_version(filename=image_name))

        # The images for document22
        document22_images_list_rawFile = []
        for image_name in document22["Images"]:
            document22_images_list_rawFile.append(image_collection_housing.get_last_version(filename=image_name))

        # The images for document23
        document23_images_list_rawFile = []
        for image_name in document23["Images"]:
            document23_images_list_rawFile.append(image_collection_housing.get_last_version(filename=image_name))

        # The images for document24
        document24_images_list_rawFile = []
        for image_name in document24["Images"]:
            document24_images_list_rawFile.append(image_collection_housing.get_last_version(filename=image_name))

        # The images for document25
        document25_images_list_rawFile = []
        for image_name in document25["Images"]:
            document25_images_list_rawFile.append(image_collection_housing.get_last_version(filename=image_name))


        ##############################################
        # Collecting record from individual documents
        ##############################################
        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document21
        #######################

        # For the text strings,
        housing_collection_document21_productID = document21["Product ID"]
        housing_collection_document21_username = document21["Username"]
        housing_collection_document21_state = document21["State"]
        housing_collection_document21_city = document21["City"]
        housing_collection_document21_description = document21["Description"]
        housing_collection_document21_mobile = document21["Mobile"]
        housing_collection_document21_email = document21["Email"]
        housing_collection_document21_category = document21["Category"]
        housing_collection_document21_condition = document21["Condition"]



        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document21_images_UTF8_list = []

        for raw_image in document21_images_list_rawFile:
            document21_binaryImage = raw_image.read()
            document21_base64Image = codecs.encode(document21_binaryImage, 'base64')
            document21_UTF8Image = document21_base64Image.decode('utf-8')
            document21_images_UTF8_list.append(document21_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        housing_collection_document21_imageA = document21_images_UTF8_list[0]

        try:
            housing_collection_document21_imageB = document21_images_UTF8_list[1]
        except:
            housing_collection_document21_imageB = document21_images_UTF8_list[0]

        try:
            housing_collection_document21_imageC = document21_images_UTF8_list[2]
        except:
            housing_collection_document21_imageC = document21_images_UTF8_list[0]

        try:
            housing_collection_document21_imageD = document21_images_UTF8_list[3]
        except:
            housing_collection_document21_imageD = document21_images_UTF8_list[0]       
        
        try:
            housing_collection_document21_imageE = document21_images_UTF8_list[4]
        except:
            housing_collection_document21_imageE = document21_images_UTF8_list[0]





        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document22
        #######################

        # For the text strings,
        housing_collection_document22_productID = document22["Product ID"]
        housing_collection_document22_username = document22["Username"]
        housing_collection_document22_state = document22["State"]
        housing_collection_document22_city = document22["City"]
        housing_collection_document22_description = document22["Description"]
        housing_collection_document22_mobile = document22["Mobile"]
        housing_collection_document22_email = document22["Email"]
        housing_collection_document22_category = document22["Category"]
        housing_collection_document22_condition = document22["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document22_images_UTF8_list = []

        for raw_image in document22_images_list_rawFile:
            document22_binaryImage = raw_image.read()
            document22_base64Image = codecs.encode(document22_binaryImage, 'base64')
            document22_UTF8Image = document22_base64Image.decode('utf-8')
            document22_images_UTF8_list.append(document22_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        housing_collection_document22_imageA = document22_images_UTF8_list[0]

        try:
            housing_collection_document22_imageB = document22_images_UTF8_list[1]
        except:
            housing_collection_document22_imageB = document22_images_UTF8_list[0]

        try:
            housing_collection_document22_imageC = document22_images_UTF8_list[2]
        except:
            housing_collection_document22_imageC = document22_images_UTF8_list[0]

        try:
            housing_collection_document22_imageD = document22_images_UTF8_list[3]
        except:
            housing_collection_document22_imageD = document22_images_UTF8_list[0]       
        
        try:
            housing_collection_document22_imageE = document22_images_UTF8_list[4]
        except:
            housing_collection_document22_imageE = document22_images_UTF8_list[0]






        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document23
        #######################

        # For the text strings,
        housing_collection_document23_productID = document23["Product ID"]
        housing_collection_document23_username = document23["Username"]
        housing_collection_document23_state = document23["State"]
        housing_collection_document23_city = document23["City"]
        housing_collection_document23_description = document23["Description"]
        housing_collection_document23_mobile = document23["Mobile"]
        housing_collection_document23_email = document23["Email"]
        housing_collection_document23_category = document23["Category"]
        housing_collection_document23_condition = document23["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document23_images_UTF8_list = []

        for raw_image in document23_images_list_rawFile:
            document23_binaryImage = raw_image.read()
            document23_base64Image = codecs.encode(document23_binaryImage, 'base64')
            document23_UTF8Image = document23_base64Image.decode('utf-8')
            document23_images_UTF8_list.append(document23_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        housing_collection_document23_imageA = document23_images_UTF8_list[0]

        try:
            housing_collection_document23_imageB = document23_images_UTF8_list[1]
        except:
            housing_collection_document23_imageB = document23_images_UTF8_list[0]

        try:
            housing_collection_document23_imageC = document23_images_UTF8_list[2]
        except:
            housing_collection_document23_imageC = document23_images_UTF8_list[0]

        try:
            housing_collection_document23_imageD = document23_images_UTF8_list[3]
        except:
            housing_collection_document23_imageD = document23_images_UTF8_list[0]       
        
        try:
            housing_collection_document23_imageE = document23_images_UTF8_list[4]
        except:
            housing_collection_document23_imageE = document23_images_UTF8_list[0]





        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document24
        #######################

        # For the text strings,
        housing_collection_document24_productID = document24["Product ID"]
        housing_collection_document24_username = document24["Username"]
        housing_collection_document24_state = document24["State"]
        housing_collection_document24_city = document24["City"]
        housing_collection_document24_description = document24["Description"]
        housing_collection_document24_mobile = document24["Mobile"]
        housing_collection_document24_email = document24["Email"]
        housing_collection_document24_category = document24["Category"]
        housing_collection_document24_condition = document24["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document24_images_UTF8_list = []

        for raw_image in document24_images_list_rawFile:
            document24_binaryImage = raw_image.read()
            document24_base64Image = codecs.encode(document24_binaryImage, 'base64')
            document24_UTF8Image = document24_base64Image.decode('utf-8')
            document24_images_UTF8_list.append(document24_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        housing_collection_document24_imageA = document24_images_UTF8_list[0]

        try:
            housing_collection_document24_imageB = document24_images_UTF8_list[1]
        except:
            housing_collection_document24_imageB = document24_images_UTF8_list[0]

        try:
            housing_collection_document24_imageC = document24_images_UTF8_list[2]
        except:
            housing_collection_document24_imageC = document24_images_UTF8_list[0]

        try:
            housing_collection_document24_imageD = document24_images_UTF8_list[3]
        except:
            housing_collection_document24_imageD = document24_images_UTF8_list[0]       
        
        try:
            housing_collection_document24_imageE = document24_images_UTF8_list[4]
        except:
            housing_collection_document24_imageE = document24_images_UTF8_list[0]






        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document25
        #######################

        # For the text strings,
        housing_collection_document25_productID = document25["Product ID"]
        housing_collection_document25_username = document25["Username"]
        housing_collection_document25_state = document25["State"]
        housing_collection_document25_city = document25["City"]
        housing_collection_document25_description = document25["Description"]
        housing_collection_document25_mobile = document25["Mobile"]
        housing_collection_document25_email = document25["Email"]
        housing_collection_document25_category = document25["Category"]
        housing_collection_document25_condition = document25["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document25_images_UTF8_list = []

        for raw_image in document25_images_list_rawFile:
            document25_binaryImage = raw_image.read()
            document25_base64Image = codecs.encode(document25_binaryImage, 'base64')
            document25_UTF8Image = document25_base64Image.decode('utf-8')
            document25_images_UTF8_list.append(document25_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        housing_collection_document25_imageA = document25_images_UTF8_list[0]

        try:
            housing_collection_document25_imageB = document25_images_UTF8_list[1]
        except:
            housing_collection_document25_imageB = document25_images_UTF8_list[0]

        try:
            housing_collection_document25_imageC = document25_images_UTF8_list[2]
        except:
            housing_collection_document25_imageC = document25_images_UTF8_list[0]

        try:
            housing_collection_document25_imageD = document25_images_UTF8_list[3]
        except:
            housing_collection_document25_imageD = document25_images_UTF8_list[0]       
        
        try:
            housing_collection_document25_imageE = document25_images_UTF8_list[4]
        except:
            housing_collection_document25_imageE = document25_images_UTF8_list[0]

        # Close our database connection and free up resources.
        client5.close()

        # Pack all return variables into a JSON Structure and use for return
        return{
            'productID21' : housing_collection_document21_productID,
            'username21' : housing_collection_document21_username,
            'state21' : housing_collection_document21_state,
            'city21' : housing_collection_document21_city,
            'description21' : housing_collection_document21_description,
            'mobile21' : housing_collection_document21_mobile,
            'email21' : housing_collection_document21_email,
            'category21' : housing_collection_document21_category,
            'condition21': housing_collection_document21_condition,
            'image21A' : housing_collection_document21_imageA,
            'image21B' : housing_collection_document21_imageB,
            'image21C' : housing_collection_document21_imageC,
            'image21D': housing_collection_document21_imageD,
            'image21E': housing_collection_document21_imageE,

            'productID22' : housing_collection_document22_productID,
            'username22' : housing_collection_document22_username,
            'state22' : housing_collection_document22_state,
            'city22' : housing_collection_document22_city,
            'description22' : housing_collection_document22_description,
            'mobile22' : housing_collection_document22_mobile,
            'email22' : housing_collection_document22_email,
            'category22' : housing_collection_document22_category,
            'condition22': housing_collection_document22_condition,
            'image22A' : housing_collection_document22_imageA,
            'image22B' : housing_collection_document22_imageB,
            'image22C' : housing_collection_document22_imageC,
            'image22D': housing_collection_document22_imageD,
            'image22E': housing_collection_document22_imageE,

            'productID23' : housing_collection_document23_productID,
            'username23' : housing_collection_document23_username,
            'state23' : housing_collection_document23_state,
            'city23' : housing_collection_document23_city,
            'description23' : housing_collection_document23_description,
            'mobile23' : housing_collection_document23_mobile,
            'email23' : housing_collection_document23_email,
            'category23' : housing_collection_document23_category,
            'condition23': housing_collection_document23_condition,
            'image23A' : housing_collection_document23_imageA,
            'image23B' : housing_collection_document23_imageB,
            'image23C' : housing_collection_document23_imageC,
            'image23D': housing_collection_document23_imageD,
            'image23E': housing_collection_document23_imageE,

            'productID24' : housing_collection_document24_productID,
            'username24' : housing_collection_document24_username,
            'state24' : housing_collection_document24_state,
            'city24' : housing_collection_document24_city,
            'description24' : housing_collection_document24_description,
            'mobile24' : housing_collection_document24_mobile,
            'email24' : housing_collection_document24_email,
            'category24' : housing_collection_document24_category,
            'condition24': housing_collection_document24_condition,
            'image24A' : housing_collection_document24_imageA,
            'image24B' : housing_collection_document24_imageB,
            'image24C' : housing_collection_document24_imageC,
            'image24D': housing_collection_document24_imageD,
            'image24E': housing_collection_document24_imageE,

            'productID25' : housing_collection_document25_productID,
            'username25' : housing_collection_document25_username,
            'state25' : housing_collection_document25_state,
            'city25' : housing_collection_document25_city,
            'description25' : housing_collection_document25_description,
            'mobile25' : housing_collection_document25_mobile,
            'email25' : housing_collection_document25_email,
            'category25' : housing_collection_document25_category,
            'condition25': housing_collection_document25_condition,
            'image25A' : housing_collection_document25_imageA,
            'image25B' : housing_collection_document25_imageB,
            'image25C' : housing_collection_document25_imageC,
            'image25D': housing_collection_document25_imageD,
            'image25E': housing_collection_document25_imageE,
        }

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
# FASHION VIEWS
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************

# ########################################################################################################################
# ########################################################################################################################
# ########################################################################################################################
# Create
@view_defaults(route_name='fashion_createNewPost')
class FashionCreateNewPostViews(object):
    def __init__(self, request):
        self.request = request

    # *************************************************************************************************************
    # *************************************************************************************************************
    @view_config(renderer='templates/fashion_templates/fashion_createNewPost.pt')
    def fashion_createNewPost(self):
        return {}


    # *************************************************************************************************************
    # *************************************************************************************************************
    # # Perform operation on query params, send values to the database and give the user a Response after creation 
    # of a new post.
    @view_config(request_method='POST', request_param='fashion_create_submitButton')
    def fashion_createNewPost_response(self):
        from pyramid.httpexceptions import HTTPFound

        # Collect variables from form fields
        # Get text items from form page
        fashion_create_username = self.request.params['fashion_create_username']
        fashion_create_statesList = self.request.params['fashion_create_statesList']
        fashion_create_city = self.request.params['fashion_create_city']
        fashion_create_textarea = self.request.params['fashion_create_textarea']
        fashion_create_mobile = self.request.params['fashion_create_mobile']
        fashion_create_email = self.request.params['fashion_create_email']
        fashion_create_category = self.request.params['fashion_create_category']
        fashion_create_condition = self.request.params['fashion_create_condition']

        # Get images from form page
        fashion_create_images = self.request.POST.getall('fashion_create_images')

        # Use this for our rest API insertion operation
        fashion_create_images_names_list = []
        for fashion_create_image_name in fashion_create_images:
            fashion_create_images_names_list.append(fashion_create_image_name.filename)

        # use this for gridFS insertion operation
        fashion_create_images_list = []
        for fashion_create_image in fashion_create_images:
            fashion_create_images_list.append(fashion_create_image)


        # Create other backend variables
        # create Product ID
        from .myModules import ran_gen_a
        fashion_create_productID = ran_gen_a(8, "AEIOSODMG23")


        # Create a UUID number
        import uuid
        fashion_create_privateUUID = uuid.uuid4()

        # Get specific date
        import datetime
        fashion_create_dateTime = datetime.datetime.utcnow()


        # Create our RES API structure and push data to the RES
        fashion_resAPI_json = {
            "Private UUID": "",
            "Product ID": "",
            "Username": "",
            "State": "",
            "City": "",
            "Description": "",
            "Mobile": "",
            "Email": "",
            "Category": "",
            "Condition": "",
            "Images": [],
            "date": "",
        }


        fashion_resAPI_json["Private UUID"] = fashion_create_privateUUID
        fashion_resAPI_json["Product ID"] = fashion_create_productID
        fashion_resAPI_json["Username"] = fashion_create_username
        fashion_resAPI_json["State"] = fashion_create_statesList
        fashion_resAPI_json["City"] = fashion_create_city
        fashion_resAPI_json["Description"] = fashion_create_textarea
        fashion_resAPI_json["Mobile"] = fashion_create_mobile
        fashion_resAPI_json["Email"] = fashion_create_email
        fashion_resAPI_json["Category"] = fashion_create_category
        fashion_resAPI_json["Condition"] = fashion_create_condition
        fashion_resAPI_json["Images"] = fashion_create_images_names_list
        fashion_resAPI_json["date"] = fashion_create_dateTime



        # Initialise database connection and perform CRUD operation on text and images
        # Perform CRUD operation on text strings
        import pymongo
        from pymongo import MongoClient
        # Extract connection string from enviroment variables
        import os
        from dotenv import load_dotenv
        load_dotenv()
        connection_string = os.environ['MY_CONNECTION_STRING']
        # Open database connection and get or create a database called spacenetng_database
        import dns
        client = MongoClient('%s' % connection_string)
        db = client.spacenetng_database

        # Create or open a text based records collection called fashion_text_collection
        text_collection= db.fashion_text_collection

        # Insert API into database and close our connected client's connection
        text_collection.insert_one(fashion_resAPI_json)


        # Perform CRUD operation on images
        import gridfs
        from gridfs import GridFS

        # Creating or getting an fashion gridfs collection called 'fashion_images_collection'
        # (Getting the GridFS object)
        image_collection = GridFS(db, "fashion_images_collection")

        # Inserting files into gridfs and close our connected client's connection
        for image in fashion_create_images_list:
            image_collection.put(image.file, filename=image.filename)

        # Close our database connection and free up resources.
        client.close()


        # # ############################################################################################
        # # Send private UUID to user's Email using login details and gmail server using inbuilt python email package
        import smtplib, os, sys
        from smtplib import SMTP
        from email.message import EmailMessage
        from dotenv import load_dotenv
        load_dotenv()

        try:
            email_content = ("""\
            Hello %s, thanks for posting on spacenetng platform, an online commercial market place where buyers and sellers
            meet to carry out business transactions. Please be advised, a private user UUID has been created for you which 
            you can use to update or delete your post and it should be kept confidential.\n
            Here is your Seceret hey: %s\n
            For support and enquiries please contact us via our contact details found on our contact page in our website.\n
            Thanks for using this service, we hope to serve you better!!.
            """
            % (fashion_create_username, fashion_create_privateUUID)
            
            )

            msg = EmailMessage()
            msg.set_content(email_content)

            msg['Subject'] = 'Your UUID from Spacenetng'
            msg['From'] = 'spacenetngbase@gmail.com'
            msg['To'] = fashion_create_email

            server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server_ssl.ehlo()

            email = os.environ['MY_EMAIL_ADDRESS']
            passWord = os.environ['MY_EMAIL_PASSWORD']

            server_ssl.login(email, passWord)
            server_ssl.send_message(msg)       
            server_ssl.quit()   # Terminate the SMTP session and free up resources       
            
            # Or And,
            # print('Message sent successfully!!')

        except:
            pass
            # Or
            # print X

        finally:
            pass


        ######################################################
        # Redirect user to view what he/she has just posted                      
        body = (
            "<html style=\"color: green; background-color: whitesmoke; \">"
            "<head><meta http-equiv=\"refresh\" content=\"6;url=/fashion_viewProducts2_page1\"></head>"
            "<body>"
            "<h4>Thanks for using our service, your post has been recorded successfully!! "
            "<br />"
            "You will be redirected shortly.</h4>"
            "</body>"
            "</html>"
        )

        return Response(body)





# ########################################################################################################################
# ########################################################################################################################
# ########################################################################################################################
# Modify
@view_defaults(route_name='fashion_modifyPost1')
class FashionModifyPostViews(object):
    def __init__(self, request):
        self.request = request


    # *************************************************************************************************************
    # *************************************************************************************************************
    @view_config(renderer='templates/fashion_templates/fashion_modifyPost1.pt')
    def fashion_modifyPost1(self):
        return {'user_warning': ''}



    # *************************************************************************************************************
    # *************************************************************************************************************
    # Handler method for modifyPost1 page form field input validation for edit mode
    # Redirect to modifyPost2 page if valid private uuid was given, else throw error.
    @view_config(request_method='POST', request_param='fashion_modify1_editButton', renderer='templates/fashion_templates/fashion_modifyPost1.pt')
    def fashion_modifyPost1_update_handler(self):
        from pyramid.renderers import render
        from pyramid.response import Response
        from pyramid.httpexceptions import HTTPFound
        import pymongo
        from pymongo import MongoClient
        from bson import ObjectId
        from uuid import UUID
        # Extract connection string from enviroment variables
        import os
        from dotenv import load_dotenv
        load_dotenv()
        connection_string = os.environ['MY_CONNECTION_STRING']
        # Open database connection and get or create a database called spacenetng_database
        import dns
        client = MongoClient('%s' % connection_string)
        db = client.spacenetng_database

        # Create or open a text based records collection called fashion_text_collection
        text_collection= db.fashion_text_collection


        fashion_update_privateUUID = self.request.params['fashion_modify1_privateUUID']

        try:
            text_collection.find_one({'Private UUID': UUID(fashion_update_privateUUID)})
            result1 = render('templates/fashion_templates/fashion_modifyPost2.pt' , {'private_UUID': fashion_update_privateUUID, 'user_warning': ''}, request=self.request)
            return Response(result1)

        except:
            # Re-render form page and throw an error message saying "Invalid Private UUID entered!!"
            return {'user_warning': 'Invalid Private UUID entered!!'}

        client.close()
            



    # *************************************************************************************************************
    # *************************************************************************************************************
    # Handler method for modifyPost1 page form field input validation for delete mode
    @view_config(request_method='POST', request_param='fashion_modify1_deleteButton', renderer='templates/fashion_templates/fashion_modifyPost1.pt')
    def fashion_modifyPost1_delete_handler(self):
        from pyramid.renderers import render
        from pyramid.response import Response
        from pyramid.httpexceptions import HTTPFound
        import pymongo
        from pymongo import MongoClient
        from bson import ObjectId
        from uuid import UUID
        # Extract connection string from enviroment variables
        import os
        from dotenv import load_dotenv
        load_dotenv()
        connection_string = os.environ['MY_CONNECTION_STRING']
        # Open database connection and get or create a database called spacenetng_database
        import dns
        client = MongoClient('%s' % connection_string)
        db = client.spacenetng_database

        # Create or open a text based records collection called fashion_text_collection
        text_collection= db.fashion_text_collection


        # Perform CRUD operation on images
        import gridfs
        from gridfs import GridFS

        # Creating or getting an fashion gridfs collection called 'fashion_images_collection'
        # (Getting the GridFS object)
        image_collection = GridFS(db, "fashion_images_collection")


        fashion_delete_privateUUID = self.request.params['fashion_modify1_privateUUID']

        # # Delete operation................................................................................
        # Perform a find() query operation on a document using the private UUID for delete permision,
        # and then obtain its "_id" field.

        try:
            # Delete operation on the main text collection initialisation
            res0 = text_collection.find_one({'Private UUID': UUID(fashion_delete_privateUUID)})
            res1 = res0['_id']    # Obtaining the '_id' attribute diff from that of gridfs

            # Delete operation On image collection
            # Obtain the '_id' values each on all images from the image collection
            # then perform the delete and/or replacement operation

            # Delete images in collection first before deleting the actual collection
            image_names_list_toDelete = res0['Images']

            for name in image_names_list_toDelete:
                res2 = image_collection.find_one({'filename': name})
                res3 = res2._id    # Obtaining the '_id' attribute
                image_collection.delete(ObjectId(res3))  # Delete format for files in gridfs

            # text collection delete
            text_collection.delete_one({'_id': ObjectId(res1)})
            client.close()

            body = (
                "<html style=\"color: green; background-color: whitesmoke; \">"
                "<head><meta http-equiv=\"refresh\" content=\"6;url=/\"></head>"
                "<body>"
                "<h4>Thanks for using our service, your post has been deleted successfully!! "
                "<br />"
                "You will be redirected shortly.</h4>"
                "</body>"
                "</html>"
            )

            return Response(body)


        except:
            # Re-render form page and throw an error message saying "Invalid Private UUID entered!!"
            return {'user_warning': 'Invalid Private UUID entered!!'}






    # *************************************************************************************************************
    # *************************************************************************************************************
    # # response for modifyPost1 page, return this page if correct params were given in modifyPost1 page.
    @view_config(route_name='fashion_modifyPost2', renderer='templates/fashion_templates/fashion_modifyPost2.pt')
    def fashion_modifyPost2(self):
        return {}



    # *************************************************************************************************************
    # *************************************************************************************************************
    # Perform operation on query params from modifyPost2 page,
    # return values and give the user a Response after creation of a new post
    @view_config(request_method='POST', request_param='fashion_update_submitButton')
    def fashion_modifyPost2_response(self):
        # -----------------------------------------------------------------------------------------------------------------
        # Updating and deleting records in database
        from pyramid.response import Response
        from pyramid.httpexceptions import HTTPFound
        import pymongo
        from pymongo import MongoClient
        from bson import ObjectId
        from uuid import UUID
        # Extract connection string from enviroment variables
        import os
        from dotenv import load_dotenv
        load_dotenv()
        connection_string = os.environ['MY_CONNECTION_STRING']
        # Open database connection and get or create a database called spacenetng_database
        import dns
        client = MongoClient('%s' % connection_string)
        db = client.spacenetng_database

        # Create or open a text based records collection called fashion_text_collection
        text_collection= db.fashion_text_collection


        # Perform CRUD operation on images
        import gridfs
        from gridfs import GridFS

        # Creating or getting an fashion gridfs collection called 'fashion_images_collection'
        # (Getting the GridFS object)
        image_collection = GridFS(db, "fashion_images_collection")


        # Perform CRUD Operation
        # Get specific date
        import datetime
        fashion_update_dateTime = datetime.datetime.utcnow()

        fashion_resAPI_json = {
            "Username": "",
            "State": "",
            "City": "",
            "Description": "",
            "Mobile": "",
            "Email": "",
            "Category": "",
            "Condition": "",
            "Images": [],
            "date": "",
            }

        #######################
        # Collect variables from form fields
        #######################

        # Get text items from form page
        fashion_update_username = self.request.params['fashion_update_username']
        fashion_update_statesList = self.request.params['fashion_update_statesList']
        fashion_update_city = self.request.params['fashion_update_city']
        fashion_update_textarea = self.request.params['fashion_update_textarea']
        fashion_update_mobile = self.request.params['fashion_update_mobile']
        fashion_update_email = self.request.params['fashion_update_email']
        fashion_update_category = self.request.params['fashion_update_category']
        fashion_update_condition = self.request.params['fashion_update_condition']
           
        # Get images from form page
        fashion_update_images = self.request.POST.getall('fashion_update_images')

        # Use this for our rest API insertion operation
        fashion_update_images_names_list = []
        for fashion_update_image_name in fashion_update_images:
            fashion_update_images_names_list.append(fashion_update_image_name.filename)

        # use this for gridFS insertion operation
        fashion_update_images_list = []
        for fashion_update_image in fashion_update_images:
            fashion_update_images_list.append(fashion_update_image)



        fashion_resAPI_json["Username"] = fashion_update_username
        fashion_resAPI_json["State"] = fashion_update_statesList
        fashion_resAPI_json["City"] = fashion_update_city
        fashion_resAPI_json["Description"] = fashion_update_textarea
        fashion_resAPI_json["Mobile"] = fashion_update_mobile
        fashion_resAPI_json["Email"] = fashion_update_email
        fashion_resAPI_json["Category"] = fashion_update_category
        fashion_resAPI_json["Condition"] = fashion_update_condition
        fashion_resAPI_json["Images"] = fashion_update_images_names_list
        fashion_resAPI_json["date"] = fashion_update_dateTime




        # Update operation.........................................................................
        # Update API in database and close our connected client's connection
        # Perform a find() query operation on a document using the private UUID to locate the particular document,
        # and then obtain its "_id" field.
        fashion_update_privateUUID = self.request.params['fashion_update_privateUUID']

        # Inititalise overall collection query using the text collection
        res1 = text_collection.find_one({'Private UUID': UUID(fashion_update_privateUUID)})
        res2 = res1['_id']         # Obtaining the '_id' attribute diff from that of gridfs


        # Before inserting files, query for previous images previously inside database,
        # delete all images there and replace/update with the new one.

        # Obtain the '_id' values each on all images from the image collection
        # then perform the delete operation followed by the replacement operation
        image_names_list_toDelete = res1['Images']

        # Delete images already present first before updating the main collection
        # delete image collection
        for name in image_names_list_toDelete:
            res3 = image_collection.find_one({'filename': name})
            res4 = res3._id    # Obtaining the '_id' attribute
            image_collection.delete(ObjectId(res4))  # Delete format for files in gridfs


        # Main text collection update
        text_collection.update_one({'_id': ObjectId(res2)}, {"$set": fashion_resAPI_json})

        # then also update the image collection with the new images
        for image in fashion_update_images_list:
            image_collection.put(image.file, filename=image.filename) # The update operation

            

        # Close our database connection and free up resources.
        client.close()

        body = (
            "<html style=\"color: green; background-color: whitesmoke; \">"
            "<head><meta http-equiv=\"refresh\" content=\"6;url=/\"></head>"
            "<body>"
            "<h4>Thanks for using our service, your post has been updated successfully!! "
            "<br />"
            "You will be redirected shortly.</h4>"
            "</body>"
            "</html>"
        )

        return Response(body)



# ########################################################################################################################
# ########################################################################################################################
# ########################################################################################################################
# View products
@view_defaults(route_name='fashion_viewProducts1')
class FashionViewProductsViews(object):
    def __init__(self, request):
        self.request = request


    # *************************************************************************************************************
    # *************************************************************************************************************
    @view_config(renderer='templates/fashion_templates/fashion_viewProducts1.pt')
    def fashion_viewProducts1(self):
        return {}


    # *************************************************************************************************************
    # *************************************************************************************************************
    # Response from viewProducts1 page and validate with records in database 
    @view_config(request_method='POST', request_param='fashion_view_submit')
    def fashion_viewProducts2_page1A(self):
        from pyramid.httpexceptions import HTTPFound
        # Perform some database matching on sub categories and redirect to the appropriate renderer.
        return HTTPFound(location='fashion_viewProducts2_page1')

    # *************************************************************************************************************
    # *************************************************************************************************************
    @view_config(route_name='fashion_viewProducts2_page1', renderer='templates/fashion_templates/fashion_viewProducts2_page1.pt')
    def fashion_viewProducts2_page1B(self):
        import pymongo
        from pymongo import MongoClient
        import gridfs
        from gridfs import GridFS
        # Extract connection string from enviroment variables
        import os
        from dotenv import load_dotenv
        load_dotenv()
        connection_string = os.environ['MY_CONNECTION_STRING']
        # Open database connection and get or create a database called spacenetng_database
        import dns
        client1 = MongoClient('%s' % connection_string)
        db = client1.spacenetng_database

        # Create or open a text based records collection called fashion_text_collection
        text_collection_fashion = db.fashion_text_collection

        # Establish gridfs collection connection
        # Creating or getting an fashion gridfs collection called 'fashion_images_collection'
        # (Getting the GridFS object)
        image_collection_fashion = GridFS(db, "fashion_images_collection")

        # Retrieve document record from database operation
        fashion_collection = text_collection_fashion.find().sort([("_id", pymongo.DESCENDING)]).limit(5) #This returns 25 records

        # Push documents into a list
        fashion_collection_list = []

        for record in fashion_collection:
            fashion_collection_list.append(record)

        document1 = fashion_collection_list[0]
        document2 = fashion_collection_list[1]
        document3 = fashion_collection_list[2]
        document4 = fashion_collection_list[3]
        document5 = fashion_collection_list[4]
        

        # Extracting images
        # The images for document1
        document1_images_list_rawFile = []
        for image_name in document1["Images"]:
            document1_images_list_rawFile.append(image_collection_fashion.get_last_version(filename=image_name))

        # For the images for document2
        document2_images_list_rawFile = []
        for image_name in document2["Images"]:
            document2_images_list_rawFile.append(image_collection_fashion.get_last_version(filename=image_name))

        # The images for document3
        document3_images_list_rawFile = []
        for image_name in document3["Images"]:
            document3_images_list_rawFile.append(image_collection_fashion.get_last_version(filename=image_name))

        # The images for document4
        document4_images_list_rawFile = []
        for image_name in document4["Images"]:
            document4_images_list_rawFile.append(image_collection_fashion.get_last_version(filename=image_name))

        # The images for document5
        document5_images_list_rawFile = []
        for image_name in document5["Images"]:
            document5_images_list_rawFile.append(image_collection_fashion.get_last_version(filename=image_name))



        ##############################################
        # Collecting record from individual documents
        ##############################################
        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document1
        #######################

        # For the text strings,
        fashion_collection_document1_productID = document1["Product ID"]
        fashion_collection_document1_username = document1["Username"]
        fashion_collection_document1_state = document1["State"]
        fashion_collection_document1_city = document1["City"]
        fashion_collection_document1_description = document1["Description"]
        fashion_collection_document1_mobile = document1["Mobile"]
        fashion_collection_document1_email = document1["Email"]
        fashion_collection_document1_category = document1["Category"]
        fashion_collection_document1_condition = document1["Condition"]



        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document1_images_UTF8_list = []

        for raw_image in document1_images_list_rawFile:
            document1_binaryImage = raw_image.read()
            document1_base64Image = codecs.encode(document1_binaryImage, 'base64')
            document1_UTF8Image = document1_base64Image.decode('utf-8')
            document1_images_UTF8_list.append(document1_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        fashion_collection_document1_imageA = document1_images_UTF8_list[0]

        try:
            fashion_collection_document1_imageB = document1_images_UTF8_list[1]
        except:
            fashion_collection_document1_imageB = document1_images_UTF8_list[0]

        try:
            fashion_collection_document1_imageC = document1_images_UTF8_list[2]
        except:
            fashion_collection_document1_imageC = document1_images_UTF8_list[0]

        try:
            fashion_collection_document1_imageD = document1_images_UTF8_list[3]
        except:
            fashion_collection_document1_imageD = document1_images_UTF8_list[0]       
        
        try:
            fashion_collection_document1_imageE = document1_images_UTF8_list[4]
        except:
            fashion_collection_document1_imageE = document1_images_UTF8_list[0]





        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document2
        #######################

        # For the text strings,
        fashion_collection_document2_productID = document2["Product ID"]
        fashion_collection_document2_username = document2["Username"]
        fashion_collection_document2_state = document2["State"]
        fashion_collection_document2_city = document2["City"]
        fashion_collection_document2_description = document2["Description"]
        fashion_collection_document2_mobile = document2["Mobile"]
        fashion_collection_document2_email = document2["Email"]
        fashion_collection_document2_category = document2["Category"]
        fashion_collection_document2_condition = document2["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document2_images_UTF8_list = []

        for raw_image in document2_images_list_rawFile:
            document2_binaryImage = raw_image.read()
            document2_base64Image = codecs.encode(document2_binaryImage, 'base64')
            document2_UTF8Image = document2_base64Image.decode('utf-8')
            document2_images_UTF8_list.append(document2_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        fashion_collection_document2_imageA = document2_images_UTF8_list[0]

        try:
            fashion_collection_document2_imageB = document2_images_UTF8_list[1]
        except:
            fashion_collection_document2_imageB = document2_images_UTF8_list[0]

        try:
            fashion_collection_document2_imageC = document2_images_UTF8_list[2]
        except:
            fashion_collection_document2_imageC = document2_images_UTF8_list[0]

        try:
            fashion_collection_document2_imageD = document2_images_UTF8_list[3]
        except:
            fashion_collection_document2_imageD = document2_images_UTF8_list[0]       
        
        try:
            fashion_collection_document2_imageE = document2_images_UTF8_list[4]
        except:
            fashion_collection_document2_imageE = document2_images_UTF8_list[0]





        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document3
        #######################

        # For the text strings,
        fashion_collection_document3_productID = document3["Product ID"]
        fashion_collection_document3_username = document3["Username"]
        fashion_collection_document3_state = document3["State"]
        fashion_collection_document3_city = document3["City"]
        fashion_collection_document3_description = document3["Description"]
        fashion_collection_document3_mobile = document3["Mobile"]
        fashion_collection_document3_email = document3["Email"]
        fashion_collection_document3_category = document3["Category"]
        fashion_collection_document3_condition = document3["Condition"]

        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document3_images_UTF8_list = []

        for raw_image in document3_images_list_rawFile:
            document3_binaryImage = raw_image.read()
            document3_base64Image = codecs.encode(document3_binaryImage, 'base64')
            document3_UTF8Image = document3_base64Image.decode('utf-8')
            document3_images_UTF8_list.append(document3_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        fashion_collection_document3_imageA = document3_images_UTF8_list[0]

        try:
            fashion_collection_document3_imageB = document3_images_UTF8_list[1]
        except:
            fashion_collection_document3_imageB = document3_images_UTF8_list[0]

        try:
            fashion_collection_document3_imageC = document3_images_UTF8_list[2]
        except:
            fashion_collection_document3_imageC = document3_images_UTF8_list[0]

        try:
            fashion_collection_document3_imageD = document3_images_UTF8_list[3]
        except:
            fashion_collection_document3_imageD = document3_images_UTF8_list[0]       
        
        try:
            fashion_collection_document3_imageE = document3_images_UTF8_list[4]
        except:
            fashion_collection_document3_imageE = document3_images_UTF8_list[0]





        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document4
        #######################

        # For the text strings,
        fashion_collection_document4_productID = document4["Product ID"]
        fashion_collection_document4_username = document4["Username"]
        fashion_collection_document4_state = document4["State"]
        fashion_collection_document4_city = document4["City"]
        fashion_collection_document4_description = document4["Description"]
        fashion_collection_document4_mobile = document4["Mobile"]
        fashion_collection_document4_email = document4["Email"]
        fashion_collection_document4_category = document4["Category"]
        fashion_collection_document4_condition = document4["Condition"]

        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document4_images_UTF8_list = []

        for raw_image in document4_images_list_rawFile:
            document4_binaryImage = raw_image.read()
            document4_base64Image = codecs.encode(document4_binaryImage, 'base64')
            document4_UTF8Image = document4_base64Image.decode('utf-8')
            document4_images_UTF8_list.append(document4_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        fashion_collection_document4_imageA = document4_images_UTF8_list[0]

        try:
            fashion_collection_document4_imageB = document4_images_UTF8_list[1]
        except:
            fashion_collection_document4_imageB = document4_images_UTF8_list[0]

        try:
            fashion_collection_document4_imageC = document4_images_UTF8_list[2]
        except:
            fashion_collection_document4_imageC = document4_images_UTF8_list[0]

        try:
            fashion_collection_document4_imageD = document4_images_UTF8_list[3]
        except:
            fashion_collection_document4_imageD = document4_images_UTF8_list[0]       
        
        try:
            fashion_collection_document4_imageE = document4_images_UTF8_list[4]
        except:
            fashion_collection_document4_imageE = document4_images_UTF8_list[0]




        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document5
        #######################

        # For the text strings,
        fashion_collection_document5_productID = document5["Product ID"]
        fashion_collection_document5_username = document5["Username"]
        fashion_collection_document5_state = document5["State"]
        fashion_collection_document5_city = document5["City"]
        fashion_collection_document5_description = document5["Description"]
        fashion_collection_document5_mobile = document5["Mobile"]
        fashion_collection_document5_email = document5["Email"]
        fashion_collection_document5_category = document5["Category"]
        fashion_collection_document5_condition = document5["Condition"]

        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document5_images_UTF8_list = []

        for raw_image in document5_images_list_rawFile:
            document5_binaryImage = raw_image.read()
            document5_base64Image = codecs.encode(document5_binaryImage, 'base64')
            document5_UTF8Image = document5_base64Image.decode('utf-8')
            document5_images_UTF8_list.append(document5_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        fashion_collection_document5_imageA = document5_images_UTF8_list[0]

        try:
            fashion_collection_document5_imageB = document5_images_UTF8_list[1]
        except:
            fashion_collection_document5_imageB = document5_images_UTF8_list[0]

        try:
            fashion_collection_document5_imageC = document5_images_UTF8_list[2]
        except:
            fashion_collection_document5_imageC = document5_images_UTF8_list[0]

        try:
            fashion_collection_document5_imageD = document5_images_UTF8_list[3]
        except:
            fashion_collection_document5_imageD = document5_images_UTF8_list[0]       
        
        try:
            fashion_collection_document5_imageE = document5_images_UTF8_list[4]
        except:
            fashion_collection_document5_imageE = document5_images_UTF8_list[0]

        
        # Close our database connection and free up resources.
        client1.close()

        # Pack all return variables into a JSON Structure and use for return
        return {
            
            'productID1' : fashion_collection_document1_productID,
            'username1' : fashion_collection_document1_username,
            'state1' : fashion_collection_document1_state,
            'city1' : fashion_collection_document1_city,
            'description1' : fashion_collection_document1_description,
            'mobile1' : fashion_collection_document1_mobile,
            'email1' : fashion_collection_document1_email,
            'category1' : fashion_collection_document1_category,
            'condition1': fashion_collection_document1_condition,
            'image1A' : fashion_collection_document1_imageA,
            'image1B' : fashion_collection_document1_imageB,
            'image1C' : fashion_collection_document1_imageC,
            'image1D': fashion_collection_document1_imageD,
            'image1E': fashion_collection_document1_imageE,

            'productID2' : fashion_collection_document2_productID,
            'username2' : fashion_collection_document2_username,
            'state2' : fashion_collection_document2_state,
            'city2' : fashion_collection_document2_city,
            'description2' : fashion_collection_document2_description,
            'mobile2' : fashion_collection_document2_mobile,
            'email2' : fashion_collection_document2_email,
            'category2' : fashion_collection_document2_category,
            'condition2': fashion_collection_document2_condition,
            'image2A' : fashion_collection_document2_imageA,
            'image2B' : fashion_collection_document2_imageB,
            'image2C' : fashion_collection_document2_imageC,
            'image2D': fashion_collection_document2_imageD,
            'image2E': fashion_collection_document2_imageE,

            'productID3' : fashion_collection_document3_productID,
            'username3' : fashion_collection_document3_username,
            'state3' : fashion_collection_document3_state,
            'city3' : fashion_collection_document3_city,
            'description3' : fashion_collection_document3_description,
            'mobile3' : fashion_collection_document3_mobile,
            'email3' : fashion_collection_document3_email,
            'category3' : fashion_collection_document3_category,
            'condition3': fashion_collection_document3_condition,
            'image3A' : fashion_collection_document3_imageA,
            'image3B' : fashion_collection_document3_imageB,
            'image3C' : fashion_collection_document3_imageC,
            'image3D': fashion_collection_document3_imageD,
            'image3E': fashion_collection_document3_imageE,

            'productID4' : fashion_collection_document4_productID,
            'username4' : fashion_collection_document4_username,
            'state4' : fashion_collection_document4_state,
            'city4' : fashion_collection_document4_city,
            'description4' : fashion_collection_document4_description,
            'mobile4' : fashion_collection_document4_mobile,
            'email4' : fashion_collection_document4_email,
            'category4' : fashion_collection_document4_category,
            'condition4': fashion_collection_document4_condition,
            'image4A' : fashion_collection_document4_imageA,
            'image4B' : fashion_collection_document4_imageB,
            'image4C' : fashion_collection_document4_imageC,
            'image4D': fashion_collection_document4_imageD,
            'image4E': fashion_collection_document4_imageE,

            'productID5' : fashion_collection_document5_productID,
            'username5' : fashion_collection_document5_username,
            'state5' : fashion_collection_document5_state,
            'city5' : fashion_collection_document5_city,
            'description5' : fashion_collection_document5_description,
            'mobile5' : fashion_collection_document5_mobile,
            'email5' : fashion_collection_document5_email,
            'category5' : fashion_collection_document5_category,
            'condition5': fashion_collection_document5_condition,
            'image5A' : fashion_collection_document5_imageA,
            'image5B' : fashion_collection_document5_imageB,
            'image5C' : fashion_collection_document5_imageC,
            'image5D': fashion_collection_document5_imageD,
            'image5E': fashion_collection_document5_imageE,
            }


    # View pages....(n)
    # *************************************************************************************************************
    # *************************************************************************************************************
    @view_config(route_name='fashion_viewProducts2_page2', renderer='templates/fashion_templates/fashion_viewProducts2_page2.pt')
    def fashion_viewProducts2_page2(self):
        import pymongo
        from pymongo import MongoClient
        import gridfs
        from gridfs import GridFS
        # Extract connection string from enviroment variables
        import os
        from dotenv import load_dotenv
        load_dotenv()
        connection_string = os.environ['MY_CONNECTION_STRING']
        # Open database connection and get or create a database called spacenetng_database
        import dns
        client2 = MongoClient('%s' % connection_string)
        db = client2.spacenetng_database

        # Create or open a text based records collection called fashion_text_collection
        text_collection_fashion = db.fashion_text_collection

        # Establish gridfs collection connection
        # Creating or getting an fashion gridfs collection called 'fashion_images_collection'
        # (Getting the GridFS object)
        image_collection_fashion = GridFS(db, "fashion_images_collection")

        # Retrieve document record from database operation
        fashion_collection = text_collection_fashion.find().sort([("_id", pymongo.DESCENDING)]).skip(5).limit(5) #This returns 25 records

        # Push documents into a list
        fashion_collection_list = []

        for record in fashion_collection:
            fashion_collection_list.append(record)

        document6 = fashion_collection_list[0]
        document7 = fashion_collection_list[1]
        document8 = fashion_collection_list[2]
        document9 = fashion_collection_list[3]
        document10 = fashion_collection_list[4]



        # The images for document6
        document6_images_list_rawFile = []
        for image_name in document6["Images"]:
            document6_images_list_rawFile.append(image_collection_fashion.get_last_version(filename=image_name))

        # The images for document7
        document7_images_list_rawFile = []
        for image_name in document7["Images"]:
            document7_images_list_rawFile.append(image_collection_fashion.get_last_version(filename=image_name))

        # The images for document8
        document8_images_list_rawFile = []
        for image_name in document8["Images"]:
            document8_images_list_rawFile.append(image_collection_fashion.get_last_version(filename=image_name))

        # The images for document9
        document9_images_list_rawFile = []
        for image_name in document9["Images"]:
            document9_images_list_rawFile.append(image_collection_fashion.get_last_version(filename=image_name))

        # The images for document10
        document10_images_list_rawFile = []
        for image_name in document10["Images"]:
            document10_images_list_rawFile.append(image_collection_fashion.get_last_version(filename=image_name))


        ##############################################
        # Collecting record from individual documents
        ##############################################
        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document6
        #######################

        # For the text strings,
        fashion_collection_document6_productID = document6["Product ID"]
        fashion_collection_document6_username = document6["Username"]
        fashion_collection_document6_state = document6["State"]
        fashion_collection_document6_city = document6["City"]
        fashion_collection_document6_description = document6["Description"]
        fashion_collection_document6_mobile = document6["Mobile"]
        fashion_collection_document6_email = document6["Email"]
        fashion_collection_document6_category = document6["Category"]
        fashion_collection_document6_condition = document6["Condition"]



        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document6_images_UTF8_list = []

        for raw_image in document6_images_list_rawFile:
            document6_binaryImage = raw_image.read()
            document6_base64Image = codecs.encode(document6_binaryImage, 'base64')
            document6_UTF8Image = document6_base64Image.decode('utf-8')
            document6_images_UTF8_list.append(document6_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        fashion_collection_document6_imageA = document6_images_UTF8_list[0]

        try:
            fashion_collection_document6_imageB = document6_images_UTF8_list[1]
        except:
            fashion_collection_document6_imageB = document6_images_UTF8_list[0]

        try:
            fashion_collection_document6_imageC = document6_images_UTF8_list[2]
        except:
            fashion_collection_document6_imageC = document6_images_UTF8_list[0]

        try:
            fashion_collection_document6_imageD = document6_images_UTF8_list[3]
        except:
            fashion_collection_document6_imageD = document6_images_UTF8_list[0]       
        
        try:
            fashion_collection_document6_imageE = document6_images_UTF8_list[4]
        except:
            fashion_collection_document6_imageE = document6_images_UTF8_list[0]





        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document7
        #######################

        # For the text strings,
        fashion_collection_document7_productID = document7["Product ID"]
        fashion_collection_document7_username = document7["Username"]
        fashion_collection_document7_state = document7["State"]
        fashion_collection_document7_city = document7["City"]
        fashion_collection_document7_description = document7["Description"]
        fashion_collection_document7_mobile = document7["Mobile"]
        fashion_collection_document7_email = document7["Email"]
        fashion_collection_document7_category = document7["Category"]
        fashion_collection_document7_condition = document7["Condition"]



        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document7_images_UTF8_list = []

        for raw_image in document7_images_list_rawFile:
            document7_binaryImage = raw_image.read()
            document7_base64Image = codecs.encode(document7_binaryImage, 'base64')
            document7_UTF8Image = document7_base64Image.decode('utf-8')
            document7_images_UTF8_list.append(document7_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        fashion_collection_document7_imageA = document7_images_UTF8_list[0]

        try:
            fashion_collection_document7_imageB = document7_images_UTF8_list[1]
        except:
            fashion_collection_document7_imageB = document7_images_UTF8_list[0]

        try:
            fashion_collection_document7_imageC = document7_images_UTF8_list[2]
        except:
            fashion_collection_document7_imageC = document7_images_UTF8_list[0]

        try:
            fashion_collection_document7_imageD = document7_images_UTF8_list[3]
        except:
            fashion_collection_document7_imageD = document7_images_UTF8_list[0]       
        
        try:
            fashion_collection_document7_imageE = document7_images_UTF8_list[4]
        except:
            fashion_collection_document7_imageE = document7_images_UTF8_list[0]




        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document8
        #######################

        # For the text strings,
        fashion_collection_document8_productID = document8["Product ID"]
        fashion_collection_document8_username = document8["Username"]
        fashion_collection_document8_state = document8["State"]
        fashion_collection_document8_city = document8["City"]
        fashion_collection_document8_description = document8["Description"]
        fashion_collection_document8_mobile = document8["Mobile"]
        fashion_collection_document8_email = document8["Email"]
        fashion_collection_document8_category = document8["Category"]
        fashion_collection_document8_condition = document8["Condition"]

   
        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document8_images_UTF8_list = []

        for raw_image in document8_images_list_rawFile:
            document8_binaryImage = raw_image.read()
            document8_base64Image = codecs.encode(document8_binaryImage, 'base64')
            document8_UTF8Image = document8_base64Image.decode('utf-8')
            document8_images_UTF8_list.append(document8_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        fashion_collection_document8_imageA = document8_images_UTF8_list[0]

        try:
            fashion_collection_document8_imageB = document8_images_UTF8_list[1]
        except:
            fashion_collection_document8_imageB = document8_images_UTF8_list[0]

        try:
            fashion_collection_document8_imageC = document8_images_UTF8_list[2]
        except:
            fashion_collection_document8_imageC = document8_images_UTF8_list[0]

        try:
            fashion_collection_document8_imageD = document8_images_UTF8_list[3]
        except:
            fashion_collection_document8_imageD = document8_images_UTF8_list[0]       
        
        try:
            fashion_collection_document8_imageE = document8_images_UTF8_list[4]
        except:
            fashion_collection_document8_imageE = document8_images_UTF8_list[0]




        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document9
        #######################

        # For the text strings,
        fashion_collection_document9_productID = document9["Product ID"]
        fashion_collection_document9_username = document9["Username"]
        fashion_collection_document9_state = document9["State"]
        fashion_collection_document9_city = document9["City"]
        fashion_collection_document9_description = document9["Description"]
        fashion_collection_document9_mobile = document9["Mobile"]
        fashion_collection_document9_email = document9["Email"]
        fashion_collection_document9_category = document9["Category"]
        fashion_collection_document9_condition = document9["Condition"]



        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document9_images_UTF8_list = []

        for raw_image in document9_images_list_rawFile:
            document9_binaryImage = raw_image.read()
            document9_base64Image = codecs.encode(document9_binaryImage, 'base64')
            document9_UTF8Image = document9_base64Image.decode('utf-8')
            document9_images_UTF8_list.append(document9_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        fashion_collection_document9_imageA = document9_images_UTF8_list[0]

        try:
            fashion_collection_document9_imageB = document9_images_UTF8_list[1]
        except:
            fashion_collection_document9_imageB = document9_images_UTF8_list[0]

        try:
            fashion_collection_document9_imageC = document9_images_UTF8_list[2]
        except:
            fashion_collection_document9_imageC = document9_images_UTF8_list[0]

        try:
            fashion_collection_document9_imageD = document9_images_UTF8_list[3]
        except:
            fashion_collection_document9_imageD = document9_images_UTF8_list[0]       
        
        try:
            fashion_collection_document9_imageE = document9_images_UTF8_list[4]
        except:
            fashion_collection_document9_imageE = document9_images_UTF8_list[0]


        # For document10
        #######################

        # For the text strings,
        fashion_collection_document10_productID = document10["Product ID"]
        fashion_collection_document10_username = document10["Username"]
        fashion_collection_document10_state = document10["State"]
        fashion_collection_document10_city = document10["City"]
        fashion_collection_document10_description = document10["Description"]
        fashion_collection_document10_mobile = document10["Mobile"]
        fashion_collection_document10_email = document10["Email"]
        fashion_collection_document10_category = document10["Category"]
        fashion_collection_document10_condition = document10["Condition"]



        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document10_images_UTF8_list = []

        for raw_image in document10_images_list_rawFile:
            document10_binaryImage = raw_image.read()
            document10_base64Image = codecs.encode(document10_binaryImage, 'base64')
            document10_UTF8Image = document10_base64Image.decode('utf-8')
            document10_images_UTF8_list.append(document10_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        fashion_collection_document10_imageA = document10_images_UTF8_list[0]

        try:
            fashion_collection_document10_imageB = document10_images_UTF8_list[1]
        except:
            fashion_collection_document10_imageB = document10_images_UTF8_list[0]

        try:
            fashion_collection_document10_imageC = document10_images_UTF8_list[2]
        except:
            fashion_collection_document10_imageC = document10_images_UTF8_list[0]

        try:
            fashion_collection_document10_imageD = document10_images_UTF8_list[3]
        except:
            fashion_collection_document10_imageD = document10_images_UTF8_list[0]       
        
        try:
            fashion_collection_document10_imageE = document10_images_UTF8_list[4]
        except:
            fashion_collection_document10_imageE = document10_images_UTF8_list[0]

        # Close our database connection and free up resources.
        client2.close()

        # Pack all return variables into a JSON Structure and use for return
        return{
            'productID6' : fashion_collection_document6_productID,
            'username6' : fashion_collection_document6_username,
            'state6' : fashion_collection_document6_state,
            'city6' : fashion_collection_document6_city,
            'description6' : fashion_collection_document6_description,
            'mobile6' : fashion_collection_document6_mobile,
            'email6' : fashion_collection_document6_email,
            'category6' : fashion_collection_document6_category,
            'condition6': fashion_collection_document6_condition,
            'image6A' : fashion_collection_document6_imageA,
            'image6B' : fashion_collection_document6_imageB,
            'image6C' : fashion_collection_document6_imageC,
            'image6D': fashion_collection_document6_imageD,
            'image6E': fashion_collection_document6_imageE,

            'productID7' : fashion_collection_document7_productID,
            'username7' : fashion_collection_document7_username,
            'state7' : fashion_collection_document7_state,
            'city7' : fashion_collection_document7_city,
            'description7' : fashion_collection_document7_description,
            'mobile7' : fashion_collection_document7_mobile,
            'email7' : fashion_collection_document7_email,
            'category7' : fashion_collection_document7_category,
            'condition7': fashion_collection_document7_condition,
            'image7A' : fashion_collection_document7_imageA,
            'image7B' : fashion_collection_document7_imageB,
            'image7C' : fashion_collection_document7_imageC,
            'image7D': fashion_collection_document7_imageD,
            'image7E': fashion_collection_document7_imageE,

            'productID8' : fashion_collection_document8_productID,
            'username8' : fashion_collection_document8_username,
            'state8' : fashion_collection_document8_state,
            'city8' : fashion_collection_document8_city,
            'description8' : fashion_collection_document8_description,
            'mobile8' : fashion_collection_document8_mobile,
            'email8' : fashion_collection_document8_email,
            'category8' : fashion_collection_document8_category,
            'condition8': fashion_collection_document8_condition,
            'image8A' : fashion_collection_document8_imageA,
            'image8B' : fashion_collection_document8_imageB,
            'image8C' : fashion_collection_document8_imageC,
            'image8D': fashion_collection_document8_imageD,
            'image8E': fashion_collection_document8_imageE,

            'productID9' : fashion_collection_document9_productID,
            'username9' : fashion_collection_document9_username,
            'state9' : fashion_collection_document9_state,
            'city9' : fashion_collection_document9_city,
            'description9' : fashion_collection_document9_description,
            'mobile9' : fashion_collection_document9_mobile,
            'email9' : fashion_collection_document9_email,
            'category9' : fashion_collection_document9_category,
            'condition9': fashion_collection_document9_condition,
            'image9A' : fashion_collection_document9_imageA,
            'image9B' : fashion_collection_document9_imageB,
            'image9C' : fashion_collection_document9_imageC,
            'image9D': fashion_collection_document9_imageD,
            'image9E': fashion_collection_document9_imageE,

            'productID10' : fashion_collection_document10_productID,
            'username10' : fashion_collection_document10_username,
            'state10' : fashion_collection_document10_state,
            'city10' : fashion_collection_document10_city,
            'description10' : fashion_collection_document10_description,
            'mobile10' : fashion_collection_document10_mobile,
            'email10' : fashion_collection_document10_email,
            'category10' : fashion_collection_document10_category,
            'condition10': fashion_collection_document10_condition,
            'image10A' : fashion_collection_document10_imageA,
            'image10B' : fashion_collection_document10_imageB,
            'image10C' : fashion_collection_document10_imageC,
            'image10D': fashion_collection_document10_imageD,
            'image10E': fashion_collection_document10_imageE,            
        }





    # *************************************************************************************************************
    # *************************************************************************************************************
    @view_config(route_name='fashion_viewProducts2_page3', renderer='templates/fashion_templates/fashion_viewProducts2_page3.pt')
    def fashion_viewProducts2_page3(self):
        import pymongo
        from pymongo import MongoClient
        import gridfs
        from gridfs import GridFS
        # Extract connection string from enviroment variables
        import os
        from dotenv import load_dotenv
        load_dotenv()
        connection_string = os.environ['MY_CONNECTION_STRING']
        # Open database connection and get or create a database called spacenetng_database
        import dns
        client3 = MongoClient('%s' % connection_string)
        db = client3.spacenetng_database

        # Create or open a text based records collection called fashion_text_collection
        text_collection_fashion = db.fashion_text_collection

        # Establish gridfs collection connection
        # Creating or getting an fashion gridfs collection called 'fashion_images_collection'
        # (Getting the GridFS object)
        image_collection_fashion = GridFS(db, "fashion_images_collection")

        # Retrieve document record from database operation
        fashion_collection = text_collection_fashion.find().sort([("_id", pymongo.DESCENDING)]).skip(10).limit(5) #This returns 25 records

        # Push documents into a list
        fashion_collection_list = []

        for record in fashion_collection:
            fashion_collection_list.append(record)



        document11 = fashion_collection_list[0]
        document12 = fashion_collection_list[1]
        document13 = fashion_collection_list[2]
        document14 = fashion_collection_list[3]
        document15 = fashion_collection_list[4]

        # Extracting images
        # The images for document11
        document11_images_list_rawFile = []
        for image_name in document11["Images"]:
            document11_images_list_rawFile.append(image_collection_fashion.get_last_version(filename=image_name))

        # The images for document12
        document12_images_list_rawFile = []
        for image_name in document12["Images"]:
            document12_images_list_rawFile.append(image_collection_fashion.get_last_version(filename=image_name))

        # The images for document13
        document13_images_list_rawFile = []
        for image_name in document13["Images"]:
            document13_images_list_rawFile.append(image_collection_fashion.get_last_version(filename=image_name))

        # The images for document14
        document14_images_list_rawFile = []
        for image_name in document14["Images"]:
            document14_images_list_rawFile.append(image_collection_fashion.get_last_version(filename=image_name))

        # The images for document15
        document15_images_list_rawFile = []
        for image_name in document15["Images"]:
            document15_images_list_rawFile.append(image_collection_fashion.get_last_version(filename=image_name))



        ##############################################
        # Collecting record from individual documents
        ##############################################
        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document11
        #######################

        # For the text strings,
        fashion_collection_document11_productID = document11["Product ID"]
        fashion_collection_document11_username = document11["Username"]
        fashion_collection_document11_state = document11["State"]
        fashion_collection_document11_city = document11["City"]
        fashion_collection_document11_description = document11["Description"]
        fashion_collection_document11_mobile = document11["Mobile"]
        fashion_collection_document11_email = document11["Email"]
        fashion_collection_document11_category = document11["Category"]
        fashion_collection_document11_condition = document11["Condition"]

        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document11_images_UTF8_list = []

        for raw_image in document11_images_list_rawFile:
            document11_binaryImage = raw_image.read()
            document11_base64Image = codecs.encode(document11_binaryImage, 'base64')
            document11_UTF8Image = document11_base64Image.decode('utf-8')
            document11_images_UTF8_list.append(document11_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        fashion_collection_document11_imageA = document11_images_UTF8_list[0]

        try:
            fashion_collection_document11_imageB = document11_images_UTF8_list[1]
        except:
            fashion_collection_document11_imageB = document11_images_UTF8_list[0]

        try:
            fashion_collection_document11_imageC = document11_images_UTF8_list[2]
        except:
            fashion_collection_document11_imageC = document11_images_UTF8_list[0]

        try:
            fashion_collection_document11_imageD = document11_images_UTF8_list[3]
        except:
            fashion_collection_document11_imageD = document11_images_UTF8_list[0]       
        
        try:
            fashion_collection_document11_imageE = document11_images_UTF8_list[4]
        except:
            fashion_collection_document11_imageE = document11_images_UTF8_list[0]





        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document12
        #######################

        # For the text strings,
        fashion_collection_document12_productID = document12["Product ID"]
        fashion_collection_document12_username = document12["Username"]
        fashion_collection_document12_state = document12["State"]
        fashion_collection_document12_city = document12["City"]
        fashion_collection_document12_description = document12["Description"]
        fashion_collection_document12_mobile = document12["Mobile"]
        fashion_collection_document12_email = document12["Email"]
        fashion_collection_document12_category = document12["Category"]
        fashion_collection_document12_condition = document12["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document12_images_UTF8_list = []

        for raw_image in document12_images_list_rawFile:
            document12_binaryImage = raw_image.read()
            document12_base64Image = codecs.encode(document12_binaryImage, 'base64')
            document12_UTF8Image = document12_base64Image.decode('utf-8')
            document12_images_UTF8_list.append(document12_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        fashion_collection_document12_imageA = document12_images_UTF8_list[0]

        try:
            fashion_collection_document12_imageB = document12_images_UTF8_list[1]
        except:
            fashion_collection_document12_imageB = document12_images_UTF8_list[0]

        try:
            fashion_collection_document12_imageC = document12_images_UTF8_list[2]
        except:
            fashion_collection_document12_imageC = document12_images_UTF8_list[0]

        try:
            fashion_collection_document12_imageD = document12_images_UTF8_list[3]
        except:
            fashion_collection_document12_imageD = document12_images_UTF8_list[0]       
        
        try:
            fashion_collection_document12_imageE = document12_images_UTF8_list[4]
        except:
            fashion_collection_document12_imageE = document12_images_UTF8_list[0]





        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document13
        #######################

        # For the text strings,
        fashion_collection_document13_productID = document13["Product ID"]
        fashion_collection_document13_username = document13["Username"]
        fashion_collection_document13_state = document13["State"]
        fashion_collection_document13_city = document13["City"]
        fashion_collection_document13_description = document13["Description"]
        fashion_collection_document13_mobile = document13["Mobile"]
        fashion_collection_document13_email = document13["Email"]
        fashion_collection_document13_category = document13["Category"]
        fashion_collection_document13_condition = document13["Condition"]

        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document13_images_UTF8_list = []

        for raw_image in document13_images_list_rawFile:
            document13_binaryImage = raw_image.read()
            document13_base64Image = codecs.encode(document13_binaryImage, 'base64')
            document13_UTF8Image = document13_base64Image.decode('utf-8')
            document13_images_UTF8_list.append(document13_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        fashion_collection_document13_imageA = document13_images_UTF8_list[0]

        try:
            fashion_collection_document13_imageB = document13_images_UTF8_list[1]
        except:
            fashion_collection_document13_imageB = document13_images_UTF8_list[0]

        try:
            fashion_collection_document13_imageC = document13_images_UTF8_list[2]
        except:
            fashion_collection_document13_imageC = document13_images_UTF8_list[0]

        try:
            fashion_collection_document13_imageD = document13_images_UTF8_list[3]
        except:
            fashion_collection_document13_imageD = document13_images_UTF8_list[0]       
        
        try:
            fashion_collection_document13_imageE = document13_images_UTF8_list[4]
        except:
            fashion_collection_document13_imageE = document13_images_UTF8_list[0]




        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document14
        #######################

        # For the text strings,
        fashion_collection_document14_productID = document14["Product ID"]
        fashion_collection_document14_username = document14["Username"]
        fashion_collection_document14_state = document14["State"]
        fashion_collection_document14_city = document14["City"]
        fashion_collection_document14_description = document14["Description"]
        fashion_collection_document14_mobile = document14["Mobile"]
        fashion_collection_document14_email = document14["Email"]
        fashion_collection_document14_category = document14["Category"]
        fashion_collection_document14_condition = document14["Condition"]

        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document14_images_UTF8_list = []

        for raw_image in document14_images_list_rawFile:
            document14_binaryImage = raw_image.read()
            document14_base64Image = codecs.encode(document14_binaryImage, 'base64')
            document14_UTF8Image = document14_base64Image.decode('utf-8')
            document14_images_UTF8_list.append(document14_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        fashion_collection_document14_imageA = document14_images_UTF8_list[0]

        try:
            fashion_collection_document14_imageB = document14_images_UTF8_list[1]
        except:
            fashion_collection_document14_imageB = document14_images_UTF8_list[0]

        try:
            fashion_collection_document14_imageC = document14_images_UTF8_list[2]
        except:
            fashion_collection_document14_imageC = document14_images_UTF8_list[0]

        try:
            fashion_collection_document14_imageD = document14_images_UTF8_list[3]
        except:
            fashion_collection_document14_imageD = document14_images_UTF8_list[0]       
        
        try:
            fashion_collection_document14_imageE = document14_images_UTF8_list[4]
        except:
            fashion_collection_document14_imageE = document14_images_UTF8_list[0]






        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document15
        #######################

        # For the text strings,
        fashion_collection_document15_productID = document15["Product ID"]
        fashion_collection_document15_username = document15["Username"]
        fashion_collection_document15_state = document15["State"]
        fashion_collection_document15_city = document15["City"]
        fashion_collection_document15_description = document15["Description"]
        fashion_collection_document15_mobile = document15["Mobile"]
        fashion_collection_document15_email = document15["Email"]
        fashion_collection_document15_category = document15["Category"]
        fashion_collection_document15_condition = document15["Condition"]



        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document15_images_UTF8_list = []

        for raw_image in document15_images_list_rawFile:
            document15_binaryImage = raw_image.read()
            document15_base64Image = codecs.encode(document15_binaryImage, 'base64')
            document15_UTF8Image = document15_base64Image.decode('utf-8')
            document15_images_UTF8_list.append(document15_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        fashion_collection_document15_imageA = document15_images_UTF8_list[0]

        try:
            fashion_collection_document15_imageB = document15_images_UTF8_list[1]
        except:
            fashion_collection_document15_imageB = document15_images_UTF8_list[0]

        try:
            fashion_collection_document15_imageC = document15_images_UTF8_list[2]
        except:
            fashion_collection_document15_imageC = document15_images_UTF8_list[0]

        try:
            fashion_collection_document15_imageD = document15_images_UTF8_list[3]
        except:
            fashion_collection_document15_imageD = document15_images_UTF8_list[0]       
        
        try:
            fashion_collection_document15_imageE = document15_images_UTF8_list[4]
        except:
            fashion_collection_document15_imageE = document15_images_UTF8_list[0]

        # Close our database connection and free up resources.
        client3.close()

        # Pack all return variables into a JSON Structure and use for return
        return{
            'productID11' : fashion_collection_document11_productID,
            'username11' : fashion_collection_document11_username,
            'state11' : fashion_collection_document11_state,
            'city11' : fashion_collection_document11_city,
            'description11' : fashion_collection_document11_description,
            'mobile11' : fashion_collection_document11_mobile,
            'email11' : fashion_collection_document11_email,
            'category11' : fashion_collection_document11_category,
            'condition11': fashion_collection_document11_condition,
            'image11A' : fashion_collection_document11_imageA,
            'image11B' : fashion_collection_document11_imageB,
            'image11C' : fashion_collection_document11_imageC,
            'image11D': fashion_collection_document11_imageD,
            'image11E': fashion_collection_document11_imageE,

            'productID12' : fashion_collection_document12_productID,
            'username12' : fashion_collection_document12_username,
            'state12' : fashion_collection_document12_state,
            'city12' : fashion_collection_document12_city,
            'description12' : fashion_collection_document12_description,
            'mobile12' : fashion_collection_document12_mobile,
            'email12' : fashion_collection_document12_email,
            'category12' : fashion_collection_document12_category,
            'condition12': fashion_collection_document12_condition,
            'image12A' : fashion_collection_document12_imageA,
            'image12B' : fashion_collection_document12_imageB,
            'image12C' : fashion_collection_document12_imageC,
            'image12D': fashion_collection_document12_imageD,
            'image12E': fashion_collection_document12_imageE,

            'productID13' : fashion_collection_document13_productID,
            'username13' : fashion_collection_document13_username,
            'state13' : fashion_collection_document13_state,
            'city13' : fashion_collection_document13_city,
            'description13' : fashion_collection_document13_description,
            'mobile13' : fashion_collection_document13_mobile,
            'email13' : fashion_collection_document13_email,
            'category13' : fashion_collection_document13_category,
            'condition13': fashion_collection_document13_condition,
            'image13A' : fashion_collection_document13_imageA,
            'image13B' : fashion_collection_document13_imageB,
            'image13C' : fashion_collection_document13_imageC,
            'image13D': fashion_collection_document13_imageD,
            'image13E': fashion_collection_document13_imageE,

            'productID14' : fashion_collection_document14_productID,
            'username14' : fashion_collection_document14_username,
            'state14' : fashion_collection_document14_state,
            'city14' : fashion_collection_document14_city,
            'description14' : fashion_collection_document14_description,
            'mobile14' : fashion_collection_document14_mobile,
            'email14' : fashion_collection_document14_email,
            'category14' : fashion_collection_document14_category,
            'condition14': fashion_collection_document14_condition,
            'image14A' : fashion_collection_document14_imageA,
            'image14B' : fashion_collection_document14_imageB,
            'image14C' : fashion_collection_document14_imageC,
            'image14D': fashion_collection_document14_imageD,
            'image14E': fashion_collection_document14_imageE,

            'productID15' : fashion_collection_document15_productID,
            'username15' : fashion_collection_document15_username,
            'state15' : fashion_collection_document15_state,
            'city15' : fashion_collection_document15_city,
            'description15' : fashion_collection_document15_description,
            'mobile15' : fashion_collection_document15_mobile,
            'email15' : fashion_collection_document15_email,
            'category15' : fashion_collection_document15_category,
            'condition15': fashion_collection_document15_condition,
            'image15A' : fashion_collection_document15_imageA,
            'image15B' : fashion_collection_document15_imageB,
            'image15C' : fashion_collection_document15_imageC,
            'image15D': fashion_collection_document15_imageD,
            'image15E': fashion_collection_document15_imageE,
        }


    # *************************************************************************************************************
    # *************************************************************************************************************        
    @view_config(route_name='fashion_viewProducts2_page4', renderer='templates/fashion_templates/fashion_viewProducts2_page4.pt')
    def fashion_viewProducts2_page4(self):
        import pymongo
        from pymongo import MongoClient
        import gridfs
        from gridfs import GridFS
        # Extract connection string from enviroment variables
        import os
        from dotenv import load_dotenv
        load_dotenv()
        connection_string = os.environ['MY_CONNECTION_STRING']
        # Open database connection and get or create a database called spacenetng_database
        import dns
        client4 = MongoClient('%s' % connection_string)
        db = client4.spacenetng_database

        # Create or open a text based records collection called fashion_text_collection
        text_collection_fashion = db.fashion_text_collection

        # Establish gridfs collection connection
        # Creating or getting an fashion gridfs collection called 'fashion_images_collection'
        # (Getting the GridFS object)
        image_collection_fashion = GridFS(db, "fashion_images_collection")

        # Retrieve document record from database operation
        fashion_collection = text_collection_fashion.find().sort([("_id", pymongo.DESCENDING)]).skip(15).limit(5) #This returns 25 records

        # Push documents into a list
        fashion_collection_list = []

        for record in fashion_collection:
            fashion_collection_list.append(record)

        document16 = fashion_collection_list[0]
        document17 = fashion_collection_list[1]
        document18 = fashion_collection_list[2]
        document19 = fashion_collection_list[3]
        document20 = fashion_collection_list[4]


        # Extracting images
        # The images for document16
        document16_images_list_rawFile = []
        for image_name in document16["Images"]:
            document16_images_list_rawFile.append(image_collection_fashion.get_last_version(filename=image_name))

        # The images for document17
        document17_images_list_rawFile = []
        for image_name in document17["Images"]:
            document17_images_list_rawFile.append(image_collection_fashion.get_last_version(filename=image_name))

        # The images for document18
        document18_images_list_rawFile = []
        for image_name in document18["Images"]:
            document18_images_list_rawFile.append(image_collection_fashion.get_last_version(filename=image_name))

        # The images for document19
        document19_images_list_rawFile = []
        for image_name in document19["Images"]:
            document19_images_list_rawFile.append(image_collection_fashion.get_last_version(filename=image_name))

        # The images for document20
        document20_images_list_rawFile = []
        for image_name in document20["Images"]:
            document20_images_list_rawFile.append(image_collection_fashion.get_last_version(filename=image_name))


        ##############################################
        # Collecting record from individual documents
        ##############################################
        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document16
        #######################

        # For the text strings,
        fashion_collection_document16_productID = document16["Product ID"]
        fashion_collection_document16_username = document16["Username"]
        fashion_collection_document16_state = document16["State"]
        fashion_collection_document16_city = document16["City"]
        fashion_collection_document16_description = document16["Description"]
        fashion_collection_document16_mobile = document16["Mobile"]
        fashion_collection_document16_email = document16["Email"]
        fashion_collection_document16_category = document16["Category"]
        fashion_collection_document16_condition = document16["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document16_images_UTF8_list = []

        for raw_image in document16_images_list_rawFile:
            document16_binaryImage = raw_image.read()
            document16_base64Image = codecs.encode(document16_binaryImage, 'base64')
            document16_UTF8Image = document16_base64Image.decode('utf-8')
            document16_images_UTF8_list.append(document16_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        fashion_collection_document16_imageA = document16_images_UTF8_list[0]

        try:
            fashion_collection_document16_imageB = document16_images_UTF8_list[1]
        except:
            fashion_collection_document16_imageB = document16_images_UTF8_list[0]

        try:
            fashion_collection_document16_imageC = document16_images_UTF8_list[2]
        except:
            fashion_collection_document16_imageC = document16_images_UTF8_list[0]

        try:
            fashion_collection_document16_imageD = document16_images_UTF8_list[3]
        except:
            fashion_collection_document16_imageD = document16_images_UTF8_list[0]       
        
        try:
            fashion_collection_document16_imageE = document16_images_UTF8_list[4]
        except:
            fashion_collection_document16_imageE = document16_images_UTF8_list[0]




        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document17
        #######################

        # For the text strings,
        fashion_collection_document17_productID = document17["Product ID"]
        fashion_collection_document17_username = document17["Username"]
        fashion_collection_document17_state = document17["State"]
        fashion_collection_document17_city = document17["City"]
        fashion_collection_document17_description = document17["Description"]
        fashion_collection_document17_mobile = document17["Mobile"]
        fashion_collection_document17_email = document17["Email"]
        fashion_collection_document17_category = document17["Category"]
        fashion_collection_document17_condition = document17["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document17_images_UTF8_list = []

        for raw_image in document17_images_list_rawFile:
            document17_binaryImage = raw_image.read()
            document17_base64Image = codecs.encode(document17_binaryImage, 'base64')
            document17_UTF8Image = document17_base64Image.decode('utf-8')
            document17_images_UTF8_list.append(document17_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        fashion_collection_document17_imageA = document17_images_UTF8_list[0]

        try:
            fashion_collection_document17_imageB = document17_images_UTF8_list[1]
        except:
            fashion_collection_document17_imageB = document17_images_UTF8_list[0]

        try:
            fashion_collection_document17_imageC = document17_images_UTF8_list[2]
        except:
            fashion_collection_document17_imageC = document17_images_UTF8_list[0]

        try:
            fashion_collection_document17_imageD = document17_images_UTF8_list[3]
        except:
            fashion_collection_document17_imageD = document17_images_UTF8_list[0]       
        
        try:
            fashion_collection_document17_imageE = document17_images_UTF8_list[4]
        except:
            fashion_collection_document17_imageE = document17_images_UTF8_list[0]





        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document18
        #######################

        # For the text strings,
        fashion_collection_document18_productID = document18["Product ID"]
        fashion_collection_document18_username = document18["Username"]
        fashion_collection_document18_state = document18["State"]
        fashion_collection_document18_city = document18["City"]
        fashion_collection_document18_description = document18["Description"]
        fashion_collection_document18_mobile = document18["Mobile"]
        fashion_collection_document18_email = document18["Email"]
        fashion_collection_document18_category = document18["Category"]
        fashion_collection_document18_condition = document18["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document18_images_UTF8_list = []

        for raw_image in document18_images_list_rawFile:
            document18_binaryImage = raw_image.read()
            document18_base64Image = codecs.encode(document18_binaryImage, 'base64')
            document18_UTF8Image = document18_base64Image.decode('utf-8')
            document18_images_UTF8_list.append(document18_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        fashion_collection_document18_imageA = document18_images_UTF8_list[0]

        try:
            fashion_collection_document18_imageB = document18_images_UTF8_list[1]
        except:
            fashion_collection_document18_imageB = document18_images_UTF8_list[0]

        try:
            fashion_collection_document18_imageC = document18_images_UTF8_list[2]
        except:
            fashion_collection_document18_imageC = document18_images_UTF8_list[0]

        try:
            fashion_collection_document18_imageD = document18_images_UTF8_list[3]
        except:
            fashion_collection_document18_imageD = document18_images_UTF8_list[0]       
        
        try:
            fashion_collection_document18_imageE = document18_images_UTF8_list[4]
        except:
            fashion_collection_document18_imageE = document18_images_UTF8_list[0]





        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document19
        #######################

        # For the text strings,
        fashion_collection_document19_productID = document19["Product ID"]
        fashion_collection_document19_username = document19["Username"]
        fashion_collection_document19_state = document19["State"]
        fashion_collection_document19_city = document19["City"]
        fashion_collection_document19_description = document19["Description"]
        fashion_collection_document19_mobile = document19["Mobile"]
        fashion_collection_document19_email = document19["Email"]
        fashion_collection_document19_category = document19["Category"]
        fashion_collection_document19_condition = document19["Condition"]

        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document19_images_UTF8_list = []

        for raw_image in document19_images_list_rawFile:
            document19_binaryImage = raw_image.read()
            document19_base64Image = codecs.encode(document19_binaryImage, 'base64')
            document19_UTF8Image = document19_base64Image.decode('utf-8')
            document19_images_UTF8_list.append(document19_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        fashion_collection_document19_imageA = document19_images_UTF8_list[0]

        try:
            fashion_collection_document19_imageB = document19_images_UTF8_list[1]
        except:
            fashion_collection_document19_imageB = document19_images_UTF8_list[0]

        try:
            fashion_collection_document19_imageC = document19_images_UTF8_list[2]
        except:
            fashion_collection_document19_imageC = document19_images_UTF8_list[0]

        try:
            fashion_collection_document19_imageD = document19_images_UTF8_list[3]
        except:
            fashion_collection_document19_imageD = document19_images_UTF8_list[0]       
        
        try:
            fashion_collection_document19_imageE = document19_images_UTF8_list[4]
        except:
            fashion_collection_document19_imageE = document19_images_UTF8_list[0]




        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document20
        #######################

        # For the text strings,
        fashion_collection_document20_productID = document20["Product ID"]
        fashion_collection_document20_username = document20["Username"]
        fashion_collection_document20_state = document20["State"]
        fashion_collection_document20_city = document20["City"]
        fashion_collection_document20_description = document20["Description"]
        fashion_collection_document20_mobile = document20["Mobile"]
        fashion_collection_document20_email = document20["Email"]
        fashion_collection_document20_category = document20["Category"]
        fashion_collection_document20_condition = document20["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document20_images_UTF8_list = []

        for raw_image in document20_images_list_rawFile:
            document20_binaryImage = raw_image.read()
            document20_base64Image = codecs.encode(document20_binaryImage, 'base64')
            document20_UTF8Image = document20_base64Image.decode('utf-8')
            document20_images_UTF8_list.append(document20_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        fashion_collection_document20_imageA = document20_images_UTF8_list[0]

        try:
            fashion_collection_document20_imageB = document20_images_UTF8_list[1]
        except:
            fashion_collection_document20_imageB = document20_images_UTF8_list[0]

        try:
            fashion_collection_document20_imageC = document20_images_UTF8_list[2]
        except:
            fashion_collection_document20_imageC = document20_images_UTF8_list[0]

        try:
            fashion_collection_document20_imageD = document20_images_UTF8_list[3]
        except:
            fashion_collection_document20_imageD = document20_images_UTF8_list[0]       
        
        try:
            fashion_collection_document20_imageE = document20_images_UTF8_list[4]
        except:
            fashion_collection_document20_imageE = document20_images_UTF8_list[0]


        # Close our database connection and free up resources.
        client4.close()

        # Pack all return variables into a JSON Structure and use for return
        return{
            'productID16' : fashion_collection_document16_productID,
            'username16' : fashion_collection_document16_username,
            'state16' : fashion_collection_document16_state,
            'city16' : fashion_collection_document16_city,
            'description16' : fashion_collection_document16_description,
            'mobile16' : fashion_collection_document16_mobile,
            'email16' : fashion_collection_document16_email,
            'category16' : fashion_collection_document16_category,
            'condition16': fashion_collection_document16_condition,
            'image16A' : fashion_collection_document16_imageA,
            'image16B' : fashion_collection_document16_imageB,
            'image16C' : fashion_collection_document16_imageC,
            'image16D': fashion_collection_document16_imageD,
            'image16E': fashion_collection_document16_imageE,

            'productID17' : fashion_collection_document17_productID,
            'username17' : fashion_collection_document17_username,
            'state17' : fashion_collection_document17_state,
            'city17' : fashion_collection_document17_city,
            'description17' : fashion_collection_document17_description,
            'mobile17' : fashion_collection_document17_mobile,
            'email17' : fashion_collection_document17_email,
            'category17' : fashion_collection_document17_category,
            'condition17': fashion_collection_document17_condition,
            'image17A' : fashion_collection_document17_imageA,
            'image17B' : fashion_collection_document17_imageB,
            'image17C' : fashion_collection_document17_imageC,
            'image17D': fashion_collection_document17_imageD,
            'image17E': fashion_collection_document17_imageE,

            'productID18' : fashion_collection_document18_productID,
            'username18' : fashion_collection_document18_username,
            'state18' : fashion_collection_document18_state,
            'city18' : fashion_collection_document18_city,
            'description18' : fashion_collection_document18_description,
            'mobile18' : fashion_collection_document18_mobile,
            'email18' : fashion_collection_document18_email,
            'category18' : fashion_collection_document18_category,
            'condition18': fashion_collection_document18_condition,
            'image18A' : fashion_collection_document18_imageA,
            'image18B' : fashion_collection_document18_imageB,
            'image18C' : fashion_collection_document18_imageC,
            'image18D': fashion_collection_document18_imageD,
            'image18E': fashion_collection_document18_imageE,

            'productID19' : fashion_collection_document19_productID,
            'username19' : fashion_collection_document19_username,
            'state19' : fashion_collection_document19_state,
            'city19' : fashion_collection_document19_city,
            'description19' : fashion_collection_document19_description,
            'mobile19' : fashion_collection_document19_mobile,
            'email19' : fashion_collection_document19_email,
            'category19' : fashion_collection_document19_category,
            'condition19': fashion_collection_document19_condition,
            'image19A' : fashion_collection_document19_imageA,
            'image19B' : fashion_collection_document19_imageB,
            'image19C' : fashion_collection_document19_imageC,
            'image19D': fashion_collection_document19_imageD,
            'image19E': fashion_collection_document19_imageE,

            'productID20' : fashion_collection_document20_productID,
            'username20' : fashion_collection_document20_username,
            'state20' : fashion_collection_document20_state,
            'city20' : fashion_collection_document20_city,
            'description20' : fashion_collection_document20_description,
            'mobile20' : fashion_collection_document20_mobile,
            'email20' : fashion_collection_document20_email,
            'category20' : fashion_collection_document20_category,
            'condition20': fashion_collection_document20_condition,
            'image20A' : fashion_collection_document20_imageA,
            'image20B' : fashion_collection_document20_imageB,
            'image20C' : fashion_collection_document20_imageC,
            'image20D': fashion_collection_document20_imageD,
            'image20E': fashion_collection_document20_imageE,
        }






    # *************************************************************************************************************
    # *************************************************************************************************************
    @view_config(route_name='fashion_viewProducts2_page5', renderer='templates/fashion_templates/fashion_viewProducts2_page5.pt')
    def fashion_viewProducts2_page5(self):
        import pymongo
        from pymongo import MongoClient
        import gridfs
        from gridfs import GridFS
        # Extract connection string from enviroment variables
        import os
        from dotenv import load_dotenv
        load_dotenv()
        connection_string = os.environ['MY_CONNECTION_STRING']
        # Open database connection and get or create a database called spacenetng_database
        import dns
        client5 = MongoClient('%s' % connection_string)
        db = client5.spacenetng_database

        # Create or open a text based records collection called fashion_text_collection
        text_collection_fashion = db.fashion_text_collection

        # Establish gridfs collection connection
        # Creating or getting an fashion gridfs collection called 'fashion_images_collection'
        # (Getting the GridFS object)
        image_collection_fashion = GridFS(db, "fashion_images_collection")

        # Retrieve document record from database operation
        fashion_collection = text_collection_fashion.find().sort([("_id", pymongo.DESCENDING)]).skip(20).limit(5) #This returns 25 records

        # Push documents into a list
        fashion_collection_list = []

        for record in fashion_collection:
            fashion_collection_list.append(record)

        document21 = fashion_collection_list[0]
        document22 = fashion_collection_list[1]
        document23 = fashion_collection_list[2]
        document24 = fashion_collection_list[3]
        document25 = fashion_collection_list[4]


        # Extracting images
        # The images for document21
        document21_images_list_rawFile = []
        for image_name in document21["Images"]:
            document21_images_list_rawFile.append(image_collection_fashion.get_last_version(filename=image_name))

        # The images for document22
        document22_images_list_rawFile = []
        for image_name in document22["Images"]:
            document22_images_list_rawFile.append(image_collection_fashion.get_last_version(filename=image_name))

        # The images for document23
        document23_images_list_rawFile = []
        for image_name in document23["Images"]:
            document23_images_list_rawFile.append(image_collection_fashion.get_last_version(filename=image_name))

        # The images for document24
        document24_images_list_rawFile = []
        for image_name in document24["Images"]:
            document24_images_list_rawFile.append(image_collection_fashion.get_last_version(filename=image_name))

        # The images for document25
        document25_images_list_rawFile = []
        for image_name in document25["Images"]:
            document25_images_list_rawFile.append(image_collection_fashion.get_last_version(filename=image_name))


        ##############################################
        # Collecting record from individual documents
        ##############################################
        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document21
        #######################

        # For the text strings,
        fashion_collection_document21_productID = document21["Product ID"]
        fashion_collection_document21_username = document21["Username"]
        fashion_collection_document21_state = document21["State"]
        fashion_collection_document21_city = document21["City"]
        fashion_collection_document21_description = document21["Description"]
        fashion_collection_document21_mobile = document21["Mobile"]
        fashion_collection_document21_email = document21["Email"]
        fashion_collection_document21_category = document21["Category"]
        fashion_collection_document21_condition = document21["Condition"]



        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document21_images_UTF8_list = []

        for raw_image in document21_images_list_rawFile:
            document21_binaryImage = raw_image.read()
            document21_base64Image = codecs.encode(document21_binaryImage, 'base64')
            document21_UTF8Image = document21_base64Image.decode('utf-8')
            document21_images_UTF8_list.append(document21_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        fashion_collection_document21_imageA = document21_images_UTF8_list[0]

        try:
            fashion_collection_document21_imageB = document21_images_UTF8_list[1]
        except:
            fashion_collection_document21_imageB = document21_images_UTF8_list[0]

        try:
            fashion_collection_document21_imageC = document21_images_UTF8_list[2]
        except:
            fashion_collection_document21_imageC = document21_images_UTF8_list[0]

        try:
            fashion_collection_document21_imageD = document21_images_UTF8_list[3]
        except:
            fashion_collection_document21_imageD = document21_images_UTF8_list[0]       
        
        try:
            fashion_collection_document21_imageE = document21_images_UTF8_list[4]
        except:
            fashion_collection_document21_imageE = document21_images_UTF8_list[0]





        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document22
        #######################

        # For the text strings,
        fashion_collection_document22_productID = document22["Product ID"]
        fashion_collection_document22_username = document22["Username"]
        fashion_collection_document22_state = document22["State"]
        fashion_collection_document22_city = document22["City"]
        fashion_collection_document22_description = document22["Description"]
        fashion_collection_document22_mobile = document22["Mobile"]
        fashion_collection_document22_email = document22["Email"]
        fashion_collection_document22_category = document22["Category"]
        fashion_collection_document22_condition = document22["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document22_images_UTF8_list = []

        for raw_image in document22_images_list_rawFile:
            document22_binaryImage = raw_image.read()
            document22_base64Image = codecs.encode(document22_binaryImage, 'base64')
            document22_UTF8Image = document22_base64Image.decode('utf-8')
            document22_images_UTF8_list.append(document22_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        fashion_collection_document22_imageA = document22_images_UTF8_list[0]

        try:
            fashion_collection_document22_imageB = document22_images_UTF8_list[1]
        except:
            fashion_collection_document22_imageB = document22_images_UTF8_list[0]

        try:
            fashion_collection_document22_imageC = document22_images_UTF8_list[2]
        except:
            fashion_collection_document22_imageC = document22_images_UTF8_list[0]

        try:
            fashion_collection_document22_imageD = document22_images_UTF8_list[3]
        except:
            fashion_collection_document22_imageD = document22_images_UTF8_list[0]       
        
        try:
            fashion_collection_document22_imageE = document22_images_UTF8_list[4]
        except:
            fashion_collection_document22_imageE = document22_images_UTF8_list[0]






        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document23
        #######################

        # For the text strings,
        fashion_collection_document23_productID = document23["Product ID"]
        fashion_collection_document23_username = document23["Username"]
        fashion_collection_document23_state = document23["State"]
        fashion_collection_document23_city = document23["City"]
        fashion_collection_document23_description = document23["Description"]
        fashion_collection_document23_mobile = document23["Mobile"]
        fashion_collection_document23_email = document23["Email"]
        fashion_collection_document23_category = document23["Category"]
        fashion_collection_document23_condition = document23["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document23_images_UTF8_list = []

        for raw_image in document23_images_list_rawFile:
            document23_binaryImage = raw_image.read()
            document23_base64Image = codecs.encode(document23_binaryImage, 'base64')
            document23_UTF8Image = document23_base64Image.decode('utf-8')
            document23_images_UTF8_list.append(document23_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        fashion_collection_document23_imageA = document23_images_UTF8_list[0]

        try:
            fashion_collection_document23_imageB = document23_images_UTF8_list[1]
        except:
            fashion_collection_document23_imageB = document23_images_UTF8_list[0]

        try:
            fashion_collection_document23_imageC = document23_images_UTF8_list[2]
        except:
            fashion_collection_document23_imageC = document23_images_UTF8_list[0]

        try:
            fashion_collection_document23_imageD = document23_images_UTF8_list[3]
        except:
            fashion_collection_document23_imageD = document23_images_UTF8_list[0]       
        
        try:
            fashion_collection_document23_imageE = document23_images_UTF8_list[4]
        except:
            fashion_collection_document23_imageE = document23_images_UTF8_list[0]





        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document24
        #######################

        # For the text strings,
        fashion_collection_document24_productID = document24["Product ID"]
        fashion_collection_document24_username = document24["Username"]
        fashion_collection_document24_state = document24["State"]
        fashion_collection_document24_city = document24["City"]
        fashion_collection_document24_description = document24["Description"]
        fashion_collection_document24_mobile = document24["Mobile"]
        fashion_collection_document24_email = document24["Email"]
        fashion_collection_document24_category = document24["Category"]
        fashion_collection_document24_condition = document24["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document24_images_UTF8_list = []

        for raw_image in document24_images_list_rawFile:
            document24_binaryImage = raw_image.read()
            document24_base64Image = codecs.encode(document24_binaryImage, 'base64')
            document24_UTF8Image = document24_base64Image.decode('utf-8')
            document24_images_UTF8_list.append(document24_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        fashion_collection_document24_imageA = document24_images_UTF8_list[0]

        try:
            fashion_collection_document24_imageB = document24_images_UTF8_list[1]
        except:
            fashion_collection_document24_imageB = document24_images_UTF8_list[0]

        try:
            fashion_collection_document24_imageC = document24_images_UTF8_list[2]
        except:
            fashion_collection_document24_imageC = document24_images_UTF8_list[0]

        try:
            fashion_collection_document24_imageD = document24_images_UTF8_list[3]
        except:
            fashion_collection_document24_imageD = document24_images_UTF8_list[0]       
        
        try:
            fashion_collection_document24_imageE = document24_images_UTF8_list[4]
        except:
            fashion_collection_document24_imageE = document24_images_UTF8_list[0]






        #######################//////////////////////////////////////////////////////////////////////////////////////////////
        # For document25
        #######################

        # For the text strings,
        fashion_collection_document25_productID = document25["Product ID"]
        fashion_collection_document25_username = document25["Username"]
        fashion_collection_document25_state = document25["State"]
        fashion_collection_document25_city = document25["City"]
        fashion_collection_document25_description = document25["Description"]
        fashion_collection_document25_mobile = document25["Mobile"]
        fashion_collection_document25_email = document25["Email"]
        fashion_collection_document25_category = document25["Category"]
        fashion_collection_document25_condition = document25["Condition"]


        # Images
        # Convert raw image into "UTF-8"(html) acceptable form
        import codecs
        document25_images_UTF8_list = []

        for raw_image in document25_images_list_rawFile:
            document25_binaryImage = raw_image.read()
            document25_base64Image = codecs.encode(document25_binaryImage, 'base64')
            document25_UTF8Image = document25_base64Image.decode('utf-8')
            document25_images_UTF8_list.append(document25_UTF8Image)


        # Hence, for the images our utf-8 images becomes,
        # Test for our variables, improvise in the cases for non-existence of
        # files in that index handle exceptions.

        fashion_collection_document25_imageA = document25_images_UTF8_list[0]

        try:
            fashion_collection_document25_imageB = document25_images_UTF8_list[1]
        except:
            fashion_collection_document25_imageB = document25_images_UTF8_list[0]

        try:
            fashion_collection_document25_imageC = document25_images_UTF8_list[2]
        except:
            fashion_collection_document25_imageC = document25_images_UTF8_list[0]

        try:
            fashion_collection_document25_imageD = document25_images_UTF8_list[3]
        except:
            fashion_collection_document25_imageD = document25_images_UTF8_list[0]       
        
        try:
            fashion_collection_document25_imageE = document25_images_UTF8_list[4]
        except:
            fashion_collection_document25_imageE = document25_images_UTF8_list[0]

        # Close our database connection and free up resources.
        client5.close()

        # Pack all return variables into a JSON Structure and use for return
        return{
            'productID21' : fashion_collection_document21_productID,
            'username21' : fashion_collection_document21_username,
            'state21' : fashion_collection_document21_state,
            'city21' : fashion_collection_document21_city,
            'description21' : fashion_collection_document21_description,
            'mobile21' : fashion_collection_document21_mobile,
            'email21' : fashion_collection_document21_email,
            'category21' : fashion_collection_document21_category,
            'condition21': fashion_collection_document21_condition,
            'image21A' : fashion_collection_document21_imageA,
            'image21B' : fashion_collection_document21_imageB,
            'image21C' : fashion_collection_document21_imageC,
            'image21D': fashion_collection_document21_imageD,
            'image21E': fashion_collection_document21_imageE,

            'productID22' : fashion_collection_document22_productID,
            'username22' : fashion_collection_document22_username,
            'state22' : fashion_collection_document22_state,
            'city22' : fashion_collection_document22_city,
            'description22' : fashion_collection_document22_description,
            'mobile22' : fashion_collection_document22_mobile,
            'email22' : fashion_collection_document22_email,
            'category22' : fashion_collection_document22_category,
            'condition22': fashion_collection_document22_condition,
            'image22A' : fashion_collection_document22_imageA,
            'image22B' : fashion_collection_document22_imageB,
            'image22C' : fashion_collection_document22_imageC,
            'image22D': fashion_collection_document22_imageD,
            'image22E': fashion_collection_document22_imageE,

            'productID23' : fashion_collection_document23_productID,
            'username23' : fashion_collection_document23_username,
            'state23' : fashion_collection_document23_state,
            'city23' : fashion_collection_document23_city,
            'description23' : fashion_collection_document23_description,
            'mobile23' : fashion_collection_document23_mobile,
            'email23' : fashion_collection_document23_email,
            'category23' : fashion_collection_document23_category,
            'condition23': fashion_collection_document23_condition,
            'image23A' : fashion_collection_document23_imageA,
            'image23B' : fashion_collection_document23_imageB,
            'image23C' : fashion_collection_document23_imageC,
            'image23D': fashion_collection_document23_imageD,
            'image23E': fashion_collection_document23_imageE,

            'productID24' : fashion_collection_document24_productID,
            'username24' : fashion_collection_document24_username,
            'state24' : fashion_collection_document24_state,
            'city24' : fashion_collection_document24_city,
            'description24' : fashion_collection_document24_description,
            'mobile24' : fashion_collection_document24_mobile,
            'email24' : fashion_collection_document24_email,
            'category24' : fashion_collection_document24_category,
            'condition24': fashion_collection_document24_condition,
            'image24A' : fashion_collection_document24_imageA,
            'image24B' : fashion_collection_document24_imageB,
            'image24C' : fashion_collection_document24_imageC,
            'image24D': fashion_collection_document24_imageD,
            'image24E': fashion_collection_document24_imageE,

            'productID25' : fashion_collection_document25_productID,
            'username25' : fashion_collection_document25_username,
            'state25' : fashion_collection_document25_state,
            'city25' : fashion_collection_document25_city,
            'description25' : fashion_collection_document25_description,
            'mobile25' : fashion_collection_document25_mobile,
            'email25' : fashion_collection_document25_email,
            'category25' : fashion_collection_document25_category,
            'condition25': fashion_collection_document25_condition,
            'image25A' : fashion_collection_document25_imageA,
            'image25B' : fashion_collection_document25_imageB,
            'image25C' : fashion_collection_document25_imageC,
            'image25D': fashion_collection_document25_imageD,
            'image25E': fashion_collection_document25_imageE,
        }

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
# SECUREYST VIEWS
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************

# ########################################################################################################################
# ########################################################################################################################
# ########################################################################################################################
# Signup
@view_defaults(route_name='secureystSignup')
class SecureystCreateAccount(object):
    def __init__(self, request):
        self.request = request

    # *************************************************************************************************************
    # *************************************************************************************************************
    @view_config(renderer='templates/secureyst_templates/secureystSignup.pt')
    def secureYst_signup(self):
        return {}

    # *************************************************************************************************************
    # *************************************************************************************************************
    @view_config(request_method='POST')
    def secureYst_signupResponse(self):
        from pyramid.httpexceptions import HTTPFound
        import pyramid.httpexceptions as exc

        # Collect variables from form fields
        # Get text items from form page
        secureyst_signup_bluetoothName = self.request.params['secureyst_signup_bluetoothName']
        secureyst_signup_password = self.request.params['secureyst_signup_password']
        secureyst_signup_city = self.request.params['secureyst_signup_city']
        secureyst_signup_mobile = self.request.params['secureyst_signup_mobile']
        secureyst_signup_email = self.request.params['secureyst_signup_email']


        # Create our RES API structure and push data to the RES
        secureyst_signup_resAPI_json = {
            "Bluetooth Name": "",
            "Password": "",
            "City": "",
            "Mobile": "",
            "date": "",
        }

        secureyst_signup_resAPI_json["Bluetooth Name"] = secureyst_signup_bluetoothName
        secureyst_signup_resAPI_json["Password"] = secureyst_signup_password
        secureyst_signup_resAPI_json["City"] = secureyst_signup_city
        secureyst_signup_resAPI_json["Mobile"] = secureyst_signup_mobile
        secureyst_signup_resAPI_json["Email"] = secureyst_signup_email



        # Initialise database connection and perform CRUD operation on text
        import pymongo
        from pymongo import MongoClient

        # Extract connection string from enviroment variables
        import os
        from dotenv import load_dotenv
        load_dotenv()
        connection_string = os.environ['MY_CONNECTION_STRING']

        # Open database connection and get or create a database called secureyst_database
        import dns
        client = MongoClient('%s' % connection_string)
        db = client.secureyst_database

        # Create or open a text based records collection called secureyst_text_collection
        secureyst_text_collection= db.secureyst_text_collection



        # # ############################################################################################
        # # Send private UUID to user's Email using login details and gmail server using inbuilt python email package
        import smtplib, os, sys
        from smtplib import SMTP
        from email.message import EmailMessage
        from dotenv import load_dotenv
        load_dotenv()

        try:
            email_content = ("""\
            Hello %s, thanks for signing up on our health platform, Please be advised, a private user UUID has been created for youand it should be kept confidential.\n
            Here is your Seceret hey: %s\n
            For support and enquiries please contact us via our contact details found on our contact page in our website.\n
            Thanks for using this service, we hope to serve you better!!.
            """
            % (secureyst_signup_bluetoothName, secureyst_signup_password)
            
            )

            msg = EmailMessage()
            msg.set_content(email_content)

            msg['Subject'] = 'Your secure password from Secureyst (Powered by Spacenetng.com)'
            msg['From'] = 'spacenetngbase@gmail.com'
            msg['To'] = secureyst_signup_email

            server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server_ssl.ehlo()

            email = os.environ['MY_EMAIL_ADDRESS']
            passWord = os.environ['MY_EMAIL_PASSWORD']

            server_ssl.login(email, passWord)
            server_ssl.send_message(msg)       
            server_ssl.quit()   # Terminate the SMTP session and free up resources       
            
            # Or And,
            # print('Message sent successfully!!')

        except:
            pass
            # Or
            # print X


        try:
            ######################################################
            res0 = secureyst_text_collection.find_one({'Bluetooth Name': secureyst_signup_bluetoothName})
            res1 = res0['Bluetooth Name']
            if res1 == secureyst_signup_bluetoothName:
                # Redirect user back to signup page                     
                body = (
                    "<html style=\"color: red; background-color: whitesmoke; \">"
                    "<head><meta http-equiv=\"refresh\" content=\"11;url=/secureyst/signup\"></head>"
                    "<body>"
                    "<h4>A user with same Bluetooth name is already registered on our COVID-19 Health platform "
                    "please try again and use another unique bluetooth identifier."
                    "<br />"
                    "You will be redirected shortly to the signup page to try again."
                    "</body>"
                    "</html>"
                )
                return Response(body)
            else:
                raise exc.HTTPBadRequest()
                    

        except:
            # Insert API into database and close our connected client's connection
            secureyst_text_collection.insert_one(secureyst_signup_resAPI_json)

            # Close our database connection and free up resources.
            client.close()
            

            # Redirect user back to the questionaire page                     
            body = (
                "<html style=\"color: green; background-color: whitesmoke; \">"
                "<head><meta http-equiv=\"refresh\" content=\"11;url=/secureyst/login\"></head>"
                "<body>"
                "<h4>Thanks for using our service, you have been successfully registered on our COVID-19 Health platform"
                "<br />"
                ".</h4>"
                "</body>"
                "</html>"
            )

            return Response(body)





# ########################################################################################################################
# ########################################################################################################################
# ########################################################################################################################
# Login
@view_defaults(route_name='secureystLogin')
class SecureystLogin(object):
    def __init__(self, request):
        self.request = request

    # *************************************************************************************************************
    # *************************************************************************************************************
    @view_config(renderer='templates/secureyst_templates/secureystLogin.pt')
    def secureYst_login(self):
        return {}

    # *************************************************************************************************************
    # *************************************************************************************************************
    @view_config(request_method='POST', renderer='json')
    def secureYst_loginResponse(self):
        # Initialise database connection and perform CRUD operation on text collection
        import pymongo
        from pymongo import MongoClient
        from bson import ObjectId

        # Extract connection string from enviroment variables
        import os
        from dotenv import load_dotenv
        load_dotenv()
        connection_string = os.environ['MY_CONNECTION_STRING']

        # Open database connection and get or create a database called secureyst_database
        import dns
        client = MongoClient('%s' % connection_string)
        db = client.secureyst_database

        # Create or open a text based records collection called secureyst_text_collection
        secureyst_text_collection = db.secureyst_text_collection

        # Obtain request parameters from login 
        secureyst_login_bluetoothName = self.request.params['secureyst_login_bluetoothName']
        secureyst_login_password = self.request.params['secureyst_login_password']


        # Obtain our JSON Response
        try:
            # Delete operation on the main text collection initialisation
            userPassword = secureyst_text_collection.find_one({'Password': secureyst_login_password})
            bluetoothName = secureyst_text_collection.find_one({'Bluetooth Name': secureyst_login_bluetoothName})

            # unneccessary query to doublecheck for BluetoothName existence with password
            bluetoothName1 = userPassword['Bluetooth Name']
            bluetoothName2 = bluetoothName['Bluetooth Name']

            # Close our database connection and free up resources.
            client.close()

            return {
                "Bluetooth Name1": bluetoothName1, "Bluetooth Name2": bluetoothName2,
            }


        except:
            body = (
                "<html style=\"color: red; background-color: whitesmoke; \">"
                "<body>"
                "<h4>No account found for this Bluetooth name and passsword, please try again with correct login details or kindly head back to the "
                "<a href=\"/secureyst/signup\">signup page</a>"
                "<br />"
                "and register.</h4>"
                "</body>"
                "</html>"
            )

            return Response(body)










# ########################################################################################################################
# ########################################################################################################################
# ########################################################################################################################
# Questionaire
@view_defaults(route_name='secureystQuestionaire')
class SecureystQuestionaire(object):
    def __init__(self, request):
        self.request = request

    # *************************************************************************************************************
    # *************************************************************************************************************
    @view_config(renderer='templates/secureyst_templates/secureystQuestionaire.pt')
    def secureYst_questionaire(self):
        return {}


    # *************************************************************************************************************
    # *************************************************************************************************************
    @view_config(request_method='POST')
    def secureYst_questionaireResponse(self):
        from pyramid.httpexceptions import HTTPFound

        # Collect variables from form fields
        # Get text items from form page
        secureyst_questionaire_passcode = self.request.params['secureyst_questionaire_passcode']
        secureyst_questionaire_international_travel_history = self.request.params['international_travel_history']
        secureyst_questionaire_fever= self.request.params['fever']
        secureyst_questionaire_breathing_difficulty = self.request.params['breathing_difficulty']
        secureyst_questionaire_body_pain = self.request.params['body_pain']
        secureyst_questionaire_fatigue_weakness = self.request.params['fatigue_weakness']
        secureyst_questionaire_sore_throat = self.request.params['sore_throat']
        secureyst_questionaire_cough = self.request.params['cough']
        secureyst_questionaire_diarrhoea = self.request.params['diarrhoea']
        secureyst_questionaire_other_medical_conditions = self.request.params['other_medical_conditions']
        secureyst_questionaire_48hrs_status = self.request.params['48hrs_status']
        secureyst_questionaire_age = self.request.params['age']


        markerList = [
            secureyst_questionaire_international_travel_history, secureyst_questionaire_fever,
            secureyst_questionaire_breathing_difficulty, secureyst_questionaire_body_pain,
            secureyst_questionaire_fatigue_weakness, secureyst_questionaire_sore_throat,
            secureyst_questionaire_cough, secureyst_questionaire_diarrhoea,
            secureyst_questionaire_other_medical_conditions, secureyst_questionaire_48hrs_status,
            secureyst_questionaire_age
        ]


        greenList = []
        yellowList = []
        redList = []

        # Create other backend variables
        # compute our covid19 status from captured data from questionaire
        for color in markerList:
            if color == 'green':
                greenList.append(color)
            elif color == 'yellow':
                yellowList.append(color)
            elif color == 'red':
                redList.append(color)

        if len(yellowList) > 3:
            secureyst_questionaire_COVID19_status_update = "Caution Zone"
        elif len(redList) > 0:
            secureyst_questionaire_COVID19_status_update = "Danger Zone"
        else:
            secureyst_questionaire_COVID19_status_update = "Safe Zone"


        # Get specific date
        import datetime
        secureyst_questionaire_dateTime = datetime.datetime.utcnow()

        # Create our RES API structure and push data to the RES
        secureyst_questionaire_resAPI_json = {
            "COVID-19 Status": "",
            "date": "",
        }

        # we are only updating the covid19 status
        secureyst_questionaire_resAPI_json["COVID-19 Status"] = secureyst_questionaire_COVID19_status_update
        secureyst_questionaire_resAPI_json["date"] = secureyst_questionaire_dateTime

        # Initialise database connection and perform CRUD operation on text collection
        import pymongo
        from pymongo import MongoClient
        from bson import ObjectId
        from uuid import UUID

        # Extract connection string from enviroment variables
        import os
        from dotenv import load_dotenv
        load_dotenv()
        connection_string = os.environ['MY_CONNECTION_STRING']

        # Open database connection and get or create a database called secureyst_database
        import dns
        client = MongoClient('%s' % connection_string)
        db = client.secureyst_database

        # Create or open a text based records collection called secureyst_text_collection
        secureyst_text_collection = db.secureyst_text_collection

        # Insert API into database and close our connected client's connection
        try:
            # Delete operation on the main text collection initialisation
            res0 = secureyst_text_collection.find_one({'Private UUID': UUID(secureyst_questionaire_passcode)})
            res1 = res0['_id']

            # Main text collection update
            secureyst_text_collection.update_one({'_id': ObjectId(res1)}, {"$set": secureyst_questionaire_resAPI_json})

            # Close our database connection and free up resources.
            client.close()

            body = (
                "<html style=\"color: green; background-color: whitesmoke; \">"
                "<body>"
                "<h4>Thanks for using our service, your questionaire status has been updated successfully!! "
                "<br />"
                "You can close this page and head back to our mobile app.</h4>"
                "</body>"
                "</html>"
            )

            return Response(body)


        except:
            body = (
                "<html style=\"color: red; background-color: whitesmoke; \">"
                "<body>"
                "<h4>No account has been created yet for you, please kindly head back to the "
                "<a href=\"/secureyst/signup\">signup page</a>"
                "<br />"
                "and register.</h4>"
                "</body>"
                "</html>"
            )

            return Response(body)












# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# AHSAN LISTINGS VIEWS
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************

# ########################################################################################################################
# ########################################################################################################################
# ########################################################################################################################
# Index
@view_defaults(route_name='ahsanListings')
class AhsanListingsIndex(object):
    def __init__(self, request):
        self.request = request

    # *************************************************************************************************************
    # *************************************************************************************************************
    @view_config(renderer='templates/ahsan_templates/index.pt')
    def ahsan_home(self):
        #################################################
        # Then connect to our database and extract document
        import pymongo
        from pymongo import MongoClient
        from bson import ObjectId

        # Extract connection string from enviroment variables
        import os
        from dotenv import load_dotenv
        load_dotenv()
        connection_string = os.environ['MY_CONNECTION_STRING']

        # Open database connection and get or create a database called ahsan_database
        import dns
        client = MongoClient('%s' % connection_string)
        db = client.ahsan_database

        # Create or open a text based records collection called category_text_collection
        category_text_collection = db.category_text_collection

        # Create or open a text based records collection called primarySubCategory_text_collection
        primarySubCategory_text_collection = db.primarySubCategory_text_collection

        # Create or open a text based records collection called secondarySubCategory_text_collection
        secondarySubCategory_text_collection = db.secondarySubCategory_text_collection


        # Extracting
        category_JSON = category_text_collection.find().sort([("_id", pymongo.ASCENDING)])
        primarySubCategory_JSON = primarySubCategory_text_collection.find().sort([("_id", pymongo.ASCENDING)])
        secondarySubCategory_JSON = secondarySubCategory_text_collection.find().sort([("_id", pymongo.ASCENDING)])

        # *********************************************************************************
        # Category Variables
        # Collecting variables for air conditionals
        category_AC_name = category_JSON[0]["CategoryNames"][0]
        category_AC_image = category_JSON[0]["CategoryImages"][0]
        category_AC_link = category_JSON[0]["CategoryLinks"][0]

        # Collecting variables for mobile phones
        category_mobile_name = category_JSON[0]["CategoryNames"][1]
        category_mobile_image = category_JSON[0]["CategoryImages"][1]
        category_mobile_link = category_JSON[0]["CategoryLinks"][1]

        # Collecting variables for televisions
        category_tv_name = category_JSON[0]["CategoryNames"][2]
        category_tv_image = category_JSON[0]["CategoryImages"][2]
        category_tv_link = category_JSON[0]["CategoryLinks"][2]

        # Collecting variables for refrigerators
        category_fridge_name = category_JSON[0]["CategoryNames"][3]
        category_fridge_image = category_JSON[0]["CategoryImages"][3]
        category_fridge_link = category_JSON[0]["CategoryLinks"][3]


        # *********************************************************************************
        # primarySubCategory Variables
        # variables1
        primarySubCategory_name1 = primarySubCategory_JSON[0]["PrimarySubCategoryNames"][0]
        primarySubCategory_image1 = primarySubCategory_JSON[0]["PrimarySubCategoryImages"][0]
        primarySubCategory_link1 = primarySubCategory_JSON[0]["PrimarySubCategoryLinks"][0]

        # variables2
        primarySubCategory_name2 = primarySubCategory_JSON[0]["PrimarySubCategoryNames"][1]
        primarySubCategory_image2 = primarySubCategory_JSON[0]["PrimarySubCategoryImages"][1]
        primarySubCategory_link2 = primarySubCategory_JSON[0]["PrimarySubCategoryLinks"][1]

        # variables3
        primarySubCategory_name3 = primarySubCategory_JSON[0]["PrimarySubCategoryNames"][2]
        primarySubCategory_image3 = primarySubCategory_JSON[0]["PrimarySubCategoryImages"][2]
        primarySubCategory_link3 = primarySubCategory_JSON[0]["PrimarySubCategoryLinks"][2]

        # variables4
        primarySubCategory_name4 = primarySubCategory_JSON[0]["PrimarySubCategoryNames"][3]
        primarySubCategory_image4 = primarySubCategory_JSON[0]["PrimarySubCategoryImages"][3]
        primarySubCategory_link4 = primarySubCategory_JSON[0]["PrimarySubCategoryLinks"][3]

        # variables5
        primarySubCategory_name5 = primarySubCategory_JSON[0]["PrimarySubCategoryNames"][4]
        primarySubCategory_image5 = primarySubCategory_JSON[0]["PrimarySubCategoryImages"][4]
        primarySubCategory_link5 = primarySubCategory_JSON[0]["PrimarySubCategoryLinks"][4]

        # variables6
        primarySubCategory_name6 = primarySubCategory_JSON[0]["PrimarySubCategoryNames"][5]
        primarySubCategory_image6 = primarySubCategory_JSON[0]["PrimarySubCategoryImages"][5]
        primarySubCategory_link6 = primarySubCategory_JSON[0]["PrimarySubCategoryLinks"][5]

        # variables7
        primarySubCategory_name7 = primarySubCategory_JSON[0]["PrimarySubCategoryNames"][6]
        primarySubCategory_image7 = primarySubCategory_JSON[0]["PrimarySubCategoryImages"][6]
        primarySubCategory_link7 = primarySubCategory_JSON[0]["PrimarySubCategoryLinks"][6]

        # variables8
        primarySubCategory_name8 = primarySubCategory_JSON[0]["PrimarySubCategoryNames"][7]
        primarySubCategory_image8 = primarySubCategory_JSON[0]["PrimarySubCategoryImages"][7]
        primarySubCategory_link8 = primarySubCategory_JSON[0]["PrimarySubCategoryLinks"][7]

        # variables9
        primarySubCategory_name9 = primarySubCategory_JSON[0]["PrimarySubCategoryNames"][8]
        primarySubCategory_image9 = primarySubCategory_JSON[0]["PrimarySubCategoryImages"][8]
        primarySubCategory_link9 = primarySubCategory_JSON[0]["PrimarySubCategoryLinks"][8]

        # variables10
        primarySubCategory_name10 = primarySubCategory_JSON[0]["PrimarySubCategoryNames"][9]
        primarySubCategory_image10 = primarySubCategory_JSON[0]["PrimarySubCategoryImages"][9]
        primarySubCategory_link10 = primarySubCategory_JSON[0]["PrimarySubCategoryLinks"][9]

        # variables11
        primarySubCategory_name11 = primarySubCategory_JSON[0]["PrimarySubCategoryNames"][10]
        primarySubCategory_image11 = primarySubCategory_JSON[0]["PrimarySubCategoryImages"][10]
        primarySubCategory_link11 = primarySubCategory_JSON[0]["PrimarySubCategoryLinks"][10]

        # variables12
        primarySubCategory_name12 = primarySubCategory_JSON[0]["PrimarySubCategoryNames"][11]
        primarySubCategory_image12 = primarySubCategory_JSON[0]["PrimarySubCategoryImages"][11]
        primarySubCategory_link12 = primarySubCategory_JSON[0]["PrimarySubCategoryLinks"][11]

        # variables13
        primarySubCategory_name13 = primarySubCategory_JSON[0]["PrimarySubCategoryNames"][12]
        primarySubCategory_image13 = primarySubCategory_JSON[0]["PrimarySubCategoryImages"][12]
        primarySubCategory_link13 = primarySubCategory_JSON[0]["PrimarySubCategoryLinks"][12]        

        # variables14
        primarySubCategory_name14 = primarySubCategory_JSON[0]["PrimarySubCategoryNames"][13]
        primarySubCategory_image14 = primarySubCategory_JSON[0]["PrimarySubCategoryImages"][13]
        primarySubCategory_link14 = primarySubCategory_JSON[0]["PrimarySubCategoryLinks"][13]

        # variables15
        primarySubCategory_name15 = primarySubCategory_JSON[0]["PrimarySubCategoryNames"][14]
        primarySubCategory_image15 = primarySubCategory_JSON[0]["PrimarySubCategoryImages"][14]
        primarySubCategory_link15 = primarySubCategory_JSON[0]["PrimarySubCategoryLinks"][14]

        # variables16
        primarySubCategory_name16 = primarySubCategory_JSON[0]["PrimarySubCategoryNames"][15]
        primarySubCategory_image16 = primarySubCategory_JSON[0]["PrimarySubCategoryImages"][15]
        primarySubCategory_link16 = primarySubCategory_JSON[0]["PrimarySubCategoryLinks"][15]




        # *********************************************************************************
        # secondarySubCategory Variables
        # variables1
        secondarySubCategory_name1 = secondarySubCategory_JSON[0]["SecondarySubCategoryNames"][0]
        secondarySubCategory_image1 = secondarySubCategory_JSON[0]["SecondarySubCategoryImages"][0]
        secondarySubCategory_link1 = secondarySubCategory_JSON[0]["SecondarySubCategoryLinks"][0]
        secondarySubCategory_price1 = secondarySubCategory_JSON[0]["SecondarySubCategoryPrice"][0]

        # variables2
        secondarySubCategory_name2 = secondarySubCategory_JSON[0]["SecondarySubCategoryNames"][1]
        secondarySubCategory_image2 = secondarySubCategory_JSON[0]["SecondarySubCategoryImages"][1]
        secondarySubCategory_link2 = secondarySubCategory_JSON[0]["SecondarySubCategoryLinks"][1]
        secondarySubCategory_price2 = secondarySubCategory_JSON[0]["SecondarySubCategoryPrice"][1]

        # variables3
        secondarySubCategory_name3 = secondarySubCategory_JSON[0]["SecondarySubCategoryNames"][2]
        secondarySubCategory_image3 = secondarySubCategory_JSON[0]["SecondarySubCategoryImages"][2]
        secondarySubCategory_link3 = secondarySubCategory_JSON[0]["SecondarySubCategoryLinks"][2]
        secondarySubCategory_price3 = secondarySubCategory_JSON[0]["SecondarySubCategoryPrice"][2]

        # variables4
        secondarySubCategory_name4 = secondarySubCategory_JSON[0]["SecondarySubCategoryNames"][3]
        secondarySubCategory_image4 = secondarySubCategory_JSON[0]["SecondarySubCategoryImages"][3]
        secondarySubCategory_link4 = secondarySubCategory_JSON[0]["SecondarySubCategoryLinks"][3]
        secondarySubCategory_price4 = secondarySubCategory_JSON[0]["SecondarySubCategoryPrice"][3]

        # variables5
        secondarySubCategory_name5 = secondarySubCategory_JSON[0]["SecondarySubCategoryNames"][4]
        secondarySubCategory_image5 = secondarySubCategory_JSON[0]["SecondarySubCategoryImages"][4]
        secondarySubCategory_link5 = secondarySubCategory_JSON[0]["SecondarySubCategoryLinks"][4]
        secondarySubCategory_price5 = secondarySubCategory_JSON[0]["SecondarySubCategoryPrice"][4]

        # variables6
        secondarySubCategory_name6 = secondarySubCategory_JSON[0]["SecondarySubCategoryNames"][5]
        secondarySubCategory_image6 = secondarySubCategory_JSON[0]["SecondarySubCategoryImages"][5]
        secondarySubCategory_link6 = secondarySubCategory_JSON[0]["SecondarySubCategoryLinks"][5]
        secondarySubCategory_price6 = secondarySubCategory_JSON[0]["SecondarySubCategoryPrice"][5]

        # variables7
        secondarySubCategory_name7 = secondarySubCategory_JSON[0]["SecondarySubCategoryNames"][6]
        secondarySubCategory_image7 = secondarySubCategory_JSON[0]["SecondarySubCategoryImages"][6]
        secondarySubCategory_link7 = secondarySubCategory_JSON[0]["SecondarySubCategoryLinks"][6]
        secondarySubCategory_price7 = secondarySubCategory_JSON[0]["SecondarySubCategoryPrice"][6]

        # variables8
        secondarySubCategory_name8 = secondarySubCategory_JSON[0]["SecondarySubCategoryNames"][7]
        secondarySubCategory_image8 = secondarySubCategory_JSON[0]["SecondarySubCategoryImages"][7]
        secondarySubCategory_link8 = secondarySubCategory_JSON[0]["SecondarySubCategoryLinks"][7]
        secondarySubCategory_price8 = secondarySubCategory_JSON[0]["SecondarySubCategoryPrice"][7]

        # variables9
        secondarySubCategory_name9 = secondarySubCategory_JSON[0]["SecondarySubCategoryNames"][8]
        secondarySubCategory_image9 = secondarySubCategory_JSON[0]["SecondarySubCategoryImages"][8]
        secondarySubCategory_link9 = secondarySubCategory_JSON[0]["SecondarySubCategoryLinks"][8]
        secondarySubCategory_price9 = secondarySubCategory_JSON[0]["SecondarySubCategoryPrice"][8]

        # variables10
        secondarySubCategory_name10 = secondarySubCategory_JSON[0]["SecondarySubCategoryNames"][9]
        secondarySubCategory_image10 = secondarySubCategory_JSON[0]["SecondarySubCategoryImages"][9]
        secondarySubCategory_link10 = secondarySubCategory_JSON[0]["SecondarySubCategoryLinks"][9]
        secondarySubCategory_price10 = secondarySubCategory_JSON[0]["SecondarySubCategoryPrice"][9]

        # variables11
        secondarySubCategory_name11 = secondarySubCategory_JSON[0]["SecondarySubCategoryNames"][10]
        secondarySubCategory_image11 = secondarySubCategory_JSON[0]["SecondarySubCategoryImages"][10]
        secondarySubCategory_link11 = secondarySubCategory_JSON[0]["SecondarySubCategoryLinks"][10]
        secondarySubCategory_price11 = secondarySubCategory_JSON[0]["SecondarySubCategoryPrice"][10]

        # variables12
        secondarySubCategory_name12 = secondarySubCategory_JSON[0]["SecondarySubCategoryNames"][11]
        secondarySubCategory_image12 = secondarySubCategory_JSON[0]["SecondarySubCategoryImages"][11]
        secondarySubCategory_link12 = secondarySubCategory_JSON[0]["SecondarySubCategoryLinks"][11]
        secondarySubCategory_price12 = secondarySubCategory_JSON[0]["SecondarySubCategoryPrice"][11]

        # variables13
        secondarySubCategory_name13 = secondarySubCategory_JSON[0]["SecondarySubCategoryNames"][12]
        secondarySubCategory_image13 = secondarySubCategory_JSON[0]["SecondarySubCategoryImages"][12]
        secondarySubCategory_link13 = secondarySubCategory_JSON[0]["SecondarySubCategoryLinks"][12]
        secondarySubCategory_price13 = secondarySubCategory_JSON[0]["SecondarySubCategoryPrice"][12]

        # variables14
        secondarySubCategory_name14 = secondarySubCategory_JSON[0]["SecondarySubCategoryNames"][13]
        secondarySubCategory_image14 = secondarySubCategory_JSON[0]["SecondarySubCategoryImages"][13]
        secondarySubCategory_link14 = secondarySubCategory_JSON[0]["SecondarySubCategoryLinks"][13]
        secondarySubCategory_price14 = secondarySubCategory_JSON[0]["SecondarySubCategoryPrice"][13]

        # variables15
        secondarySubCategory_name15 = secondarySubCategory_JSON[0]["SecondarySubCategoryNames"][14]
        secondarySubCategory_image15 = secondarySubCategory_JSON[0]["SecondarySubCategoryImages"][14]
        secondarySubCategory_link15 = secondarySubCategory_JSON[0]["SecondarySubCategoryLinks"][14]
        secondarySubCategory_price15 = secondarySubCategory_JSON[0]["SecondarySubCategoryPrice"][14]

        # variables16
        secondarySubCategory_name16 = secondarySubCategory_JSON[0]["SecondarySubCategoryNames"][15]
        secondarySubCategory_image16 = secondarySubCategory_JSON[0]["SecondarySubCategoryImages"][15]
        secondarySubCategory_link16 = secondarySubCategory_JSON[0]["SecondarySubCategoryLinks"][15]
        secondarySubCategory_price16 = secondarySubCategory_JSON[0]["SecondarySubCategoryPrice"][15]

        # variables17
        secondarySubCategory_name17 = secondarySubCategory_JSON[0]["SecondarySubCategoryNames"][16]
        secondarySubCategory_image17 = secondarySubCategory_JSON[0]["SecondarySubCategoryImages"][16]
        secondarySubCategory_link17 = secondarySubCategory_JSON[0]["SecondarySubCategoryLinks"][16]
        secondarySubCategory_price17 = secondarySubCategory_JSON[0]["SecondarySubCategoryPrice"][16]

        # variables18
        secondarySubCategory_name18 = secondarySubCategory_JSON[0]["SecondarySubCategoryNames"][17]
        secondarySubCategory_image18 = secondarySubCategory_JSON[0]["SecondarySubCategoryImages"][17]
        secondarySubCategory_link18 = secondarySubCategory_JSON[0]["SecondarySubCategoryLinks"][17]
        secondarySubCategory_price18 = secondarySubCategory_JSON[0]["SecondarySubCategoryPrice"][17]

        # variables19
        secondarySubCategory_name19 = secondarySubCategory_JSON[0]["SecondarySubCategoryNames"][18]
        secondarySubCategory_image19 = secondarySubCategory_JSON[0]["SecondarySubCategoryImages"][18]
        secondarySubCategory_link19 = secondarySubCategory_JSON[0]["SecondarySubCategoryLinks"][18]
        secondarySubCategory_price19 = secondarySubCategory_JSON[0]["SecondarySubCategoryPrice"][18]

        # variables20
        secondarySubCategory_name20 = secondarySubCategory_JSON[0]["SecondarySubCategoryNames"][19]
        secondarySubCategory_image20 = secondarySubCategory_JSON[0]["SecondarySubCategoryImages"][19]
        secondarySubCategory_link20 = secondarySubCategory_JSON[0]["SecondarySubCategoryLinks"][19]
        secondarySubCategory_price20 = secondarySubCategory_JSON[0]["SecondarySubCategoryPrice"][19]

        # variables21
        secondarySubCategory_name21 = secondarySubCategory_JSON[0]["SecondarySubCategoryNames"][20]
        secondarySubCategory_image21 = secondarySubCategory_JSON[0]["SecondarySubCategoryImages"][20]
        secondarySubCategory_link21 = secondarySubCategory_JSON[0]["SecondarySubCategoryLinks"][20]
        secondarySubCategory_price21 = secondarySubCategory_JSON[0]["SecondarySubCategoryPrice"][20]

        # variables22
        secondarySubCategory_name22 = secondarySubCategory_JSON[0]["SecondarySubCategoryNames"][21]
        secondarySubCategory_image22 = secondarySubCategory_JSON[0]["SecondarySubCategoryImages"][21]
        secondarySubCategory_link22 = secondarySubCategory_JSON[0]["SecondarySubCategoryLinks"][21]
        secondarySubCategory_price22 = secondarySubCategory_JSON[0]["SecondarySubCategoryPrice"][21]

        # variables23
        secondarySubCategory_name23 = secondarySubCategory_JSON[0]["SecondarySubCategoryNames"][22]
        secondarySubCategory_image23 = secondarySubCategory_JSON[0]["SecondarySubCategoryImages"][22]
        secondarySubCategory_link23 = secondarySubCategory_JSON[0]["SecondarySubCategoryLinks"][22]
        secondarySubCategory_price23 = secondarySubCategory_JSON[0]["SecondarySubCategoryPrice"][22]

        # variables24
        secondarySubCategory_name24 = secondarySubCategory_JSON[0]["SecondarySubCategoryNames"][23]
        secondarySubCategory_image24 = secondarySubCategory_JSON[0]["SecondarySubCategoryImages"][23]
        secondarySubCategory_link24 = secondarySubCategory_JSON[0]["SecondarySubCategoryLinks"][23]
        secondarySubCategory_price24 = secondarySubCategory_JSON[0]["SecondarySubCategoryPrice"][23]

        # variables25
        secondarySubCategory_name25 = secondarySubCategory_JSON[0]["SecondarySubCategoryNames"][24]
        secondarySubCategory_image25 = secondarySubCategory_JSON[0]["SecondarySubCategoryImages"][24]
        secondarySubCategory_link25 = secondarySubCategory_JSON[0]["SecondarySubCategoryLinks"][24]
        secondarySubCategory_price25 = secondarySubCategory_JSON[0]["SecondarySubCategoryPrice"][24]

        # variables26
        secondarySubCategory_name26 = secondarySubCategory_JSON[0]["SecondarySubCategoryNames"][25]
        secondarySubCategory_image26 = secondarySubCategory_JSON[0]["SecondarySubCategoryImages"][25]
        secondarySubCategory_link26 = secondarySubCategory_JSON[0]["SecondarySubCategoryLinks"][25]
        secondarySubCategory_price26 = secondarySubCategory_JSON[0]["SecondarySubCategoryPrice"][25]


        # Close our connection and free up some resources 
        client.close()
        return {
            # Category dictionairies
            "category_AC_name": category_AC_name,
            "category_AC_image": category_AC_image,
            "category_AC_link": category_AC_link,

            "category_mobile_name": category_mobile_name,
            "category_mobile_image": category_mobile_image,
            "category_mobile_link": category_mobile_link,
            
            "category_tv_name": category_tv_name,
            "category_tv_image": category_tv_image,
            "category_tv_link": category_tv_link,

            "category_fridge_name": category_fridge_name,
            "category_fridge_image": category_fridge_image,
            "category_fridge_link": category_fridge_link,

            # For primary subccategories
            "primarySubCategory_name1": primarySubCategory_name1,
            "primarySubCategory_image1": primarySubCategory_image1,
            "primarySubCategory_link1": primarySubCategory_link1,

            "primarySubCategory_name2": primarySubCategory_name2,
            "primarySubCategory_image2": primarySubCategory_image2,
            "primarySubCategory_link2": primarySubCategory_link2,

            "primarySubCategory_name3": primarySubCategory_name3,
            "primarySubCategory_image3": primarySubCategory_image3,
            "primarySubCategory_link3": primarySubCategory_link3,

            "primarySubCategory_name4": primarySubCategory_name4,
            "primarySubCategory_image4": primarySubCategory_image4,
            "primarySubCategory_link4": primarySubCategory_link4,

            "primarySubCategory_name5": primarySubCategory_name5,
            "primarySubCategory_image5": primarySubCategory_image5,
            "primarySubCategory_link5": primarySubCategory_link5,

            "primarySubCategory_name6": primarySubCategory_name6,
            "primarySubCategory_image6": primarySubCategory_image6,
            "primarySubCategory_link6": primarySubCategory_link6,

            "primarySubCategory_name7": primarySubCategory_name7,
            "primarySubCategory_image7": primarySubCategory_image7,
            "primarySubCategory_link7": primarySubCategory_link7,

            "primarySubCategory_name8": primarySubCategory_name8,
            "primarySubCategory_image8": primarySubCategory_image8,
            "primarySubCategory_link8": primarySubCategory_link8,

            "primarySubCategory_name9": primarySubCategory_name9,
            "primarySubCategory_image9": primarySubCategory_image9,
            "primarySubCategory_link9": primarySubCategory_link9,

            "primarySubCategory_name10": primarySubCategory_name10,
            "primarySubCategory_image10": primarySubCategory_image10,
            "primarySubCategory_link10": primarySubCategory_link10,

            "primarySubCategory_name11": primarySubCategory_name11,
            "primarySubCategory_image11": primarySubCategory_image11,
            "primarySubCategory_link11": primarySubCategory_link11,

            "primarySubCategory_name12": primarySubCategory_name12,
            "primarySubCategory_image12": primarySubCategory_image12,
            "primarySubCategory_link12": primarySubCategory_link12,

            "primarySubCategory_name13": primarySubCategory_name13,
            "primarySubCategory_image13": primarySubCategory_image13,
            "primarySubCategory_link13": primarySubCategory_link13,

            "primarySubCategory_name14": primarySubCategory_name14,
            "primarySubCategory_image14": primarySubCategory_image14,
            "primarySubCategory_link14": primarySubCategory_link14,

            "primarySubCategory_name15": primarySubCategory_name15,
            "primarySubCategory_image15": primarySubCategory_image15,
            "primarySubCategory_link15": primarySubCategory_link15,

            "primarySubCategory_name16": primarySubCategory_name16,
            "primarySubCategory_image16": primarySubCategory_image16,
            "primarySubCategory_link16": primarySubCategory_link16,


            # For secondary subccategories
            "secondarySubCategory_name1": secondarySubCategory_name1,
            "secondarySubCategory_image1": secondarySubCategory_image1,
            "secondarySubCategory_link1": secondarySubCategory_link1,
            "secondarySubCategory_price1": secondarySubCategory_price1,

            "secondarySubCategory_name2": secondarySubCategory_name2,
            "secondarySubCategory_image2": secondarySubCategory_image2,
            "secondarySubCategory_link2": secondarySubCategory_link2,
            "secondarySubCategory_price2": secondarySubCategory_price2,

            "secondarySubCategory_name3": secondarySubCategory_name3,
            "secondarySubCategory_image3": secondarySubCategory_image3,
            "secondarySubCategory_link3": secondarySubCategory_link3,
            "secondarySubCategory_price3": secondarySubCategory_price3,

            "secondarySubCategory_name4": secondarySubCategory_name4,
            "secondarySubCategory_image4": secondarySubCategory_image4,
            "secondarySubCategory_link4": secondarySubCategory_link4,
            "secondarySubCategory_price4": secondarySubCategory_price4,

            "secondarySubCategory_name5": secondarySubCategory_name5,
            "secondarySubCategory_image5": secondarySubCategory_image5,
            "secondarySubCategory_link5": secondarySubCategory_link5,
            "secondarySubCategory_price5": secondarySubCategory_price5,

            "secondarySubCategory_name6": secondarySubCategory_name6,
            "secondarySubCategory_image6": secondarySubCategory_image6,
            "secondarySubCategory_link6": secondarySubCategory_link6,
            "secondarySubCategory_price6": secondarySubCategory_price6,

            "secondarySubCategory_name7": secondarySubCategory_name7,
            "secondarySubCategory_image7": secondarySubCategory_image7,
            "secondarySubCategory_link7": secondarySubCategory_link7,
            "secondarySubCategory_price7": secondarySubCategory_price7,

            "secondarySubCategory_name8": secondarySubCategory_name8,
            "secondarySubCategory_image8": secondarySubCategory_image8,
            "secondarySubCategory_link8": secondarySubCategory_link8,
            "secondarySubCategory_price8": secondarySubCategory_price8,

            "secondarySubCategory_name9": secondarySubCategory_name9,
            "secondarySubCategory_image9": secondarySubCategory_image9,
            "secondarySubCategory_link9": secondarySubCategory_link9,
            "secondarySubCategory_price9": secondarySubCategory_price9,

            "secondarySubCategory_name10": secondarySubCategory_name10,
            "secondarySubCategory_image10": secondarySubCategory_image10,
            "secondarySubCategory_link10": secondarySubCategory_link10,
            "secondarySubCategory_price10": secondarySubCategory_price10,

            "secondarySubCategory_name11": secondarySubCategory_name11,
            "secondarySubCategory_image11": secondarySubCategory_image11,
            "secondarySubCategory_link11": secondarySubCategory_link11,
            "secondarySubCategory_price11": secondarySubCategory_price11,

            "secondarySubCategory_name12": secondarySubCategory_name12,
            "secondarySubCategory_image12": secondarySubCategory_image12,
            "secondarySubCategory_link12": secondarySubCategory_link12,
            "secondarySubCategory_price12": secondarySubCategory_price12,

            "secondarySubCategory_name13": secondarySubCategory_name13,
            "secondarySubCategory_image13": secondarySubCategory_image13,
            "secondarySubCategory_link13": secondarySubCategory_link13,
            "secondarySubCategory_price13": secondarySubCategory_price13,

            "secondarySubCategory_name14": secondarySubCategory_name14,
            "secondarySubCategory_image14": secondarySubCategory_image14,
            "secondarySubCategory_link14": secondarySubCategory_link14,
            "secondarySubCategory_price14": secondarySubCategory_price14,

            "secondarySubCategory_name15": secondarySubCategory_name15,
            "secondarySubCategory_image15": secondarySubCategory_image15,
            "secondarySubCategory_link15": secondarySubCategory_link15,
            "secondarySubCategory_price15": secondarySubCategory_price15,

            "secondarySubCategory_name16": secondarySubCategory_name16,
            "secondarySubCategory_image16": secondarySubCategory_image16,
            "secondarySubCategory_link16": secondarySubCategory_link16,
            "secondarySubCategory_price16": secondarySubCategory_price16,

            "secondarySubCategory_name17": secondarySubCategory_name17,
            "secondarySubCategory_image17": secondarySubCategory_image17,
            "secondarySubCategory_link17": secondarySubCategory_link17,
            "secondarySubCategory_price17": secondarySubCategory_price17,

            "secondarySubCategory_name18": secondarySubCategory_name18,
            "secondarySubCategory_image18": secondarySubCategory_image18,
            "secondarySubCategory_link18": secondarySubCategory_link18,
            "secondarySubCategory_price18": secondarySubCategory_price18,

            "secondarySubCategory_name19": secondarySubCategory_name19,
            "secondarySubCategory_image19": secondarySubCategory_image19,
            "secondarySubCategory_link19": secondarySubCategory_link19,
            "secondarySubCategory_price19": secondarySubCategory_price19,

            "secondarySubCategory_name20": secondarySubCategory_name20,
            "secondarySubCategory_image20": secondarySubCategory_image20,
            "secondarySubCategory_link20": secondarySubCategory_link20,
            "secondarySubCategory_price20": secondarySubCategory_price20,

            "secondarySubCategory_name21": secondarySubCategory_name21,
            "secondarySubCategory_image21": secondarySubCategory_image21,
            "secondarySubCategory_link21": secondarySubCategory_link21,
            "secondarySubCategory_price21": secondarySubCategory_price21,

            "secondarySubCategory_name22": secondarySubCategory_name22,
            "secondarySubCategory_image22": secondarySubCategory_image22,
            "secondarySubCategory_link22": secondarySubCategory_link22,
            "secondarySubCategory_price22": secondarySubCategory_price22,

            "secondarySubCategory_name23": secondarySubCategory_name23,
            "secondarySubCategory_image23": secondarySubCategory_image23,
            "secondarySubCategory_link23": secondarySubCategory_link23,
            "secondarySubCategory_price23": secondarySubCategory_price23,

            "secondarySubCategory_name24": secondarySubCategory_name24,
            "secondarySubCategory_image24": secondarySubCategory_image24,
            "secondarySubCategory_link24": secondarySubCategory_link24,
            "secondarySubCategory_price24": secondarySubCategory_price24,

            "secondarySubCategory_name25": secondarySubCategory_name25,
            "secondarySubCategory_image25": secondarySubCategory_image25,
            "secondarySubCategory_link25": secondarySubCategory_link25,
            "secondarySubCategory_price25": secondarySubCategory_price25,

            "secondarySubCategory_name26": secondarySubCategory_name26,
            "secondarySubCategory_image26": secondarySubCategory_image26,
            "secondarySubCategory_link26": secondarySubCategory_link26,
            "secondarySubCategory_price26": secondarySubCategory_price26,

        }