"""Schema for the action request body. Woot, woot."""

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Tuple, Union

from pydantic.dataclasses import Field, dataclass


@dataclass
class RequestError:
    field: Optional[str] = None
    message: Optional[str] = None
    code: Optional[str] = None


@dataclass
class GenericId:
    id: Optional[float] = None


@dataclass
class CannedResponse:
    id: Optional[int] = None
    content: Optional[str] = None
    short_code: Optional[str] = None
    account_id: Optional[int] = None


@dataclass
class CustomAttribute:
    id: Optional[int] = None
    attribute_display_name: Optional[str] = None
    attribute_display_type: Optional[str] = None
    attribute_description: Optional[str] = None
    attribute_key: Optional[str] = None
    attribute_values: Optional[str] = None
    default_value: Optional[str] = None
    attribute_model: Optional[str] = None
    account_id: Optional[int] = None


class EventName(Enum):
    conversation_created = "conversation_created"
    conversation_updated = "conversation_updated"
    message_created = "message_created"


@dataclass
class AutomationRule:
    event_name: Optional[EventName] = None
    name: Optional[str] = None
    description: Optional[str] = None
    active: Optional[bool] = None
    actions: Optional[List[Dict[str, Any]]] = None
    conditions: Optional[List[Dict[str, Any]]] = None
    account_id: Optional[int] = None


class Status(Enum):
    open = "open"
    resolved = "resolved"
    pending = "pending"


class ContentType(Enum):
    text = "text"
    input_select = "input_select"
    cards = "cards"
    form = "form"


class MessageType(Enum):
    incoming = "incoming"
    outgoing = "outgoing"
    activity = "activity"
    template = "template"


@dataclass
class Message:
    content: Optional[str] = None
    content_type: Optional[ContentType] = None
    content_attributes: Optional[Dict[str, Any]] = None
    message_type: Optional[MessageType] = None
    created_at: Optional[int] = None
    private: Optional[bool] = None
    attachment: Optional[Dict[str, Any]] = None
    sender: Optional[Dict[str, Any]] = None
    conversation_id: Optional[float] = None


class Role(Enum):
    agent = "agent"
    administrator = "administrator"


class AvailabilityStatus(Enum):
    available = "available"
    busy = "busy"
    offline = "offline"


@dataclass
class Agent:
    id: Optional[int] = None
    uid: Optional[str] = None
    name: Optional[str] = None
    available_name: Optional[str] = None
    display_name: Optional[str] = None
    email: Optional[str] = None
    account_id: Optional[int] = None
    role: Optional[Role] = None
    confirmed: Optional[bool] = None
    availability_status: Optional[AvailabilityStatus] = None
    auto_offline: Optional[bool] = None
    custom_attributes: Optional[Dict[str, Any]] = None


@dataclass
class Inbox:
    id: Optional[float] = None
    name: Optional[str] = None
    website_url: Optional[str] = None
    channel_type: Optional[str] = None
    avatar_url: Optional[str] = None
    widget_color: Optional[str] = None
    website_token: Optional[str] = None
    enable_auto_assignment: Optional[bool] = None
    web_widget_script: Optional[str] = None
    welcome_title: Optional[str] = None
    welcome_tagline: Optional[str] = None
    greeting_enabled: Optional[bool] = None
    greeting_message: Optional[str] = None


@dataclass
class AgentBot:
    id: Optional[float] = None
    name: Optional[str] = None
    description: Optional[str] = None
    account_id: Optional[float] = None
    outgoing_url: Optional[str] = None


@dataclass
class ContactInboxes:
    source_id: Optional[str] = None
    inbox: Optional[Inbox] = None


@dataclass
class ContactableInboxes:
    source_id: Optional[str] = None
    inbox: Optional[Inbox] = None


class Type(Enum):
    conversation = "conversation"
    contact = "contact"
    report = "report"


@dataclass
class CustomFilter:
    id: Optional[float] = None
    name: Optional[str] = None
    type: Optional[Type] = None
    query: Optional[Dict[str, Any]] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None


