""" Resources for the simple_rest_client to work with chatwoot API.

P.S. I'm proud of this one.
"""
import re
import pprint
import httpx
from httpx import URL
from urllib.parse import unquote
import functools
from dataclasses import fields
from types import MethodType
from simple_rest_client.resource import (
    Resource,
    BaseResource,
    make_async_request,
    Request,
)
from simple_rest_client.exceptions import ActionURLMatchError


import woot.actions as a
from woot.utils import update_signature, extract_path_params


class ActionMeta(type):
    def __new__(cls, name, bases, attrs, actions):
        attrs["default_actions"] = {v.name: v.default for v in fields(actions)}
        new_class = super().__new__(cls, name, bases, attrs)
        return new_class


class WootResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for action_name in self.actions.keys():
            self.update_action(action_name)

    def update_action(self, action_name):
        action_schema = self.actions[action_name].schema_
        action_query = self.actions[action_name].query
        url_params = extract_path_params(self.actions[action_name].url)
        if action_schema is not None:
            action_schema = action_schema.__dataclass_fields__
        else:
            action_schema = {}
        if action_query is not None:
            action_query = action_query.__dataclass_fields__
        else:
            action_query = {}

        action_method = getattr(self, action_name)

        @update_signature(action_schema, action_name, url_params, action_query)
        def wrapped_action_method(self, *args, **kwargs):
            if len(args) > 0:
                raise TypeError("Positional arguments are not allowed")

            schema_fields = action_schema.keys()
            query_params = action_query.keys()
            parts = {k: str(v) for k, v in kwargs.items() if k in url_params}
            query = {k: v for k, v in kwargs.items() if k in query_params}
            body = {k: v for k, v in kwargs.items() if k in schema_fields}
            kwargs = {
                k: v
                for k, v in kwargs.items()
                if k not in body and k not in parts and k not in query
            }
            self.actions[action_name].url = unquote(
                str(URL(self.actions[action_name].url).copy_merge_params(params=query))
            )

            return action_method(
                *parts.values(),
                body=body,
                params=None,
                headers=None,
                action_name=action_name,
                **kwargs,
            )

        setattr(self, action_name, MethodType(wrapped_action_method, self))

    def get_action_full_url(self, action_name, *parts):
        action = self.get_action(action_name)
        try:
            url = action["url"]
            url = re.sub(r"{\w+}", "{}", url).format(*parts)
        except IndexError:
            raise ActionURLMatchError('No url match for "{}"'.format(action_name))

        if self.append_slash and not url.endswith("/"):
            url += "/"
        if not self.api_root_url.endswith("/"):
            self.api_root_url += "/"
        if url.startswith("/"):
            url = url.replace("/", "", 1)
        return self.api_root_url + url

    def __repr__(self):
        actions = self.actions
        resource_name = self.__class__.__name__ + " actions:"
        max_action_len = max([len(action) for action in self.actions.keys()])
        max_method_len = max([len(action.method) for action in self.actions.values()])
        max_url_len = max([len(action.url) for action in self.actions.values()])
        header_width = max_action_len + max_method_len + max_url_len + 7
        header = f"{resource_name}\n{'-' * (header_width)}\n"
        actions_str = ""

        for action_name, action in actions.items():
            actions_str += (
                f"{action_name}:".ljust(max_action_len + 2)
                + f"{action.method}".ljust(max_method_len + 2)
                + f"{action.url}".ljust(max_url_len + 2)
            )
            indent_const = max_action_len + max_method_len + 4
            if action.query:
                if len(action.query.__annotations__) <= 1:
                    special_indent_q = indent_const + 2
                else:
                    special_indent_q = 0
                actions_str += f"\n{' ' * (indent_const)}Query parameters: \n{' ' * (special_indent_q)}{pprint.pformat(action.query.__annotations__, indent=indent_const + 2, compact=True, width=header_width)}"
            if action.schema_:
                if len(action.schema_.__annotations__) <= 1:
                    special_indent_p = indent_const + 2
                else:
                    special_indent_p = 0
                actions_str += f"\n{' ' * (indent_const)}Body schema: \n{' ' * (special_indent_p)}{pprint.pformat(action.schema_.__annotations__, indent=indent_const + 2, compact=True, width=header_width)}"
            actions_str += "\n\n"

        return header + actions_str


