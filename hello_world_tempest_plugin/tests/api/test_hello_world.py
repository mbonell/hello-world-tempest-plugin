from hello_world_tempest_plugin.tests.api import base
from tempest import test


class TestHelloWorld(base.BaseHelloWorldTest):

    @classmethod
    def resource_setup(cls):
        super(TestHelloWorld, cls).resource_setup()

    @test.attr(type="smoke")
    def test_hello_world(self):
        self.assertEqual('Hello world!', 'Hello world!')

    @classmethod
    def resource_cleanup(cls):
        super(TestHelloWorld, cls).resource_cleanup()
