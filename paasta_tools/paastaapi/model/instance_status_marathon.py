# coding: utf-8

"""
    Paasta API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

import nulltype  # noqa: F401

from paasta_tools.paastaapi.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from paasta_tools.paastaapi.model.envoy_status import EnvoyStatus
    from paasta_tools.paastaapi.model.marathon_app_status import MarathonAppStatus
    from paasta_tools.paastaapi.model.marathon_autoscaling_info import MarathonAutoscalingInfo
    from paasta_tools.paastaapi.model.marathon_mesos_status import MarathonMesosStatus
    from paasta_tools.paastaapi.model.smartstack_status import SmartstackStatus
    globals()['EnvoyStatus'] = EnvoyStatus
    globals()['MarathonAppStatus'] = MarathonAppStatus
    globals()['MarathonAutoscalingInfo'] = MarathonAutoscalingInfo
    globals()['MarathonMesosStatus'] = MarathonMesosStatus
    globals()['SmartstackStatus'] = SmartstackStatus


class InstanceStatusMarathon(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('bounce_method',): {
            'BRUTAL': "brutal",
            'UPTHENDOWN': "upthendown",
            'DOWNTHENUP': "downthenup",
            'CROSSOVER': "crossover",
        },
        ('desired_state',): {
            'START': "start",
            'STOP': "stop",
        },
        ('deploy_status',): {
            'RUNNING': "Running",
            'DEPLOYING': "Deploying",
            'STOPPED': "Stopped",
            'DELAYED': "Delayed",
            'WAITING': "Waiting",
            'WAITING_FOR_BOUNCE': "Waiting for bounce",
            'NOTRUNNING': "NotRunning",
        },
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'app_count': (int,),  # noqa: E501
            'bounce_method': (str,),  # noqa: E501
            'desired_state': (str,),  # noqa: E501
            'active_shas': ([[str, none_type]],),  # noqa: E501
            'app_statuses': ([MarathonAppStatus],),  # noqa: E501
            'autoscaling_info': (MarathonAutoscalingInfo,),  # noqa: E501
            'backoff_seconds': (int,),  # noqa: E501
            'deploy_status': (str,),  # noqa: E501
            'desired_app_id': (str,),  # noqa: E501
            'envoy': (EnvoyStatus,),  # noqa: E501
            'error_message': (str,),  # noqa: E501
            'expected_instance_count': (int,),  # noqa: E501
            'mesos': (MarathonMesosStatus,),  # noqa: E501
            'running_instance_count': (int,),  # noqa: E501
            'smartstack': (SmartstackStatus,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'app_count': 'app_count',  # noqa: E501
        'bounce_method': 'bounce_method',  # noqa: E501
        'desired_state': 'desired_state',  # noqa: E501
        'active_shas': 'active_shas',  # noqa: E501
        'app_statuses': 'app_statuses',  # noqa: E501
        'autoscaling_info': 'autoscaling_info',  # noqa: E501
        'backoff_seconds': 'backoff_seconds',  # noqa: E501
        'deploy_status': 'deploy_status',  # noqa: E501
        'desired_app_id': 'desired_app_id',  # noqa: E501
        'envoy': 'envoy',  # noqa: E501
        'error_message': 'error_message',  # noqa: E501
        'expected_instance_count': 'expected_instance_count',  # noqa: E501
        'mesos': 'mesos',  # noqa: E501
        'running_instance_count': 'running_instance_count',  # noqa: E501
        'smartstack': 'smartstack',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, app_count, bounce_method, desired_state, *args, **kwargs):  # noqa: E501
        """InstanceStatusMarathon - a model defined in OpenAPI

        Args:
            app_count (int): The number of different running versions of the same service (0 for stopped, 1 for running and 1+ for bouncing)
            bounce_method (str): Method to transit between new and old versions of a service
            desired_state (str): Desired state of a service, for Marathon

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            active_shas ([[str, none_type]]): List of git/config SHAs running.. [optional]  # noqa: E501
            app_statuses ([MarathonAppStatus]): Statuses of each app of the service. [optional]  # noqa: E501
            autoscaling_info (MarathonAutoscalingInfo): [optional]  # noqa: E501
            backoff_seconds (int): backoff in seconds before launching the next task. [optional]  # noqa: E501
            deploy_status (str): Deploy status of a marathon service. [optional]  # noqa: E501
            desired_app_id (str): ID of the desired version of a service instance. [optional]  # noqa: E501
            envoy (EnvoyStatus): [optional]  # noqa: E501
            error_message (str): Error message when a marathon job ID cannot be found. [optional]  # noqa: E501
            expected_instance_count (int): The number of desired instances of the service. [optional]  # noqa: E501
            mesos (MarathonMesosStatus): [optional]  # noqa: E501
            running_instance_count (int): The number of actual running instances of the service. [optional]  # noqa: E501
            smartstack (SmartstackStatus): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.app_count = app_count
        self.bounce_method = bounce_method
        self.desired_state = desired_state
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
