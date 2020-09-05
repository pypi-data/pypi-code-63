"""
SPDX-License-Identifier: BSD-3-Clause
Copyright (c) 2020 Deutsches Elektronen-Synchrotron DESY.
See LICENSE.txt for license details.
"""

from frugy.types import FruAreaBase, fixed_field, fixed_string_field, GuidField, array_field, bytearray_field, ipv4_field, bin2hex_helper
from frugy.multirecords import ipmi_multirecord, MultirecordEntry
from frugy.fru_registry import FruRecordType, rec_register, rec_lookup_by_id


@ipmi_multirecord(0xc0)
class PicmgEntry(MultirecordEntry):
    ''' PICMG AMC.0 Specification R2.0 '''
    ''' Superclass of all PICMG OEM multirecords '''

    _picmg_identifier = 0x315a

    def _payload_prologue(self):
        return self._picmg_identifier.to_bytes(3, 'little') + self._record_id.to_bytes(length=1, byteorder='little') + b'\x00'
    
    @classmethod
    def from_payload(cls, payload):
        picmg_id, payload = payload[:3], payload[3:]
        rec_id, rec_fmt_version, payload = payload[0], payload[1], payload[2:]
        picmg_id = int.from_bytes(picmg_id, 'little')

        if picmg_id != cls._picmg_identifier:
            raise ValueError(f"PICMG identifier mismatch: expected 0x{cls._picmg_identifier:06x}, received 0x{picmg_id:06x} ({picmg_id})")

        if rec_fmt_version not in [0x00, 0x01]:
            raise RuntimeError(f"Unexpected record format version: 0x{rec_fmt_version:02x}")

        try:
            cls_inst = rec_lookup_by_id(FruRecordType.picmg_multirecord, rec_id)()
        except KeyError:
            raise RuntimeError(f"Unknown PICMG entry 0x{rec_id:02x}")

        if len(payload) == 0:
            raise EOFError(f"Skipping creation of {cls_inst.__class__.__name__} due to empty payload")

        cls_inst._deserialize(payload)
        return cls_inst
        

# PICMG AMC.0 multirecords

def picmg_multirecord(rec_id):
    def register_and_set_id(cls):
        cls._record_id = rec_id
        rec_register(cls, FruRecordType.picmg_multirecord, rec_id)
        return cls
    return register_and_set_id

def picmg_secondary(cls):
    rec_register(cls, FruRecordType.picmg_secondary)
    return cls


@picmg_multirecord(0x16)
class ModuleCurrentRequirements(PicmgEntry):
    ''' PICMG AMC.0 Specification R2.0, Table 3-10 '''

    _schema = [
        ('current_draw', fixed_field('u8', div=0.1))
    ]

# Array entry classes for PointToPointConnectivity

@picmg_secondary
class AmcChannelDescriptor(FruAreaBase):
    ''' PICMG AMC.0 Specification R2.0, Table 3-17 '''

    _lanes = [f'_lane{n}_port' for n in range(4)]
    _lane_unused = 0b11111

    _schema = [
        ('_reserved', fixed_field('u4', default=0b1111)),
        ('_lane3_port', fixed_field('u5', default=_lane_unused)),
        ('_lane2_port', fixed_field('u5', default=_lane_unused)),
        ('_lane1_port', fixed_field('u5', default=_lane_unused)),
        ('_lane0_port', fixed_field('u5', default=_lane_unused)),
    ]
    _mergeBitfield = True
    
    def to_dict(self):
        return [self[l] for l in AmcChannelDescriptor._lanes if self[l] != AmcChannelDescriptor._lane_unused]
    
    def update(self, val):
        for i, l in enumerate(AmcChannelDescriptor._lanes):
            self[l] = val[i] if i < len(val) else AmcChannelDescriptor._lane_unused


@picmg_secondary
class AmcLinkDescriptor(FruAreaBase):
    ''' PICMG AMC.0 Specification R2.0, Table 3-19 '''

    _lane_flag_names = [f'_lane{n}_flag' for n in range(4)]

    _link_type_standard_constants = {
            'pcie': 0x02,
            'pcie_advanced': 0x03,
            'pci_advanced_1': 0x04,
            'ethernet': 0x05,
            'serial_rapidio': 0x06,
            'storage': 0x07
    }
    _link_type_oem_constants = {
        f'oem_guid_{n}': n+0xf0 for n in range(15)
    }

    _schema = [
        ('_reserved', fixed_field('u6', default=0b111111)),
        ('asymm_match', fixed_field('u2', constants={
            'match_exact': 0b00,
            'match_10b': 0b01,
            'match_01b': 0b10
        })),
        ('grouping_id', fixed_field('u8')),
        ('link_type_ext', fixed_field('u4', default=0)),
        ('link_type', fixed_field('u8', constants={
            **_link_type_standard_constants,
            **_link_type_oem_constants
        })),
        ('_lane3_flag', fixed_field('u1')),
        ('_lane2_flag', fixed_field('u1')),
        ('_lane1_flag', fixed_field('u1')),
        ('_lane0_flag', fixed_field('u1')),
        ('channel_id', fixed_field('u8')),
    ]
    _mergeBitfield = True

    def to_dict(self):
        result = super().to_dict()
        result['lane_flags'] = [self[f] for f in self._lane_flag_names]
        return result
    
    def update(self, val):
        for n, f in enumerate(self._lane_flag_names):
            self[f] = val['lane_flags'][n]
        del val['lane_flags']
        super().update(val)


