import zigpy.types as t

CONF_NWK_CHANNEL_DEFAULT = 15
CONF_NWK_CHANNELS_DEFAULT = [15, 20, 25]
CONF_NWK_EXTENDED_PAN_ID_DEFAULT = None
CONF_NWK_PAN_ID_DEFAULT = None
CONF_NWK_KEY_DEFAULT = None
CONF_NWK_KEY_SEQ_DEFAULT = 0x00
CONF_NWK_TC_ADDRESS_DEFAULT = None
CONF_NWK_TC_LINK_KEY_DEFAULT = t.KeyData(
    [
        0x5A,
        0x69,
        0x67,
        0x42,
        0x65,
        0x65,
        0x41,
        0x6C,
        0x6C,
        0x69,
        0x61,
        0x6E,
        0x63,
        0x65,
        0x30,
        0x39,
    ]
)
CONF_NWK_UPDATE_ID_DEFAULT = 0x00
CONF_OTA_IKEA_DEFAULT = False
CONF_OTA_LEDVANCE_DEFAULT = False
CONF_OTA_OTAU_DIR_DEFAULT = None