class Subscription(Enum):
    conversation_created = "conversation_created"
    conversation_status_changed = "conversation_status_changed"
    conversation_updated = "conversation_updated"
    message_created = "message_created"
    message_updated = "message_updated"
    webwidget_triggered = "webwidget_triggered"


@dataclass
class Webhook:
    id: Optional[float] = None
    url: Optional[str] = None
    subscriptions: Optional[List[Subscription]] = None
    account_id: Optional[float] = None


class Role2(Enum):
    administrator = "administrator"
    agent = "agent"


@dataclass
class Account:
    id: Optional[float] = None
    name: Optional[str] = None
    role: Optional[Role2] = None


@dataclass
class PlatformAccount:
    id: Optional[float] = None
    name: Optional[str] = None


@dataclass
class Team:
    id: Optional[float] = None
    name: Optional[str] = None
    description: Optional[str] = None
    allow_auto_assign: Optional[bool] = None
    account_id: Optional[float] = None
    is_member: Optional[bool] = None


@dataclass
class IntegrationsApp:
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    hook_type: Optional[str] = None
    enabled: Optional[bool] = None
    allow_multiple_hooks: Optional[bool] = None
    hooks: Optional[List[Dict[str, Any]]] = None


@dataclass
class IntegrationsHook:
    id: Optional[str] = None
    app_id: Optional[str] = None
    inbox_id: Optional[str] = None
    account_id: Optional[str] = None
    status: Optional[bool] = None
    hook_type: Optional[bool] = None
    settings: Optional[Dict[str, Any]] = None


@dataclass
class PublicContact:
    id: Optional[int] = None
    source_id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
    pubsub_token: Optional[str] = None


@dataclass
class PublicConversation:
    id: Optional[int] = None
    inbox_id: Optional[str] = None
    messages: Optional[List[Message]] = None
    contact: Optional[Dict[str, Any]] = None


@dataclass
class PublicMessage:
    id: Optional[str] = None
    content: Optional[str] = None
    message_type: Optional[str] = None
    content_type: Optional[str] = None
    content_attributes: Optional[str] = None
    created_at: Optional[str] = None
    conversation_id: Optional[str] = None
    attachments: Optional[List[Dict[str, Any]]] = None
    sender: Optional[Dict[str, Any]] = None


@dataclass
class AccountCreateUpdatePayload:
    name: Optional[str] = None


@dataclass
class AgentBotCreateUpdatePayload:
    name: Optional[str] = None
    description: Optional[str] = None
    outgoing_url: Optional[str] = None


@dataclass
class UserCreateUpdatePayload:
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    custom_attributes: Optional[Dict[str, Any]] = None


@dataclass
class CannedResponseCreateUpdatePayload:
    content: Optional[str] = None
    short_code: Optional[str] = None


@dataclass
class CustomAttributeCreateUpdatePayload:
    attribute_display_name: Optional[str] = None
    attribute_display_type: Optional[int] = None
    attribute_description: Optional[str] = None
    attribute_key: Optional[str] = None
    attribute_values: Optional[List[str]] = None
    attribute_model: Optional[int] = None


@dataclass
class ContactCreate:
    inbox_id: float
    name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    avatar: Optional[bytes] = None
    avatar_url: Optional[str] = None
    identifier: Optional[str] = None
    custom_attributes: Optional[Dict[str, Any]] = None


@dataclass
class ContactUpdate:
    name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    avatar: Optional[bytes] = None
    avatar_url: Optional[str] = None
    identifier: Optional[str] = None
    custom_attributes: Optional[Dict[str, Any]] = None


class MessageType1(Enum):
    outgoing = "outgoing"
    incoming = "incoming"


class ContentType1(Enum):
    input_email = "input_email"
    cards = "cards"
    input_select = "input_select"
    form = "form"
    article = "article"


@dataclass
class ConversationMessageCreate:
    content: str
    message_type: Optional[MessageType1] = None
    private: Optional[bool] = None
    content_type: Optional[ContentType1] = None
    content_attributes: Optional[Dict[str, Any]] = None


@dataclass
class ConversationMessageAttachmentCreate:
    content: str
    files: Optional[Dict[str, Union[str, Any]]] = None
    message_type: Optional[MessageType1] = None
    file_type: Optional[str] = None