@picmg_multirecord(0x19)
class PointToPointConnectivity(PicmgEntry):
    ''' PICMG AMC.0 Specification R2.0, Table 3-16 '''

    _schema = [
        ('_guid_count', fixed_field('u8', default=0)),
        ('guids', array_field(GuidField, num_elems_field='_guid_count')),
        ('record_type', fixed_field('u1', constants={
            'amc_module': 1,
            'on_carrier_device': 0
        })),
        ('_reserved', fixed_field('u3', default=0)),
        ('connected_dev_id', fixed_field('u4', default=0)),
        ('_channel_desc_count', fixed_field('u8', default=0)),
        ('channel_descriptors', array_field(AmcChannelDescriptor, num_elems_field='_channel_desc_count')),
        ('link_descriptors', array_field(AmcLinkDescriptor)),
    ]


# Array entry classes for ClockConfig

_clock_id_constants = {
    # Predefined Clock IDs for AMC clocks, Table 3-33
    # TODO: Are these enough, or do we also need the ATCA Backplane clocks (Table 3-34)?
    'TCLKA': 1,
    'TCLKB': 2,
    'TCLKC': 3,
    'TCLKD': 4,
    'FCLKA': 5,
}

_resource_type_constants = {
    # Clock Resource IDs, Table 3-31
    'on_carrier': 0b00,
    'amc_module': 0b01,
    'backplane': 0b10
}

@picmg_secondary
class DirectClockDescriptor(FruAreaBase):
    ''' PICMG AMC.0 Specification R2.0, Table 3-38 '''

    _schema = [
        ('_reserved', fixed_field('u6', default=0)),
        ('pll_connect', fixed_field('u1')),
        ('asymm_match', fixed_field('u1', constants={
            'clk_source': 1,
            'clk_receiver': 0
        })),
        ('family', fixed_field('u8', constants={
            'unspecified': 0,
            'sonet_sdh_pdh': 1,
            'pcie_reserved': 2
        })),
        ('accuracy', fixed_field('u8')),
        ('frequency', fixed_field('u32')),
        ('freq_min', fixed_field('u32')),
        ('freq_max', fixed_field('u32')),
    ]


@picmg_secondary
class IndirectClockDescriptor(FruAreaBase):
    ''' PICMG AMC.0 Specification R2.0, Table 3-37 '''

    _schema = [
        ('_reserved', fixed_field('u6', default=0)),
        ('pll_connect', fixed_field('u1')),
        ('asymm_match', fixed_field('u1', constants={
            'clk_src': 1,
            'clk_recv': 0
        })),
        ('dep_clk_id', fixed_field('u8')),
    ]


@picmg_secondary
class ClockConfigDescriptor(FruAreaBase):
    ''' PICMG AMC.0 Specification R2.0, Table 3-36 '''
    
    _schema = [
        ('clk_id', fixed_field('u8', constants=_clock_id_constants)),
        ('_reserved', fixed_field('u7', default=0)),
        ('activation', fixed_field('u1', constants={
            'by_carrier': 0,
            'by_application': 1
        })),
        ('_indirect_clk_desc_count', fixed_field('u8', default=0)),
        ('_direct_clk_desc_count', fixed_field('u8', default=0)),
        ('indirect_clk_desc', array_field(IndirectClockDescriptor, num_elems_field='_indirect_clk_desc_count')),
        ('direct_clk_desc', array_field(DirectClockDescriptor, num_elems_field='_direct_clk_desc_count')),
    ]


@picmg_multirecord(0x2d)
class ClockConfig(PicmgEntry):
    ''' PICMG AMC.0 Specification R2.0, Table 3-35 '''

    _schema = [
        ('resource_type', fixed_field('u2', constants=_resource_type_constants)),
        ('_reserved', fixed_field('u2', default=0)),
        ('dev_id', fixed_field('u4')),
        ('_conf_desc_count', fixed_field('u8', default=0)),
        ('conf_desc', array_field(ClockConfigDescriptor, num_elems_field='_conf_desc_count')),
    ]


