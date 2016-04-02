import webtest
import paste.fixture
import pylons.test


from ckan.tests import factories
import ckan.model as model
import ckan.tests.helpers as helpers
import ckan.config
import ckan.plugins


class TestRomaniaTheme(helpers.FunctionalTestBase):
    @classmethod
    def setup_class(cls):
        cls.app = paste.fixture.TestApp(pylons.test.pylonsapp)
        ckan.plugins.load('romania_theme')

    def setup(self):
        super(TestRomaniaTheme, self).setup()
        self.user = factories.User()
        self.user_env = {'REMOTE_USER': self.user['name'].encode('ascii')}

    def teardown(self):
        model.repo.rebuild_db()

    @classmethod
    def teardown_class(cls):
        ckan.plugins.unload('romania_theme')

    def test_motto(self):
        response = self.app.get('/')
        motto = 'Date accesibile, reutilizabile, ce pot fi redistribuite'
        assert motto in response.body

    def test_(self):
        response = self.app.get(url='/en/dataset/new', extra_environ=self.user_env )
        field = 'Maintainer email'
        assert field not in response.body
