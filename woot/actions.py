""" All actions for resources are defined here. """

from typing import Any, Optional, Union, Type
from pydantic.dataclasses import dataclass

import woot.schema as ws


# I want to use pydantic's dataclass decorator and I also want default values.
class WootAction:
    def __getitem__(self, item):
        return getattr(self, item)


@dataclass
class Action(WootAction):
    method: str
    url: str
    query: Optional[Union[Type, Any]] = None
    schema_: Optional[Union[Type, Any]] = None


@dataclass
class AccountActions(WootAction):
    create: Action = Action(
        method="POST",
        url="platform/api/v1/accounts",
        schema_=ws.AccountCreateUpdatePayload,
    )
    get: Action = Action(
        method="GET",
        url="platform/api/v1/accounts/{account_id}",
    )
    update: Action = Action(
        method="PATCH",
        url="platform/api/v1/accounts/{account_id}",
        schema_=ws.AccountCreateUpdatePayload,
    )
    delete: Action = Action(
        method="DELETE",
        url="platform/api/v1/accounts/{account_id}",
        schema_=ws.PlatformApiV1AccountsAccountIdAccountUsersDeleteRequest,
    )


@dataclass
class AccountUsersActions:
    list: Action = Action(
        method="GET", url="platform/api/v1/accounts/{account_id}/account_users"
    )
    create: Action = Action(
        method="POST", url="platform/api/v1/accounts/{account_id}/account_users"
    )
    delete: Action = Action(
        method="DELETE", url="platform/api/v1/accounts/{account_id}/account_users/"
    )


@dataclass
class AgentBotsActions:
    list: Action = Action(method="GET", url="platform/api/v1/agent_bots")
    create: Action = Action(method="POST", url="platform/api/v1/agent_bots")
    get: Action = Action(method="GET", url="platform/api/v1/agent_bots/{id}")
    update: Action = Action(method="PATCH", url="platform/api/v1/agent_bots/{id}")
    delete: Action = Action(method="DELETE", url="platform/api/v1/agent_bots/{id}")


@dataclass
class UsersActions:
    list: Action = Action(method="GET", url="platform/api/v1/users")
    create: Action = Action(method="POST", url="platform/api/v1/users/")
    get: Action = Action(method="GET", url="platform/api/v1/users/{id}")
    update: Action = Action(method="PATCH", url="platform/api/v1/users/{id}")
    delete: Action = Action(method="DELETE", url="platform/api/v1/users/{id}")
    get_sso_link: Action = Action(method="GET", url="platform/api/v1/users/{id}/login")


@dataclass
class AccountAgentBotActions:
    list: Action = Action(method="GET", url="api/v1/accounts/{account_id}/agent_bots")
    create: Action = Action(
        method="POST", url="api/v1/accounts/{account_id}/agent_bots"
    )
    delete: Action = Action(
        method="DELETE", url="api/v1/accounts/{account_id}/agent_bots/{id}"
    )
    get: Action = Action(
        method="GET", url="api/v1/accounts/{account_id}/agent_bots/{id}"
    )
    update: Action = Action(
        method="PATCH", url="api/v1/accounts/{account_id}/agent_bots/{id}"
    )


@dataclass
class AgentsActions:
    list: Action = Action(method="GET", url="api/v1/accounts/{account_id}/agents")
    create: Action = Action(method="POST", url="api/v1/accounts/{account_id}/agents")
    update: Action = Action(
        method="PATCH", url="api/v1/accounts/{account_id}/agents/{id}"
    )
    delete: Action = Action(
        method="DELETE", url="api/v1/accounts/{account_id}/agents/{id}"
    )


@dataclass
class CannedResponsesActions:
    list: Action = Action(
        method="GET", url="api/v1/accounts/{account_id}/canned_responses"
    )
    create: Action = Action(
        method="POST", url="api/v1/accounts/{account_id}/canned_responses"
    )
    delete: Action = Action(
        method="DELETE", url="api/v1/accounts/{account_id}/canned_responses/{id}"
    )


