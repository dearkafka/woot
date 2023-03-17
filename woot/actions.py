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
        method="GET",
        url="platform/api/v1/accounts/{account_id}/account_users",
    )
    create: Action = Action(
        method="POST",
        url="platform/api/v1/accounts/{account_id}/account_users",
        schema_=ws.PlatformApiV1AccountsAccountIdAccountUsersPostRequest,
    )
    delete: Action = Action(
        method="DELETE",
        url="platform/api/v1/accounts/{account_id}/account_users/",
        schema_=ws.PlatformApiV1AccountsAccountIdAccountUsersDeleteRequest,
    )


@dataclass
class AgentBotsActions:
    list: Action = Action(method="GET", url="platform/api/v1/agent_bots")
    create: Action = Action(
        method="POST",
        url="platform/api/v1/agent_bots",
        schema_=ws.AgentBotCreateUpdatePayload,
    )
    get: Action = Action(method="GET", url="platform/api/v1/agent_bots/{id}")
    update: Action = Action(
        method="PATCH",
        url="platform/api/v1/agent_bots/{id}",
        schema_=ws.AgentBotCreateUpdatePayload,
    )
    delete: Action = Action(method="DELETE", url="platform/api/v1/agent_bots/{id}")


@dataclass
class UsersActions:
    list: Action = Action(method="GET", url="platform/api/v1/users")
    create: Action = Action(
        method="POST", url="platform/api/v1/users/", schema_=ws.UserCreateUpdatePayload
    )
    get: Action = Action(method="GET", url="platform/api/v1/users/{id}")
    update: Action = Action(
        method="PATCH",
        url="platform/api/v1/users/{id}",
        schema_=ws.UserCreateUpdatePayload,
    )
    delete: Action = Action(method="DELETE", url="platform/api/v1/users/{id}")
    get_sso_link: Action = Action(method="GET", url="platform/api/v1/users/{id}/login")


@dataclass
class AccountAgentBotActions:
    list: Action = Action(method="GET", url="api/v1/accounts/{account_id}/agent_bots")
    create: Action = Action(
        method="POST",
        url="api/v1/accounts/{account_id}/agent_bots",
        schema_=ws.AgentBotCreateUpdatePayload,
    )
    delete: Action = Action(
        method="DELETE", url="api/v1/accounts/{account_id}/agent_bots/{id}"
    )
    get: Action = Action(
        method="GET", url="api/v1/accounts/{account_id}/agent_bots/{id}"
    )
    update: Action = Action(
        method="PATCH",
        url="api/v1/accounts/{account_id}/agent_bots/{id}",
        schema_=ws.AgentBotCreateUpdatePayload,
    )


