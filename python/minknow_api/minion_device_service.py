### THIS FILE IS AUTOGENERATED. DO NOT EDIT THIS FILE DIRECTLY ###
from .minion_device_pb2_grpc import *
from . import minion_device_pb2
from minknow_api.minion_device_pb2 import *
from minknow_api._support import MessageWrapper, ArgumentError
import time
import logging

__all__ = [
    "MinionDeviceService",
    "TemperatureRange",
    "SamplingFrequencyParameters",
    "MinionDeviceSettings",
    "ChangeSettingsRequest",
    "ChangeSettingsResponse",
    "GetSettingsRequest",
    "GetSettingsResponse",
]

def run_with_retry(method, message, timeout, unwraps, full_name):
    retry_count = 20
    error = None
    for i in range(retry_count):
        try:
            result = MessageWrapper(method(message, timeout=timeout), unwraps=unwraps)
            return result
        except grpc.RpcError as e:
            # Retrying unidentified grpc errors to keep clients from crashing
            retryable_error = (e.code() == grpc.StatusCode.UNKNOWN and "Stream removed" in e.details() or \
                                (e.code() == grpc.StatusCode.INTERNAL and "RST_STREAM" in e.details()))
            if retryable_error:
                logging.info('Bypassed ({}: {}) error for grpc: {}. Attempt {}.'.format(e.code(), e.details(), full_name, i))
            else:
                raise
            error = e
        time.sleep(1)
    raise error


class MinionDeviceService(object):
    def __init__(self, channel):
        self._stub = MinionDeviceServiceStub(channel)
        self._pb = minion_device_pb2

    def change_settings(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.change_settings, _message, _timeout, [], "minknow_api.minion_device.MinionDeviceService")

        unused_args = set(kwargs.keys())

        _message = ChangeSettingsRequest()

        if "bias_voltage" in kwargs:
            unused_args.remove("bias_voltage")
            _message.settings.bias_voltage.value = kwargs['bias_voltage']

        if "sampling_frequency" in kwargs:
            unused_args.remove("sampling_frequency")
            _message.settings.sampling_frequency.value = kwargs['sampling_frequency']

        if "channel_config" in kwargs:
            unused_args.remove("channel_config")
            _message.settings.channel_config.update(kwargs['channel_config'])
            

        if "enable_temperature_control" in kwargs:
            unused_args.remove("enable_temperature_control")
            _message.settings.enable_temperature_control.value = kwargs['enable_temperature_control']

        if "temperature_target" in kwargs:
            unused_args.remove("temperature_target")
            _message.settings.temperature_target.CopyFrom(kwargs['temperature_target'])

        if "int_capacitor" in kwargs:
            unused_args.remove("int_capacitor")
            _message.settings.int_capacitor = kwargs['int_capacitor']

        if "test_current" in kwargs:
            unused_args.remove("test_current")
            _message.settings.test_current.value = kwargs['test_current']

        if "unblock_voltage" in kwargs:
            unused_args.remove("unblock_voltage")
            _message.settings.unblock_voltage.value = kwargs['unblock_voltage']

        if "overcurrent_limit" in kwargs:
            unused_args.remove("overcurrent_limit")
            _message.settings.overcurrent_limit.value = kwargs['overcurrent_limit']

        if "samples_to_reset" in kwargs:
            unused_args.remove("samples_to_reset")
            _message.settings.samples_to_reset.value = kwargs['samples_to_reset']

        if "th_gain" in kwargs:
            unused_args.remove("th_gain")
            _message.settings.th_gain = kwargs['th_gain']

        if "sinc_delay" in kwargs:
            unused_args.remove("sinc_delay")
            _message.settings.sinc_delay.value = kwargs['sinc_delay']

        if "th_sample_time" in kwargs:
            unused_args.remove("th_sample_time")
            _message.settings.th_sample_time.value = kwargs['th_sample_time']

        if "int_reset_time" in kwargs:
            unused_args.remove("int_reset_time")
            _message.settings.int_reset_time.value = kwargs['int_reset_time']

        if "sinc_decimation" in kwargs:
            unused_args.remove("sinc_decimation")
            _message.settings.sinc_decimation = kwargs['sinc_decimation']

        if "low_pass_filter" in kwargs:
            unused_args.remove("low_pass_filter")
            _message.settings.low_pass_filter = kwargs['low_pass_filter']

        if "non_overlap_clock" in kwargs:
            unused_args.remove("non_overlap_clock")
            _message.settings.non_overlap_clock = kwargs['non_overlap_clock']

        if "bias_current" in kwargs:
            unused_args.remove("bias_current")
            _message.settings.bias_current.value = kwargs['bias_current']

        if "compensation_capacitor" in kwargs:
            unused_args.remove("compensation_capacitor")
            _message.settings.compensation_capacitor.value = kwargs['compensation_capacitor']

        if "sampling_frequency_params" in kwargs:
            unused_args.remove("sampling_frequency_params")
            _message.settings.sampling_frequency_params.CopyFrom(kwargs['sampling_frequency_params'])

        if "enable_asic_power" in kwargs:
            unused_args.remove("enable_asic_power")
            _message.settings.enable_asic_power.value = kwargs['enable_asic_power']

        if "fan_speed" in kwargs:
            unused_args.remove("fan_speed")
            _message.settings.fan_speed = kwargs['fan_speed']

        if "allow_full_fan_stop" in kwargs:
            unused_args.remove("allow_full_fan_stop")
            _message.settings.allow_full_fan_stop.value = kwargs['allow_full_fan_stop']

        if "enable_soft_temperature_control" in kwargs:
            unused_args.remove("enable_soft_temperature_control")
            _message.settings.enable_soft_temperature_control.value = kwargs['enable_soft_temperature_control']

        if "enable_bias_voltage_lookup" in kwargs:
            unused_args.remove("enable_bias_voltage_lookup")
            _message.settings.enable_bias_voltage_lookup.value = kwargs['enable_bias_voltage_lookup']

        if "bias_voltage_lookup_table" in kwargs:
            unused_args.remove("bias_voltage_lookup_table")
            _message.settings.bias_voltage_lookup_table.extend(kwargs['bias_voltage_lookup_table'])

        if "channel_config_default" in kwargs:
            unused_args.remove("channel_config_default")
            _message.channel_config_default = kwargs['channel_config_default']

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to change_settings: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.change_settings, _message, _timeout, [], "minknow_api.minion_device.MinionDeviceService")

    def get_settings(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.get_settings, _message, _timeout, ["settings"], "minknow_api.minion_device.MinionDeviceService")

        unused_args = set(kwargs.keys())

        _message = GetSettingsRequest()

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to get_settings: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.get_settings, _message, _timeout, ["settings"], "minknow_api.minion_device.MinionDeviceService")