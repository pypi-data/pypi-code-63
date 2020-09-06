# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: steammessages_friendmessages.proto
# plugin: python-betterproto

from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class CFriendMessagesGetRecentMessagesRequest(betterproto.Message):
    steamid1: int = betterproto.fixed64_field(1)
    steamid2: int = betterproto.fixed64_field(2)
    count: int = betterproto.uint32_field(3)
    most_recent_conversation: bool = betterproto.bool_field(4)
    rtime32_start_time: int = betterproto.fixed32_field(5)
    bbcode_format: bool = betterproto.bool_field(6)
    start_ordinal: int = betterproto.uint32_field(7)
    time_last: int = betterproto.uint32_field(8)
    ordinal_last: int = betterproto.uint32_field(9)


@dataclass
class CFriendMessagesGetRecentMessagesResponse(betterproto.Message):
    messages: List["CFriendMessagesGetRecentMessagesResponseFriendMessage"] = betterproto.message_field(1)
    more_available: bool = betterproto.bool_field(4)


@dataclass
class CFriendMessagesGetRecentMessagesResponseFriendMessage(betterproto.Message):
    accountid: int = betterproto.uint32_field(1)
    timestamp: int = betterproto.uint32_field(2)
    message: str = betterproto.string_field(3)
    ordinal: int = betterproto.uint32_field(4)


@dataclass
class CFriendsMessagesGetActiveMessageSessionsRequest(betterproto.Message):
    lastmessage_since: int = betterproto.uint32_field(1)
    only_sessions_with_messages: bool = betterproto.bool_field(2)


@dataclass
class CFriendsMessagesGetActiveMessageSessionsResponse(betterproto.Message):
    message_sessions: List[
        "CFriendsMessagesGetActiveMessageSessionsResponseFriendMessageSession"
    ] = betterproto.message_field(1)
    timestamp: int = betterproto.uint32_field(2)


@dataclass
class CFriendsMessagesGetActiveMessageSessionsResponseFriendMessageSession(betterproto.Message):
    accountid_friend: int = betterproto.uint32_field(1)
    last_message: int = betterproto.uint32_field(2)
    last_view: int = betterproto.uint32_field(3)
    unread_message_count: int = betterproto.uint32_field(4)


@dataclass
class CFriendMessagesSendMessageRequest(betterproto.Message):
    steamid: int = betterproto.fixed64_field(1)
    chat_entry_type: int = betterproto.int32_field(2)
    message: str = betterproto.string_field(3)
    contains_bbcode: bool = betterproto.bool_field(4)
    echo_to_sender: bool = betterproto.bool_field(5)
    low_priority: bool = betterproto.bool_field(6)
    client_message_id: str = betterproto.string_field(8)


@dataclass
class CFriendMessagesSendMessageResponse(betterproto.Message):
    modified_message: str = betterproto.string_field(1)
    server_timestamp: int = betterproto.uint32_field(2)
    ordinal: int = betterproto.uint32_field(3)
    message_without_bb_code: str = betterproto.string_field(4)


@dataclass
class CFriendMessagesAckMessageNotification(betterproto.Message):
    steamid_partner: int = betterproto.fixed64_field(1)
    timestamp: int = betterproto.uint32_field(2)


@dataclass
class CFriendMessagesIncomingMessageNotification(betterproto.Message):
    steamid_friend: int = betterproto.fixed64_field(1)
    chat_entry_type: int = betterproto.int32_field(2)
    from_limited_account: bool = betterproto.bool_field(3)
    message: str = betterproto.string_field(4)
    rtime32_server_timestamp: int = betterproto.fixed32_field(5)
    ordinal: int = betterproto.uint32_field(6)
    local_echo: bool = betterproto.bool_field(7)
    message_no_bbcode: str = betterproto.string_field(8)
    low_priority: bool = betterproto.bool_field(9)