@dataclass
class AgentsActions:
    list: Action = Action(method="GET", url="api/v1/accounts/{account_id}/agents")
    create: Action = Action(
        method="POST",
        url="api/v1/accounts/{account_id}/agents",
        schema_=ws.ApiV1AccountsAccountIdAgentsPostRequest,
    )
    update: Action = Action(
        method="PATCH",
        url="api/v1/accounts/{account_id}/agents/{id}",
        schema_=ws.ApiV1AccountsAccountIdAgentsIdPatchRequest,
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
        method="POST",
        url="api/v1/accounts/{account_id}/canned_responses",
        schema_=ws.CannedResponseCreateUpdatePayload,
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
    create: Action = Action(
        method="POST",
        url="api/v1/accounts/{account_id}/contacts",
        schema_=ws.ContactCreate,
    )
    update: Action = Action(
        method="PATCH",
        url="api/v1/accounts/{account_id}/contacts/{id}",
        schema_=ws.ContactUpdate,
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
        schema_=ws.ApiV1AccountsAccountIdConversationsConversationIdAssignmentsPostRequest,
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
        schema_=ws.ApiV1AccountsAccountIdConversationsConversationIdLabelsPostRequest,
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
        method="POST",
        url="api/v1/accounts/{account_id}/conversations",
        schema_=ws.ApiV1AccountsAccountIdConversationsPostRequest,
    )
    get: Action = Action(
        method="GET",
        url="api/v1/accounts/{account_id}/conversations/{conversation_id}",
    )
    filter: Action = Action(
        method="GET",
        url="api/v1/accounts/{account_id}/conversations/filter",
        query=ws.ApiV1AccountsAccountIdConversationsFilterPostParametersQuery,
        schema_=ws.ApiV1AccountsAccountIdConversationsFilterPostRequest,
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
        method="POST",
        url="api/v1/accounts/{account_id}/custom_attribute_definitions",
        schema_=ws.CustomAttributeCreateUpdatePayload,
    )
    get: Action = Action(
        method="GET",
        url="api/v1/accounts/{account_id}/custom_attribute_definitions/{id}",
    )
    update: Action = Action(
        method="PATCH",
        url="api/v1/accounts/{account_id}/custom_attribute_definitions/{id}",
        schema_=ws.CustomAttributeCreateUpdatePayload,
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
        schema_=ws.CustomFilterCreateUpdatePayload,
    )
    get: Action = Action(
        method="GET",
        url="api/v1/accounts/{account_id}/custom_filters/{custom_filter_id}",
    )
    update: Action = Action(
        method="PATCH",
        url="api/v1/accounts/{account_id}/custom_filters/{custom_filter_id}",
        schema_=ws.CustomFilterCreateUpdatePayload,
    )
    delete: Action = Action(
        method="DELETE",
        url="api/v1/accounts/{account_id}/custom_filters/{custom_filter_id}",
    )


@dataclass
class InboxActions:
    list: Action = Action(method="GET", url="api/v1/accounts/{account_id}/inboxes")
    create: Action = Action(
        method="POST",
        url="api/v1/accounts/{account_id}/inboxes",
        schema_=ws.ApiV1AccountsAccountIdInboxesPostRequest,
    )
    get: Action = Action(method="GET", url="api/v1/accounts/{account_id}/inboxes/{id}")
    update: Action = Action(
        method="PATCH",
        url="api/v1/accounts/{account_id}/inboxes/{id}",
        schema_=ws.ApiV1AccountsAccountIdInboxesIdPatchRequest,
    )
    delete: Action = Action(
        method="DELETE", url="api/v1/accounts/{account_id}/inboxes/{id}"
    )
    get_associated_agent_bot: Action = Action(
        method="GET", url="api/v1/accounts/{account_id}/inboxes/{id}/agent_bot"
    )
    set_agent_bot: Action = Action(
        method="POST",
        url="api/v1/accounts/{account_id}/inboxes/{id}/set_agent_bot",
        schema_=ws.ApiV1AccountsAccountIdInboxesIdSetAgentBotPostRequest,
    )
    list_agents: Action = Action(
        method="GET", url="api/v1/accounts/{account_id}/inbox_members/{inbox_id}"
    )
    delete_agent: Action = Action(
        method="DELETE",
        url="api/v1/accounts/{account_id}/inbox_members/{inbox_id}",
        schema_=ws.ApiV1AccountsAccountIdInboxMembersInboxIdDeleteRequest,
    )
    add_agent: Action = Action(
        method="POST",
        url="api/v1/accounts/{account_id}/inbox_members",
        schema_=ws.ApiV1AccountsAccountIdInboxMembersPostRequest,
    )
    update_agent: Action = Action(
        method="PATCH",
        url="api/v1/accounts/{account_id}/inbox_members",
        schema_=ws.ApiV1AccountsAccountIdInboxMembersPatchRequest,
    )


@dataclass
class IntegrationsActions:
    list: Action = Action(
        method="GET", url="api/v1/accounts/{account_id}/integrations/apps"
    )
    create: Action = Action(
        method="POST",
        url="api/v1/accounts/{account_id}/integrations/hooks",
        schema_=ws.IntegrationsHookCreatePayload,
    )
    update: Action = Action(
        method="PATCH",
        url="api/v1/accounts/{account_id}/integrations/hooks/{hook_id}",
        schema_=ws.IntegrationsHookUpdatePayload,
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
        schema_=ws.ConversationMessageCreate,
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
    create: Action = Action(
        method="POST",
        url="api/v1/accounts/{account_id}/teams",
        schema_=ws.TeamCreateUpdatePayload,
    )
    get: Action = Action(
        method="GET", url="api/v1/accounts/{account_id}/teams/{team_id}"
    )
    update: Action = Action(
        method="PATCH",
        url="api/v1/accounts/{account_id}/teams/{team_id}",
        schema_=ws.TeamCreateUpdatePayload,
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
        schema_=ws.AccountsAccountIdTeamsTeamIdTeamMembersDeleteRequest,
    )
    add_agent: Action = Action(
        method="POST",
        url="api/v1/accounts/{account_id}/teams/{team_id}/team_members",
        schema_=ws.AccountsAccountIdTeamsTeamIdTeamMembersPostRequest,
    )
    update_agent: Action = Action(
        method="PATCH",
        url="api/v1/accounts/{account_id}/teams/{team_id}/team_members",
        schema_=ws.AccountsAccountIdTeamsTeamIdTeamMembersPatchRequest,
    )


@dataclass
class WebhooksActions:
    list: Action = Action(method="GET", url="api/v1/accounts/{account_id}/webhooks")
    create: Action = Action(
        method="POST",
        url="api/v1/accounts/{account_id}/webhooks",
        schema_=ws.WebhookCreateUpdatePayload,
    )
    update: Action = Action(
        method="PATCH",
        url="api/v1/accounts/{account_id}/webhooks/{webhook_id}",
        schema_=ws.WebhookCreateUpdatePayload,
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
        method="POST",
        url="api/v1/accounts/{account_id}/automation_rules",
        schema_=ws.AutomationRuleCreateUpdatePayload,
    )
    get: Action = Action(
        method="GET", url="api/v1/accounts/{account_id}/automation_rules/{id}"
    )
    update: Action = Action(
        method="PATCH",
        url="api/v1/accounts/{account_id}/automation_rules/{id}",
        schema_=ws.AutomationRuleCreateUpdatePayload,
    )
    delete: Action = Action(
        method="DELETE", url="api/v1/accounts/{account_id}/automation_rules/{id}"
    )


@dataclass
class ClientContactsActions:
    create: Action = Action(
        method="POST",
        url="public/api/v1/inboxes/{inbox_identifier}/contacts",
        schema_=ws.PublicContactCreateUpdatePayload,
    )
    get: Action = Action(
        method="GET",
        url="public/api/v1/inboxes/{inbox_identifier}/contacts/{contact_identifier}",
    )
    update: Action = Action(
        method="PATCH",
        url="public/api/v1/inboxes/{inbox_identifier}/contacts/{contact_identifier}",
        schema_=ws.PublicContactCreateUpdatePayload,
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
        schema_=ws.PublicMessageCreatePayload,
    )
    update: Action = Action(
        method="PATCH",
        url="public/api/v1/inboxes/{inbox_identifier}/contacts/{contact_identifier}/conversations/{conversation_id}/messages/{message_id}",
        schema_=ws.PublicMessageUpdatePayload,
    )