@dataclass
class TeamCreateUpdatePayload:
    name: Optional[str] = None
    description: Optional[str] = None
    allow_auto_assign: Optional[bool] = None


@dataclass
class CustomFilterCreateUpdatePayload:
    name: Optional[str] = None
    type: Optional[Type] = None
    query: Optional[Dict[str, Any]] = None


@dataclass
class WebhookCreateUpdatePayload:
    url: Optional[str] = None
    subscriptions: Optional[List[Subscription]] = None


@dataclass
class IntegrationsHookCreatePayload:
    app_id: Optional[str] = None
    inbox_id: Optional[str] = None
    settings: Optional[Dict[str, Any]] = None


@dataclass
class IntegrationsHookUpdatePayload:
    settings: Optional[Dict[str, Any]] = None


@dataclass
class AutomationRuleCreateUpdatePayload:
    name: Optional[str] = None
    description: Optional[str] = None
    event_name: Optional[EventName] = None
    active: Optional[bool] = None
    actions: Optional[List[Dict[str, Any]]] = None
    conditions: Optional[List[Dict[str, Any]]] = None


@dataclass
class PublicContactCreateUpdatePayload:
    identifier: Optional[str] = None
    identifier_hash: Optional[str] = None
    email: Optional[str] = None
    name: Optional[str] = None
    phone_number: Optional[str] = None
    avatar_url: Optional[str] = None
    custom_attributes: Optional[Dict[str, Any]] = None


@dataclass
class PublicMessageCreatePayload:
    content: Optional[str] = None
    echo_id: Optional[str] = None


@dataclass
class PublicMessageUpdatePayload:
    submitted_values: Optional[Dict[str, Any]] = None


class AvailabilityStatus1(Enum):
    online = "online"
    offline = "offline"


@dataclass
class Sender:
    id: Optional[float] = None
    name: Optional[str] = None
    thumbnail: Optional[str] = None
    channel: Optional[str] = None


@dataclass
class Meta1:
    mine_count: Optional[float] = None
    unassigned_count: Optional[float] = None
    assigned_count: Optional[float] = None
    all_count: Optional[float] = None


class CurrentStatus(Enum):
    open = "open"
    resolved = "resolved"


@dataclass
class Payload:
    success: Optional[bool] = None
    current_status: Optional[CurrentStatus] = None
    conversation_id: Optional[float] = None


@dataclass
class ConversationStatusToggle:
    status: Status


@dataclass
class ConversationLabels:
    payload: Optional[List[str]] = None


@dataclass
class ExtendedMessage(GenericId, Message):
    source_id: Optional[float] = None
    sender: Optional[Dict[str, Any]] = None


@dataclass
class Previous:
    avg_first_response_time: Optional[str] = None
    avg_resolution_time: Optional[str] = None
    conversations_count: Optional[float] = None
    incoming_messages_count: Optional[float] = None
    outgoing_messages_count: Optional[float] = None
    resolutions_count: Optional[float] = None


@dataclass
class AccountSummary:
    avg_first_response_time: Optional[str] = None
    avg_resolution_time: Optional[str] = None
    conversations_count: Optional[float] = None
    incoming_messages_count: Optional[float] = None
    outgoing_messages_count: Optional[float] = None
    resolutions_count: Optional[float] = None
    previous: Optional[Previous] = None


@dataclass
class Metric:
    open: Optional[float] = None
    unattended: Optional[float] = None


@dataclass
class AgentConversationMetrics:
    id: Optional[float] = None
    name: Optional[str] = None
    email: Optional[str] = None
    thumbnail: Optional[str] = None
    availability: Optional[str] = None
    metric: Optional[Metric] = None


@dataclass
class PlatformApiV1AccountsAccountIdAccountUsersGetResponse:
    account_id: Optional[int] = None
    user_id: Optional[int] = None
    role: Optional[str] = None


@dataclass
class PlatformApiV1AccountsAccountIdAccountUsersPostRequest:
    user_id: int
    role: str


