# import site
# site.addsitedir('/home/cybernetor066/Desktop/Software-IT-Web-Dev/GIT-Repos/spacenetng-webApps/Back-End/spacenetng_venv1/lib/python3.5/site-packages')
# import os
# from paste.deploy import loadapp
# from waitress import serve

# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 5000))
#     app = loadapp('config:production.ini', relative_to='.')

#     serve(app, host='0.0.0.0', port=port)

import os
import plaster
from waitress import serve

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    loader = plaster.get_loader('production.ini', protocols=['wsgi'])
    setttings = loader.get_settings('app:main')  # To get any section out of the config file
    app_config = loader.get_wsgi_app_settings()  # To get settings for a WSGI app, defaults to main
    app = loader.get_wsgi_app()     # Defaults to main
    serve(app, host='0.0.0.0', port=port)