@picmg_multirecord(0x30)
class Zone3InterfaceCompatibility(PicmgEntry):
    ''' PICMG MicroTCA.4 Enhancements for Rear I/O and Timing R1.0, Table 3-3 '''
    ''' The identifier body is represented as transparent bytearray '''

    _schema = [
        ('identifier_type', fixed_field('u8', constants={
            'PICMG_IRTM0_REP': 0,
            'PICMG_OTHER': 1,
            'GUID': 2,
            'OEM': 3,
            'MTCA4_REP': 4
        })),
        # "format depends on the type" so we assume it's a binary blob
        ('identifier_body', bytearray_field(hex=True)),
    ]


@picmg_secondary
class PartitionDescriptor(FruAreaBase):
    ''' PICMG Specification MTCA.0 R1.0, Table 3-11 '''

    _schema = [
        ('offset', fixed_field('u16', div=0x10)),
        ('length', fixed_field('u16')),
    ]


@picmg_multirecord(0x20)
class FruPartition(PicmgEntry):
    ''' PICMG Specification MTCA.0 R1.0, Table 3-10 '''

    _schema = [
        ('_desc_count', fixed_field('u8', default=0)),
        ('descriptors', array_field(PartitionDescriptor, num_elems_field='_desc_count')),
    ]


@picmg_multirecord(0x21)
class CarrierManagerIPLink(PicmgEntry):
    ''' PICMG Specification MTCA.0 R1.0, Table 3-12 '''
    _schema = [
        ('shelf_manager_ip', ipv4_field()),
        ('carrier_manager_ip', ipv4_field()),
        ('mch1_ip', ipv4_field()),
        ('mch2_ip', ipv4_field()),
        ('subnet', ipv4_field()),
        ('gateway0', ipv4_field()),
        ('gateway1', ipv4_field()),
        ('username', fixed_string_field(17, default='')),
        ('password', fixed_string_field(21, default='')),
    ]


# PICMG Specification MTCA.0 R1.0 Table 3-14

_site_type_std = {
    'cooling_unit': 0x04,
    'advanced_mc': 0x07,
    'rtm': 0x09,
    'mtca_carrier_hub': 0x0a,
    'power_module': 0x0b,
    'unknown': 0xff
}
_site_type_oem = {
    f'oem_module_{n}': 0xc0 + n for n in range(16)
}
_site_type_constants = {
    **_site_type_std,
    **_site_type_oem
}


@picmg_secondary
class SlotEntry(FruAreaBase):
    ''' PICMG Specification MTCA.0 R1.0, Table 3-17 '''

    _schema = [
        ('site_no', fixed_field('u8')),
        ('site_type', fixed_field('u8', constants=_site_type_constants)),
        ('slot_no', fixed_field('u8')),
        ('tier_no', fixed_field('u8')),
        ('slot_org_y', fixed_field('u16')),
        ('slot_org_x', fixed_field('u16')),
    ]


@picmg_multirecord(0x22)
class MtcaCarrierInformation(PicmgEntry):
    ''' PICMG Specification MTCA.0 R1.0, Table 3-16 '''

    _schema = [
        ('number', fixed_field('u8', default=0xff)),
        ('orientation', fixed_field('u1', constants={
            'l2r': 0,
            'b2t': 1
        })),
        ('_slot_entry_count', fixed_field('u7', default=0)),
        ('slot_entries', array_field(SlotEntry, num_elems_field='_slot_entry_count')),
    ]


@picmg_secondary
class PowerPolicyDescriptor(FruAreaBase):
    ''' PICMG Specification MTCA.0 R1.0, Table 3-24 '''

    _schema = [
        ('site_no', fixed_field('u8')),
        ('max_current_override', fixed_field('u16', div=0.1)),
        ('pm_role', fixed_field('u8', constants={
            'primary': 0x00,
            'redundant': 0x01,
            'unspecified': 0xff
        })),
        ('_channel_count', fixed_field('u8')),
        ('_channels', bytearray_field(num_elems_field='_channel_count')),
    ]

    def to_dict(self):
        ''' Convert _channels from bytearray to list of ints '''
        result = super().to_dict()
        result['channels'] = list(self._dict['_channels']._value)
        return result
    
    def update(self, val):
        ''' Convert channels from list of ints to bytearray '''
        self._dict['_channels']._value = bytearray(val['channels'])
        del val['channels']
        super().update(val)


@picmg_multirecord(0x25)
class PowerPolicyRecord(PicmgEntry):
    ''' PICMG Specification MTCA.0 R1.0, Table 3-23 '''

    _schema = [
        ('_num_descriptors', fixed_field('u8', default=0)),
        ('descriptors', array_field(PowerPolicyDescriptor, num_elems_field='_num_descriptors')),
    ]


