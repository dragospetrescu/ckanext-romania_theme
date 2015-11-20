import ckan.model as model
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import os


def get_number_of_files():
    return model.Session.execute("select count(*) from resource where state = 'active'").first()[0]


def get_number_of_external_links():
    return model.Session.execute("select count(*) from resource where state = 'active' and url not LIKE '%data.gov.ro%'").first()[0]


class Romania_ThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IResourceController)

    # IConfigurer
    def update_config(self, config):
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')
        toolkit.add_resource('fanstatic', 'romania_theme')

    def get_helpers(self):
        return {'get_number_of_files': get_number_of_files,
                'get_number_of_external_links': get_number_of_external_links}

    # IResourceController
    def before_create(self, context, resource):
        if resource['upload'].type == 'application/pdf':
            raise toolkit.ValidationError(['Resource type not allowed as resource.'])