@dataclass
class PlatformApiV1AccountsAccountIdAccountUsersPostResponse:
    account_id: Optional[int] = None
    user_id: Optional[int] = None
    role: Optional[str] = None


@dataclass
class PlatformApiV1AccountsAccountIdAccountUsersDeleteRequest:
    user_id: int


@dataclass
class PlatformApiV1UsersIdLoginGetResponse:
    url: Optional[str] = None


class Role3(Enum):
    agent = "agent"
    administrator = "administrator"


class AvailabilityStatus2(Enum):
    available = "available"
    busy = "busy"
    offline = "offline"


@dataclass
class ApiV1AccountsAccountIdAgentsPostRequest:
    name: str
    email: str
    role: Role3
    availability_status: Optional[AvailabilityStatus2] = None
    auto_offline: Optional[bool] = None


class Availability(Enum):
    available = "available"
    busy = "busy"
    offline = "offline"


@dataclass
class ApiV1AccountsAccountIdAgentsIdPatchRequest:
    role: Role3
    availability: Optional[Availability] = None
    auto_offline: Optional[bool] = None


class AttributeModel(Enum):
    field_0 = "0"
    field_1 = "1"


@dataclass
class ApiV1AccountsAccountIdCustomAttributeDefinitionsGetParametersQuery:
    attribute_model: AttributeModel


class Sort(Enum):
    name = "name"
    email = "email"
    phone_number = "phone_number"
    last_activity_at = "last_activity_at"
    field_name = "-name"
    field_email = "-email"
    field_phone_number = "-phone_number"
    field_last_activity_at = "-last_activity_at"


@dataclass
class ApiV1AccountsAccountIdContactsGetParametersQuery:
    sort: Optional[Sort] = None
    page: Optional[int] = 1


@dataclass
class ApiV1AccountsAccountIdContactsSearchGetParametersQuery:
    q: Optional[str] = None
    sort: Optional[Sort] = None
    page: Optional[int] = 1


@dataclass
class ApiV1AccountsAccountIdContactsFilterPostParametersQuery:
    page: Optional[int] = None


class FilterOperator(Enum):
    equal_to = "equal_to"
    not_equal_to = "not_equal_to"
    contains = "contains"
    does_not_contain = "does_not_contain"


class QueryOperator(Enum):
    AND = "AND"
    OR = "OR"


@dataclass
class ApiV1AccountsAccountIdContactsFilterPostRequest:
    attribute_key: Optional[str] = None
    filter_operator: Optional[FilterOperator] = None
    values: Optional[List[str]] = None
    query_operator: Optional[QueryOperator] = None


@dataclass
class ApiV1AccountsAccountIdContactsIdContactInboxesPostRequest:
    inbox_id: float
    source_id: Optional[str] = None


@dataclass
class ApiV1AccountsAccountIdAutomationRulesGetParametersQuery:
    page: Optional[int] = 1


class Status1(Enum):
    open = "open"
    resolved = "resolved"
    pending = "pending"
    snoozed = "snoozed"


@dataclass
class ApiV1AccountsAccountIdConversationsMetaGetParametersQuery:
    q: Optional[str] = None
    inbox_id: Optional[int] = None
    team_id: Optional[int] = None
    labels: Optional[List[str]] = None
    status: Optional[Status1] = "open"


@dataclass
class ApiV1AccountsAccountIdConversationsMetaGetResponse:
    meta: Optional[Meta1] = None


class AssigneeType(Enum):
    me = "me"
    unassigned = "unassigned"
    all = "all"
    assigned = "assigned"


@dataclass
class ApiV1AccountsAccountIdConversationsGetParametersQuery:
    q: Optional[str] = None
    inbox_id: Optional[int] = None
    team_id: Optional[int] = None
    labels: Optional[List[str]] = None
    assignee_type: Optional[AssigneeType] = "all"
    status: Optional[Status1] = "open"
    page: Optional[int] = 1


class Status3(Enum):
    open = "open"
    resolved = "resolved"
    pending = "pending"