@dataclass
class ContactsActions:
    list: Action = Action(
        method="GET",
        url="api/v1/accounts/{account_id}/contacts",
        query=ws.ApiV1AccountsAccountIdContactsGetParametersQuery,
    )
    create: Action = Action(method="POST", url="api/v1/accounts/{account_id}/contacts")
    update: Action = Action(
        method="PATCH", url="api/v1/accounts/{account_id}/contacts/{id}"
    )
    delete: Action = Action(
        method="DELETE", url="api/v1/accounts/{account_id}/contacts/{id}"
    )
    get: Action = Action(method="GET", url="api/v1/accounts/{account_id}/contacts/{id}")
    get_conversations: Action = Action(
        method="GET", url="api/v1/accounts/{account_id}/contacts/{id}/conversations"
    )
    search: Action = Action(
        method="GET",
        url="api/v1/accounts/{account_id}/contacts/search",
        query=ws.ApiV1AccountsAccountIdContactsSearchGetParametersQuery,
    )
    filter: Action = Action(
        method="GET",
        url="api/v1/accounts/{account_id}/contacts/filter",
        schema_=ws.ApiV1AccountsAccountIdContactsFilterPostRequest,
        query=ws.ApiV1AccountsAccountIdContactsFilterPostParametersQuery,
    )


@dataclass
class ConversationAssignmentActions:
    assign: Action = Action(
        method="POST",
        url="api/v1/accounts/{account_id}/conversations/{conversation_id}/assignments",
    )


@dataclass
class ConversationLabelsActions:
    list: Action = Action(
        method="GET",
        url="api/v1/accounts/{account_id}/conversations/{conversation_id}/labels",
    )
    create: Action = Action(
        method="POST",
        url="api/v1/accounts/{account_id}/conversations/{conversation_id}/labels",
    )


@dataclass
class ConversationsActions:
    get_meta: Action = Action(
        method="GET",
        url="api/v1/accounts/{account_id}/conversations/meta",
        query=ws.ApiV1AccountsAccountIdConversationsMetaGetParametersQuery,
    )
    list: Action = Action(
        method="GET",
        url="api/v1/accounts/{account_id}/conversations",
        query=ws.ApiV1AccountsAccountIdConversationsGetParametersQuery,
    )
    create: Action = Action(
        method="POST", url="api/v1/accounts/{account_id}/conversations"
    )
    get: Action = Action(
        method="GET", url="api/v1/accounts/{account_id}/conversations/{conversation_id}"
    )
    filter: Action = Action(
        method="GET",
        url="api/v1/accounts/{account_id}/conversations/filter",
        query=ws.ApiV1AccountsAccountIdConversationsFilterPostParametersQuery,
    )
    toggle_status: Action = Action(
        method="POST",
        url="api/v1/accounts/{account_id}/conversations/{conversation_id}/toggle_status",
    )


@dataclass
class CustomAttributesActions:
    list: Action = Action(
        method="GET",
        url="api/v1/accounts/{account_id}/custom_attribute_definitions",
        query=ws.ApiV1AccountsAccountIdCustomAttributeDefinitionsGetParametersQuery,
    )
    create: Action = Action(
        method="POST", url="api/v1/accounts/{account_id}/custom_attribute_definitions"
    )
    get: Action = Action(
        method="GET",
        url="api/v1/accounts/{account_id}/custom_attribute_definitions/{id}",
    )
    update: Action = Action(
        method="PATCH",
        url="api/v1/accounts/{account_id}/custom_attribute_definitions/{id}",
    )
    delete: Action = Action(
        method="DELETE",
        url="api/v1/accounts/{account_id}/custom_attribute_definitions/{id}",
    )


