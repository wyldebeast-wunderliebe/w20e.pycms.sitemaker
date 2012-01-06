from pyramid.config import Configurator
import pyramid_zcml
from w20e.pycms import appmaker, root_factory


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    config = Configurator(root_factory=root_factory, settings=settings)
    zcml_file = settings.get('configure_zcml', 'configure.zcml')

    config.hook_zca()
    config.include(pyramid_zcml)
    config.include('pyramid_mailer')

    config.load_zcml('w20e.pycms:bootstrap.zcml')
    config.commit()
    
    config.load_zcml(zcml_file)
    config.commit()

    appmaker(config)

    return config.make_wsgi_app()