@dataclass
class ApiV1AccountsAccountIdConversationsPostRequest:
    source_id: Optional[str] = None
    inbox_id: Optional[str] = None
    contact_id: Optional[str] = None
    additional_attributes: Optional[Dict[str, Any]] = None
    custom_attributes: Optional[Dict[str, Any]] = None
    status: Optional[Status3] = None
    assignee_id: Optional[str] = None
    team_id: Optional[str] = None


@dataclass
class ApiV1AccountsAccountIdConversationsPostResponse:
    id: Optional[float] = None
    account_id: Optional[float] = None
    inbox_id: Optional[float] = None


@dataclass
class ApiV1AccountsAccountIdConversationsFilterPostParametersQuery:
    page: Optional[int] = None


@dataclass
class ApiV1AccountsAccountIdConversationsFilterPostRequest:
    attribute_key: Optional[str] = None
    filter_operator: Optional[FilterOperator] = None
    values: Optional[List[str]] = None
    query_operator: Optional[QueryOperator] = None


@dataclass
class ApiV1AccountsAccountIdConversationsConversationIdToggleStatusPostRequest:
    status: Status3


@dataclass
class ApiV1AccountsAccountIdConversationsConversationIdAssignmentsPostRequest:
    assignee_id: Optional[float] = None
    team_id: Optional[float] = None


@dataclass
class ApiV1AccountsAccountIdConversationsConversationIdLabelsPostRequest:
    labels: Optional[List[str]] = None


class Type2(Enum):
    web_widget = "web_widget"


@dataclass
class Channel:
    type: Optional[Type2] = None
    website_url: Optional[str] = None
    welcome_title: Optional[str] = None
    welcome_tagline: Optional[str] = None
    agent_away_message: Optional[str] = None
    widget_color: Optional[str] = None


@dataclass
class ApiV1AccountsAccountIdInboxesPostRequest:
    name: Optional[str] = None
    avatar: Optional[bytes] = None
    channel: Optional[Channel] = None


@dataclass
class Channel1:
    website_url: Optional[str] = None
    welcome_title: Optional[str] = None
    welcome_tagline: Optional[str] = None
    agent_away_message: Optional[str] = None
    widget_color: Optional[str] = None


@dataclass
class ApiV1AccountsAccountIdInboxesIdPatchRequest:
    enable_auto_assignment: bool
    name: Optional[str] = None
    avatar: Optional[bytes] = None
    channel: Optional[Channel1] = None


@dataclass
class ApiV1AccountsAccountIdInboxesIdSetAgentBotPostRequest:
    agent_bot: float


@dataclass
class ApiV1AccountsAccountIdInboxMembersInboxIdDeleteRequest:
    user_ids: List[int]
    inbox_id: str = Field(alias="inbox_id_")


@dataclass
class ApiV1AccountsAccountIdInboxMembersPostRequest:
    inbox_id: str
    user_ids: List[int]


@dataclass
class ApiV1AccountsAccountIdInboxMembersPatchRequest:
    inbox_id: str
    user_ids: List[int]


@dataclass
class ApiV1AccountsAccountIdConversationsConversationIdMessagesGetResponse(
    GenericId, Message
):
    pass


@dataclass
class ApiV1AccountsAccountIdConversationsConversationIdMessagesPostResponse(
    GenericId, Message
):
    pass


@dataclass
class AccountsAccountIdTeamsTeamIdTeamMembersPostRequest:
    user_ids: List[int]


@dataclass
class AccountsAccountIdTeamsTeamIdTeamMembersPatchRequest:
    user_ids: List[int]


@dataclass
class AccountsAccountIdTeamsTeamIdTeamMembersDeleteRequest:
    user_ids: List[int]


class FilterType(Enum):
    conversation = "conversation"
    contact = "contact"
    report = "report"


@dataclass
class ApiV1AccountsAccountIdCustomFiltersGetParametersQuery:
    filter_type: Optional[FilterType] = None


@dataclass
class ApiV1AccountsAccountIdCustomFiltersPostParametersQuery:
    filter_type: Optional[FilterType] = None


class Metric1(Enum):
    conversations_count = "conversations_count"
    incoming_messages_count = "incoming_messages_count"
    outgoing_messages_count = "outgoing_messages_count"
    avg_first_response_time = "avg_first_response_time"
    avg_resolution_time = "avg_resolution_time"
    resolutions_count = "resolutions_count"