@dataclass
class CustomFiltersActions:
    list: Action = Action(
        method="GET",
        url="api/v1/accounts/{account_id}/custom_filters",
        query=ws.ApiV1AccountsAccountIdCustomFiltersGetParametersQuery,
    )
    create: Action = Action(
        method="POST",
        url="api/v1/accounts/{account_id}/custom_filters",
        query=ws.ApiV1AccountsAccountIdCustomFiltersPostParametersQuery,
    )
    get: Action = Action(
        method="GET",
        url="api/v1/accounts/{account_id}/custom_filters/{custom_filter_id}",
    )
    update: Action = Action(
        method="PATCH",
        url="api/v1/accounts/{account_id}/custom_filters/{custom_filter_id}",
    )
    delete: Action = Action(
        method="DELETE",
        url="api/v1/accounts/{account_id}/custom_filters/{custom_filter_id}",
    )


@dataclass
class InboxActions:
    list: Action = Action(method="GET", url="api/v1/accounts/{account_id}/inboxes")
    create: Action = Action(method="POST", url="api/v1/accounts/{account_id}/inboxes")
    get: Action = Action(method="GET", url="api/v1/accounts/{account_id}/inboxes/{id}")
    update: Action = Action(
        method="PATCH", url="api/v1/accounts/{account_id}/inboxes/{id}"
    )
    delete: Action = Action(
        method="DELETE", url="api/v1/accounts/{account_id}/inboxes/{id}"
    )
    get_associated_agent_bot: Action = Action(
        method="GET", url="api/v1/accounts/{account_id}/inboxes/{id}/agent_bot"
    )
    set_agent_bot: Action = Action(
        method="POST", url="api/v1/accounts/{account_id}/inboxes/{id}/set_agent_bot"
    )
    list_agents: Action = Action(
        method="GET", url="api/v1/accounts/{account_id}/inbox_members/{inbox_id}"
    )
    delete_agent: Action = Action(
        method="DELETE", url="api/v1/accounts/{account_id}/inbox_members/{inbox_id}"
    )
    add_agent: Action = Action(
        method="POST", url="api/v1/accounts/{account_id}/inbox_members"
    )
    update_agent: Action = Action(
        method="PATCH", url="api/v1/accounts/{account_id}/inbox_members"
    )


@dataclass
class IntegrationsActions:
    list: Action = Action(
        method="GET", url="api/v1/accounts/{account_id}/integrations/apps"
    )
    create: Action = Action(
        method="POST", url="api/v1/accounts/{account_id}/integrations/hooks"
    )
    update: Action = Action(
        method="PATCH", url="api/v1/accounts/{account_id}/integrations/hooks/{hook_id}"
    )
    delete: Action = Action(
        method="DELETE", url="api/v1/accounts/{account_id}/integrations/hooks/{hook_id}"
    )


@dataclass
class MessagesActions:
    list: Action = Action(
        method="GET",
        url="api/v1/accounts/{account_id}/conversations/{conversation_id}/messages",
    )
    create: Action = Action(
        method="POST",
        url="api/v1/accounts/{account_id}/conversations/{conversation_id}/messages",
    )
    delete: Action = Action(
        method="DELETE",
        url="api/v1/accounts/{account_id}/conversations/{conversation_id}/messages/{message_id}",
    )


@dataclass
class ProfileActions:
    get: Action = Action(method="GET", url="api/v1/accounts/{account_id}/profile")


@dataclass
class ReportsActions:
    get_accounts_report: Action = Action(
        method="GET",
        url="api/v1/accounts/{account_id}/reports",
        query=ws.ApiV2AccountsAccountIdReportsGetParametersQuery,
    )
    get_account_report_summary: Action = Action(
        method="GET",
        url="api/v1/accounts/{account_id}/reports/summary",
        query=ws.ApiV2AccountsAccountIdReportsSummaryGetParametersQuery,
    )
    get_conversation_metrics_for_account: Action = Action(
        method="GET",
        url="api/v1/accounts/{account_id}/reports/conversations",
        query=ws.ApiV2AccountsAccountIdReportsConversationsGetParametersQuery,
    )
    get_conversation_metrics_for_agent: Action = Action(
        method="GET",
        url="api/v1/accounts/{account_id}/reports/conversations",
        query=ws.ApiV2AccountsAccountIdReportsConversationsGetParametersQuery1,
    )


