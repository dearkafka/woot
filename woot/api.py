""" Chatwoot API wrapper is here."""

from abc import abstractproperty
from simple_rest_client.api import API

import woot.resources as wr
from woot.utils import get_account_name


class _BaseChatwoot:
    def __init__(self, chatwoot_url, access_key, **kwargs) -> None:
        self._chatwoot_url = chatwoot_url
        self._access_key = access_key
        self._timeout = kwargs.get("timeout", 60)
        self._json_encode_body = kwargs.get("json_encode_body", True)

        self._api = API(
            api_root_url=self._chatwoot_url,
            params={},
            headers={"api_access_token": f"{self._access_key}"},
            timeout=self._timeout,
            json_encode_body=self._json_encode_body,
        )
        self._add_resources()

    def _add_resources(self):
        for resource in self.resources:
            resource = getattr(wr, resource)
            self._api.add_resource(
                resource_name=get_account_name(resource.__name__),
                resource_class=resource,
            )
            setattr(
                self,
                get_account_name(resource.__name__),
                getattr(self._api, get_account_name(resource.__name__)),
            )  # because I want resources to be attributes of Chatwoot and AsyncChatwoot

        @abstractproperty
        def resources(self):
            pass

    def __repr__(self):
        resource_names = [get_account_name(resource) for resource in self.resources]
        max_len = max([len(name) for name in resource_names]) + 2
        header = f"Available actions:\n{'-' * max_len}\n"
        actions = ""
        for name in resource_names:
            actions += f"{name:<{max_len}}"
            actions += f"\n{' ' * (max_len + 1)}"
            for action, details in getattr(getattr(self, name), "actions").items():
                actions += (
                    f"{action}: {details.method} {details.url}\n{' ' * (max_len + 1)}"
                )
            actions += "\n"  # Add blank line after actions for each resource
        return header + actions


class Chatwoot(_BaseChatwoot):
    @property
    def resources(self):
        return wr._ALL_RESOURCES


class AsyncChatwoot(_BaseChatwoot):
    @property
    def resources(self):
        return wr._ALL_ASYNC_RESOURCES
