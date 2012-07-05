from w20e.pycms import make_pycms_app


def main(global_config, **settings):

    return make_pycms_app(__package__, **settings)
