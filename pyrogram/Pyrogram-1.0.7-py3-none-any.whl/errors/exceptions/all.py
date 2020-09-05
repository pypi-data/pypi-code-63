# Pyrogram - Telegram MTProto API Client Library for Python
# Copyright (C) 2017-2020 Dan <https://github.com/delivrance>
#
# This file is part of Pyrogram.
#
# Pyrogram is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pyrogram is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

count = 186

exceptions = {
    420: {
        "_": "Flood",
        "FLOOD_WAIT_X": "FloodWait",
        "TAKEOUT_INIT_DELAY_X": "TakeoutInitDelay",
        "SLOWMODE_WAIT_X": "SlowmodeWait",
    },
    401: {
        "_": "Unauthorized",
        "AUTH_KEY_UNREGISTERED": "AuthKeyUnregistered",
        "AUTH_KEY_INVALID": "AuthKeyInvalid",
        "USER_DEACTIVATED": "UserDeactivated",
        "USER_DEACTIVATED_BAN": "UserDeactivatedBan",
        "SESSION_REVOKED": "SessionRevoked",
        "SESSION_EXPIRED": "SessionExpired",
        "ACTIVE_USER_REQUIRED": "ActiveUserRequired",
        "AUTH_KEY_PERM_EMPTY": "AuthKeyPermEmpty",
        "SESSION_PASSWORD_NEEDED": "SessionPasswordNeeded",
    },
    403: {
        "_": "Forbidden",
        "CHAT_WRITE_FORBIDDEN": "ChatWriteForbidden",
        "RIGHT_FORBIDDEN": "RightForbidden",
        "CHAT_ADMIN_INVITE_REQUIRED": "ChatAdminInviteRequired",
        "MESSAGE_DELETE_FORBIDDEN": "MessageDeleteForbidden",
        "CHAT_SEND_MEDIA_FORBIDDEN": "ChatSendMediaForbidden",
        "MESSAGE_AUTHOR_REQUIRED": "MessageAuthorRequired",
    },
    400: {
        "_": "BadRequest",
        "FIRSTNAME_INVALID": "FirstnameInvalid",
        "LASTNAME_INVALID": "LastnameInvalid",
        "PHONE_NUMBER_INVALID": "PhoneNumberInvalid",
        "PHONE_CODE_HASH_EMPTY": "PhoneCodeHashEmpty",
        "PHONE_CODE_EMPTY": "PhoneCodeEmpty",
        "PHONE_CODE_EXPIRED": "PhoneCodeExpired",
        "PHONE_CODE_INVALID": "PhoneCodeInvalid",
        "API_ID_INVALID": "ApiIdInvalid",
        "PHONE_NUMBER_OCCUPIED": "PhoneNumberOccupied",
        "PHONE_NUMBER_UNOCCUPIED": "PhoneNumberUnoccupied",
        "USERS_TOO_FEW": "UsersTooFew",
        "USERS_TOO_MUCH": "UsersTooMuch",
        "TYPE_CONSTRUCTOR_INVALID": "TypeConstructorInvalid",
        "FILE_PART_INVALID": "FilePartInvalid",
        "FILE_PARTS_INVALID": "FilePartsInvalid",
        "FILE_PART_X_MISSING": "FilePartMissing",
        "MD5_CHECKSUM_INVALID": "Md5ChecksumInvalid",
        "PHOTO_INVALID_DIMENSIONS": "PhotoInvalidDimensions",
        "FIELD_NAME_INVALID": "FieldNameInvalid",
        "FIELD_NAME_EMPTY": "FieldNameEmpty",
        "MSG_WAIT_FAILED": "MsgWaitFailed",
        "PEER_ID_INVALID": "PeerIdInvalid",
        "MESSAGE_EMPTY": "MessageEmpty",
        "ENCRYPTED_MESSAGE_INVALID": "EncryptedMessageInvalid",
        "INPUT_METHOD_INVALID": "InputMethodInvalid",
        "PASSWORD_HASH_INVALID": "PasswordHashInvalid",
        "USERNAME_NOT_OCCUPIED": "UsernameNotOccupied",
        "USERNAME_INVALID": "UsernameInvalid",
        "MESSAGE_ID_INVALID": "MessageIdInvalid",
        "MESSAGE_NOT_MODIFIED": "MessageNotModified",
        "ENTITY_MENTION_USER_INVALID": "EntityMentionUserInvalid",
        "MESSAGE_TOO_LONG": "MessageTooLong",
        "ACCESS_TOKEN_EXPIRED": "AccessTokenExpired",
        "BOT_METHOD_INVALID": "BotMethodInvalid",
        "QUERY_TOO_SHORT": "QueryTooShort",
        "SEARCH_QUERY_EMPTY": "SearchQueryEmpty",
        "CHAT_ID_INVALID": "ChatIdInvalid",
        "DATE_EMPTY": "DateEmpty",
        "PERSISTENT_TIMESTAMP_EMPTY": "PersistentTimestampEmpty",
        "CDN_METHOD_INVALID": "CdnMethodInvalid",
        "VOLUME_LOC_NOT_FOUND": "VolumeLocNotFound",
        "FILE_ID_INVALID": "FileIdInvalid",
        "LOCATION_INVALID": "LocationInvalid",
        "CHAT_ADMIN_REQUIRED": "ChatAdminRequired",
        "PHONE_NUMBER_BANNED": "PhoneNumberBanned",
        "ABOUT_TOO_LONG": "AboutTooLong",
        "MULTI_MEDIA_TOO_LONG": "MultiMediaTooLong",
        "USERNAME_OCCUPIED": "UsernameOccupied",
        "BOT_INLINE_DISABLED": "BotInlineDisabled",
        "INLINE_RESULT_EXPIRED": "InlineResultExpired",
        "INVITE_HASH_INVALID": "InviteHashInvalid",
        "USER_ALREADY_PARTICIPANT": "UserAlreadyParticipant",
        "TTL_MEDIA_INVALID": "TtlMediaInvalid",
        "MAX_ID_INVALID": "MaxIdInvalid",
        "CHANNEL_INVALID": "ChannelInvalid",
        "DC_ID_INVALID": "DcIdInvalid",
        "LIMIT_INVALID": "LimitInvalid",
        "OFFSET_INVALID": "OffsetInvalid",
        "EMAIL_INVALID": "EmailInvalid",
        "USER_IS_BOT": "UserIsBot",
        "WEBPAGE_CURL_FAILED": "WebpageCurlFailed",
        "STICKERSET_INVALID": "StickersetInvalid",
        "PEER_FLOOD": "PeerFlood",
        "MEDIA_CAPTION_TOO_LONG": "MediaCaptionTooLong",
        "USER_NOT_MUTUAL_CONTACT": "UserNotMutualContact",
        "USER_CHANNELS_TOO_MUCH": "UserChannelsTooMuch",
        "API_ID_PUBLISHED_FLOOD": "ApiIdPublishedFlood",
        "USER_NOT_PARTICIPANT": "UserNotParticipant",
        "CHANNEL_PRIVATE": "ChannelPrivate",
        "MESSAGE_IDS_EMPTY": "MessageIdsEmpty",
        "WEBPAGE_MEDIA_EMPTY": "WebpageMediaEmpty",
        "QUERY_ID_INVALID": "QueryIdInvalid",
        "MEDIA_EMPTY": "MediaEmpty",
        "USER_IS_BLOCKED": "UserIsBlocked",
        "YOU_BLOCKED_USER": "YouBlockedUser",
        "ADMINS_TOO_MUCH": "AdminsTooMuch",
        "BOTS_TOO_MUCH": "BotsTooMuch",
        "USER_ADMIN_INVALID": "UserAdminInvalid",
        "INPUT_USER_DEACTIVATED": "InputUserDeactivated",
        "PASSWORD_RECOVERY_NA": "PasswordRecoveryNa",
        "PASSWORD_EMPTY": "PasswordEmpty",
        "PHONE_NUMBER_FLOOD": "PhoneNumberFlood",
        "TAKEOUT_INVALID": "TakeoutInvalid",
        "TAKEOUT_REQUIRED": "TakeoutRequired",
        "MESSAGE_POLL_CLOSED": "MessagePollClosed",
        "MEDIA_INVALID": "MediaInvalid",
        "BOT_SCORE_NOT_MODIFIED": "BotScoreNotModified",
        "USER_BOT_REQUIRED": "UserBotRequired",
        "IMAGE_PROCESS_FAILED": "ImageProcessFailed",
        "USERNAME_NOT_MODIFIED": "UsernameNotModified",
        "CALL_ALREADY_ACCEPTED": "CallAlreadyAccepted",
        "CALL_ALREADY_DECLINED": "CallAlreadyDeclined",
        "PHOTO_EXT_INVALID": "PhotoExtInvalid",
        "EXTERNAL_URL_INVALID": "ExternalUrlInvalid",
        "CHAT_NOT_MODIFIED": "ChatNotModified",
        "RESULTS_TOO_MUCH": "ResultsTooMuch",
        "RESULT_ID_DUPLICATE": "ResultIdDuplicate",
        "ACCESS_TOKEN_INVALID": "AccessTokenInvalid",
        "INVITE_HASH_EXPIRED": "InviteHashExpired",
        "USER_BANNED_IN_CHANNEL": "UserBannedInChannel",
        "MESSAGE_EDIT_TIME_EXPIRED": "MessageEditTimeExpired",
        "FOLDER_ID_INVALID": "FolderIdInvalid",
        "MEGAGROUP_PREHISTORY_HIDDEN": "MegagroupPrehistoryHidden",
        "CHAT_LINK_EXISTS": "ChatLinkExists",
        "LINK_NOT_MODIFIED": "LinkNotModified",
        "BROADCAST_ID_INVALID": "BroadcastIdInvalid",
        "MEGAGROUP_ID_INVALID": "MegagroupIdInvalid",
        "BUTTON_DATA_INVALID": "ButtonDataInvalid",
        "START_PARAM_INVALID": "StartParamInvalid",
        "ARTICLE_TITLE_EMPTY": "ArticleTitleEmpty",
        "FILE_PART_TOO_BIG": "FilePartTooBig",
        "FILE_PART_EMPTY": "FilePartEmpty",
        "FILE_PART_SIZE_INVALID": "FilePartSizeInvalid",
        "FILE_PART_SIZE_CHANGED": "FilePartSizeChanged",
        "FILE_MIGRATE_X": "FileMigrate",
        "RESULT_TYPE_INVALID": "ResultTypeInvalid",
        "PHOTO_THUMB_URL_EMPTY": "PhotoThumbUrlEmpty",
        "PHOTO_THUMB_URL_INVALID": "PhotoThumbUrlInvalid",
        "PHOTO_CONTENT_URL_EMPTY": "PhotoContentUrlEmpty",
        "PHOTO_CONTENT_TYPE_INVALID": "PhotoContentTypeInvalid",
        "WEBDOCUMENT_INVALID": "WebdocumentInvalid",
        "WEBDOCUMENT_URL_EMPTY": "WebdocumentUrlEmpty",
        "WEBDOCUMENT_URL_INVALID": "WebdocumentUrlInvalid",
        "WEBDOCUMENT_MIME_INVALID": "WebdocumentMimeInvalid",
        "BUTTON_URL_INVALID": "ButtonUrlInvalid",
        "AUTH_BYTES_INVALID": "AuthBytesInvalid",
        "USER_ID_INVALID": "UserIdInvalid",
        "CHANNELS_TOO_MUCH": "ChannelsTooMuch",
        "ADMIN_RANK_INVALID": "AdminRankInvalid",
        "ADMIN_RANK_EMOJI_NOT_ALLOWED": "AdminRankEmojiNotAllowed",
        "FILE_REFERENCE_EMPTY": "FileReferenceEmpty",
        "FILE_REFERENCE_INVALID": "FileReferenceInvalid",
        "REPLY_MARKUP_TOO_LONG": "ReplyMarkupTooLong",
        "SECONDS_INVALID": "SecondsInvalid",
        "QUIZ_MULTIPLE_INVALID": "QuizMultipleInvalid",
        "QUIZ_CORRECT_ANSWERS_EMPTY": "QuizCorrectAnswersEmpty",
        "QUIZ_CORRECT_ANSWER_INVALID": "QuizCorrectAnswerInvalid",
        "QUIZ_CORRECT_ANSWERS_TOO_MUCH": "QuizCorrectAnswersTooMuch",
        "OPTIONS_TOO_MUCH": "OptionsTooMuch",
        "POLL_ANSWERS_INVALID": "PollAnswersInvalid",
        "POLL_QUESTION_INVALID": "PollQuestionInvalid",
        "FRESH_CHANGE_ADMINS_FORBIDDEN": "FreshChangeAdminsForbidden",
        "BROADCAST_PUBLIC_VOTERS_FORBIDDEN": "BroadcastPublicVotersForbidden",
        "INPUT_FILTER_INVALID": "InputFilterInvalid",
        "EMOTICON_EMPTY": "EmoticonEmpty",
        "EMOTICON_INVALID": "EmoticonInvalid",
        "VIDEO_FILE_INVALID": "VideoFileInvalid",
        "PRIVACY_TOO_LONG": "PrivacyTooLong",
    },
    406: {
        "_": "NotAcceptable",
        "AUTH_KEY_DUPLICATED": "AuthKeyDuplicated",
        "FILEREF_UPGRADE_NEEDED": "FilerefUpgradeNeeded",
        "STICKERSET_INVALID": "StickersetInvalid",
    },
    303: {
        "_": "SeeOther",
        "FILE_MIGRATE_X": "FileMigrate",
        "PHONE_MIGRATE_X": "PhoneMigrate",
        "NETWORK_MIGRATE_X": "NetworkMigrate",
        "USER_MIGRATE_X": "UserMigrate",
    },
    500: {
        "_": "InternalServerError",
        "AUTH_RESTART": "AuthRestart",
        "RPC_CALL_FAIL": "RpcCallFail",
        "RPC_MCGET_FAIL": "RpcMcgetFail",
        "PERSISTENT_TIMESTAMP_OUTDATED": "PersistentTimestampOutdated",
        "HISTORY_GET_FAILED": "HistoryGetFailed",
        "REG_ID_GENERATE_FAILED": "RegIdGenerateFailed",
        "RANDOM_ID_DUPLICATE": "RandomIdDuplicate",
        "WORKER_BUSY_TOO_LONG_RETRY": "WorkerBusyTooLongRetry",
        "INTERDC_X_CALL_ERROR": "InterdcCallError",
        "INTERDC_X_CALL_RICH_ERROR": "InterdcCallRichError",
        "FOLDER_DEAC_AUTOFIX_ALL": "FolderDeacAutofixAll",
        "MSGID_DECREASE_RETRY": "MsgidDecreaseRetry",
        "MEMBER_OCCUPY_PRIMARY_LOC_FAILED": "MemberOccupyPrimaryLocFailed",
    },
}