@dataclass
class TeamsActions:
    list: Action = Action(method="GET", url="api/v1/accounts/{account_id}/teams")
    create: Action = Action(method="POST", url="api/v1/accounts/{account_id}/teams")
    get: Action = Action(
        method="GET", url="api/v1/accounts/{account_id}/teams/{team_id}"
    )
    update: Action = Action(
        method="PATCH", url="api/v1/accounts/{account_id}/teams/{team_id}"
    )
    delete: Action = Action(
        method="DELETE", url="api/v1/accounts/{account_id}/teams/{team_id}"
    )
    list_agents: Action = Action(
        method="GET", url="api/v1/accounts/{account_id}/teams/{team_id}/team_members"
    )
    delete_agent: Action = Action(
        method="DELETE",
        url="api/v1/accounts/{account_id}/teams/{team_id}/team_members}",
    )
    add_agent: Action = Action(
        method="POST", url="api/v1/accounts/{account_id}/teams/{team_id}/team_members"
    )
    update_agent: Action = Action(
        method="PATCH", url="api/v1/accounts/{account_id}/teams/{team_id}/team_members"
    )


@dataclass
class WebhooksActions:
    list: Action = Action(method="GET", url="api/v1/accounts/{account_id}/webhooks")
    create: Action = Action(method="POST", url="api/v1/accounts/{account_id}/webhooks")
    update: Action = Action(
        method="PATCH", url="api/v1/accounts/{account_id}/webhooks/{webhook_id}"
    )
    delete: Action = Action(
        method="DELETE", url="api/v1/accounts/{account_id}/webhooks/{webhook_id}"
    )


@dataclass
class AutomationRuleActions:
    list: Action = Action(
        method="GET",
        url="api/v1/accounts/{account_id}/automation_rules",
        query=ws.ApiV1AccountsAccountIdAutomationRulesGetParametersQuery,
    )
    create: Action = Action(
        method="POST", url="api/v1/accounts/{account_id}/automation_rules"
    )
    get: Action = Action(
        method="GET", url="api/v1/accounts/{account_id}/automation_rules/{id}"
    )
    update: Action = Action(
        method="PATCH", url="api/v1/accounts/{account_id}/automation_rules/{id}"
    )
    delete: Action = Action(
        method="DELETE", url="api/v1/accounts/{account_id}/automation_rules/{id}"
    )


@dataclass
class ClientContactsActions:
    create: Action = Action(
        method="POST", url="public/api/v1/inboxes/{inbox_identifier}/contacts"
    )
    get: Action = Action(
        method="GET",
        url="public/api/v1/inboxes/{inbox_identifier}/contacts/{contact_identifier}",
    )
    delete: Action = Action(
        method="DELETE",
        url="public/api/v1/inboxes/{inbox_identifier}/contacts/{contact_identifier}",
    )


@dataclass
class ClientConversationsActions:
    list: Action = Action(
        method="GET",
        url="public/api/v1/inboxes/{inbox_identifier}/contacts/{contact_identifier}/conversations",
    )
    create: Action = Action(
        method="POST",
        url="public/api/v1/inboxes/{inbox_identifier}/contacts/{contact_identifier}/conversations",
    )


@dataclass
class ClientMessagesActions:
    list: Action = Action(
        method="GET",
        url="public/api/v1/inboxes/{inbox_identifier}/contacts/{contact_identifier}/conversations/{conversation_id}/messages",
    )
    create: Action = Action(
        method="POST",
        url="public/api/v1/inboxes/{inbox_identifier}/contacts/{contact_identifier}/conversations/{conversation_id}/messages",
    )
    update: Action = Action(
        method="PATCH",
        url="public/api/v1/inboxes/{inbox_identifier}/contacts/{contact_identifier}/conversations/{conversation_id}/messages/{message_id}",
    )
