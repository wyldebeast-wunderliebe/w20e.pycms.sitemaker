from paste.script.templates import Template, var

vars = [
    var('pycms_project_path', 'Path to your PyCMS project'),
    ]

class PyCMSBuildoutTemplate(Template):
    _template_dir = './buildout_skel'
    summary = 'PyCMS buildout template'
    vars = vars


    def write_files(self, command, output_dir, vars):    

        """ Override so as to put the files in '.' """

        Template.write_files(self, command, ".", vars)