@picmg_secondary
class MtcaCarrierActivCurrDescriptor(FruAreaBase):
    ''' PICMG Specification MTCA.0 R1.0, Table 3-26 '''

    _mgr_constants={
        'reserved': 0b11,
        'shelf_mgr': 0b10,
        'carrier_mgr': 0b01,
        'system_mgr': 0b00
    }
    _schema = [
        ('site_type', fixed_field('u8', constants=_site_type_constants)),
        ('site_no', fixed_field('u8')),
        ('pwr_ch', fixed_field('u8')),
        ('max_current', fixed_field('u8', div=0.1)),
        ('activation_ctrl', fixed_field('u2', constants=_mgr_constants)),
        ('pwr_delay', fixed_field('u6', div=0.1)),
        ('deactivation_ctrl', fixed_field('u2', constants=_mgr_constants)),
        ('_reserved', fixed_field('u6', default=0))
    ]


@picmg_multirecord(0x26)
class MtcaCarrierActivationPm(PicmgEntry):
    ''' PICMG Specification MTCA.0 R1.0, Table 3-25 '''

    _schema = [
        ('readiness_allowance', fixed_field('u8')),
        ('_num_descriptors', fixed_field('u8', default=0)),
        ('descriptors', array_field(MtcaCarrierActivCurrDescriptor, num_elems_field='_num_descriptors')),
    ]


@picmg_secondary
class P2pPortDescriptor(FruAreaBase):
    ''' PICMG AMC.0 Specification R2.0, Table 3-15 '''

    _mergeBitfield = True

    _schema = [
        ('_reserved0', fixed_field('u6', default=0)),
        ('local_port', fixed_field('u5')),
        ('remote_port', fixed_field('u5')),
        ('resource_type', fixed_field('u1', constants={
            'amc': 1,
            'carrier': 0
        })),
        ('_reserved1', fixed_field('u3', default=0)),
        ('site_no', fixed_field('u4')),
    ]


@picmg_secondary
class P2pAmcResourceDescriptor(FruAreaBase):
    ''' PICMG AMC.0 Specification R2.0, Table 3-14 '''

    _schema = [
        ('resource_type', fixed_field('u1', constants={
            'amc': 1,
            'carrier': 0
        })),
        ('_reserved', fixed_field('u3', default=0)),
        ('site_no', fixed_field('u4')),
        ('_port_count', fixed_field('u8')),
        ('port_descriptors', array_field(P2pPortDescriptor, num_elems_field='_port_count')),
    ]


@picmg_multirecord(0x18)
class CarrierP2pConnectivity(PicmgEntry):
    ''' PICMG AMC.0 Specification R2.0, Table 3-13 '''

    _schema = [
        ('resource_descriptors', array_field(P2pAmcResourceDescriptor)),
    ]


@picmg_secondary
class P2pClockConnectionDescriptor(FruAreaBase):
    ''' PICMG AMC.0 Specification R2.0, Table 3-32 '''

    _schema = [
        ('local_clock_id', fixed_field('u8', constants=_clock_id_constants)),
        ('remote_clock_id', fixed_field('u8', constants=_clock_id_constants)),
        ('resource_type', fixed_field('u2', constants=_resource_type_constants)),
        ('_reserved', fixed_field('u2', default=0)),
        ('dev_id', fixed_field('u4')),
    ]


@picmg_secondary
class ClockP2pResourceDescriptor(FruAreaBase):
    ''' PICMG AMC.0 Specification R2.0, Table 3-30 '''

    _schema = [
        ('resource_type', fixed_field('u2', constants=_resource_type_constants)),
        ('_reserved', fixed_field('u2', default=0)),
        ('dev_id', fixed_field('u4')),
        ('_p2p_clk_conn_count', fixed_field('u8', default=0)),
        ('p2p_clk_conn_descriptors', array_field(P2pClockConnectionDescriptor, num_elems_field='_p2p_clk_conn_count'))
    ]


@picmg_multirecord(0x2c)
class CarrierClkP2pConnectivity(PicmgEntry):
    ''' PICMG AMC.0 Specification R2.0, Table 3-29 '''

    _schema = [
        ('_clk_p2p_resource_desc_count', fixed_field('u8', default=0)),
        ('clk_p2p_resource_descriptors', array_field(ClockP2pResourceDescriptor, num_elems_field='_clk_p2p_resource_desc_count')),
    ]

@picmg_multirecord(0x32)
class Zone3InterfaceDocumentation(PicmgEntry):
    ''' PICMG MicroTCA.4 Enhancements for Rear I/O and Timing R1.0, Table 3-15 '''

    _schema = [
        ('url', bytearray_field(hex=False)),
    ]
