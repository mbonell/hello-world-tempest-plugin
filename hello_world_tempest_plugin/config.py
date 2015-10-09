from oslo_config import cfg
from tempest import config

service_available_group = cfg.OptGroup(
    name="service_available",
    title="Available OpenStack Services"
)

ServiceAvailableGroup = [
    cfg.BoolOpt("hello_world_tempest_plugin", default=True,
                help="Whether or not Hello World is expected to be available")
]

hello_world_group = cfg.OptGroup(
    name="hello_world",
    title="Hello World Test Variables"
)

HelloWorldGroup = [
    cfg.StrOpt("my_custom_variable", default="custom value",
               help="My custom variable.")
]
