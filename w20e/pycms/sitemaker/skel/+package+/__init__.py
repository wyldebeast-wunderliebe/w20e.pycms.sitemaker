from pyramid.config import Configurator
from pyramid_zodbconn import get_connection
import pyramid_zcml
from w20e.pycms.models.page import Page
from w20e.pycms import appmaker


def root_factory(request):
    conn = get_connection(request)
    return appmaker(conn.root())


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

    return config.make_wsgi_app()