class Type3(Enum):
    account = "account"
    agent = "agent"
    inbox = "inbox"
    label = "label"
    team = "team"


@dataclass
class ApiV2AccountsAccountIdReportsGetParametersQuery:
    metric: Metric1
    type: Type3
    id: Optional[str] = None
    since: Optional[str] = None
    until: Optional[str] = None


@dataclass
class ApiV2AccountsAccountIdReportsGetResponse:
    value: Optional[str] = None
    timestamp: Optional[float] = None


@dataclass
class ApiV2AccountsAccountIdReportsSummaryGetParametersQuery:
    type: Type3
    id: Optional[str] = None
    since: Optional[str] = None
    until: Optional[str] = None


class Type5(Enum):
    account = "account"


@dataclass
class ApiV2AccountsAccountIdReportsConversationsGetParametersQuery:
    type: Type5


@dataclass
class ApiV2AccountsAccountIdReportsConversationsGetResponse:
    open: Optional[float] = None
    unattended: Optional[float] = None
    unassigned: Optional[float] = None


class Type6(Enum):
    agent = "agent"


@dataclass
class ApiV2AccountsAccountIdReportsConversationsGetParametersQuery1:
    type: Type6
    user_id: Optional[str] = None


@dataclass
class BadRequestError:
    description: Optional[str] = None
    errors: Optional[List[RequestError]] = None


@dataclass
class Contact:
    email: Optional[str] = None
    name: Optional[str] = None
    phone_number: Optional[str] = None
    thumbnail: Optional[str] = None
    additional_attributes: Optional[Dict[str, Any]] = None
    custom_attributes: Optional[Dict[str, Any]] = None
    contact_inboxes: Optional[List[ContactInboxes]] = None


@dataclass
class Conversation:
    id: Optional[float] = None
    messages: Optional[List[Message]] = None
    account_id: Optional[float] = None
    inbox_id: Optional[float] = None
    status: Optional[Status] = None
    timestamp: Optional[str] = None
    contact_last_seen_at: Optional[str] = None
    agent_last_seen_at: Optional[str] = None
    unread_count: Optional[float] = None
    additional_attributes: Optional[Dict[str, Any]] = None
    custom_attributes: Optional[Dict[str, Any]] = None


@dataclass
class User:
    id: Optional[float] = None
    uid: Optional[str] = None
    name: Optional[str] = None
    available_name: Optional[str] = None
    display_name: Optional[str] = None
    email: Optional[str] = None
    account_id: Optional[float] = None
    role: Optional[Role] = None
    confirmed: Optional[bool] = None
    custom_attributes: Optional[Dict[str, Any]] = None
    accounts: Optional[List[Account]] = None


@dataclass
class ExtendedContact(Contact):
    id: Optional[float] = None
    availability_status: Optional[AvailabilityStatus1] = None


@dataclass
class ContactBase(GenericId, Contact):
    pass


@dataclass
class ContactListItem(GenericId, Contact):
    pass


ContactList = List[ContactListItem]


@dataclass
class Meta:
    sender: Optional[Sender] = None
    assignee: Optional[User] = None


@dataclass
class ContactConversation(Conversation):
    meta: Optional[Meta] = None
    display_id: Optional[float] = None


ContactConversations = List[ContactConversation]


@dataclass
class Meta2:
    sender: Optional[Sender] = None
    assignee: Optional[User] = None


@dataclass
class PayloadItem(GenericId, Conversation):
    meta: Optional[Meta2] = None


@dataclass
class Data:
    meta: Optional[Meta1] = None
    payload: Optional[List[PayloadItem]] = None


@dataclass
class ConversationList:
    data: Optional[Data] = None


@dataclass
class Meta3:
    sender: Optional[Sender] = None
    assignee: Optional[User] = None


@dataclass
class ConversationShow(GenericId, Conversation):
    meta: Optional[Meta3] = None


@dataclass
class ApiV1AccountsAccountIdContactsSearchGetResponse:
    payload: Optional[ContactList] = None