# unfortunately I need to copy-paste the whole class
# because I need to re-create httpx client as its closed after each request
class AsyncResource(BaseResource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = httpx.AsyncClient(verify=self.ssl_verify)
        for action_name in self.actions.keys():
            self.add_action(action_name)

    def add_action(self, action_name):
        async def action_method(
            self,
            *args,
            body=None,
            params=None,
            headers=None,
            action_name=action_name,
            **kwargs,
        ):
            self.client = httpx.AsyncClient(verify=self.ssl_verify)
            url = self.get_action_full_url(action_name, *args)
            method = self.get_action_method(action_name)
            request = Request(
                url=url,
                method=method,
                params=params or {},
                body=body,
                headers=headers or {},
                timeout=self.timeout,
                kwargs=kwargs,
            )
            request.params.update(self.params)
            request.headers.update(self.headers)
            async with self.client as client:
                return await make_async_request(client, request)

        setattr(self, action_name, MethodType(action_method, self))


class AsyncWootResource(AsyncResource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for action_name in self.actions.keys():
            self.update_action(action_name)

    def update_action(self, action_name):
        action_schema = self.actions[action_name].schema_
        action_query = self.actions[action_name].query
        url_params = extract_path_params(self.actions[action_name].url)
        if action_schema is not None:
            action_schema = action_schema.__dataclass_fields__
        else:
            action_schema = {}
        if action_query is not None:
            action_query = action_query.__dataclass_fields__
        else:
            action_query = {}

        action_method = getattr(self, action_name)

        @update_signature(action_schema, action_name, url_params, action_query)
        def wrapped_action_method(self, *args, **kwargs):
            if len(args) > 0:
                raise TypeError("Positional arguments are not allowed")

            schema_fields = action_schema.keys()
            query_params = action_query.keys()
            parts = {k: str(v) for k, v in kwargs.items() if k in url_params}
            query = {k: v for k, v in kwargs.items() if k in query_params}
            body = {k: v for k, v in kwargs.items() if k in schema_fields}
            kwargs = {
                k: v
                for k, v in kwargs.items()
                if k not in body and k not in parts and k not in query
            }
            self.actions[action_name].url = unquote(
                str(URL(self.actions[action_name].url).copy_merge_params(params=query))
            )

            return action_method(
                *parts.values(),
                body=body,
                params=None,
                headers=None,
                action_name=action_name,
                **kwargs,
            )

        setattr(self, action_name, MethodType(wrapped_action_method, self))

    def get_action_full_url(self, action_name, *parts):
        action = self.get_action(action_name)
        try:
            url = action["url"]
            url = re.sub(r"{\w+}", "{}", url).format(*parts)
        except IndexError:
            raise ActionURLMatchError('No url match for "{}"'.format(action_name))

        if self.append_slash and not url.endswith("/"):
            url += "/"
        if not self.api_root_url.endswith("/"):
            self.api_root_url += "/"
        if url.startswith("/"):
            url = url.replace("/", "", 1)
        return self.api_root_url + url

    def __repr__(self):
        actions = self.actions
        resource_name = self.__class__.__name__ + " actions:"
        max_action_len = max([len(action) for action in self.actions.keys()])
        max_method_len = max([len(action.method) for action in self.actions.values()])
        max_url_len = max([len(action.url) for action in self.actions.values()])
        header_width = max_action_len + max_method_len + max_url_len + 7
        header = f"{resource_name}\n{'-' * (header_width)}\n"
        actions_str = ""

        for action_name, action in actions.items():
            actions_str += (
                f"{action_name}:".ljust(max_action_len + 2)
                + f"{action.method}".ljust(max_method_len + 2)
                + f"{action.url}".ljust(max_url_len + 2)
            )
            indent_const = max_action_len + max_method_len + 4
            if action.query:
                if len(action.query.__annotations__) <= 1:
                    special_indent_q = indent_const + 2
                else:
                    special_indent_q = 0
                actions_str += f"\n{' ' * (indent_const)}Query parameters: \n{' ' * (special_indent_q)}{pprint.pformat(action.query.__annotations__, indent=indent_const + 2, compact=True, width=header_width)}"
            if action.schema_:
                if len(action.schema_.__annotations__) <= 1:
                    special_indent_p = indent_const + 2
                else:
                    special_indent_p = 0
                actions_str += f"\n{' ' * (indent_const)}Body schema: \n{' ' * (special_indent_p)}{pprint.pformat(action.schema_.__annotations__, indent=indent_const + 2, compact=True, width=header_width)}"
            actions_str += "\n\n"

        return header + actions_str


class AccountResource(WootResource, metaclass=ActionMeta, actions=a.AccountActions):
    pass


class AccountUsersResource(
    WootResource, metaclass=ActionMeta, actions=a.AccountUsersActions
):
    pass


class AgentBotsResource(WootResource, metaclass=ActionMeta, actions=a.AgentBotsActions):
    pass


class UsersResource(WootResource, metaclass=ActionMeta, actions=a.UsersActions):
    pass


class AccountAgentBotResource(
    WootResource, metaclass=ActionMeta, actions=a.AccountAgentBotActions
):
    pass


class AgentsResource(WootResource, metaclass=ActionMeta, actions=a.AgentsActions):
    pass


class CannedResponsesResource(
    WootResource, metaclass=ActionMeta, actions=a.CannedResponsesActions
):
    pass


class ContactsResource(WootResource, metaclass=ActionMeta, actions=a.ContactsActions):
    pass


class ConversationAssignmentResource(
    WootResource, metaclass=ActionMeta, actions=a.ConversationAssignmentActions
):
    pass


class ConversationLabelsResource(
    WootResource, metaclass=ActionMeta, actions=a.ConversationLabelsActions
):
    pass


class ConversationsResource(
    WootResource, metaclass=ActionMeta, actions=a.ConversationsActions
):
    pass


class CustomAttributesResource(
    WootResource, metaclass=ActionMeta, actions=a.CustomAttributesActions
):
    pass


class CustomFiltersResource(
    WootResource, metaclass=ActionMeta, actions=a.CustomFiltersActions
):
    pass


class InboxResource(WootResource, metaclass=ActionMeta, actions=a.InboxActions):
    pass


class IntegrationsResource(
    WootResource, metaclass=ActionMeta, actions=a.IntegrationsActions
):
    pass


class MessagesResource(WootResource, metaclass=ActionMeta, actions=a.MessagesActions):
    pass


class ProfileResource(WootResource, metaclass=ActionMeta, actions=a.ProfileActions):
    pass


class ReportsResource(WootResource, metaclass=ActionMeta, actions=a.ReportsActions):
    pass


class TeamsResource(WootResource, metaclass=ActionMeta, actions=a.TeamsActions):
    pass


class WebhooksResource(WootResource, metaclass=ActionMeta, actions=a.WebhooksActions):
    pass


class AutomationRuleResource(
    WootResource, metaclass=ActionMeta, actions=a.AutomationRuleActions
):
    pass


# Async


class AsyncAccountResource(
    AsyncWootResource, metaclass=ActionMeta, actions=a.AccountActions
):
    pass


class AsyncAccountUsersResource(
    AsyncWootResource, metaclass=ActionMeta, actions=a.AccountUsersActions
):
    pass


class AsyncAgentBotsResource(
    AsyncWootResource, metaclass=ActionMeta, actions=a.AgentBotsActions
):
    pass


class AsyncUsersResource(
    AsyncWootResource, metaclass=ActionMeta, actions=a.UsersActions
):
    pass


class AsyncAccountAgentBotResource(
    AsyncWootResource, metaclass=ActionMeta, actions=a.AccountAgentBotActions
):
    pass


class AsyncAgentsResource(
    AsyncWootResource, metaclass=ActionMeta, actions=a.AgentsActions
):
    pass


class AsyncCannedResponsesResource(
    AsyncWootResource, metaclass=ActionMeta, actions=a.CannedResponsesActions
):
    pass


class AsyncContactsResource(
    AsyncWootResource, metaclass=ActionMeta, actions=a.ContactsActions
):
    pass


class AsyncConversationAssignmentResource(
    AsyncWootResource, metaclass=ActionMeta, actions=a.ConversationAssignmentActions
):
    pass


class AsyncConversationLabelsResource(
    AsyncWootResource, metaclass=ActionMeta, actions=a.ConversationLabelsActions
):
    pass


class AsyncConversationsResource(
    AsyncWootResource, metaclass=ActionMeta, actions=a.ConversationsActions
):
    pass


class AsyncCustomAttributesResource(
    AsyncWootResource, metaclass=ActionMeta, actions=a.CustomAttributesActions
):
    pass


class AsyncCustomFiltersResource(
    AsyncWootResource, metaclass=ActionMeta, actions=a.CustomFiltersActions
):
    pass


class AsyncInboxResource(
    AsyncWootResource, metaclass=ActionMeta, actions=a.InboxActions
):
    pass


class AsyncIntegrationsResource(
    AsyncWootResource, metaclass=ActionMeta, actions=a.IntegrationsActions
):
    pass


class AsyncMessagesResource(
    AsyncWootResource, metaclass=ActionMeta, actions=a.MessagesActions
):
    pass


class AsyncProfileResource(
    AsyncWootResource, metaclass=ActionMeta, actions=a.ProfileActions
):
    pass


class AsyncReportsResource(
    AsyncWootResource, metaclass=ActionMeta, actions=a.ReportsActions
):
    pass


class AsyncTeamsResource(
    AsyncWootResource, metaclass=ActionMeta, actions=a.TeamsActions
):
    pass


class AsyncWebhooksResource(
    AsyncWootResource, metaclass=ActionMeta, actions=a.WebhooksActions
):
    pass


class AsyncAutomationRuleResource(
    AsyncWootResource, metaclass=ActionMeta, actions=a.AutomationRuleActions
):
    pass


_ALL_RESOURCES = [
    k
    for k, v in globals().items()
    if all(
        [
            "Resource" in k,
            isinstance(v, ActionMeta),
            not k.startswith("Async"),
            k not in ("Resource", "AsyncResource", "WootResource", "AsyncWootResource"),
        ]
    )
]

_ALL_ASYNC_RESOURCES = [
    k
    for k, v in globals().items()
    if all(
        [
            "Resource" in k,
            k.startswith("Async"),
            k not in ("Resource", "AsyncResource", "WootResource", "AsyncWootResource"),
        ]
    )
]
